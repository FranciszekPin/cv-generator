# CV Generator

Script for generating latex CV document
The idea is not to write latex, but only to edit `cv_data` which is a simple text file.

## Usage

`cv_data` consists of key-value pairs in the following format:

```
key@ value
key@ value
...
key@ value
```

It allows you to specify name, email, etc.


For realized projects data should be organized in the following format:

```
projects@
link@ link to your project1
name@ name of your project1
description@ description of your project1
...
link@ link to your project2
name@ name of your project2
description@ description of your project2
projects@
```
Similarly, you can specify technologies, tools, and languages.

`cv_data` is provided with example values.
Just edit `cv_data` with appropriate values and type `make` to build your document.
It will be generated in `cv.pdf`

## Hacking

Latex source is generated from `tex_templates/*` file, so you can modify them to introduce changes in the generated document, for example changing the font size.
