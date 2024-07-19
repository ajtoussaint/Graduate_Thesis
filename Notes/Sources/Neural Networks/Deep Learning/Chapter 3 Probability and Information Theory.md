- [[Probability Theory]] is a mathematical frame work for representing uncertainty that is responsible for both guiding AI behavior and evaluating AI performance
- [[Information Theory]] is used to quantify a level of uncertainty in a [[Probability Distribution]]

## 3.1 Why Probability?
- [[Stochastic]] is another word for non-deterministic
- There are three sources of uncertainty in the world
	1. Inherit [[Stochastic]] behavior such as a truly random dice roll
	2. Incomplete observability such as the Monty Hall problem or not knowing all of the forces applied to the die being rolled
	3. Incomplete modeling - not knowing enough physics to fully simulate the outcome based on the forces applied to the die
- In many cases it is more practical to use a model that is simple but has some uncertainty than a complete deterministic model
- [[Probability]] has two definitions
	1. In frequentist statistics it is the portion of times over an infinite number of trials that some event will occur
	2. In Bayesian statistics it is the degree of belief that something is true
	- Both theories are controlled by a few commons sense axioms
## 3.2 Random Variables
- A [[Random Variable]] is a variable that takes on different values randomly. It is usually represented with lowercase plain type
	- The possible values of a given variable are indicated by script font with numbered subscript: $x_1, x_2$ 
## 3.3 Probability Distributions
- A [[Probability Distribution]] describes how likely a [[Random Variable]] is to take on each of the possible states it may have
- A [[Probability Mass Function]] or PMF describes the [[Probability Distribution]] for discrete [[Random Variable|random variables]]. 
	- Represented with uppercase "P"
	- The domain of P is all states of x $\forall x \in x, 0 \le p(x) \le 1$ 
	- Typically normalized such that $\sum_{x \in x}P(x) = 1$ 
	- In a Uniform [[Probability Distribution]] each state is equally as likely
- A [[Joint Probability Distribution]] is a [[Probability Mass Function]] acting on many variables at once: P(x,y)
- [[Probability Density Function]] describes probability for continuous variables
	- Represented with lowercase "p"
	- domain of p includes $\forall x \in x, p(x) \ge 0$ such that $\int p(x)dx = 1$ 
	- The probability that a variable will fall within some range can be found with an integral: $p(x) \in \mathbb{S}, \mathbb{S} = [a,b] = \int_{a}^{b}p(x)dx$ 
## 3.4 Marginal Probability
- [[Marginal Probability Distribution]] is the probability distribution for a subset of [[Random Variable|random variables]] $\forall x \in x, P(x = x) = \sum_{y}P(x=x, y=y)$ 
	- For continuous: $\forall x \in x, P(x = x) =\int p(x,y)dy$ 
## 3.5 Conditional Probability
- [[Conditional Probability]] is the probability of some event occurring given that another event did occur: $P(y=y | x=x)$ (Probability of y given x)
	- $P(y=y | x=x) = P(y=y, x=x)/P(x=x)$ 
	- This does not work when interpreted as the consequences of an action
## 3.6 The Chain Rule of Conditional Probabilities
- [[Chain Rule]] (aka product rule) states that any [[Joint Probability Distribution]] over n [[Random Variable|random variables]] can decompose into [[Conditional Probability]] distributions over each random variable
	- $P(x^{(1)}, ..., x^{(n)}) = P(x^{(1)}\Pi_{i=2}P(x^{(i)},...,x^{(i-1)})$ 
	- $P(a,b,c) = P(a|bc)P(b|c)P(c)$
## 3.7 Independence and Conditional Independence
- [[Independent Variables]] have no effect on each other's probability
	- $\forall x \in x, y \in y, p(x=x,y=y) = p(x=x)p(y=y)$ sometimes written $x|y$ 
- [[Conditionally Independent Variables]] have no effect on each other's probability within a given value of some other variable "z"
	- $p(x=x, y=y|z=z) = p(x=x)p(y=y)$ written $x \perp y | z$ 
	- Consider the probability of having a certain gene (x), the probability of having a certain disease (z) and the probability of exhibiting some symptom (y). When all variables are considered it seems that those with the gene may be more likely to have a symptom. When the disease variable is kept constant though, it can be shown that the symptom only occurs because of the disease and it makes no difference if you have the gene unless you get the disease.
## 3.8 Expectation, Variance, and Covariance
- [[Expected Value]] is the average of a [[Probability Distribution]] or the value we could most likely expect on a single sample
	- $\mathbb{E}_{x~p}[f(x)] = \sum_{x} P(x)f(x)$ or $\int p(x)f(x)$ 
	- Expected values are linear and have the properties of linear equations when combined or modified:
		- $\mathbb{E}_x[\alpha f(x)+ \beta g(x)] = \alpha \mathbb{E}_x[f(x)] + \beta \mathbb{E}_x[g(x)]$ 
- [[Variance]] is a measure of how much random values of x differ from each other
	- $Var(f(x)) = \mathbb{E}_x[f(x) - \mathbb{E}[f(x)]^2]$ 
	- low variance means that values will be clustered close to the [[Expected Value]]
- [[Standard Deviation]] is $\sqrt{Var(f(x))}$ 
- [[Covariance]] measures linear relation and and scale of values
	- $Cov(f(x),g(y)) = \mathbb{E}[(f(x) - \mathbb{E}[f(x)])(g(y) - \mathbb{E}[g(y)])]$ 
	- A covariance with a high absolute value indicates that values of each function change a lot and are far from their respective  averages
	- A positive covariance indicates values for each function are simultaneously high and low while negative implies that they are opposites
	- [[Independent Variables]] have a covariance of 0 there must be no [[Linear Dependence]] for this to work.
		- Dependent variables can have 0 [[Covariance]] if the relation is non linear
- The [[Covariance Matrix]] of a vector is size n x n and $Cov(x)_{i,j} = Cov(x_i,x_j)$
	- The [[Diagonal]] elements of the [[Matrix]] give the [[Variance]] : $Cov(x_i,x_i) = Var_x(x_i)$ 
- [[Correlation]] is a metric used to measure the relation of variables similar to [[Covariance]] but [[Correlation]] is normalized to not be impacted by scale
## 3.9 Common Probability Distributions
- The [[Bernoulli Distribution]]  is a [[Probability Distribution]] that models a single binary [[Random Variable]]
	- $\phi \in [0,1] = P(x=1)$ 
	- $P(x=0) = 1 - \phi$ 
	- $P(x=x) = \phi^{x}(1-\phi)^{1-x}$
	- $\mathbb{E}_x[x]=\phi$
	- $Var_x(x) = \phi(1-\phi)$ 
- The [[Multinoulli Distribution]] also called the categorical distribution, is used to model a single [[Random Variable]] which has "k" discrete states
	- $p \in [0,1]^{k-1}$ where p is a vector describing the [[Probability Distribution]]
	- Used to describe categories of objects
	- [[Variance]] and Mean are typically not of interest
- [[Bernoulli Distribution]] and [[Multinoulli Distribution]] are sufficient to describe any distribution within their specialized domains
- [[Gaussian Distribution]] is also called the normal distribution.
	- $\mathcal{N}(x;\mu,\sigma^2) = \sqrt{1/(2\pi\sigma^2)}exp(-1/(2\sigma^2)(x-\mu)^2)$ 
	- $\mu\in\mathbb{R}, \sigma\in(0,\infty)$
	- $\mathbb{E}[x] = \mu$ which is at the central peak of the distribution
	- $\sigma$ is the [[Standard Deviation]] and $\sigma^2$ is the [[Variance]]
	- $\beta$ represents the "Precision" which is $\beta^{-1}=\sigma^2$
	- It is common to evaluate the [[Probability Density Function]] using $\beta$ so that the equation simplifies:$\mathcal{N}(x; \mu, \beta^{-1}) = \sqrt{\beta/(2\pi)}exp(-1/2\beta(x-\mu)^2)$
	- If nothing about some [[Probability Distribution]] is known it is reasonable to assume that it is normal
		- This encodes the maximum uncertainty over $\mathbb{R}$ which means minimal assumptions
	- The [[Standard Normal Distribution]] is a [[Gaussian Distribution]] where $\mu = 0, \sigma = 1$ 
- The [[Central Limit Theorem]] states that the cumulation of many [[Independent Variables]] is distributed according to a [[Gaussian Distribution]]
	- Essentially any complex system is just normally distributed noise
- [[Multivariate Normal Distribution]] is a [[Gaussian Distribution]] generalized to $\mathbb{R}^2$ 
	- $\mathcal{N}(x;\mu,\Sigma)=\sqrt{1/(2\pi)^n det(\sigma)} exp(-1/2(x-\mu)^T \sigma^{-1}(x-\mu))$
	- $\mu$ is the mean as a vector
	- $\Sigma$ is the [[Covariance Matrix]] 
	- The precision matrix $\beta^{-1} = \Sigma$ can be used for easier evaluation of 
		- $\Sigma$ is usually [[Diagonal]] or [[Isotopic]]
			- An [[Isotopic]] [[Matrix]] is a [[Scalar]] value multiplied by the [[Identity Matrix]]
	- the [[Probability Density Function]] similar to with a [[Gaussian Distribution]]
- The [[Exponential Distribution]] is a [[Probability Distribution]] notable for its sharp point at x=0
	- $p(x;\lambda) = \lambda l_{x \ge 0} exp(-\lambda x)$ 
	- $l_{x \ge 0}$ is an "indicator function" that assigns a probability of 0 to any negative x
- The [[Laplace Distribution]] is a [[Probability Distribution]] with a sharp point at an arbitrary value $\mu$ 
	- $Laplace(x;\mu,\gamma) = 1/(2\gamma)exp(-(\lvert x - \mu \rvert)/\gamma)$
- The [[Dirac Delta Function]] clusters mass in the [[Probability Distribution]] around a point, $\mu$ 
	- $p(x) = \delta(x-\mu)$ 
	- The function is 0 everywhere but integrates to 1. It is a generalized function defined by this property
- The [[Empirical Distribution]] is a [[Probability Distribution]] with a probability mass of 1/m on each of m points.
	- $\hat{p}(x) = \frac{1}{m}\sum_{i=1}^m\delta(x-x^{(i)})$ 
		- Where $\delta$ is the [[Dirac Delta Function]]
	- Essentially [[Multinoulli Distribution]] for continuous variables
	- Usually associated with a real training dataset because it perfectly maximizes the likelihood of training data in a continuous distribution.
- The [[Mixture Distribution]] is a [[Probability Distribution]] that combines several component distributions. On any given trial the distributions are sampled to generate a result.
	- $P(x) = \sum P(c=i)P(x|c=i)$ where P(c) is each component distribution
- A [[Latent Variable]] is an unobservable [[Random Variable]]
- A [[Gaussian Mixture]] is a [[Mixture Distribution]] [[Probability Distribution]] where all included distributions are gaussian.
	- A Gaussian mixture specifies a [[Prior Probability]] and a [[Posterior Probability]]
	- Gaussian mixtures are universal approximators which can approximate any smooth density with a specific amount of nonzero error with enough components.
- A [[Prior Probability]] describes the belief about distribution $i$ before any observation.
	- $\alpha_i = P(c=i)$
- A [[Posterior Probability]] is computed from the [[Prior Probability]] after observation
	- $P(c|x)$ 
## 3.10 Useful Properties of Common Functions
- [[Logistic Sigmoid Function]] can be used to produce the $\phi$ of a [[Bernoulli Distribution]]
	- $\sigma(x) = \frac{1}{1+ exp(-x)}$ 
	- Range is (0,1)
	- The function saturates and becomes insensitive to changes when the value of x is large (flat curve)
- [[Softplus Function]] is used to produce $\beta$ or $\sigma$ for a [[Gaussian Distribution]]
	- $\zeta(x) = log(1+exp(-x))$ 
	- Range is (0, $\infty$ )
	- A smoothed out version of the [[Rectify Linear Unit]] function that includes some negative values
		- [[Rectify Linear Unit]] makes negatives 0 and positives unchanged
- [[Logit]] is $\sigma^{-1}(x)$ where $\sigma$ is the derivative of the [[Softplus Function]] 
	- $\sigma(x) = \frac{exp(x)}{exp(x) +exp(0)}$
	- $\frac{d}{dx}\sigma(x) = \sigma(x)(1 - \sigma(x))$
	- $1 - \sigma(x) = \sigma(-x)$
	- $log(\sigma(x)) = -\zeta(-x)$
	- $\frac{d}{dx}\zeta(x) = \sigma(x)$
	- $\forall x \in (0,1), \sigma^{-1}(x) = log(\frac{x}{x-1})$
	- $\forall x > 0, \zeta^{-1}(x) = log(exp(x) - 1)$
	- $\zeta(x) = \int_{-\infty}^{x}\sigma(y)dy$
	- $\zeta(x) - \zeta(-x) = x$ 
## 3.11 Bayes' Rule
- [[Bayes Rule]] is used to find the probability of y given x if we know the probability of x given y
	- $P(x|y) = \frac{P(x)P(y|x)}{P(y)}$ 
	- In most situations one can compute P(y)
		- $P(y) = \sum_xP(y|x)P(x)$
## 3.12 Technical Details of Continuous Variables
- [[Measure Theory]] is used to determine the set of sets [[Probability Theory]] can be applied to without paradox
- [[Measure Zero]] is a set of negligibly small points within some space
- [[Almost Everywhere]] is a specific math term used to describe all of a space except for [[Measure Zero]]
- In probability if $y=g(x)$ it is not necessary that $P_y(y) = P_x(g^{-1}(y))$
## 3.13 Information Theory
- [[Information Theory]] is a branch of mathematics that is used to quantify the amount of information in a signal.
- Knowing that an unlikely event occurred includes more information than a likely event
- [[Independent Variables|Independent]] events have additive information values
- [[Self Information]] or the quantity of information from a single observation is defined as $I(x) = -log(P(x))$ (using natural log)
- Nats are the unit of measure of information when natural log is used. You could also use base 2 log and measure in bits
- [[Shannon Entropy]] is the uncertainty within an entire [[Probability Distribution]]
	- $H(x) = \mathbb{E}_{x~p}[I(x)] = -\mathbb{E}_{x~p}[log(P(x))]$ 
	- This is the expected amount of information from sampling
	- The lower bound is the number of bits to encode a symbol drawn from P
	- [[Differential Entropy]] is [[Shannon Entropy]] for continuous [[Random Variable]]
	- Low entropy systems are easier to predict
- [[Kullback-Leibler Divergance]] is a metric for measuring the difference in two [[Probability Distribution]] over some [[Random Variable]] x
	- $D_{KL}(P||Q) = \mathbb{E}_{x~P}[log(\frac{P(x)}{Q(x)})] = \mathbb{E}_{x~P}[logP(x) - logQ(x)]$ 
	- The KLD can be used to determine how many extra symbols it takes to send a message from P using a code that was optimized for Q
	- 0 iff P = Q
	- Always non-negative
	- Not symmetric: $D_{KL}(P||Q) \ne D_{KL}(Q||P)$
	- If p is a real value an q is an approximation
		- Use DKL(p||q) to place a high probability for the approximation anywhere the true distribution does
		- Use DKL(q||p) to avoid placing a high probability for the approximation anywhere the true distribution is low
- [[Cross Entropy]] is related to [[Kullback-Leibler Divergance]] in that minimizing cross entropy is equivalent to minimizing KLD
	- By convention 0log(0) = 0
	- $H(P,Q) = -\mathbb{E}_{x~P}log Q(x)$
## 3.14 Structured Probabilistic Models
- ML often involves many [[Probability Distribution]] over unrelated [[Random Variable|Random Variables]] so it is useful to simplify
	- Suppose a -> b, b -> c, a|c given b where -> represents one variables influence on another and "|" is [[Conditionally Independent Variables]]
	- $p(a,b,c) = p(a)p(b|a)p(c|b)$
		- Called "factorization"
		- Reduces the number of parameters to describe a distribution
- A [[Structured Probabilistic Model]] aka a graph can represent the "factorization" of p with a graph
	- Nodes = [[Random Variable]]
	- Edges represent interaction
- A Directed [[Structured Probabilistic Model]] has an arrow associated with each edge that represents the factorization into a conditional distribution
	- $p(x) = \prod_{i}p(x_{i}|Pa_{\mathcal{G}}(x_i))$  
	- $p(a,b,c,d,e) = p(a)p(b|a)p(c|a,b)p(d|a,b)p(d|b)p(e|c)$
		- Each variable is "|" on the nodes pointing to it
- An Undirected [[Structured Probabilistic Model]] factorizes into a set of functions:
	- $P(x) =\frac{1}{Z}\prod_i\phi^{(i)}(C^{(i)})$
	- $p(a,b,c,d,e) = \frac{1}{Z}\phi^{(1)}(a,b,c)\phi^{(2)}(b,d)\phi^{(3)}(c,e)$ 
	- A clique is a set of nodes which are connected in the graph, each clique has a "factor" $\phi$ which is a non-negative [[Scalar]]
	- The probability of any given configuration of [[Random Variable]] is proportional to the product of $\phi$ (not necessarilly 1)
	- Z is the sum (or integral) of all states which is used to normalize the function
- Directed vs. undirected [[Structured Probabilistic Model|SPMs]] are just different ways of representing the same thing
[[Goodfellow, Bengio, Courville 2016]]