from available_stock import stocks
import random

def update_stock_data(stock):
    stock.current_price = round(random.uniform(10, 500.0), 2)
    stock.volume = random.randint(1, 5000)
    stock.update_min_price(stock.current_price)
    stock.update_max_price(stock.current_price)
    return stock

def get_stock_resolver(obj, info, symbol):        
    stock_matching = [s for s in stocks if s.symbol.lower() == symbol.lower()]
    stock_found = None
    if len(stock_matching) > 0:
        stock_found = stock_matching[0]
        stock_found = update_stock_data(stock_found)
    return stock_found

def get_stocks_resolver(obj, info):
    return stocks
