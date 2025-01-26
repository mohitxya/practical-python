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
#These statements should take the list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.
def make_report(portfolio,prices):
    final=[]
    pflio=portfolio
    # portfolio is a list [{name:hfh,shares: kdj, price:kjd},{},{}...so on]

    prce=prices
    # prce is a dictionary with keys and values.
    # we want a list of tuples.
    for i in range(len(pflio)):
        temp=pflio[i]['name']
        tup=(pflio[i]['name'],pflio[i]['shares'],prce[temp],prce[temp]-pflio[i]['price'])
        final.append(tup)
    headers = ('Name', 'Shares', 'Price', 'Change')

    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    separator = f"{'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s}"
    print(separator)
    for name, shares, price, change in final:
        print(f"{name:>10s} {shares:>10d} {f'${price:.2f}':>10s} {change:>10.2f}")

    
    
    
