A [[Diagonal]] [[Matrix]] has the property that $D_{ij} = 0$ if $i \ne j$ 
	- The [[Identity Matrix]] is [[Diagonal]]
	- It is efficient to multiply: $diag(v)x = v \odot x$ (element wise multiplication)
		- The diag operation [[Broadcasting|broadcasts]] a [[vector]] of length n into a n x n diagonal [[Matrix]]
	- If every diagonal element in the matrix is non-zero then: $diag(V)^{-1} = diag([1/v_1 ... 1/v_n]^T)$ 