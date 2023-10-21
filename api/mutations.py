from available_stock import stocks
from models.stock import Stock

from ariadne import convert_kwargs_to_snake_case


# Creates a new Book into the database.
@convert_kwargs_to_snake_case
def add_stock_resolver(obj, info, symbol, name, current_price, volume):    
	
	print("@@@@@@@@")
	# Creating a new Stock object from the parameters from the user.
	new_stock =  Stock(symbol, name, current_price, volume)
	stock_matching = [s for s in stocks if s.symbol.lower() == symbol.lower()]
	stock_found = None
	if len(stock_matching) > 0:
		stock_found = stock_matching[0]
	if stock_found is None:
		stocks.append(new_stock)
		return new_stock
	else:
		stock_found.update_volume(volume)
		stock_found.update_name(name)
		stock_found.update_price(current_price)
		stock_found.update_min_price(current_price)
		stock_found.update_max_price(current_price)
        
		return stock_found