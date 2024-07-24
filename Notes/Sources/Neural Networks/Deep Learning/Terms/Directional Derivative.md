- The [[Directional Derivative]] of a function represents the slope of that function along a given direction
	- The reason for traveling opposite the [[Gradient]] in [[Gradient Descent]] is explained below:
	- The derivative of $f(x +\alpha u)$ with respect to $\alpha$ where $u$ is the [[Unit]] [[Vector]] of the direction and $\alpha=0$ so the derivative is $u^T\nabla_xf(x)$ 
	- The above derivative is minimized to find the descent direction: $min \lVert u \rVert_2 \lVert\nabla f(x)\rVert_2 cos(\theta)$ where $\theta$ is the angle between $u$ and the direction of descent
		- Theta will be the opposite direction of the gradient to minimize