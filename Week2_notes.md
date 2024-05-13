# Multiple features (variables)

$$f(W,b)(x) = W_{1}X_{1} + W_{2}X_{2} + \cdots + W_{n}X_{n} + b$$

W(is a vector) = [w1, w2, ... , wn]
X(is a vector) = [x1, x2, ... , xn]

$$f(W,b)(X) = W \cdot X + b$$ => multiple linear regression


# Vector notation for gradient descent

$$f(W,b)(X) = W \cdot X + b$$

Gradient descent

for loop {
	w = w - alpha (d/dw) J(W,b)
	b = b - alpha (d/db) J(W,b)
}

or 

for loop {
	w of (1) = w of (1) - alpha (1/m * sum from i = 1, to m (f(W,b)(X of (i)) - y of (i)) * x of (i) => J = 1
	...
	w of (n) = w of (n) - alpha (1/m * sum from i = 1, to m (f(W,b)(X of (i)) - y of (i)) * x of (i) => J = n

	b = b - alpha (1/m * sum from i = 1, to m (f(W,b)(X of (i)) - y of (i))
}


# Feature Scaling

To rescale large or small number, we divide each values by the max value for that 
feature.

Example:- -0.00001 < x < 0.001 => rescale it to -0.01 < x < 1

Example:- -100 < x < 100 => rescale it to -1 < x < 1


# Checking gradient descent for convergence

Making sure graident descent is working correctly means the J(W,b) is being minimized
after each iteration. When the gradient descent converges it means the curve of the
J(W,b) is almost flat and cannot take a noticable decrease in the graph. This method
is one way to check when our model is done training.

Another way is to use Automatic convergence test. Let epsilon(e) be 0.001, if J(W,b)
decreases by <= e in one iteration, then declare convergence (found parameter W,b to
get close to global minimum).


# Choosing the learning rate

If the alpha is too big, the function would diverge. To make sure J(W,b) 
decrease and don't have a bug in the code, try alpha with smaller number, 
which would decrease J(W,b) and if it doesn't that means there is a bug 
in your code. 


# Feature engineering

$$f(W,b)(x) = W_{1}X_{1} + W_{2}X_{2} + b$$

$$Area = X_{1} * X_{2}$$

$$X_{3} = X_{1} * X_{2}$$

New feature

$$f(W,b)(x) = W_{1}X_{1} + W_{2}X_{2} + W_{3}X_{3} + b$$

Feature engineering:- using intuition to design new features, by 
transforming or combining original features.


# Polynomial regression

If a curve fits the data model rather than a straight line, we 
could use a quadratic or cubic lines.

$$f(W,b)(x) = W_{1}X_{1} + W_{2}(X_{2})^2 + b$$
or
$$f(W,b)(x) = W_{1}X_{1} + W_{2}(X_{2})^2 + W_{3}(X_{3})^3 + b$$
