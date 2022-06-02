from dbsnipper.vcf_parser import VcfParser
from .setup import TestCase

import pandas as pd


class TestVcfParser(TestCase):

    def setUp(self):
        self.set_up(py_path=__file__)

    def tearDown(self):
        self.tear_down()

    def test_init(self):
        parser = VcfParser(vcf=f'{self.indir}/tiny.vcf')
        expected = f'''\
##fileformat=VCFv4.3
##fileDate=20090805
##source=myImputationProgramV3.1
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tNA00001\tNA00002\tNA00003
'''
        self.assertEqual(first=expected, second=parser.header)

    def test_next(self):
        parser = VcfParser(vcf=f'{self.indir}/tiny.vcf')

        actual = parser.next()
        expected = f'1\t101\trs6054257\tG\tA\t29\tPASS\tNS=3;DP=14;AF=0.5;DB;H2'
        self.assertEqual(expected, actual)

        # actual = parser.next()
        # expected = f'2\t102\t.\tT\tA\t3\tq10\tNS=3;DP=11;AF=0.017'
        # self.assertEqual(expected, actual)

        # actual = parser.next()
        # expected = '3\t103\trs6040355\tA\tG,T\t67\tPASS\tNS=2;DP=10;AF=0.333,0.667;AA=T;DB'
        # self.assertEqual(expected, actual)
