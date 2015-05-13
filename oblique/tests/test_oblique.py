import unittest

from lxml import html

from oblique.oblique import Oblique, get_items


class TestOblique(unittest.TestCase):
    def setUp(self):
        o = Oblique()

    def test_get_items_empty(self):
        doc = html.document_fromstring(
            '<!doctype html>'
            '<html>'
            '<head>'
            '</head>'
            '<body>'
            '</body>'
            '</html>'
        )
        self.assertEqual(len(get_items(doc)), 0)

    def test_get_items(self):
        doc = html.document_fromstring(
            '<!doctype html>'
            '<html>'
            '<head>'
            '</head>'
            '<body>'

            '<div class="post" itemscope itemtype="http://schema.org/BlogPosting">'
            '</div>'

            '<div class="post" itemscope itemtype="http://schema.org/BlogPosting">'
            '</div>'

            '</body>'
            '</html>'
        )
        self.assertEqual(len(get_items(doc)), 2)
