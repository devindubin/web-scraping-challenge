# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
from pprint import pprint


def init_browser():
    
    executable_path = {"executable_path":"chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)




def scrape():

    browser = init_browser()
    the_one = {}
    
    ###########
    #Step 1.1: NASA Mars News
    ###########
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')

    art_title = soup.find('ul',class_ = 'item_list').find('div',class_='content_title').text

    art_teaser = soup.find('div',class_ = "article_teaser_body").text

    
    the_one['article_title'] = art_title
    
    the_one['article_teser'] = art_teaser

    
    ###########
    #Step 1.2: JPL Mars Space Images - Featured Image
    ###########
    time.sleep(1)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(1)
    browser.find_by_id("full_image").click()
    time.sleep(1)
    browser.links.find_by_partial_text("more info").click()
    time.sleep(1)
    browser.find_by_css('.main_image').click()
    time.sleep(1)


    html = browser.html

    soup = BeautifulSoup(html,'html.parser')

    featured_image_url = soup.find('img')['src']
    #print(featured_image_url)
    the_one['featured_image'] = featured_image_url

    
    #########
    #Step 1.3: Mars Facts
    #########
    url = 'https://space-facts.com/mars/'
    ht_read = pd.read_html(url)[0].to_html()
    #pprint(ht_read)
    the_one['Mars Facts Table'] = ht_read


    ##########
    #Step 1.4: Mars Hemispheres
    ##########
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)

    html = browser.html


    soup = BeautifulSoup(html,'html.parser')

    hemi_names = [_.text for _ in soup.find_all('h3')]
    hemisphere_image_urls = []

    for name in hemi_names:
        browser.click_link_by_partial_text(name)
        time.sleep(2)
        soup = BeautifulSoup(browser.html,'html.parser')

        link = soup.find(string='Sample').parent['href']

        hemisphere_image_urls.append({"title":name,"img_url":link})
        time.sleep(2)
        browser.back()
        time.sleep(2)

    the_one['hemi_dict'] = hemisphere_image_urls
    
    return the_one




