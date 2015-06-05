# Oblique

[![Build Status](https://img.shields.io/travis/nikolas/oblique/master.svg)](https://travis-ci.org/nikolas/oblique)

## ¿   ?

An indirect static site generator: it compiles your entries from an
`index.html` file into a full site. By using HTML as the authoring medium,
Oblique removes the markup layer of abstraction, while retaining the
organizational convenience of static site templates. This approach could
be thought of as "static site assembly".

When you make a site with Oblique, the build step is optional. You
can author the content in HTML and have a site that will render just
fine in the web browser. Then, you can use Oblique on whatever
aggregate files you want to create the archived, "detail" pages for
each entry in the aggregate.

For example:

```html
<!doctype html>
<html>
<head>
    <title>Notes from another time</title>
</head>
<body>
    <div class="post">
         <h1 class="title">
             <a href="/-/today-i-learned-something-weird.html">
               Today I learned something weird
             </a>
         </h1>
         <time>April 18, 2027</time>
         <div class="blog-post">
         <p>
            Well, I never thought I would learn that, but I did.
         </p>
         </div>
    </div>

    <div class="post">
         <h1 class="title">
             <a href="/-/a-note-from-the-roaring-20s.html">
               A note from the roaring 20s
             </a>
         </h1>
         <time>February 12, 2027</time>
         <div class="blog-post">
         <p>
            Dear diary, I'd like to tell you everything, but
            I can't say it all at once.
         </p>
         </div>
    </div>
</body>
</html>
```
    $ python3 oblique/oblique.py index.html

Given this index page, Oblique's simple job is to archive
the posts into `/-/today-i-learned-something-weird.html` and
`/-/a-note-from-the-roaring-20s.html`.

## Testing

    $ source env/bin/activate
    $ python setup.py test
