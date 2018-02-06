
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser


# In[2]:


url = "https://mars.nasa.gov/news/";
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.body.prettify())


# In[7]:


# NASA Mars News
result = soup.find('div', class_='content_title')
news_title = result.a.text

result = soup.find('div', class_='image_and_description_container')
news_para = result.a.text

if news_title and news_para:
    print("news_title:" , news_title)
    print("news_para: " , news_para)


# In[43]:


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
featured_image_url = url + img
print('featured_image_url: '+ featured_image_url)



# In[57]:


browser = Browser('chrome', headless=False)
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
tweet_container = soup.find('div', class_ = 'js-tweet-text-container')
para = tweet_container.find('p', class_ = 'TweetTextSize')
mars_weather = para.text.strip()
print(mars_weather)


# In[70]:


import pandas as pd
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
tables


# In[71]:


df = tables[0]


# In[72]:


df.columns=['fact', 'data_fact']


# In[73]:


print(df)


# In[74]:


df.set_index('fact', inplace=True)
df.head()


# In[75]:


html_table = df.to_html()
print(html_table)


# In[77]:


df.to_html('mars_fact_table.html')


# In[78]:


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
print(hemisphere_image_urls)

