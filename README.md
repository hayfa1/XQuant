# Checking a number presence in a matrix

Given an 10*10 matrix where each cell has random degits.
In this example we used the given example in the assignement. You can generate a random matrix like this :
 code: 

```python

np.random.randint(10, size=(10,10))

```

The script will count the number of times a given number can be found in the table, and the coordinate of the cells where the number is found. 
The idea is looking for the first digit of the input sequence and then chechking it's neighbours. so if we are at location (x,y) and the first digit was found,
we serach in (x,y+1) (x,y-1), (x+1,y) or (x-1,y) for the second digit of the sequence
if the next digit at the distination cell is found than we can pass to the next cell  and do the same research.


system info:

- windows 10
- python 3.8.3





update pip:
```bash
pip install --upgrade pip
```
install requirements:
```bash
pip install numpy
```



## usage



```bash
python3 test.py 
```




