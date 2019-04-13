import os
import sys

a = os.path.abspath(__file__)
print(a)


b = os.getcwd()
print(b)

with open('../data/data.csv','r') as c:
    print(c.read())