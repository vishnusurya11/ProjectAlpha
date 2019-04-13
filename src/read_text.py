import os
import sys

a = os.path.abspath(__file__)
print(a)


b = os.getcwd()
print(b)

#using "../folder/filename" will go one directory above
with open('../data/data.csv','r') as c:
    print(c.read())