# Neural Cognitive Diagnosis Model with Text Factor Extension
## Qualitative Description
The CNCD-F model is an extension of [[NCDM]] that considers the difficulty of phrasing in a question based on text factors when determining student response probability. A separate "TextCNN" network model is sued to evaluate the text and develop a "text factor" that indicates how confusing or straightforward the wording of the question may be. This factor is include as an input to the main network used in NCDM. Additionally the "A" and "Q" matrices used in NCDM are extended to include a skill that represents a students ability to deal with difficult texts.
## Input Data
- See [[NCDM]]
## Output Data
- See [[NCDM]]
## Process
1. The "Text CNN" architecture is borrowed from another paper, "Convolutional neural networks for sentence classification" (Y. Kim)
	1. Three filters are used in the Text CNN of size 150, 150, and 150 with kernel size 3, 4, and 5
	2. Average Pooling was used after each filter
	3. Rectify Linear Unit activation function was used for convolution layers and Sigmoid for the output layer
	4. Dropout of the output layer was set to 0.5
2. The plain text of the problem is fed through the above network to generate a text factor
3. The text factor is included in the input equation of [[NCDM]] as shown in the figure below. Note that Q and A are expanded as mentioned in the qualitative description above to accommodate the text factor.![[CNCD-F_Image_1.JPG]]

# Source Paper
[[Wang, Fei, et al. 2022]]
# Code Link
[https://github.com/bigdata-ustc/Neural_Cognitive_Diagnosis-NeuralCD]

# Performance
Testing of the model was performed using a random split of data as well as a separate scenario where data was split to simulate performance when knowledge concept coverages of students' training data are low. Model performance was validated by its ability to correctly predict if a students response to an exercise would be correct. Tests were performed with an 80/20 train test split using 5-fold cross validation runs to generate the results shown.

| Dataset  |        Condition         | [[ACC]] | [[RMSE]] | [[AUC]] |
| :------: | :----------------------: | :-----: | :------: | :-----: |
| [[MATH]] |    Random data split     |  .802   |   .370   |  .840   |
| [[MATH]] | Weak-coverage data split |  .741   |   .419   |  .732   |
Notably this model out performed [[NCDM]] in every experiment and had the highest AUC score of any model in it's source paper under both conditions