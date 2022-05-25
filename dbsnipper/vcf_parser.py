from typing import IO


class VcfParser:

    header: str
    fh: IO

    def __init__(self, vcf: str):
        self.fh = open(vcf, 'r')

        self.header = ''
        temp = []
        for line in self.fh:
            if line.startswith("#"):
                temp.append(line)
                self.header = ''.join(temp)
