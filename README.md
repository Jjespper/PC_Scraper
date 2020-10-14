# PC Scraper

The scope of this project is to develop a web scraper script to get and store in a MySQL database all the articles from a list of categories from this website: https://www.pccomponentes.com

PC Components is a Spanish e-commerce portal specialized in computer, electronic and appliance products. Belongs to the YF Networks group and operates in Spain and Portugal.

These are the categories that will be scrapped.

Components
 
`Graphics cards`
`Processors` 
`Motherboards`
`Hard drives hdd & sdd -RAMs`
`Power source`
`Multi-readers`
`Sound cards`
`Towers`
`Fans`
`DVD, blue-ray`
`Capturers`
`Periferics`
`Screens`
`Keyboards`
`Microphones`
`Laptops`
`Smartphones`
`TV`
`Tablets`
`PS4`
`Nintendo Switch`
`Xbox-One`
`Nintendo DS/3DS`

This is a web scraper built with Selenium, 5 features are extracted.

<ul>
  <li>Article: Name of product</li>
  <li>Category: Product category</li>
  <li>Price: €</li>
  <li>Stock: 1)Available 2)Available soon 3) Available soon 4) No stock </li>
  <li>Date: YYYY/MM/DD</li>
</ul>

This scraper take more than 9000 articles daily. ![](https://user-images.githubusercontent.com/51057882/94199543-45b33a00-feb9-11ea-8523-d36862ec3f23.png)

The idea of this project is to automate the scrap, create a large database for easy access to use in different analyzes, machine learning models, dashborads or whatever you want.

## Files & Folders
This repository have several files and folders, to make it easier lets explain briefly:

**Env**
`environment.yml`: YAML-formatted environment manifest of the application to configure the environment

`main.py`: Executable script to collect the data from the scrapping in a MySQL database.

**[WIP]**
