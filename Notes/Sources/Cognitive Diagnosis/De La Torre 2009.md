# DINA Model and Parameter Estimation: A Didactic

## Summary
The [[DINA]] and [[HO-DINA]] models are discussed and explained in detail. Both models are cognitive diagnosis models rather than item response models. The goal of CDMs is to provide a binary skill vector that represents the presence or absence of specific skills within a student. Alternatively, item response focuses on discovering a single continuous proficiency value. 

The DINA model assumes that each latent skill is independent and binary. Due to this assumption there are 2^k possible configurations of the skill vector with k being the number of skills measured. The DINA model formulates a function for the probability of a student having each skill given their response to a set of exercises taking into account guess and slip parameters. A marginal maximum likelihood estimation is performed using the expectation maximization algorithm to determine the most likely configuration of latent skills.

This process can be computationally intensive when "k" becomes large. The [[HO-DINA]] model is introduced to solve this problem by assuming that all of the specific skill traits are contingent on another higher order "aptitude" trait which represents a students general aptitude for learning skills in the given subject. This simplifies the computation.

The authors warn that interpretability of results is not guaranteed due to factors such as test length, Q matrix labeling accuracy, and attribute pattern identifiability.

Variables
- X = matrix of student responses to exercises
- alpha = skill vector
- Q matrix
- n = latent response vector produced as a product of alpha and Q (1 if all skills possessed, otherwise 0)
- s = slip probability
- g = guess probability (or use of alt skill set)


# Models
[[DINA]]
# Link
[DINA Model and Parameter Estimation: A Didactic - Jimmy de la Torre, 2009 (sagepub.com)](https://journals.sagepub.com/doi/abs/10.3102/1076998607309474)
# Citation
De La Torre, Jimmy. "DINA model and parameter estimation: A didactic." _Journal of educational and behavioral statistics_ 34.1 (2009): 115-130.
# In Other Papers
Cited by [[Wang, Fei, et al. 2022]] to compare [[DINA]] to their proposed model.