# Data-analytic methods for latent partially ordered classification models

## Summary
A novel model for describing and predicting student knowledge states is proposed. For a given subject various knowledge concepts are defined and associated with exercises. A partially ordered set or "poset" of all the possible states a student may be in with respect to these knowledge concepts is defined. A given state shows a student as having mastered a concept, not mastered a concept, or lacks information about the students relationship to the concept. As such some states are ordered above others. The state of mastering all concepts is ordered above a given state of having mastered some, which is ordered above having mastered none. The dichotomous state descriptions are similar to [[DINA]].

Once the poset of states is defined it can be used in conjunction with response data to determine the probability that a student is within a given state. Opportunities for guesses and slips are taken into account. Each exercise will partition the model into states that are adequate to answer the exercise and those that are not. Adequate states still have a chance to slip and inadequate states have a chance to guess so a states probability of correct response is governed by a distribution.

To compute the student states a Monte Carlo Markov Chain approach is used:
	1. $p_u(e_i)$ is the probability of a state in the adequate partition answering exercise *i* correctly and $p_l(e_i)$ is the probability of an inadequate state guessing. These are estimated using MCMC according to (Gelfand 1992) using Bernoulli distributions to generate a prior distribution. It is given that pu > pl.
	2. Values for $p_u(e_i)$ and $p_l(e_i)$ are sampled from the prior distribution  with pu always sampling higher than pl.
	3. A response vector from a student is used to calculate a posterior distribution
	4. States are sampled for each test subject
	5. For each exercise response received the prior distribution is updated to obtain posterior beta distributions for the item parameters
	6. Repeat steps 2 - 6 until convergence is achieved. Select the state with the largest posterior probability as the most likely state for each student.

Discrimination of a partition (exercise) is judged by Kullback-Leibler information value which determines how quickly the probability of a subject having that state converges to 1. An area where the probability density is spread among several states suggests the existence of another state that is not accounted for. If very few students are classified into a state it may suggest it is not useful to have. Model fit is largely determined by the appropriate classification of states and labeling of problems.

This approach is specific to questions that are completed in order and is largely focused on reducing the number of questions to be asked before convergence is achieved. As mentioned in [[Wang, Fei, et al. 2022]] cognitive diagnosis models can be equally effective on datasets that are obtained sequentially or from a single event. Complex underlying cognitive models are necessary to describe cognitive processes.

 The theory was tested in an experiment using 20 questions related to fraction subtraction. 
# Link
https://academic.oup.com/jrsssc/article/51/3/337/7112881
# Citation
Tatsuoka, Curtis. "Data analytic methods for latent partially ordered classification models." Journal of the Royal Statistical Society Series C: Applied Statistics 51.3 (2002): 337-350.
# In Other Papers
Cited by [[De La Torre, Douglas 2004]] for its fraction subtraction dataset and successful estimation techniques