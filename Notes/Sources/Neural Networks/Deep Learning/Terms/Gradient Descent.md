- [[Gradient Descent]] (aka slope descent) is an algorithm for optimizing an [[Objective Function]] by moving the input value small steps opposite the direction of the function's derivative (in the common case of minimization).
	- $x' = x - \epsilon\nabla_xf(x)$ where $\epsilon$ is some small value aka [[Learning Rate]], $x'$ represents the new value of x after moving along the gradient and $x$ represents the original value
		- Chose $\epsilon$ to be a positive small constant [[Scalar]] that causes the [[Directional Derivative]] to vanish when minimizing the [[Objective Function]]
		- [[Line Search]] is a version of [[Gradient Descent]] where $\epsilon$ is chosen from one of several values such that it minimizes the [[Objective Function]]
		- You can also choose $\epsilon$ according to $\epsilon^*=g^Tg/g^TH$ where g is the [[Gradient]] and H is the [[Hessian]] to prevent [[Curvature]] from ruining your descent
	- The method converges when every element of $\nabla \approx 0$
	- [[Hill Climbing]] is [[Gradient Descent]] generalized to discrete spaces
	- Optimization methods that only consider the first derivative are [[First Order Optimization]]