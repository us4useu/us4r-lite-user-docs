# Building

First, clone this repository, e.g. in command line:
```
git clone https://github.com/us4useu/us4r-user-docs.git
```

## Prerequisites

All platforms:
- Python >= 3.8 (Miniconda 3 is recommended),
- the packages specified in the : `pip install -r docs/requirements.txt`
- Windows 10 or later:
  - The latest [MiKTeX](https://miktex.org/) with packages: `ha-prosper`, `prosper`, `latex-tools`
  - install the latest version of [strawberry perl](strawberryperl.com)
- Linux:
```
sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk
sudo apt-get install latexmk
```

## Building the documentation

To build the documentation on Linux:
```
make html latexpdf
```
(note: you can skip the `html` or `pdf` if you don't need that output format)

To build the documentation on Windows:
```
make.bat latexpdf
```

