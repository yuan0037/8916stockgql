#GraphQL Stock Service

This project is based on flask and ariadne. Once it is launched, the graphql client GUI tool can be accessied by http://127.0.0.1:5000/graphql 

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