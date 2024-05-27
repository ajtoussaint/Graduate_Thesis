# Neural Cognitive Diagnosis Model with Q Matrix Refinement
## Qualitative Description
The CNCD-Q model is an extension of [[NCDM]] that is enhanced to include a larger Q matrix with automatically identified knowledge concepts based on the text of a given exercise. A separate pre-trained CNN model is used to identify knowledge concepts from exercises.
## Input Data
- See [[NCDM]]
## Output Data
- See [[NCDM]]
## Process
 The process of CNCD-Q is similar to [[NCDM]] however additional preprocessing steps are taken to refine the Q matrix
 1. A CNN including 3 convolutional layers and a fully connected layer is pre trained on the Q matrix to determine knowledge concepts from text. 
	 1. Channel sizes are 400, 200, 100 and kernel sizes are 3, 4, 5
	 2. Max pooling was used after the 1st and 3rd convolutional layers
	 3. Rectify Linear Unity activation function was used for intermediate layers with Sigmoid used for the final output
	 4. Multi-label binary cross entropy was used as a loss function
2. For each exercise the trained CNN generates a one-hot vector "V" for the top "k" knowledge concepts present in the exercise
3. The output vector "V" of the CNN is combined with the existing Q matrix using a pairwise Bayesian method that considers the Q-matrix to be more reliable.
4. This new matrix is used in place of "Q" in NCDM![[CNCD-Q_Image_1.JPG]]
# Source Paper
[[Wang, Fei, et al. 2022]]
# Code Link
[https://github.com/bigdata-ustc/Neural_Cognitive_Diagnosis-NeuralCD]
# Performance
Testing of the model was performed using a random split of data as well as a separate scenario where data was split to simulate performance when knowledge concept coverages of students' training data are low. Model performance was validated by its ability to correctly predict if a students response to an exercise would be correct. Tests were performed with an 80/20 train test split using 5-fold cross validation runs to generate the results shown.

| Dataset  |        Condition         | [[ACC]] | [[RMSE]] | [[AUC]] |
| :------: | :----------------------: | :-----: | :------: | :-----: |
| [[MATH]] |    Random data split     |  0.804  |  0.371   |  0.835  |
| [[MATH]] | Weak-coverage data split |  0.748  |  0.418   |  0.725  |
Notably this model out performed [[NCDM]] in every experiment