# Higher Order Deterministic Inputs Noisy "and" Gate
## Qualitative Description
The HO-DINA model is an extension of the [[DINA]] model to include a higher order "aptitude" parameter as well as the standard latent skill parameters a student possesses. The success of a student at answering a question given their skill parameters is independent among skills considering a single latent aptitude. The process of the model is to mathematically formulate a probability of answering correctly and then use a Monte Carlo Markov Chain (MCMC) approach to generate the probabilities of latent traits which are made binary with a 0.5 cutoff.
## Input Data
- A labeled "Q" matrix similar to [[NCDM]]
- Some set of students "S", exercises "E", and knowledge concepts "K"
-  A set of response logs (s, e, r) where s is a given student, e an exercise, and r the student's percentage score on the exercise from 0 to 1.
## Output Data
Latent skill parameters for a student in the given labeled skills. Additionally, the student's latent "aptitude" parameter is measured.
## Process
1. A set of prior, joint, and conditional distributions for each of the major latent parameters is defined: ![[HO-DINA_Image_1.JPG]] ![[HO-DINA_Image_2.JPG]] ![[HO-DINA_Image_3.JPG]]
	- Theta: the latent aptitude
	- s: slip chance
	- g: guess chance (or use of method not captured by model)
	- alpha: latent skill attributes for the student
	- lambda: A latent aptitude for a specific skill (part of theta)
2. Using the above distributions the MCMC method is applied to estimate an average and standard deviation for the unobserved latent traits.![[HO-DINA_Image_4.JPG]]


# Source Paper
[[De La Torre, Douglas 2004]]
# Performance
The model was proven by first generating data with known parameters and then using the defined approach to reverse estimate these parameters successfully. 

(Data shown below is from [[Wang, Zhifeng, et al. 2023]] as this is more comparable to other relevant models)


|     Dataset     |     Condition     | [[AUC]] | [[RMSE]] |
| :-------------: | :---------------: | :-----: | :------: |
|    [[CL21]]     | Random Data Split |  .7037  |  .4723   |
|    [[Math1]]    | Random Data Split |  .6658  |  .5215   |
| [[Synthetic-5]] | Random Data Split |  .7245  |  .4988   |


