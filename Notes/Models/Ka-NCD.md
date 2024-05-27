# Neural Cognitive Diagnosis Model with Knowledge Association Based Extension
## Qualitative Description
In reality obtaining student data the richly covers all knowledge concepts is not practical. These data gaps can be filled in with the associations between concepts to make an educated estimate of a student's proficiency in a concept they had not already been tested on. Explicit knowledge relations may not always be defined so in this case they are computed from existing response logs.

Latent traits are assumed to be the cause of skill in a number of knowledge concepts. The matrices "A" and "B" used in NCDM are recalculated using the latent trait model to account for concept overlap.

## Input Data
- See [[NCDM]]
## Output Data
- See [[NCDM]]

## Process
1. Step 1 of [[NCDM]] is replaced. Instead of training the Matrix "A" the following procedure is used:
	1. Students are represented by a latent trait vector "l_s" and knowledge concepts are represented by a latent trait vector "l_k". Latent vectors are trainable.
	2. The proficiency of a student on an exercise is calculated as shown below with a Sigmoid activation function:
	![[Ka-NCD_Images_1.JPG]]
	3. The matrix "A" is then calculated using trainable weights and biases on the vector "a": ![[Ka-NCD_Images_2.JPG]]
2. A similar process is applied to Step 3 of NCDM to calculate the "B" matrix with trainable weights and biases: 
![[Ka-NCD_Images_3.JPG]]
3. The rest of the process is the same as NCDM

# Source Paper
[[Wang, Fei, et al. 2022]]
# Code Link
[https://github.com/bigdata-ustc/Neural_Cognitive_Diagnosis-NeuralCD]
# Performance
Testing of the model was performed using a random split of data as well as a separate scenario where data was split to simulate performance when knowledge concept coverages of students' training data are low. Model performance was validated by its ability to correctly predict if a students response to an exercise would be correct. Tests were performed with an 80/20 train test split using 5-fold cross validation runs to generate the results shown.

|     Dataset     |        Condition         | [[ACC]] | [[RMSE]] | [[AUC]] |
| :-------------: | :----------------------: | :-----: | :------: | :-----: |
|    [[MATH]]     |    Random data split     |  .805   |   .368   |  .836   |
| [[ASSIST09-10]] |    Random data split     |  .732   |   .424   |  .767   |
|    [[MATH]]     | Weak-coverage data split |  .736   |   .430   |  .691   |
| [[ASSIST09-10]] | Weak-coverage data split |  .720   |   .435   |  .732   |
Notably, Ka-NCD performs better than [[NCDM]] in all experiments but is only comparable to CNCD-Q/F in the random data scenario and performs worse in the weak-coverage scenario.