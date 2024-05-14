# Logistic regression

$$f(W,b)(X) = W \cdot X + b$$

$$z = W \cdot X + b$$

$$g(z) = \frac{1}{1 + e^{-z}}$$

$$f(W,b)(X) = g(W \cdot X + b) = \frac{1}{1 + e^{-(W \cdot X + b)}}$$


# Decision boundary

$$f(W,b)(X) = W \cdot X + b$$

$$z = W \cdot X + b$$

$$g(z) = \frac{1}{1 + e^{-z}}$$

Non-linear decision boundaries

$$g(z) = g(w_1x_1^{2} + w_2x_2^{2} + b)$$ => The graph for $g(z)$ would be a circle


# Cost function for logistic regression

Linear regression:
$$f(W,b(X)) = W \cdot X + b$$

Squared error cost: The only difference is the 1/2 is put inside the summation
$$J(W,b) = \frac{1}{m} \left( \sum_{i = 1}^{m} \frac{1}{2}(f(W,b(X_{i}) - y_{i})^2 \right)$$
	 
Logistic loss function:

$$L(f(W,b(X_{i}, y_{i}))) = \begin{cases} -\log(f(W,b(X_{i}))) & \text{if } y_{i} = 1 \\ 
						-\log(1 - f(W,b(X_{i}))) & \text{if } y_{i} = 0 \end{cases}$$

Loss is lowest when $f(W,b(X_{i}))$ predicts close to true label $y_{i}$. for $y_{i} = 1$

The further prediction $f(W,b(X_{i}))$ is from target $y_{i}$, the higher the loss. for $y_{i} = 0$


# Simplified Cost Function for Logistic Regression

$$L(f(W,b(X_{i}, y_{i}))) = -y_{i} \cdot \log(f(W,b(X_{i}))) - (1 - y_{i}) \cdot \log(f(W,b(X_{i})))$$ => y can be 0 or 1

$$J(W,b) = \frac{1}{m} \left( \sum_{i = 1}^{m} L(f(W,b(X_{i}, y_{i})))^2 \right)$$

$$= -\frac{1}{m} \left( \sum_{i = 1}^{m} \left( y_{i} \cdot \log(f(W,b(X_{i}))) + (1 - y_{i}) \cdot \log(f(W,b(X_{i}))) \right)^2 \right)$$


# Gradient Descent Implementation

Cost function

$$J(W,b) =  -\frac{1}{m} \left( \sum_{i = 1}^{m} \left( y_{i} \cdot \log(f(W,b(X_{i}))) + (1 - y_{i}) \cdot \log(f(W,b(X_{i}))) \right)^2 \right)$$

Gradient descent

repeat {
  $$w_{j} = w_{j} - \alpha \cdot \frac{\partial}{\partial w_{j}} J(W, b)$$
  $$b = b - \alpha \cdot \frac{\partial}{\partial b} J(W, b)$$
}

$$\frac{\partial}{\partial w_{j}} J(W, b) = \frac{1}{m} \cdot \sum_{i = 1}^{m} (f_{(W,b)} (X_{i}) - y_{i}) \cdot x_{j}$$

$$\frac{\partial}{\partial b} J(W, b) = \frac{1}{m} \cdot \sum_{i = 1}^{m} (f_{(W,b)} (X_{i}) - y_{i})$$

repeat {
 $$w_{j} = w_{j} - \alpha \cdot \frac{1}{m} \cdot \sum_{i = 1}^{m} (f_{(W,b)} (X_{i}) - y_{i}) \cdot x_{j}$$

$$b = b - \alpha \cdot \frac{1}{m} \cdot \sum_{i = 1}^{m} (f_{(W,b)} (X_{i}) - y_{i})$$
}

We can monitor logistic logistic regression to converge as we do for gradient descent.


# The Problem of Overfitting

Regression example 

When the curves has less features it wouldn't fit the training set well it is called underfitting, which is also called high bias.

When the curves has many features it wouldn't fit the training set extremely well it is called overfitting, which is also called high variance.

Generalization is when we generlize a good feature or curve to fit the training set.

# Addressing Overfitting

There are 3 ways to address overfitting:
1. **Collecting more data:** this is not always ideal because data is always limited. 
2. **Feature selection:** selecting important feature from the input data.
 3. **Reducing size of parameters:** this includes using regularization. Applying regularization, increasing the number of training examples, or selecting a subset of the most relevant features are methods for addressing overfitting (high variance). It helps the model generalize better to new examples that are not in the training set.


# Cost Function with Regularization

$$\min_{W, b}[J(W, b)] = \min_{W, b}\left[\frac{1}{2m} \cdot \sum_{i = 1}^{m} (f_{(W,b)} (X^{(i)}) - y^{(i)})^2 + \left(\frac{\lambda}{2m}\right) \cdot \sum_{j = 1}^{n} (w_{j})^2\right]$$

The $\frac{\lambda}{2m} \cdot (\sum_{j = 1}^{n} (w_{j})^2)$ is the regularization term

lambda is a regularization parameter where it is greater 0.

If lambda is zero the model would overfit and if it is a large number it will underfit. If lambda increases the size of parameters w1, w2, wn wil decrease.


# Regularized Linear Regression

$$\min_{W, b}[J(W, b)] = \min_{W, b}\left[\frac{1}{2m} \cdot \sum_{i = 1}^{m} (f_{(W,b)} (X^{(i)}) - y^{(i)})^2 + \left(\frac{\lambda}{2m}\right) \cdot \sum_{j = 1}^{n} (w_{j})^2\right]$$


Gradient descent

for loop {
$$w = w - \alpha \cdot \frac{d}{dw} J(w,b)$$

$$b = b - \alpha \cdot \frac{d}{db} J(w,b)$$
}

Changed to the following below for gradient descent

for loop {
$$w = w_j - \alpha \cdot \left(\frac{1}{m} \cdot \sum_{i = 1}^m (f(W,b)(X_i) - y_i) \cdot X_j\right)$$

$$b = b - \alpha \cdot \left(\frac{1}{m} \cdot \sum_{i = 1}^m (f(W,b)(X_i) - y_i)\right)$$
}


Now with regularization it changes to 
for loop {
$$w = w_j - \alpha \cdot \left[\left(\frac{1}{m} \cdot \sum_{i = 1}^m (f(W,b)(X_i) - y_i) \cdot X_j\right) + \left(\frac{\lambda}{m}\right) \cdot w_{j}\right]$$

$$b = b - \alpha \cdot \left(\frac{1}{m} \cdot \sum_{i = 1}^m (f(W,b)(X_i) - y_i)\right)$$
}


# Regularized Logistic Regression

$$J(W, b) = -\frac{1}{m} \left( \sum_{i = 1}^{m} \left( y^{(i)} \cdot \log(f(W,b(X^{(i)}))) + (1 - y^{(i)}) \cdot \log(f(W,b(X^{(i)}))) \right)^2 \right) + \left(\frac{\lambda}{2m}\right) \cdot \sum_{j = 1}^{n} (w_{j})^2$$

Gradient descent

for loop {
$$w = w - \alpha \cdot \frac{d}{dw} J(w,b)$$

$$b = b - \alpha \cdot \frac{d}{db} J(w,b)$$
}

Changed to the following below for gradient descent

for loop {
$$w = w_j - \alpha \cdot \left(\frac{1}{m} \cdot \sum_{i = 1}^m (f(W,b)(X_i) - y_i) \cdot X_j\right)$$

$$b = b - \alpha \cdot \left(\frac{1}{m} \cdot \sum_{i = 1}^m (f(W,b)(X_i) - y_i)\right)$$
}

Now with regularization it changes to 
for loop {
$$w = w_j - \alpha \cdot \left[\left(\frac{1}{m} \cdot \sum_{i = 1}^m (f(W,b)(X_i) - y_i) \cdot X_j\right) + \left(\frac{\lambda}{m}\right) \cdot w_{j}\right]$$

$$b = b - \alpha \cdot \left(\frac{1}{m} \cdot \sum_{i = 1}^m (f(W,b)(X_i) - y_i)\right)$$
}

For regularized logistic regression the gradient descent update is the same with linear regression, except for the $$f(X)$$, which is the sigmoid (logistic) function, whereas for linear regression, $$f(X)$$ is a linear function.
