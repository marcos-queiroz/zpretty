# coding=utf-8
from unittest import TestCase
from zpretty.text import lstrip_first_line
from zpretty.text import rstrip_last_line


class TestFunctions(TestCase):
    ''' Test functions used by zpretty
    '''

    def test_lstrip_first_line_oneline(self):
        self.assertEqual(
            lstrip_first_line(u' a'), u'a'
        )

    def test_lstrip_first_line_twolines(self):
        self.assertEqual(
            lstrip_first_line(u' a \n b'),
            (u'a \n b')
        )

    def test_rstrip_larst_line_oneline(self):
        self.assertEqual(
            rstrip_last_line(u'a'), u'a'
        )

    def test_rstrip_larst_line_twoline(self):
        self.assertEqual(
            rstrip_last_line(u'a\n b '),
            (u'a\n b')
        )

    def test_none(self):
        self.assertEqual(lstrip_first_line(None), None)
        self.assertEqual(rstrip_last_line(None), None)
