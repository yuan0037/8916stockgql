#GraphQL Stock Service

This project is based on flask and ariadne. 

## Installation

1. Clone/Download repo
2. Open the project in VS Code. 
3. In VS Code, open the Command Palette (View > Command Palette or (⇧⌘P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment (Python V3.x) you want to use to create it.
4. Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
| |────api/
| | |────__init__.py
| | |────mutations.py
| | |────queries.py
| |────models/
| | |────__init__.py
| | |────stock.py
|──────app.py
|──────available_stock.py

```
5. Run the app
python app.py

6. Use the app

Once it is launched, the graphql client GUI tool can be accessied by http://127.0.0.1:5000/graphql 

##Query:

###Get Stock List
```
{
  getStocks {
    symbol
    name
    currentPrice
    minPrice
    maxPrice
  }
}
```

###Get A Certain Stock (stock price will be a randomized as well as the volume)
```
{
  getStock(symbol:"AAPL") {
    symbol
    name
    volume
    currentPrice
    minPrice
    maxPrice
  }
}
```

###Add Stock
```
mutation{
    addStock(symbol:"NVDA", name:"Nvidia", currentPrice:33.33, volume: 3000) {
    symbol
    name
    currentPrice
    minPrice
    maxPrice
  }
}
``` 