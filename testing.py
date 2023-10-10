import os 
import pandas as pd 

with open("fhv_nyc.html","r") as nycdata:
    data=nycdata.read()
    print(data)

print(nycdata.closed)
