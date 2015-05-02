# favicon

Simple script for generating favicon and touch icons. Django integration included!

## Motivation

Well, if you've ever tried to generate favicon and touch icons for **all**
screens and devices, you know why. The main reasons are:

1. It should be **automated** (there's zero logic)
2. It should be kept **updated** (new devices emerge often)

Interesting reading:

- [https://mathiasbynens.be/notes/touch-icons](https://mathiasbynens.be/notes/touch-icons)

## Installation

Simply install package via pip:

```
pip install favicon
python -m favicon -v  # check if it works
```

## Usage

You can use it either as standalone script or plug it into Django project.

### Standalone script

By default it will generate all possible favicon sizes and touch icons:

```
python -m favicon source-image.png favicon/
```

The script will read image `source-image.png` and output all icons to directory
`favicon/`.

If you want to see all available options, see the help:

```
python -m favicon -h
```

## Licence

MIT
