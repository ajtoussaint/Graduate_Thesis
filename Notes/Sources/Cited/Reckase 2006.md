# Multidimensional Item Response Theory
## Summary
A textbook that provides an overview of IRT and MIRT as well as implementation details and how they can be applied for the purpose of categorical adaptive testing. Content of the text is summarized in each of the notes pertaining to the specific models linked below.

## MIRT
- Two types of models
	- Linear combination of theta coordinates (compensatory)
	- Cognitive task is separated into parts and a separate [[IRT]] model is applied to each part. The final probability of correctness is the product of the individual parts. As a result different traits are less capable of compensating for each other (partially compensatory)
	- I would assume in reality a combination of these things is true
- Majority of models are based on dichotomous questions
- any number of latent skills may be included in the model. The "trait space" that describes theta will have dimensions according to the number of latent skills
- Unidimensional models will have poor fit for items that can be known to require multiple traits
- The MIRT model assumes a monotonic increase across all theta dimensions
- MIRT can fit a single test item vs. [[IRT]] fitting an entire test/collection of items
- Test items are sensitive to different combinations of skill as well as difficulty
- Structural: parameters that describe the functioning of the test items
- Incidental: the vector of coordinates describing the location of individuals
- MIRT model is developed by fitting to proportions of correct responses (but wouldn't this require existing knowledge of theta?)
- nu: vector of structural (knowledge concept) parameters describing a test item
- U: score on the test item 
- u: possible score on the test item (1=right, 0=wrong)
- theta: a persons location in the "knowledge space"
- local independence assumption: each test item is unaffected in terms of response chance by the presence of other test items -> individuals with same/similar theta values will respond similarly to test items.
Compensatory Extension of IRT
- Two parameter logistic model can be extended into: 
![[MIRT_Image_1.JPG]]
- In this case, a is a 1xm vector of item discrimination parameters, theta is a 1xm vector of person coordinates in the theta space, and d is a scalar that is equivalent to (-ab) in the IRT model
	- Note: theta is transposed in the equation to theta' so that the result is a scalar value
- This formula was created by multiplying a through in the 2PL IRT model
- The exponent of e is a y = mx + b form line defined in m-dimensional space -> All theta vectors that satisfy "k = a\*theta +d", where k is some constant, will yield the same probability of a correct response -> you can graph a relation between theta_1 and theta_2 for some constant response probability
- The model is "compensatory" because high ability in one dimension may compensate for low in another
- It is standard to scale theta from -4 to 4 in each dimension, but the real scale is infinity
	- Perhaps beyond this point increases in proficiency are irrelevant with respect to the slip parameter
- "a" represents the rate at which probability of correctness changes in the theta space -> a is called slope or discrimination
- "d" does NOT represent difficulty, -d/a_i gives a relative metric of difficulty alternatively, the distance from the "0.5 chance of correct response line" to the origin can be used: -d/SQRT(SUM(a^2)) for m "a" values in an m-dimensional theta space. 
	- The value is called MDIFF
- The 3PL model can also be extended: ![[MIRT_Image_2.JPG]]
Partially Compensatory extensions of IRT
- A partial compensatory model is based on the product of m 2PL IRT models multiplied by the guess parameter: 
![[MIRT_Image_3.JPG]]
- Guess parameter is applied to the whole thing because you just guess at the end
- Probability of correct response can never be greater than the lowest component probability
- When theta = 0 and b =0 the probability is 0.5^m for m dimensional knowledge space of a given item

Comparison
- Usefulness of model depends on how well it fits the test design
- Models for more than 2 score categories exist but I don't care
# Models
- [[IRT]]
- [[MIRT]]
# Link
[18 Multidimensional Item Response Theory - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0169716106260188)
# Citation
Reckase, Mark D. "18 Multidimensional Item Response Theory." _Handbook of statistics_ 26 (2006): 607-642.
# In Other Papers
Cited in [[Wang, Fei, et al. 2022]] as a reference for [[IRT]] and [[MIRT]].