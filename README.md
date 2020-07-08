# Mouthshut Web Scrapper
This repository contains python script for extracting consumer reviews from India's largest consumer platform Mouthshut.com which utilised beautiful soup and selenium for automating the scrapping of the reviews from the website.

## Dependencies
* Beautiful soup
* Selenium
* Chrome webdirver

For installing the above dependencies you can run the following command:

``` pip install -r requirements.txt```

## Running the scipt
Script can be run from the terminal which requires some arguments, whose usage is defined as below:
```
usage: mouthshut_webscrapper.py [-h] --out-dir <str> --url <str> --page <int>

optional arguments:
  -h, --help       show this help message and exit
  --out-dir <str>  Path of the output file
  --url <str>      website url from to be scrapped
  --page <int>     Number of pages to be scraped
```
