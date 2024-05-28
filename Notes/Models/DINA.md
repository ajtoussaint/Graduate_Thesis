# Deterministic Input Noisy "and" Gate
## Qualitative Description
The DINA model assumes that each latent skill variable is independent of other latent skills. Based on a labeled Q matrix and exercise response logs for students the model generates a binary skill vector for a given student. This is done by applying a marginal maximum likelihood estimation through the expectation maximization algorithm. Results also include guess and slip rates for each exercise. When then number of latent skills becomes large the model may be computationally impractical and [[HO-DINA]] is preferred.
## Input Data
- similar to [[NCDM]]
## Output Data
A binary vector representing presence or absence of student skills with the maximum likelihood of being accurate. The model also generates guess and slip rates for each exercise. 
## Process
1. The marginal maximum likelihood of skill presence is formulated as shown:![[DINA_Image_1.JPG]]
	- X = matrix of student responses to exercises
	- alpha = skill vector
	- L(X) is the marginalized likelihood of the response vector of examinee i.
2. The expectation maximization algorithm is applied. Appendix A of [[De La Torre 2009]] provides the complete working of the algorithm

# Source Paper
[[De La Torre 2009]]

# Performance
|     Dataset     |        Condition         | [[ACC]] | [[RMSE]] | [[AUC]] |
| :-------------: | :----------------------: | :-----: | :------: | :-----: |
|    [[MATH]]     |    Random data split     |  0.593  |  0.487   |  0.686  |
| [[ASSIST09-10]] |    Random data split     |  0.650  |  0.467   |  0.676  |
|    [[MATH]]     | Weak-coverage data split |  0.223  |  0.502   |  0.560  |
| [[ASSIST09-10]] | Weak-coverage data split |  0.471  |  0.490   |  0.588  |
Data taken from [[Wang, Fei, et al. 2022]] to be comparable to other models