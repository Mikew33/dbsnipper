from typing import IO, Dict
import gzip

class VcfParser:

    header: str
    fh: IO
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
        if vcf.endswith('.gz'):
            self.fh = gzip.open(vcf, 'rt')  # rt: read text
        else:
            self.fh = open(vcf, 'r')
        self.set_header()

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

    def next(self) -> Dict[str, str]:
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
        for i in range(len(self.VCF_KEYS)):
            data_dict[self.VCF_KEYS[i]] = assemble_lst[i]

        for element in data_dict['INFO'].split(';'):
            if '=' in element:
                key, val = element.split('=')
            else:
                key, val = element, None
            data_dict[key] = val

        data_dict.pop('INFO')

        return data_dict
