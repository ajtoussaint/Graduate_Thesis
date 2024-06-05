# Item Response Theory
Item Response Theory is possibly the simplest model for some type of cognitive diagnosis. It is assumed that the relation between locations in multidimensional cognitive space and probabilities of a correct response can be modeled by a continuous function. Each student is represented by a single aptitude value in the subject matter of an assessment which governs their ability to respond correctly to questions according to question difficulty. It is assumed that questions are independent and that probability of correct answer increases monotonically with aptitude. Many different IRT models can be used depending on how the function relating aptitude, difficulty, and correctness of response is formulated. Typically, questions are designated either correct or incorrect dichotomously although their are extensions to the model for continuous response grade levels. 

IRT is limited to storing all student aptitude data in a single variable. It has been shown ([[Reckase 2006]]) that [[MIRT]] is a valuable expansion of IRT.
## Input Data
- A set of student responses to questions
- Associated "difficulty value" for each question 
## Output Data
- A single aptitude value for each student
## Process
- Interactions between a person and an exercise can be described by a *single* parameter representing the ability of the person
	- Theta: persons ability
	- nu: vector of parameters describing the exercise
	- u: possible value of score on the item
	- U: actual value of score on the item
![[IRT_Image_1.JPG]]
- Function f must provide scales for its inputs and generate a response (0,1)

A number of different processes could be employed to determine the aptitude value given a formulation. The most common is using the maximum likelihood criteria. This method determines what the most likely value for the theta vector is given a distribution of responses. Accuracy is increased with the number of recorded responses. Other relevant methods are the maximum a posteriori Bayesian criterion, and the least squares criterion

The various formulations of IRT's f-function commonly used are as follows:
- The simplest form of IRT is shown: ![[IRT_Image_2.JPG]]
	- b_i: the difficulty level of the "i"th question
	- The function is expanded to include A as theta and B as b:![[IRT_Image_3.JPG]]
	- This ensures monotonicity and is the simplest expression of IRT
	- Disadvantage: for a given B value the lower half probability (0, 0.5) of answering correctly is mapped to A values from (0,B) while the upper half is mapped from (B, infinity)
- Logarithmic Scaling (Rasch model) (one parameter)
	- Typically used over the above model![[IRT_Image_4.JPG]]
	- Psi: the cumulative logistic density function
	- theta scales form -infinity to +infinity as does b. High values of theta represent high proficiency and high values of b represent difficult questions
	- The slope of the response curve increases as theta is closer to b which means a question of b difficulty best differentiates students whose theta value is close to b
	- All persons with the same number of correct responses will have the same Maximum Likelihood estimation of theta
	- theta and b can be estimated independently
	- All questions have the same maximum slope for their item characteristic curves (ICC) which suggests that this model may not accurately capture the fact that some questions are more discriminating
- Two Parameter Logistic Model
	- A slight complexification of the Rasch Model:![[IRT_Image_5.JPG]]
	- a is a parameter related to the maximum slope of the item characteristic curve (differentiability of an item)
	- Max slope is still at theta = b but the value may be different between questions
	- The "a" value appears when estimating theta as a "weight" on questions. All students who have the same number of correct questions when weighted by "a" will have the same theta estimate
- Three Parameter Logistic Model
	- Incorporates the guess chance:![[IRT_Image_6.JPG]]
	- c: guessing parameter, defines a lower asymptote for the response curve
	- max slope is still at b=theta
	- A given question is less discriminating (ICC has smaller max slope) due to presence of guessing
	- Empirical estimates of guess parameter often show it as less than 1/(number of possible responses) indicating those who get the answer wrong were most likely not randomly guessing
	- In some cases the formula is written as: ![[IRT_Image_6.1.JPG]]
	- [nces]([NAEP Analysis and Scaling - The Three-Parameter Logistic Model (ed.gov)](https://nces.ed.gov/nationsreportcard/tdw/analysis/scaling_models_3pl.aspx))This version of the formula includes the 1.7 constant to equate the ICC curves to the normal ogive model mentioned below. This was used in the EduCDM model zoo by default. Brief testing showed results were comprable between the two formulas with this one being slightly better.
- Normal ogive (Three parameter)
	- ![[IRT_Image_7.JPG]]
	- z = (a_i * (theta_j - b_i))
	- When a constant of 1.7 is applied to the exponents of the Three parameter logistic model then the resulting ICC's are virtually identical
# Source Paper
[[Reckase 2006]]

# Performance

|     Dataset     |        Condition         | [[ACC]] | [[RMSE]] | [[AUC]] |
| :-------------: | :----------------------: | :-----: | :------: | :-----: |
|    [[MATH]]     |    Random data split     |  .782   |   .387   |  .795   |
| [[ASSIST09-10]] |    Random data split     |  .674   |   .464   |  .685   |
|    [[MATH]]     | Weak-coverage data split |  .624   |   .467   |  .638   |
| [[ASSIST09-10]] | Weak-coverage data split |  .657   |   .464   |  .633   |
Data taken from [[Wang, Fei, et al. 2022]] to be comparable to other models. Notably [[MIRT]] performs better than IRT when knowledge concepts are accurately covered, and worse when there is weak coverage.