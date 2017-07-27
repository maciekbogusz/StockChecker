'''
Created on 26.07.2017

@author: mcbg
'''
from methods import get_data, put_dictionary, print_dictionary
from stock import Stock

newStock = Stock('PXM')
stockPrice =  get_data(newStock)

newStock.setPrice(stockPrice)
result = put_dictionary(newStock)

print_dictionary(result)