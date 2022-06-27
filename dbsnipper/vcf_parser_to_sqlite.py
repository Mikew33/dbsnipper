import gzip
import sqlite3
import pandas as pd
from sqlalchemy import create_engine


class VcfParser():
    VCF_KEYS = [
        'CHROM',
        'POS',
        'ID',
        'REF',
        'ALT',
        'QUAL',
        'FILTER',
        'INFO'
    ]

    def __init__(self, vcf: str):
        self.vcf = vcf
        if vcf.endswith('.gz'):
            self.fh = gzip.open(vcf, 'rt')
        else:
            self.fh = open(vcf, 'r')

    def set_header(self):
        num_header_lines = 0
        for line in self.fh:
            if line.startswith('#'):
                num_header_lines += 1

        self.fh.seek(0)

        temp = []
        i = 0
        for line in self.fh:
            i += 1
            temp.append(line)
            if i == num_header_lines:
                break
        self.header = ''.join(temp)
        with open('all_header.txt', 'w') as f:
            f.write(self.header)

    def next(self):

        collected_lst = []
        conn = sqlite3.connect('database.db')
        engine = create_engine('sqlite:///database.db')

        while True:
            line = self.fh.readline()
            temp_lst = line.split('\t')

            count = 0
            assemble_lst = []
            for i in temp_lst:
                count += 1
                assemble_lst.append(i)
                if count == 8:
                    break

            data_dict = {}
            try:
                for i, element in enumerate(self.VCF_KEYS):
                    data_dict[element] = assemble_lst[i]
            except IndexError:
                break

            info_data = data_dict['INFO'].split(';')

            info_collected = []
            for element in info_data:
                info_pieces = element.split('=')
                info_collected.append(info_pieces)

            info_dict = {}
            for item in info_collected:
                try:
                    info_dict[item[0]] = item[1]
                except IndexError:
                    info_dict[item[0]] = None

            data_dict.pop('INFO')
            data_dict.update(info_dict)
            collected_lst.append(data_dict)

        df = pd.DataFrame(collected_lst)
        df.to_sql('VCF_data', engine, if_exists='append', index=False)


parser = VcfParser('pick_in_random_for_compressed_and_uncompressed.vcf.gz')
parser.set_header()
parser.next()
