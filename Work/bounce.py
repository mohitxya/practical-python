# bounce.py
# starts from 100 and height reduces to 3/5th every bounce
# Exercise 1.5
height=100
for i in range(10):
    height=height*3/5
    print(round(height,4))