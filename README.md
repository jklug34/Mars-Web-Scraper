# Mars-Web-Scraper
A web application to scrape various websites for real time data related to a future mission to the planet Mars, outputs all the information in an easy view web page and stores the data in a MongoDB database.


# To Use App

- Run app.py in visual studio code or IDE of your choice
- Click on the local link generated and open in google chrome
- Click on blue button "Scrape Mars Data" to scrape the web for the most recent Mars Data
- After a few seconds the data will populate the webpage


# Websites Scraped (BeautifulSoup/Splinter)


Latest Mars News
- https://mars.nasa.gov/news/

Featured Mars High Resolution Images
- https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

Mars Weather Data
- https://twitter.com/marswxreport?lang=en

General Information on Mars
- https://space-facts.com/mars/

High Resolution Images of Mars Hemisphers (4)
- https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars


# Dependences

- Jupyter notebook, pandas, BeautifulSoup, Splinter, PyMongo


# In the file 

- A jupyter notebook/pandas file with all of the analysis and HTML parsing needed to scrape various websites for Mars related data.

- A Flask app (app.py, scrape_mars.py, index.html (bootstrap structured) and style.css) web scraper with data stored in a MongoDB database.


# Screen Shot of HTML Output

![HTML Output Screen Shot](https://user-images.githubusercontent.com/48166327/61418815-afe14f80-a8b0-11e9-88d1-f58987c7785f.PNG)

![HTML Output Screen Shot (2)](https://user-images.githubusercontent.com/48166327/61418820-b40d6d00-a8b0-11e9-99b3-f9e8ffd54bca.PNG)


# MongoDB database

![MongoDB Database](https://user-images.githubusercontent.com/48166327/61413615-c7b0d780-a8a0-11e9-95d3-7b442015a4e5.PNG)