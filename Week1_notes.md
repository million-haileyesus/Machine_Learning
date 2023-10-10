f(x) = m*x + b
f(x) is y, x is x, m is the slope and b is the y-intercept.

To find the slope using the graph you calculate rise divided by run.



Cost function or Squared error cost function: (y_hat - y) = error
				sum from i = 1 to m ((y_hat(i) - y(i))^2) => Total square error
				m = number of training examples

			If we don't want get bigger as the training size gets bigger we divided it by m to get the average. 



GRADIENT DESCENT ALGORITHM

"=" is assignment and d is derivative.
alpha is a learning rate, which is always positive

w = w - alpha * (d/dw) * J(w,b) // What this does is it updates parameter w by a small amount, 
b = b - alpha * (d/db) * J(w,b) // in order to reduce the cost J.

We are simultaneously updating w and b.

temp_w = w - alpha * (d/dw) * J(w,b)
temp_b = b - alpha * (d/db) * J(w,b)

w = temp_w
b = temp_b

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

Linear regression model => f(w,b)(x) = wx + b

Gradient descent => 
$$w = w - &alpha * (1/m * sum from i = 1, to m (f(w,b)(x of (i)) - y of (i)) * x of (i)$$ => derived
b = b - alpha * (1/m * sum from i = 1, to m (f(w,b)(x of (i)) - y of (i)) => derived

Square error cost has only one global local minimum



