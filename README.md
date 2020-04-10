# devnote-scrapy

### Devnote-Scrapy Integration

This project integrates the Django and Scrapy frameworks. For example, a scrapping of blog posts https://devnote.in is done, creating in django a Blog model with name,image and category.

### How to run
**scraper** folder inside below command execute : 
Here **/devnote-scrapy/scraper/**

### Running the spider
<pre>scrapy crawl devnote</pre>

### You can create **json** file data store. Like this command :
<pre>scrapy crawl devnote -o output.json</pre>

Below follows a screenshot of the image scraping process running :

![](http://devnote.in/personal_data/scraping-data.png)

**Also read** : [How to create crawl a web page with scrapy and python](https://devnote.in/how-to-create-crawl-a-web-page-with-scrapy-and-python/)
