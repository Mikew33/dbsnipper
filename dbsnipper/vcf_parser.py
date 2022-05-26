from typing import IO


class VcfParser:

    header: str
    fh: IO

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
