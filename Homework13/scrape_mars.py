# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

def scrape():
    # use beautiful soup to scrape 
    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.body.prettify())

    # NASA Mars News
    result = soup.find('div', class_='content_title')
    news_title = result.a.text
    result = soup.find('div', class_='image_and_description_container')
    news_para = result.a.text

    #if news_title and news_para:
    #    print("news_title:" , news_title)
    #    print("news_para: " , news_para)


    # JPL Mars Space Images - Featured Image
    browser = Browser('chrome', headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    carousel = soup.find('div', class_='carousel_items')
    article = carousel.find('article', class_ = 'carousel_item')
    image = article['style']
    img = image[23:-3]
    nasa_url = 'https://www.jpl.nasa.gov'
    featured_image_url =  url + img
    #print('featured_image_url: '+ featured_image_url)
    main_image_url = {"mars_img_url": featured_image_url}

    # Mars Weather paragraph
    browser = Browser('chrome', headless=False)
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweet_container = soup.find('div', class_ = 'js-tweet-text-container')
    para = tweet_container.find('p', class_ = 'TweetTextSize')
    mars_weather = para.text.strip()
    print(mars_weather)

    # Mars Facts table
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    tables
    df = tables[0]
    df.columns=['fact', 'data_fact']
    df.set_index('fact', inplace=True)
    df.head()
    facts_table = df.to_dict(orient = 'records')
    html_table = df.to_html()
    #df.to_html('mars_fact_table.html')

    # Mars Hemispheres images
    cerberus_img = 'https://astrogeology.usgs.gov/cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif_thumb.png'
    cerberus_title = 'Cerberus Hemisphere'
    schiaparelli_img = 'https://astrogeology.usgs.gov/cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif_thumb.png'
    schiaparelli_title = 'Schiaparelli Hemisphere'
    syrtis_img = 'https://astrogeology.usgs.gov/cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif_thumb.png'
    syrtis_title = 'Syrtis Hemisphere'
    marineris_img = 'https://astrogeology.usgs.gov/cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif_thumb.png'
    marineris_title = 'Valle Marineris Hemisphere'

    hemisphere_image_urls = [ 
        {"title": cerberus_title, "img_url": cerberus_img},
        {"title": schiaparelli_title, "img_url": schiaparelli_img},
        {"title": syrtis_title, "img_url": syrtis_img},
        {"title": marineris_title, "img_url": marineris_img}
    ]
    #print(hemisphere_image_urls)

    mars_dict = {
        "News_Title": news_title,
        "News_Para": news_para,
        "Featured_Img_URL": main_image_url,
        "Mars_Weather": mars_weather,
        "Mars_Facts": html_table,
        "Mars_Hemispheres": hemisphere_image_urls
    }

    return mars_dict
