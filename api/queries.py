from available_stock import stocks

def get_stock_resolver(obj, info, symbol):        
    stock_matching = [s for s in stocks if s.symbol.lower() == symbol.lower()]
    stock_found = None
    if len(stock_matching) > 0:
        stock_found = stock_matching[0]
    return stock_found

def get_stocks_resolver(obj, info):
    return stocks
