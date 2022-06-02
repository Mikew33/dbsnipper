from typing import IO


class VcfParser:

    context: str
    temporary: str
    header: str
    fh: IO

    def __init__(self, vcf: str):
        self.fh = open(vcf, 'r')
        self.set_header()
        self.next()

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

    def next(self):
        self.fh.seek(0)

        count = 0
        temp1 = []
        for line in self.fh:
            if count == 1:
                break
            if line.startswith('#'):
                continue
            else:
                temp1.append(line)
                count += 1
        self.temporary = ''.join(temp1)

        temp2 = []
        word_count = 0
        for w in self.temporary:
            word_count += 1
            temp2.append(w)
            if word_count == 51:
                break
        self.context = ''.join(temp2)
