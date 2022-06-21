from typing import IO, Dict


class VcfParser:

    header: str
    fh: IO

    VCF_KEYS = [
        'CHROM',
        'POS',
        'ID',
        '',
        '',
        '',
        '',
        '',
    ]

    def __init__(self, vcf: str):
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

        ret = '\t'.join(assemble_lst)
        return ret
