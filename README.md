# PyDorker

A dorking tool written in Python3

[![Python 3.7](https://img.shields.io/badge/python-3.7-FADA5E.svg?logo=python)](https://www.python.org/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-red.svg)](https://www.python.org/dev/peps/pep-0008/) [![License](https://img.shields.io/badge/license-GPL3-lightgrey.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![Twitter](https://img.shields.io/badge/twitter-sneakerhax-38A1F3?logo=twitter)](https://twitter.com/sneakerhax)

## Install

```bash
python3 -m pip install -r requirements.txt
```

## Run with Docker

```bash
docker build -t pyreconer .
```
Build Docker image

```bash
docker run -it pyreconer <site> <dorklist>
```
Run Docker container with site and dorklist

## Usage
To run a Google dork you have to create a file with a list of Dorks for the particular thing you are looking for and place it in the dorkfiles folder. I will be adding more lists over time.

Google will often block you if it detects automated queries so you may have to research a bit to avoid this

```bash
python Pydorker.py <site> <dorklist>
```
