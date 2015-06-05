import builtins
from unittest import TestCase
from unittest.mock import mock_open, patch
from copy import deepcopy

from lxml import html

from oblique.oblique import Oblique, get_items


class TestOblique(TestCase):
    def setUp(self):
        self.o = Oblique()
        self.doc_with_posts = html.document_fromstring(
            '<!doctype html>'
            '<html>'
            '<head>'
            '</head>'
            '<body>'

            '<div class="post" itemscope '
            'itemtype="http://schema.org/BlogPosting">'
            '</div>'

            '<div class="post" itemscope '
            'itemtype="http://schema.org/BlogPosting">'
            '</div>'

            '</body>'
            '</html>'
        )

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
        self.assertEqual(len(get_items(self.doc_with_posts)), 2)

    def test_write_doc(self):
        doc = self.doc_with_posts
        myskel = deepcopy(doc)
        map(lambda x: x.drop_tree(), myskel.cssselect('.post'))
        post = doc.cssselect('.post')[0]

        open_ = mock_open()
        with patch.object(builtins, 'open', open_):
            self.o.write_doc('abc', '123', post, myskel)
        open_.assert_called_once_with('/tmp/abc/123', 'w')
