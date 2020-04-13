# pdf4py

[![Build Status](https://travis-ci.org/Halolegend94/pdf4py.svg?branch=master)](https://travis-ci.org/Halolegend94/pdf4py) [![Documentation Status](https://readthedocs.org/projects/pdf4py/badge/?version=latest)](https://pdf4py.readthedocs.io/en/latest/?badge=latest)

A PDF parser written in Python 3 with no external dependencies.

The package pdf4py allows the user to interact with a PDF file at a low level and to build higher level functionalities (e.g. text and/or image extraction). In particular, it defines the class Parser that reads the Cross Reference Table of a PDF document and uses its entries to give the user the ability to locate PDF objects within the file and parse them into suitable Python objects.

## Quick example

Here is a quick demostration on how to use pdf4py.

```python
>>> from pdf4py.parser import Parser
>>> fp = open('tests/pdfs/0000.pdf', 'rb')
>>> parser = Parser(fp)
>>> info_ref = parser.trailer['Info']
>>> print(info_ref)
PDFReference(object_number=114, generation_number=0)
>>> info = parser.parse_reference(info_ref).value
>>> print(info)
{'Creator': PDFLiteralString(value=b'PaperCept Conference Management System'),
    ... , 'Producer': PDFLiteralString(value=b'PDFlib+PDI 7.0.3 (Perl 5.8.0/Linux)')}
>>> creator = info['Creator'].value.decode('utf8')
>>> print(creator)
PaperCept Conference Management System
```

## Installation

You can install `pdf4py` using pip:

```
python3 -m pip install pdf4py
```

## Extracting text or images

Extracting text from a PDF and other higher level analysis tasks are not natively supported because
of two reasons:

- their complexity is not trivial and would require a not indifferent amount of work which now I prefer
investing into developing a complete and reliable parser;
- they are conceptually different tasks from PDF parsing, since the PDF does not define the concept of
structured document from the content point of view.

Therefore, they require a separate implementation built on top of `pdf4py`.

## Why this package

One day at work I was asked to analyze some PDF files; to my surprise I have discovered that
there is not an established Python module to easily parse a PDF document. In order to understand
why I delved into the PDF 1.7 specification: since that moment I've got interested more and more
in the inner workings of one of the most important and ubiquitous file format. And what's
a better way to understand the PDF than writing a parser for it?


## Documentation

You can read the documentation for this package on [readthedocs.io](https://pdf4py.readthedocs.io/en/latest/).


## Contributing

Contributions are more than welcome! You can

- filing a new issue;
- proposing changes and additions through a pull request.
