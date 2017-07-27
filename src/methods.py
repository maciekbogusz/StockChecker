'''
Created on 26.07.2017

@author: Maciek
'''
from lxml import html
import requests
from csv_writer import write_csv

def get_data(
    stock
    ):
    lower_index = stock.name.lower()
    page = requests.get('https://stooq.pl/q/?s='+lower_index)
    tree = html.fromstring(page.content)
    price = tree.xpath('//span[@id="aq_'+lower_index+'_c2|3"]/text()')
    return price
    
def put_dictionary(
        stock
        ):
    name = stock.name
    price = stock.getPrice() 
    my_dictionary = [name, price]
    return my_dictionary
    
def print_dictionary(
            dictionary
        ):    
   # write_csv(dictionary)
    print(dictionary)