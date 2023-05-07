# line graph
To create a two-dimensional line graph, use the plot function. For example, a sine function drawn on a vector of linear intervals from 0 to 2π:
```matlab
x = linspace(0,2*pi);
y = sin(x);
plot(x,y)
```
By default, MATLAB clears the drawing window every time a drawing function is called, and coordinates and other elements are reset in preparation for a new drawing.

To add a drawing to an existing drawing window, use hold on. All the drawings are displayed in the current diagram window before you use hold off or close the window.
```matlab
x = linspace(0,2*pi);
y = sin(x);
plot(x,y)

hold on

y2 = cos(x);
plot(x,y2,":")
legend("sin","cos")

hold off
```

# Multiple drawings

You can use tiledlayout or subplot to display multiple plots in different parts of the same window.

The `tiledlayout` function, introduced in R2019B, provides more control over tags and spacing than subplot. For example, create a 2 × 2 layout in a diagram window. Then, whenever you want a drawing to appear in the next area, call `nexttile`.
```matlab
t = tiledlayout(2,2);
title(t,"Trigonometric Functions")
x = linspace(0,30);

nexttile
plot(x,sin(x))
title("Sine")

nexttile
plot(x,cos(x))
title("Cosine")

nexttile
plot(x,tan(x))
title("Tangent")

nexttile
plot(x,sec(x))
title("Secant")
```
`subplot` can do the similar thing:
```matlab
subplot(2,2,1)
x = linspace(0,10);
y1 = sin(x);
plot(x,y1)
title('Subplot 1: sin(x)')

subplot(2,2,2)
y2 = sin(2*x);
plot(x,y2)
title('Subplot 2: sin(2x)')

subplot(2,2,3)
y3 = sin(4*x);
plot(x,y3)
title('Subplot 3: sin(4x)')

subplot(2,2,4)
y4 = sin(8*x);
plot(x,y4)
title('Subplot 4: sin(8x)')
```

# New diagram
Just use figure to start a new window:
```matlab
x = linspace(0,2*pi);
y = sin(x);
plot(x,y)

figure

y2 = cos(x);
plot(x,y2,":")

hold off
```