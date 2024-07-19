 [[Principal Component Analysis]] is used to encode/decode [[Vector|Vectors]] into a compressed space while minimizing loss of information
	- encode $x$ using $f(x) = c$ and decode with $g(f(x)) \approx x$ 
	- To encode from $\mathbb{R}^{n} \to \mathbb{R}^l$ use $g(c) = Dc$ where $D \in \mathbb{R}^{n \times l}$ 
	- D is $n \times l$ has columns [[Orthogonal]] to each other and each column has a [[Unit]] [[Norm]]
	- Optimal code $c^* = argmin \lVert x - g(c) \rVert$ so we select each coded point to minimize [[Euclidian Norm]] or [[Squared L2 Norm]] for simplicity 
	- Evaluating this minimum yields: $c = D^Tx$ which is minimized using vector calculus as described in [[#4.3 Gradient Based Optimization]] selecting a D that minimizes [[Frobenius Norm]]