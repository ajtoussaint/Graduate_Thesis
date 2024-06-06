# HIGHER-ORDER LATENT TRAIT MODELS FOR COGNITIVE DIAGNOSIS

## Summary
A statistical model for estimating student aptitude on answering test questions is proposed. The model assumes a set of latent skills influence a students ability to complete a task. The skill may either be conjunctive which indicates that every skill is required to have a possibility of answering the question correctly outside of guessing or subjunctive which means there may be multiple subsets of skills that offer the student a full opportunity to answer correctly. Slip factors are considered in addition to guessing. An expert in the subject matter must select the appropriate model for a given set of tasks. Above these latent skills is another latent trait "aptitude" which is indicative of a students ability to put given skills to use and functions more broadly than any of the specific skills (Tatsuoka 1995). 

A Markov Chain Monte Carlo approach is used to test the success of these models. First data was generated based on the model and some provided distributions. Then the model was used to repeatedly estimate the latent traits that were known for the generated data. The results of the estimate and true values were compared. It was shown that correct selection of the model and labeling of the Q-matrix (which maps knowledge concepts to exercises) contribute to successful estimation. A real data set regarding faction subtraction was also tested ([[Tatsuoka 2002]]) showing similar results. 

A large number of specific attributes lead to a better estimation of latent aptitude.

In this model the guess parameter is general and can represent the use of any strategy not included in the Q matrix to solve the problem. A high chance of guess estimated by the model indicates a poorly fit model or poorly labeled question. In some cases a "more obvious" solution that does not require the expected skills is present.

In general the "higher order" model that considers the aptitude parameter out performed the independent model except in instances of poor fit.

# Models
- [[HO-DINA]]
# Link
[aliquote.org/pub/delatorre2004.pdf](https://www.aliquote.org/pub/delatorre2004.pdf)
# Citation
De La Torre, Jimmy, and Jeffrey A. Douglas. "Higher-order latent trait models for cognitive diagnosis." Psychometrika 69.3 (2004): 333-353.

# In Other Papers
Cited by [[Wang, Fei, et al. 2022]] for comparison of [[HO-DINA]] model and as evidence that latent traits govern student's mastery of knowledge concepts and therefore it is not valid to assume the concept proficiencies are independent.

