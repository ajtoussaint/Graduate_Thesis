# Multidimensional Item Response Theory
MIRT can be viewed as an extension of [[IRT]] that expands the theta scalar into a vector of "m" different qualities that combine to generate the probability of a correct response. There are two dominant models of *how* the dimensions of theta combine: compensatory and partially compensatory. Which model is appropriate may depend on the type of test item. MIRT also operates at the level of individual test items while IRT is better suited to an entire test which is a collection of items as this better fits IRT's unidimensionality constraint. MIRT as discussed here will focus on the case where question responses are dichotomously correct or incorrect although it can be expanded to more complex models.

Local independence among questions and [[monotonicity]] assumptions still apply.

## Input Data
- A set of student responses to questions
- Associated "difficulty value" for each question 
## Output Data
- An m-dimensional theta vector representing aptitudes in each of m latent skills
- The model will also learn question difficulty, discrimination, and guess parameters
## Process
- Interactions between a person and an exercise can be described by a vector of parameters representing the ability of the person in "m" areas relevant to the exercise
	- Theta: persons ability vector (m-dimensional)
	- nu: vector of parameters describing the exercise
	- u: possible value of score on the item
	- U: actual value of score on the item
![[IRT_Image_1.JPG]]
- Function f must provide scales for its inputs and generate a response (0,1)
- It is standard that the output scale for theta is from -4 to 4 although it is theoretically infinite

Two Parameter Logistic Compensatory Model
- Two parameter logistic model can be extended into: 
![[MIRT_Image_1.JPG]]
- In this case, a is a 1xm vector of item discrimination parameters, theta is a 1xm vector of person coordinates in the theta space, and d is a scalar that is equivalent to (-ab) in the IRT model
	- Note: theta is transposed in the equation to theta' so that the result is a scalar value
- This formula was created by multiplying a through in the 2PL IRT model
- High ability in one dimension can make up for low ability in another. Problems become easier when more concepts are involved.
- "a" is the discrimination parameter representing the rate at which probability of correctness changes in theta space
- MDIFF :"-d/a_i" can represent the relative difficulty of exercise i. d itself is an arbitrary scalar value. Another formulation is d/SQRT(SUM(a^2)) for m "a" values in an m-dimensional theta space
Three Parameter Logistic Compensatory Model
- Very similar to the above model except the guess parameter is include as in IRT:  ![[MIRT_Image_2.JPG]]

Three Parameter Logistic Partially Compensatory Model
- A partial compensatory model is based on the product of m 2PL IRT models multiplied by the guess parameter: 
![[MIRT_Image_3.JPG]]
- Guess parameter is applied to the whole thing because you just guess at the end
- Probability of correct response can never be greater than the lowest component probability
- When theta = 0 and b =0 the probability is 0.5^m for m dimensional knowledge space of a given item. Therefore problems become more difficult when more concepts are involved.

Similar to IRT a maximum likelihood estimate can be used to determine theta given response data.

# Source Paper
[[Reckase 2006]]

# Performance

|     Dataset     |        Condition         | [[ACC]] | [[RMSE]] | [[AUC]] |
| :-------------: | :----------------------: | :-----: | :------: | :-----: |
|    [[MATH]]     |    Random data split     |  .793   |   .378   |  .813   |
| [[ASSIST09-10]] |    Random data split     |  .701   |   .461   |  .719   |
|    [[MATH]]     | Weak-coverage data split |  .620   |   .583   |  .572   |
| [[ASSIST09-10]] | Weak-coverage data split |  .637   |   .505   |  .612   |
Data taken from [[Wang, Fei, et al. 2022]] to be comparable to other models. Notably MIRT performs better than [[IRT]] when knowledge concepts are accurately covered, and worse when there is weak coverage.