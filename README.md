# Python Regression 


<small> :cold_face: :cold_face: :space_invader: :space_invader: :robot: :robot: :see_no_evil: :see_no_evil: :kiss: :kiss: :hear_no_evil: :hear_no_evil: </small>


#### *Find a trend in data*

<hr />

Without diving deep into Scipy, this repo supports **fast** and **accurate** data trend analysis.

## Get Started

```
git clone https://github.com/Weilory/python-regression
```

place `regression` folder to base level directory. 

<hr />

```python
from regression.regress import regression

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
y = [1, 3.2, 5, 7.1, 9, 11, 13, 15.2, 17, 19.1, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

expression = regression(x=x, y=y)
print(expression.write)
# y = 2.0 * x**1 + 1.0
my_formula = expression.formula

print(my_formula(2))
# 5.0
```

<hr />

> ### if you know the general equation of the data, it will be faster and more accurate

<hr />


### Linear 

<a href="https://www.codecogs.com/eqnedit.php?latex=y=kx&plus;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y=kx&plus;b" title="y=kx+b" /></a>

```python
from regression.regress import linear_regression

x = [0, 1, 2, 3, -4, 5, 6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -18, 19]
y = [1, 3.2, 5, 7.1, 9, 11, 13, 15.2, 17, 19.1, 20, 22.5, 24.7, 26.3, 28.9, 31.2, 33.1, 34.3, 36.8, 38.7]

expression = linear_regression(x=x, y=y)
print(expression.write)
# y = 1.939 * x + 1.406
my_formula = expression.formula

print(my_formula(2))
# 5.284625463284197
```

![linear](https://github.com/Weilory/python-regression/blob/master/docs/img/linear.JPG)

<hr />

### Parabola 

<a href="https://www.codecogs.com/eqnedit.php?latex=y=2x^{2}&plus;3x&plus;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y=2x^{2}&plus;3x&plus;1" title="y=2x^{2}+3x+1" /></a>

```
from regression.regress import parabola_regression

x = [0, 1, 2, 3, -4, 5, 6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -18, 19]
y = [1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378, 435, 496, 561, 630, 703, 780]

expression = parabola_regression(x=x, y=y)
print(expression.write)
# y = 2.0 * x**2 + 3.0 * x**1 + 1.0
my_formula = expression.formula

print(my_formula(2))
# 15
```

![parabola](https://github.com/Weilory/python-regression/blob/master/docs/img/parabola.JPG)

<hr />

### Cubic Parabola 

<a href="https://www.codecogs.com/eqnedit.php?latex=y=0.5x^{3}&plus;2x^{2}&plus;3x&plus;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y=0.5x^{3}&plus;2x^{2}&plus;3x&plus;1" title="y=0.5x^{3}+2x^{2}+3x+1" /></a>

```
from regression.regress import cubic_regression

x = [0, 1, 2, 3, -4, 5, 6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -18, 19]
y = [1.0, 6.5, 19.0, 41.5, 77.0, 128.5, 199.0, 291.5, 409.0, 554.5, 731.0, 941.5, 1189.0, 1476.5, 1807.0, 2183.5, 2609.0, 3086.5, 3619.0, 4209.5]

expression = cubic_regression(x=x, y=y)
print(expression.write)
# y = 0.5 * x**3 + 2.0 * x**2 + 3.0 * x**1 + 1.0
my_formula = expression.formula

print(my_formula(2))
# 19.0
```
![cubic](https://github.com/Weilory/python-regression/blob/master/docs/img/cubic.JPG)

<hr />

> #### Notice that, 
>  * parabola
>  * cubic
>  * quadratic
> they have similarities such that 

<a href="https://www.codecogs.com/eqnedit.php?latex=y=ax^{n}&space;&plus;&space;bx^{n-1}&space;&plus;&space;cx^{n-2}..." target="_blank"><img src="https://latex.codecogs.com/gif.latex?y=ax^{n}&space;&plus;&space;bx^{n-1}&space;&plus;&space;cx^{n-2}..." title="y=ax^{n} + bx^{n-1} + cx^{n-2}..." /></a>

> they are categorised as `Exponential Parabola`, with a specification to maximum `x exponential`, for the `cubic` function exampled above, instead, we can write following:

### Exponential Parabola 

<a href="https://www.codecogs.com/eqnedit.php?latex=y=ax^{n}&space;&plus;&space;bx^{n-1}&space;&plus;&space;cx^{n-2}..." target="_blank"><img src="https://latex.codecogs.com/gif.latex?y=ax^{n}&space;&plus;&space;bx^{n-1}&space;&plus;&space;cx^{n-2}..." title="y=ax^{n} + bx^{n-1} + cx^{n-2}..." /></a>

```python
from regression.regress import exponential_parabola_regression

x = [0, 1, 2, 3, -4, 5, 6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -18, 19]
y = [1.0, 6.5, 19.0, 41.5, 77.0, 128.5, 199.0, 291.5, 409.0, 554.5, 731.0, 941.5, 1189.0, 1476.5, 1807.0, 2183.5, 2609.0, 3086.5, 3619.0, 4209.5]

expression = exponential_parabola_regression(x=x, y=y, x_exp=3)
print(expression.write)
# y = 0.5 * x**3 + 2.0 * x**2 + 3.0 * x**1 + 1.0
my_formula = expression.formula

print(my_formula(2))
# 19.0
``` 

> this method support any positive integer as max x exponential.

<hr />

### Truncus 

<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;\frac{1}{(4x&plus;1)^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;\frac{1}{(4x&plus;1)^2}" title="y = \frac{1}{(4x+1)^2}" /></a>

```
from regression.regress import truncus_regression

x = [0, 1, 2, 3, -4, 5, 6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -18, 19]
y = [1.0, 0.04, 0.012345679012345678, 0.005917159763313609, 0.0034602076124567475, 0.0022675736961451248, 0.0016, 0.0011890606420927466, 0.0009182736455463728, 0.0007304601899196494, 0.000594883997620464, 0.0004938271604938272, 0.00041649312786339027, 0.000355998576005696, 0.0003077870113881194, 0.0002687449610319806, 0.00023668639053254438, 0.00021003990758244065, 0.00018765246762994934, 0.00016866250632484398]

expression = truncus_regression(x=x, y=y)
print(expression.write)
# y ** 1 = 1 / (16.0 * x**2 + 8.0 * x**1 + 1.0)
my_formula = expression.formula

print(my_formula(2))
# 0.012345679012345675
```

![Truncus](https://github.com/Weilory/python-regression/blob/master/docs/img/truncus.JPG)

<hr />

> #### Notice that, 
>  * truncs general equation 

<a href="https://www.codecogs.com/eqnedit.php?latex=y^{y_{exp}}&space;=&space;\frac{product}{ax^n&plus;bx^{n-1}&plus;..}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y^{y_{exp}}&space;=&space;\frac{product}{ax^n&plus;bx^{n-1}&plus;..}" title="y^{y_{exp}} = \frac{product}{ax^n+bx^{n-1}+..}" /></a>

>  * when we know the power on y, the product, the maximum power on x, we can use `Inverse Exponential Parabola`
>  * take the truncs above as an example, where `y_exp=1`, `product=1`, 'x_exp=2'

### Inverse Exponential Parabola

```
from regression.regress import inverse_exponential_regression

x = [0, 1, 2, 3, -4, 5, 6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -18, 19]
y = [1.0, 0.04, 0.012345679012345678, 0.005917159763313609, 0.0034602076124567475, 0.0022675736961451248, 0.0016, 0.0011890606420927466, 0.0009182736455463728, 0.0007304601899196494, 0.000594883997620464, 0.0004938271604938272, 0.00041649312786339027, 0.000355998576005696, 0.0003077870113881194, 0.0002687449610319806, 0.00023668639053254438, 0.00021003990758244065, 0.00018765246762994934, 0.00016866250632484398]

expression = inverse_exponential_regression(x=x, y=y, x_exp=2, y_exp=1, product=1)
print(expression.write)
# y ** 1 = 1 / (16.0 * x**2 + 8.0 * x**1 + 1.0)
my_formula = expression.formula

print(my_formula(2))
# 0.012345679012345675
```
