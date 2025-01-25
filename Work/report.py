import csv

def read_portfolio(filename):
    portfolio=[]

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding={}
            holding['name']=row[0]
            holding['shares']=int(row[1])
            holding['price']=float(row[2])
            portfolio.append(holding)
    return portfolio

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost

def read_prices(filename):
    prices={}

    with open(filename,'rt') as f:
        rows=csv.reader(f)
        for row in rows:
            try:
                prices[row[0]]=float(row[1])
            except IndexError as e:
                continue
    return prices 
            
