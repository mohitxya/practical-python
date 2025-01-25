import csv
import sys

def portfolio_cost(file):
    sum=0
    try:
        with open(file) as f:
            rows=csv.reader(f)
            headers=next(rows)
            for line in rows:
                sum+=float(line[1])*float(line[2])
    except FileNotFoundError:
        print("Please enter a legit file name")
    return sum

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
