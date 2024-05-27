# Degree of Agreement
An interpretability metric used in cognitive diagnosis which measures the degree of agreement between cognitive results and response records. DOA is calculated for each knowledge concept and averaged as an evaluation metric.

For a given knowledge concept "k" the DOA is calculated as shown ([[Wang, Fei, et al. 2022]]):![[DOA_Image_1.JPG]]

F^s_ak is the proficiency of student a for knowledge concept k. When Fa > Fb the of that function is 1, otherwise 0. 

I_jk is 1 if an exercise contains the given knowledge concept and 0 otherwise.

J(j, a, b) is 1 if both students a and b did the exercise and 0 otherwise

