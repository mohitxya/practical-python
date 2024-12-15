# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months=0
start=61
end=108
extra=1000
#he pays extra 1000 for first 12 months
while principal > 0:
    if months<end and months>start:
        principal = principal * (1+rate/12) - (payment+extra)
        total_paid = total_paid + payment+extra
        print(total_paid, principal)
    else:
        principal = principal * (1+rate/12) - (payment)
        total_paid = total_paid + payment
        print(round(total_paid,2), round(principal,2))
    months+=1
print('Total paid', total_paid)
print('Months',months)