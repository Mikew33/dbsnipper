from typing import IO


class VcfParser:

    header: str
    fh: IO

    def __init__(self, vcf: str):
        self.fh = open(vcf, 'r')

        self.header = ''
        for line in self.fh:
            print(line)
