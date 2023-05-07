MATLAB provides a number of functions that perform computational tasks.
# Call the functions
To call a function, such as `max`, enclose its input arguments in brackets(**not square brackets**):
```matlab
A = [1 3 5];
max(A)
```
If there are multiple input parameters, use commas to separate them:
```matlab
A = [1 3 5];
B = [3 6 9];
union(A,B)
```
Returns the output of a function by assigning it to a variable:
```matlab
A = [1 3 5];
maxA = max(A);
maxA
```
If there are multiple output parameters, enclose them in square brackets:
```matlab
A = [1 3 5];
[minA,maxA] = bounds(A)
```