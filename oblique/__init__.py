import re
import sys
from lxml import html


class ObliqueDoc:
    """An Oblique Document."""
    filename = 'doc.html'


def get_item_filename(el):
    """Given an lxml element, return a filename.

    :rtype: string
    """
    filename = 'doc.html'
    title_link_el = el.cssselect('h1 a')[0]
    href = title_link_el.get('href')
    match = re.match(r'.*/(\S+.html)$', href)
    if match:
        filename = match.groups()[0]
    return filename


def get_items(doc):
    """Given the document, return a list of oblique items.

    :rtype: list
    """
    return doc.find_class('post')


def parse_doc(docstring):
    """
    :rtype: string
    """
    doc = html.document_fromstring(docstring)
    posts = get_items(doc)
    print('Found %d posts' % len(posts))
    for post in posts:
        fname = get_item_filename(post)
        if fname:
            # Create a detail page for this post.
            pass
    return doc


if __name__ == '__main__':
    try:
        f = open(sys.argv[1], 'r')
        s = f.read()
        print(parse_doc(s))
        f.close()
    except:
        print('Usage:\n\toblique filename.html')
