import time
import requests #(IP address connected + URL)
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import numpy as np



            #  Web Scraping Essential Jewellry #
#Adapted code from Week-5-Web-data-and-generative-text, available at: https://git.arts.ac.uk/tbroad/web-scrape-nursery-rhymes/commit/da77acf4524ab39b2476c1a6d5feddad888375f9.
# Create my own code that scrapes Essential Jewellry, taking into account the formatting of the HTML, cleans out the data and sorts this into a data frame. 

# list all jewellry from which all HTML data will be stored, depending on the category of jewellry.

rings = []
earrings =[]
wristwear =[]
neckwear =[]
body_jewellry =[]
chains =[]

#call rings: 
for page in range(1, 15): #there are 13 pages in total
    url1 = f'https://essentialjewellery.com/collections/all-rings' #stores website to variable url.

    # retrieve the HTML content...
    response = requests.get(url1)
    
    html_content = response.content

    # parse the HTML content using BeautifulSoup...
    soup = BeautifulSoup(html_content, 'html.parser')

# Find  product items and extract the price and title
    product_items = soup.find_all( class_='product-item') #class found using by analysing the structure of the web HTML.
    for item in product_items:
        product_name = item.find('a', class_='product-item-meta__title').text
        product_price = item.find('span', class_='price').text
        
             #append the above ring list to add the price and product name
        rings.append([product_name, product_price]) # the 'ring' variable contains a list of all the rings and their sale price.

    time.sleep(1) #code from https://www.geeksforgeeks.org/sleep-in-python/. This code adds a delay in my request for pricing data, Essential's website has a terms of service which mentions to not overload servers with too many requests. Without the following code,my code produced an error output.


    #call wristwear:
for page in range(1, 8): #there are 7 pages in total
    url2 = f'https://essentialjewellery.com/collections/all-wristwear' #stores website to variable url.

        # retrieve the HTML content from url.
    response = requests.get(url2)
        
    html_content = response.content

        # parse the HTML 
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find product items and extract the price and title
    product_items = soup.find_all( class_='product-item') #class found using by analysing the structure of the web HTML.
    for item in product_items:
        product_name = item.find('a', class_='product-item-meta__title').text
        product_price = item.find('span', class_='price').text
            
                #append the above ring list to add the price and product name
        wristwear.append([product_name, product_price]) # the 'ring' variable contains a list of all the rings and their sale price.

    time.sleep(1) 


    #call earrings:
for page in range(1, 29): #there are 28 pages in total
    url3 = f'https://essentialjewellery.com/collections/all-earrings' #stores website to variable url.

        # retrieve the HTML content from url.
    response = requests.get(url3)
        
    html_content = response.content

        # parse the HTML 
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find product items and extract the price and title
    product_items = soup.find_all( class_='product-item') #class found using by analysing the structure of the web HTML.
    for item in product_items:
        product_name = item.find('a', class_='product-item-meta__title').text
        product_price = item.find('span', class_='price').text
            
                #append the above ring list to add the price and product name
        earrings.append([product_name, product_price]) # the 'ring' variable contains a list of all the rings and their sale price.

        time.sleep(1)


    #call neckwear
for page in range(1, 15):
    url4 =  f'https://essentialjewellery.com/collections/all-neckwear'
 # retrieve the HTML content from url.
    response = requests.get(url3)
    
    html_content = response.content

    # parse HTML 
    soup = BeautifulSoup(html_content, 'html.parser')

# Find  product items and extract the price and title
    product_items = soup.find_all( class_='product-item') #class found using by analysing the structure of the web HTML.
    for item in product_items:
        product_name = item.find('a', class_='product-item-meta__title').text
        product_price = item.find('span', class_='price').text
        
             #append the above ring list to add the price and product name
        neckwear.append([product_name, product_price])
        time.sleep(1)


#call body_jewellry
for page in range(1, 6):
    url5 =  f'https://essentialjewellery.com/collections/all-body-jewellery'
 
 # retrieve HTML content
    response = requests.get(url5)
    
    html_content = response.content

    # parse 
    soup = BeautifulSoup(html_content, 'html.parser')

# Find  product items and extract the price and title
    product_items = soup.find_all( class_='product-item') #class found using by analysing the structure of the web HTML.
    for item in product_items:
        product_name = item.find('a', class_='product-item-meta__title').text
        product_price = item.find('span', class_='price').text
        
             #append the above ring list to add the price and product name
        body_jewellry.append([product_name, product_price])
        time.sleep(1)


#call chains
for page in range(1, 2):
    url6 =  f'https://essentialjewellery.com/collections/cartilage-and-helix'
 # retrieve the HTML content from url.
    response = requests.get(url6)
    
    html_content = response.content

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

# Find  product items and extract the price and title
    product_items = soup.find_all( class_='product-item') #class found using by analysing the structure of the web HTML.
    for item in product_items:
        product_name = item.find('a', class_='product-item-meta__title').text
        product_price = item.find('span', class_='price').text
        
             #append the above ring list to add the price and product name
        chains.append([product_name, product_price]) # the 'ring' variable contains a list of all the rings and their sale price.
        time.sleep(1)


df_rings = pd.DataFrame(rings, columns=['Product Name', 'Sale price'])
df_earrings= pd.DataFrame(earrings, columns=['Product Name', 'Sale price'])
df_wristwear= pd.DataFrame(wristwear, columns=['Product Name', 'Sale price'])
df_neckwear= pd.DataFrame(neckwear, columns=['Product Name', 'Sale price'])
df_body_jewellry= pd.DataFrame(body_jewellry, columns=['Product Name', 'Sale price'])
df_chains= pd.DataFrame(chains, columns=['Product Name', 'Sale price'])

# Combine the above data using pandas. code adapted from https://realpython.com/pandas-merge-join-and-concat/.
dataframe =[df_rings,df_earrings,df_wristwear,df_neckwear, df_body_jewellry, df_chains ]
df_combine = pd.concat (dataframe, ignore_index=True) #used an 'ignore_index',within the concatination function, which creates a Boolean value. 

print(df_combine)

