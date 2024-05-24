# Neural Cognitive Diagnosis Model
## Qualitative Description
The NCDM model seeks to perform cognitive diagnosis by leveraging neural networks to model the complex non-linear process of students interacting with exercises. The model aims to produce an interpretable diagnostic report of student proficiency of knowledge concepts based on a set of student responses to exercises and an association between exercises and knowledge concepts. 

## Input Data
-  The exists some set of students "S", exercises "E", and knowledge concepts "K"
- Q matrix relating a set of exercises to a set of knowledge concepts. The value of Q_ij is 1 if concept j is relevant to exercise i and 0 otherwise. Typically the Q matrix is labeled by an expert in the subject matter.
- A set of response logs (s, e, r) where s is a given student, e an exercise, and r the student's percentage score on the exercise from 0 to 1.
## Output Data
 - Students proficiency in knowledge concepts
## Process
 1.  Student proficiency for each exercise (hs) is determined by multiplying a student one-hot vector which identifies a single student by id with a trainable matrix A. ![[NCDM_Image_2.JPG]]
 2. Knowledge relevancy (Qe) is determined by multiplying an exercise one-hot vector which identifies a single exercise by id with the provided Q matrix: ![[NCDM_Image_3.JPG]]

 3. Knowledge difficulty (hdiff) is determined by multiplying the exercise one-hot vector with a trainable matrix B. Values within B are restricted to be positive:![[NCDM_Image_4.JPG]]
 4. Knowledge discrimination (hdisc) is determined by multiplying the exercise one-hot vector with a trainable matrix D. Values within D are restricted to being positive:![[NCDM_Image_5.JPG]]
 5. The first interaction of these 4 input variables is based on [[MIRT]] models. The open circle represents element wise multiplication of Qe and the result of (hs - hdiff):![[NCDM_Image_6.JPG]]
 
6. The resulting vector x is then passed through two fully connected layers of a neural network and a final output layer that each have trainable weights and biases. The layer dimensions were 512, 256, and 1 respectively. The activation function used is the sigmoid function. The [[monotonicity]] assumption is implemented by restricting W1, W2, and W3 to non-negative values: 
![[NCDM_Image_7.JPG]]

The entire process is summarized in the following Image:![[NCDM_Image_1.JPG]]
# Source Paper
[[Wang, Fei et al. 2022]]
# Code Link
[https://github.com/bigdata-ustc/Neural_Cognitive_Diagnosis-NeuralCD]
# Performance
Testing of the model was performed using a random split of data as well as a separate scenario where data was split to simulate performance when knowledge concept coverages of students' training data are low. Model performance was validated by its ability to correctly predict if a students response to an exercise would be correct. Tests were performed with an 80/20 train test split using 5-fold cross validation runs to generate the results shown.

|     Dataset     |        Condition         | [[ACC]] | [[RMSE]] | [[AUC]] |
| :-------------: | :----------------------: | :-----: | :------: | :-----: |
|    [[MATH]]     |    Random data split     |  0.792  |  0.378   |  0.820  |
| [[ASSIST09-10]] |    Random data split     |  0.719  |  0.439   |  0.749  |
|    [[MATH]]     | Weak-coverage data split |  0.735  |  0.432   |  0.649  |
| [[ASSIST09-10]] | Weak-coverage data split |  0.710  |  0.455   |  0.633  |

