# Array creation
To create a matrix with multiple rows, separate the rows with semicolons.
```matlab
a = [1 3 5; 2 4 6; 7 8 10];
```
Another way to create matrices is to use functions such as `ones`, `zeros`, or `rand`. For example, create a 5 × 1 column vector of zeros.
```matlab
z = zeros(5,1)
```
In addition, the colon operator allows you to create equidistant vector values using the more general format `start: step: end`.
```matlab
B = 0:10:100
```
# Matrix and array operations
MATLAB allows you to use a single arithmetic operator or function to process all the values in the matrix.
```matlab
a = [1 3 5; 2 4 6; 7 8 10];
a + 10
sin(a)
```
To transpose a matrix, use single quotes (') :
```matlab
a = [1 3 5; 2 4 6; 7 8 10];
a'
```
You can perform standard matrix multiplication using the `*` operator, which computes the inner product between rows and columns. For example, a confirmation matrix multiplied by its inverse returns the identity matrix:
```matlab
a = [1 3 5; 2 4 6; 7 8 10];
p = a*inv(a)
```
To perform element-level multiplication instead of matrix multiplication, use `.*` operator:
```matlab
a = [1 3 5; 2 4 6; 7 8 10];
p = a.*a
```
# Array indexing
Each variable in MATLAB is an array that can contain many numbers. If you want to access the selected elements of an array, use the index.    
There are two ways in specific reference array elements.The most common method is to specify rows and columns subscript, for example:
```matlab
A = [1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16];
A(4,2)
```
To reference multiple array elements, use the colon operator, which allows you to specify a range formatted as start: end. For example, list the elements in the first three rows and the second column of A:
```matlab
A = [1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16];
A(1:3,2)
```
A separate colon (with no starting or ending value) specifies all elements in the dimension. For example, select all columns in the third row of a:
```matlab
A = [1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16];
A(3,:)
```