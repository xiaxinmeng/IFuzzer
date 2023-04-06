from turtle import *

col = ["black", "white"]

for rad in range(40, 0, -1): 
    dot(5*rad, col[rad % 2])
    
done()