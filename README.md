# glitch-assets-parser

Parses Glitch assets (food and drink) metadata into a JSON format

I was playing around with the [Glitch assets](http://www.glitch.com/licensing/) but I wanted a lookup of all the food and drink items with a path to their icons. This parses the Glitch encyclopedia and assets file structure to build that index.

If you just want the end result of this, take a look at [items.json](items.json).

## Usage


```
usage: parser.py [-h] [-f FILENAME]

Parses Glitch assets (food and drink) metadata into a JSON format

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        file to output to
```

