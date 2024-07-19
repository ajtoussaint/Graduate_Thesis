- [[Numerical Computation]] is the use of an algorithm to solve an equation by incrementally updating an estimate of the correct answer until you can be sure that it is correct within a certain margin of error
	- The process is optimized by finding the min or max of a function by changing the input. Typically the min is used and if you want to find the max just multiply by -1
	- [[System of Linear Equations]] must be solved to optimize
	- Computers will always have some level of approximation error in this process because a continuous $\mathbb{R}$eal number cannot be exactly represented with bits
## 4.1 Overflow and Underflow
- [[Underflow]] occurs when a small number is rounded to 0
	- Causes divide by 0 errors and also errors when attempting to take the log of 0
- [[Overflow]] occurs when a large number is rounded to $\frac{+}{-}\infty$ and causes similar errors
- [[Softmax]] function is used to stabilize against [[Underflow]] and [[Overflow]]
	- $softmax(x)_i = \frac{exp(x_i)}{\sum^{n}_{j=1} exp(x_j)}$ 
	- If all $x_i$ are the same and there are very many $x_i$ then $exp(x_i)$ may [[Underflow]]
		- To solve this instead use $z =x - max_i x_i$ and solve $softmax(z)$ instead. Therefore the largest argument is 0 and the denominator will sum to 1
		- Adding a [[Scalar]] value to softmax doesn't change the result
	- log(softmax(x)) may still cause underflow but this can be fixed in the same way
	- Usually a code library will handle all of this stabilization
## 4.2 Poor Conditioning
- [[Conditioning]] is how rapidly a function responds to input changes. (How much does a small change on input impact the output)
	- [[Conditioning Number]] is the ratio of the largest to the smallest [[Eigenvalue]] in a [[Matrix]]
		- When the CN is large the matrix is input sensitive and therefore has poor conditioning

## 4.3 Gradient-Based Optimization
- The [[Objective Function]] aka the criterion is the function f(x) that we desire to optimize
	- aka cost/loss/error
	- $x^*$ is the theoretical optimal value for this function
	- We can use the derivative to determine what changes need to be made to the function input to optimize the output
- [[Gradient Descent]] (aka slope descent) is an algorithm for optimizing an [[Objective Function]] by moving the input value small steps opposite the direction of the function's derivative (in the common case of minimization).
	- $x' = x - \epsilon\nabla_xf(x)$ where $\epsilon$ is some small value aka [[Learning Rate]], $x'$ represents the new value of x after moving along the gradient and $x$ represents the original value
		- Chose $\epsilon$ to be a positive small constant [[Scalar]] that causes the [[Directional Derivative]] to vanish when minimizing the [[Objective Function]]
		- [[Line Search]] is a version of [[Gradient Descent]] where $\epsilon$ is chosen from one of several values such that it minimizes the [[Objective Function]]
		- You can also choose $\epsilon$ according to $\epsilon^*=g^Tg/g^TH$ where g is the [[Gradient]] and H is the [[Hessian]] to prevent [[Curvature]] from ruining your descent
	- The method converges when every element of $\nabla \approx 0$
	- [[Hill Climbing]] is [[Gradient Descent]] generalized to discrete spaces
	- Optimization methods that only consider the first derivative are [[First Order Optimization]]
- [[Critical Point]] is a point on a function where $f'(x) = 0$ so there is no information about which direction needs to be traveled. 
	- For an n-dimensional function the point occurs when each $\nabla = 0$ 
	- Can be a local min/max or a saddle point
	- Local min/max makes it no longer possible to use the incremental approach and _may_ be the true optimal solution.
	- Often times you will need to settle for a good low point that is not the global minimum
	- For functions with multiple input variables the partial derivatives are each analyzed independently
- [[Gradient]] is a vector containing all the partial first derivatives of a function
	- $\nabla_xf(x)$
- The [[Directional Derivative]] of a function represents the slope of that function along a given direction
	- The reason for traveling opposite the [[Gradient]] in [[Gradient Descent]] is explained below:
	- The derivative of $f(x +\alpha u)$ with respect to $\alpha$ where $u$ is the [[Unit]] [[Vector]] of the direction and $\alpha=0$ so the derivative is $u^T\nabla_xf(x)$ 
	- The above derivative is minimized to find the descent direction: $min \lVert u \rVert_2 \lVert\nabla f(x)\rVert_2 cos(\theta)$ where $\theta$ is the angle between $u$ and the direction of descent
		- Theta will be the opposite direction of the gradient to minimize
- The [[Jacobian]] [[Matrix]] contains the partial derivatives of a function that has [[Vector|vectors]] as the inputs and outputs of the function
	- The function:$f:\mathbb{R}^m \to \mathbb{R}^n$ 
	- Jacobian: $J \in \mathbb{R}^{n\times m}$ such that $J_{i,j} = \frac{\partial}{\partial x_j}f(x)_i$ 
- [[Curvature]] is the term used to describe the second derivative of a function. It relates the magnitude of the improvement that will be obtained by following the gradient
	- The curvature can be used to determine what type of [[Critical Point]] a function is at: positive is a relative minimum, negative is a relative maximum, 0 is not necessarily a saddle point, the type cannot be determined. This is called the [[Second Derivative Test]]
- A [[Hessian]] [[Matrix]] contains the second derivatives for a function with n input dimensions
	- $H(f)(x)_{i,j} = \frac{\partial^2}{\partial x_j \partial x_i}f(x)$ 
	- This is the [[Jacobian]] of the [[Gradient]]
	- The Hessian is [[Symmetric]] when the 2nd partial derivative is continuous (which is usually everywhere)
	- Because Hessian is real and Symmetric it decomposes into [[Eigenvalue|eigenvalues]] and an [[Orthogonal]] basis of [[Eigenvector|eigenvectors]] ([[Eigendecomposition]])
	- When using the [[Second Derivative Test]]
		- A [[Positive]] [[Definite]] [[Hessian]] is a local minimum
		- A [[Negative]] [[Definite]] [[Hessian]] is a local maximum
		- When [[Eigenvalue|eigenvalues]] are mixed signs then the point is some type of saddle point
		- If the matrix is [[Semidefinite]] and the signs are not mixed then the result is inconclusive
	- The [[Conditioning Number]] of a [[Hessian]] measures how much the 2nd derivatives differ at a given point
		- [[Gradient Descent]] works best when conditioning is good
	- Optimization methods that involve the [[Hessian]] are [[Second Order Optimization]]
- [[Newton's Method]] is a form of[[Gradient Descent]] that uses information in the [[Hessian]] to guide the descent
	- $x^*=x^{(0)}-H(f)(x^{(0)})^{-1}\nabla_xf(x^{(0)})$ can be applied to jump directly to the minimum if f is quadratic
	- If f approximates a  quadratic this approach can be applied iteratively
	- This is faster than [[Gradient Descent]] but can get stuck on saddle points
- [[Lipschitz Continuous Function]] is a function whos rate of change is bound by $\mathcal{L}$ (the Lipschitz Constant)
	- $\forall x, \forall y, \lvert f(x) - f(y) \rvert \le \mathcal{L} \lVert x - y \rVert_2$ 
	- qualifies that a small change in input can only result in a small change in output
	- Any problem can be modified to adhere to a Lipschitz Constant
- [[Convex Optimization]] is achieved when the [[Objective Function]] always has a [[Positive]] [[Semidefinite]] [[Hessian]] (convex hessian) and therefore no saddle points exist
	- All local minimums are global minimums
	- hard to fit to a deep learning problem
## 4.4 Constrained Optimization
- [[Constrained Optimization]] is a type of optimization problem where the [[Objective Function]] is restricted to only a specified set of inputs and the optimal input within this set must be determined.
	- [[Feasible Point]] is a point within the subset $\mathbb{S}$ that may be applied to the function
	- Use [[Line Search]] [[Gradient Descent]] to adjust the [[Learning Rate]], $\epsilon$, so that only values in $\mathbb{S}$ are iterated through
	- Could also use a transformation to modify the original problem arithmetically and change the solution space
- The [[Karush-Kuhn-Tucker Approach]] is a method for solving [[Convex Optimization]] problems
	- Define $\mathbb{S}$ such that $\mathbb{S} = \{x|\forall i, g^{(i)}(x) = 0$ and $\forall j, h^{(j)}(x) \le 0\}$  
	- the $g^{(i)}$ equations are equality constraints
	- the $h^{(i)}$ are inequality constraints. Inequality constraints are only active if $h^{(i)}(x^*) = 0$ 
		- If a constraint is not active then the solution found using that constraint would remain at least a local solution if that constraint were removed.
		- For all $i$ at least one of the constraints $\alpha_i \ge 0$ or $h^{(i)}(x) \le 0$ must be "active"
	- Define a generalized [[Lagrangian]]: $L(x, \lambda, \alpha) = f(x) + \sum_i \lambda_i g^{(i)}(x) + \sum_i \alpha_j h^{(j)}(x)$ 
		- This is a single function that incorporates the original [[Objective Function]] as well as the [[Constrained Optimization|constraints]] into a single function
		- As long as there are [[Feasible Point|feasible points]] where $x \ne \infty$ the [[Constrained Optimization]] problem can be solved by solving the unconstrained [[Lagrangian]]
	- 
	- The optimal solution will be on a boundary of the constraint or constraining the problem makes no difference than finding an unconstrained solution.
	- The solution is found when $\nabla Lagrange = 0$ , all constraints are satisfied, and $\alpha \odot h(x) = 0$ 
## 4.5 Example: Linear Least Squares
Find the value of x that minimizes $f(x) = \frac{1}{2}\lVert Ax - b\rVert^2_2$ 
1. Define the [[Gradient]]: $\nabla_xf(x)=A^T(Ax-b) = A^TAx-A^Tb$ 
2. Set [[Learning Rate]] $\epsilon$ and error tolerance $\delta$ to small positive values
3. Follow the following algorithm:
	- while $\lVert A^T Ax-A^Tb\rVert_2 > \delta$ do:
		- $x \gets x - \epsilon (A^TAx-A^Tb)$ 
	- end while
Could also just use [[Newton's Method]]

Constrained version where $x^Tx \le 1$ 
1. Define the [[Gradient]]: $\nabla_xf(x)=A^T(Ax-b) = A^TAx-A^Tb$ 
2. Introduce [[Lagrangian]]: $L(x, \lambda) = f(x) + \lambda (x^Tx-1)$ 
3. Use [[Moore-Penrose Pseudoinverse]] $x=A^+b$ to solve
4. Differentiate [[Lagrangian]]: $A^TAx-A^Tb+2\lambda x = 0$ 
	- therefore: $x = (A^TA+2\lambda I)^{-1}A^Tb$ 
5. Perform [[Gradient Descent]] on $\lambda$ 
	- $\frac{\partial}{\partial \lambda}L(x, \lambda) = x^Tx-1$ 

From chat gpt:
```
import numpy as np

def projected_gradient_descent(A, b, x0, alpha, tol, max_iter):
    x = x0
    for i in range(max_iter):
        gradient = A.T @ (A @ x - b)
        x_new = x - alpha * gradient
        
        if np.linalg.norm(x_new)**2 > 1:
            x_new = x_new / np.linalg.norm(x_new)
        
        if np.linalg.norm(x_new - x) < tol:
            break
        
        x = x_new
    
    return x

# Example usage:
A = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])
x0 = np.array([0.5, 0.5])
alpha = 0.01
tol = 1e-6
max_iter = 1000

x_opt = projected_gradient_descent(A, b, x0, alpha, tol, max_iter)
print(x_opt)

```