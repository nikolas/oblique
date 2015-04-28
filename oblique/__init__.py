import sys
from lxml import html


class Oblique:
    def get_items(self, doc):
        """Given the document, return a list of oblique items."""
        return doc.find_class('post')

    def parse_doc(self, docstring):
        """Returns a string."""
        doc = html.document_fromstring(docstring)
        posts = self.get_items(doc)
        print('Found %d posts' % len(posts))
        return doc


if __name__ == '__main__':
    try:
        f = open(sys.argv[1], 'r')
        s = f.read()
        o = Oblique()
        print(o.parse_doc(s))
        f.close()
    except:
        print('Usage:\n\toblique filename.html')
