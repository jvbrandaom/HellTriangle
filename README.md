# HellTriangle
Given a triangle of numbers, find the maximum total from top to bottom

Example: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 5  
&nbsp;&nbsp;&nbsp;&nbsp;9 7 1  
&nbsp;&nbsp;&nbsp;4 6 8 4  

In this triangle the maximum total is 6 + 5 + 7 + 8 = 26 
 
An element can only be summed with one of the two nearest elements in the next row 
So the element 3 in row 2 can be summed with 9 and 7, but not with 1 

The code will receive an (multidimensional) array as input. 
The triangle from above would be: 
 
example = [[6],[3,5],[9,7,1],[4,6,8,4]]
 
## Running

You need Python 3.5 or higher in order to run this script

Open terminal and run the following command:
```
python HellTriangle.py "[[6],[3,5],[9,7,1],[4,6,8,4]]"
```

## Running Tests

Open terminal and run the following command::

```
python -m unittest -v TestHellTriangle
```