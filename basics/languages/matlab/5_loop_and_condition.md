Loops the `for` or `while` keyword, and conditional statements use `if` or `switch`.

# Loop

Loops are useful when creating sequences. For example, using a `for` loop to calculate the first 100 numbers of Fibonacci number. In this sequence, the first two numbers are 1, and each subsequent number is the sum of the first two numbers, $F(N) = F(N-1) + F(N-2)$.
```matlab
N = 100;
f(1) = 1;
f(2) = 1;

for n = 3:N
    f(n) = f(n-1) + f(n-2);
end
f(1:10)
```

# Condition
A conditional statement is executed only when the given expression is true. For example, a variable is assigned a value based on the size of the random number: 'Low' , 'medium' , or 'high' . In this case, the random number is an integer between 1 and 100.

```matlab
num = randi(100)
if num < 34
   sz = 'low'
elseif num < 67
   sz = 'medium'
else
   sz = 'high'
end
```
The statement `sz = ' high'` is executed only if num is greater than or equal to 67.