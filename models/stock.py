class Stock:
    def __init__(self, symbol, name, current_price, volume, min_price=None, max_price=None):
        self.symbol = symbol
        self.name = name
        self.current_price = current_price
        self.volume = volume
        if min_price is None:
            self.min_price = current_price
        else:
            self.min_price = min_price
        if max_price is None: 
            self.max_price = current_price
        else:
            self.max_price = max_price

    def update_name(self, new_name):
        self.name = new_name
        
    def update_price(self, new_price):
        self.current_price = new_price

    def update_volume(self, new_volume):
        self.volume = new_volume

    def update_min_price(self, new_price):
        if self.min_price>new_price:
            self.min_price = new_price

    def update_max_price(self, new_price):
        if self.max_price < new_price:
            self.max_price = new_price

    def get_stock_info(self):
        info = f"Stock Symbol: {self.symbol}\n"
        info = f"Name: {self.name}\n"
        info += f"Current Price: {self.current_price}\n"
        info += f"Volume: {self.volume}\n"
        info += f"Min Price: {self.min_price}\n"
        info += f"Max Price: {self.max_price}\n"
        return info

# # Create an instance of the Stock class
# apple_stock = Stock("AAPL", 150.25, 1000000, 149.50, 152.75)

# # Update stock information
# apple_stock.update_price(151.00)
# apple_stock.update_volume(1200000)
# apple_stock.update_min_price(149.00)
# apple_stock.update_max_price(152.25)

# # Get and print the stock information
# stock_info = apple_stock.get_stock_info()
# print(stock_info)
   