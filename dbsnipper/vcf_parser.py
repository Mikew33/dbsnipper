from typing import IO


class VcfParser:

    header: str
    fh: IO

    def __init__(self, vcf: str):
        self.fh = open(vcf, 'r')
        self.set_header()
        print(self.fh.readline())

    def set_header(self):
        num_header_lines = 4
        # for loop

        temp = []
        i = 0
        for line in self.fh:
            i += 1
            temp.append(line)
            if i == num_header_lines:
                break
        self.header = ''.join(temp)
