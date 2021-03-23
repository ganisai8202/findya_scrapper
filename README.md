# findya_scrapper
a scrapy bot that scrapes webpages
## Description

The bot generates a `csv` and `json` file of the necklace sets from the webiste [houseoffindya](https://www.houseofindya.com/zyra/necklace-sets/cat).
the files contain name,price,scription and image_urls of the sets.

## usage
Downlaod the the github repository 

`git clone https://github.com/ganisai8202/findya_scrapper.git`

Navigate to the repository 

`cd findya_scrapper`

Install the required packages

`pip install -r requirements.txt`

Run the program
```
scrapy crawl findya_scrapper -o <output_file_name>.csv
scarpy crawl findya_scrapper -o <output_file_name.json>
```
