# Finding slope in a Graph
$$f(x) = m * x + b$$
f(x) is y, x is x, m is the slope and b is the y-intercept.

To find the slope using the graph you calculate rise divided by run.


# Cost Function or Squared Error Cost Function
y-hat is for the slope and y is for the error point from the slope.

Cost function or Error: 

$$\overline{y} - y$$

Total square error or sum of square error and m is number of training examples

Loss function:

$$\sum_{i = 1}^m (\overline{y} - y)^{2}$$

If we don't want our cost function to get bigger as our training size gets bigger, we should divided
our summation by m, which would get us the average.


# Gradient Descent Algorithm

"=" is assignment and d is derivative.
alpha is a learning rate, which is always positive

What this does is it updates parameter w by a small amount in order to reduce the cost J.
$$w = w - &alpha; * \frac{d}{dw} J(w,b)$$

$$b = b - &alpha; * \frac{d}{db} J(w,b)$$

We are simultaneously updating w and b.

$$w_{temp} = w - &alpha; * \frac{\partial}{\partial w} J(w,b)$$

$$b_{temp} = b - &alpha; * \frac{\partial}{\partial b} J(w,b)$$

$$w = w_{temp}$$

$$b = b_{temp}$$

We repeat the assignment of w and b until the algorithm converges, meaning the local 
min where the parameters w and b doesn't change much after each iteration.

If we have a parbolic graph of J(w), with J(w) as the y-axis and w as the
x-axis. If there is a point on the parbolic graph.

We would draw a tangent line or a straight line that touches the point and
The slope of that line is the derivative of the function J at that point.
To find the slope we use rise over ran.

This works the same with a negative slope also as we are getting close to zero

If alpha(learning rate) is too small the gradient descent may be slow or 
we might reach the minimum slowly. If it is too large, then the gradient 
descent may overshoot and never reach the minimum or go further away from
the minimum after each iteration or fail to converage or diverage.

If gradient descent is at a local min, it would stay at a local min not 
matter the size of the alpha.


# Linear regression model 
$$f(w,b)(x) = w * x + b$$

Gradient descent => both derived

$$w = w - &alpha; * (\frac{1}{m} * \sum_{i = 1}^m (f(w,b)(x_i) - y_i) * x_i)$$

$$b = b - &alpha; * (\frac{1}{m}  * \sum_{i = 1}^m (f(w,b)(x_i) - y_i))$$

Square error cost has only one global local minimum



