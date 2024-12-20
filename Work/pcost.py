sum=0
with open("Data/portfolio.csv") as f:
    next(f)
    for line in f:
        row=line.split(",")
        a=int(row[1])
        row2=row[2].split("\n")
        b=float(row2[0])
        sum+=a*b
        #sum+=int(row[1])*int(row[2])
print(f"The total cost is: {sum}")