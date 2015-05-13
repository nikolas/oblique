import os
import re
import sys
from copy import deepcopy

from lxml import etree, html


class ObliqueDoc:
    """An Oblique Document."""
    filename = 'doc.html'


def item_has_title_link(el):
    """Returns True if the given element has a title link."""
    return len(el.cssselect('h1 a')) > 0


def get_item_filepath(el):
    """Given an lxml element, return a dirname and filename.

    :rtype: string, string
    """
    dirname = '-'
    filename = 'doc.html'
    title_link_el = el.cssselect('h1 a')[0]
    href = title_link_el.get('href')
    match = re.match(r'.*/(\S)/(\S+.html)$', href)
    if match:
        dirname = match.groups()[0]
        filename = match.groups()[1]
    return dirname, filename


def get_items(doc):
    """Given the document, return a list of oblique items.

    :rtype: list
    """
    return doc.find_class('post')


class Oblique:
    def parse_doc(self, docstring):
        """
        :rtype: string
        """
        doc = html.document_fromstring(docstring)
        posts = get_items(doc)
        print('Found %d posts' % len(posts))
        skeleton = deepcopy(doc)
        for post in skeleton.cssselect('.post'):
            post.drop_tree()
        for post in posts:
            if item_has_title_link(post):
                myskel = deepcopy(skeleton)
                el = myskel.cssselect('body')[0]
                el.append(post)

                dname, fname = get_item_filepath(post)
                # Create a detail page for this post.
                try:
                    os.mkdir('/tmp/%s' % dname)
                except:
                    pass
                print(dname, fname)
                with open('/tmp/%s/%s' % (dname, fname), 'w') as f:
                    f.write(bytes.decode(html.tostring(myskel)))

        return doc

    def open_doc(self, docname):
        f = open(docname, 'r')
        s = f.read()
        print(self.parse_doc(s))
        f.close()


if __name__ == '__main__':
    try:
        o = Oblique()
        o.open_doc(sys.argv[1])
    except:
        print('Usage:\n\toblique filename.html')
