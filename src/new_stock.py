'''
Created on 26.07.2017

@author: mcbg
'''
from stock import Stock
from methods import get_data, put_dictionary

newStock = Stock('PXM')
stock_price = get_data(newStock)

newStock.setPrice(stock_price)
put_dictionary(newStock)