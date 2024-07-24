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