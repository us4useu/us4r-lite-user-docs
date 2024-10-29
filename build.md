# Building

First, clone this repository, using Github Desktop, e.g. in command line:
```
git clone https://github.com/us4useu/us4r-user-docs.git
```

## Prerequisites

### Windows 10 or later

1. Download and install [Miniconda3](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe).
2. Download and install [MiKTeX](https://miktex.org/) with packages: `ha-prosper`, `prosper`, `latex-tools`.
3. Download install [Strawberry Perl](https://strawberryperl.com)
4. Open Anaconda Powershell Prompt. 
5. _Optional: Create and activate Minconda3 envinronment dedicated for the documentation development: conda create -n docs python=3.10._
6. Install Python requirements: `pip install -r docs/requirements.txt`

### Linux (Ubuntu 20.04 or later)

1. Download and install [Miniconda3](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh).
2. Install texlive: 
```
sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk
sudo apt-get install latexmk
```
3. _Optional: Create and activate Minconda3 envinronment dedicated for the documentation development: conda create -n docs python=3.10._
4. Install Python requirements: `pip install -r docs/requirements.txt`


## Building the documentation

To build the documentation on Linux:
```
make html latexpdf
```
(note: you can skip the `html` or `pdf` if you don't need that output format)

To build the documentation on Windows:
```
make.bat clean
make.bat latexpdf
```

