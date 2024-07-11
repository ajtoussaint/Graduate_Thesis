#todo
# A unified interpretable intelligent learning diagnosis framework for learning performance prediction in intelligent tutoring systems
## Summary
- [[Maris 1999]] shows the problems of interpretability for statistical models and also they don't work on big data, and this has continued due to black box nature of neural networks
- Goal is to create a model that can leverage power of neural network while being interpretable with respect to cognitive parameters, learner-resource response network, and weights of self-attention mechanism,
- Students outnumber teachers, personal intervention is essential
The model
- Multichannel psychometric models are used to initialize the learning diagnosis of learners
- separate networks are used to represent the learner and the learning resource
- A third network extracts deep features from the output of the other two
- Deep features are fused with shallow features and weighed according to an attention network
- Two models were created:
	- LDM-ID is IRT + DINA
	- LDM HMI is HoDINA + IRT + MIRT
- !!! AUC is used as a metric of accuracy and RMSE as stability
- CL21 dataset is available on github
Suggestions for future work:
- introduce more diagnosis models into the framework
Related Work
- This paper segregates other works into "psychometric" which focuses on mining cognitive situation and "deep learning" which focus on prediction of learning performance
- psychometric models can be continuous like [[IRT]] or discrete like [[DINA]]
- discrete models seek to classify a learner into one of 2^k states while continuous models seek to determine a specific value for each k
- Psychometric models suffer from focusing on a pre-selected set of cognitive parameters and struggle to generalize
- This paper has some good references for the general utility history of deep learning methods in other fields
- 5 types of nns used in this task
	- recurrent
		- considers the sequence in which questions are answered
	- convolutional
		- personalized to consider prior knowledge and learning rate from the learner, can combine with recurrent
	- memory
		- limited
	- graph
		- Knowledge graphs model the relationships between concepts
	- deep
		- lacks the ability to provide useful feedback, black box
	- A multitude of other sources for each of these types of models exist
- This paper was motivated by 3 research questions
	- Can we create a framework that uses multidimensional cognitive parameters in a broader range of learning scenarios
	- Can we create a framework that accurately characterizes learners and resources while maintaining effective interactions
	- Can we improver performance and usability

Model Assumptions:
- data is authentic and complete
- learners answers are partially independent
	- not affected by other students responses or the content of other exercises
Model Definitions
- Shallow feature of learning resource: essentially a knowledge concept
- Shallow feature of learners: same dimension as ^
- Deep feature of learning resource and learners: higher order bottleneck features characterizing the response between learners and resources
Model outputs
- parameters of learners, resources, learner performance prediction
Model process:
- Initial Learning Diagnosis: makes a preliminary diagnosis on the learner (SC) and resource (EC) based on historical data. Multiple psychometric models are applied and combined into a vector
- Learner and Learning Resources Representation Network: 
	- SC is encoded as a $d_0$ and EC is encoded as $d_1$ which are one hot vectors
	- separate two  layer auto-encoders are applied to $d_0$ and $d_1$ to excavate valuable features
- Learner Resource Response Network
	- concatenates the out put of the autoencoders and applies it as the input to another layer which simulates the "answer process"
	- tanh activation function is used for all layers described above
- Self attention mechanism
	- self attention mechanism and convolutional layer fully mine fusion of learner and resource to determine which features have an impact
- Learning Performance Prediction
	- A CNN kernel size 3, step size 1, ReLU activation function, max pooling
		- Obtains a predicted value p of a learners answer on a specific task
	- Use cross entropy function between real answer and predicted
Interpretability
- cognitive state, Difficulty and discrimination are practically interpretable in relation to psychometric theory
- Learner-Resource response network shows info about the interaction between the two
- Self attention module explains why the network makes the predictions that it does




# Models
- [[LDM-ID]]
- [[LDM-HMI]]


# Link
[A Unified Interpretable Intelligent Learning Diagnosis Framework for Learning Performance Prediction in Intelligent Tutoring Systems (hindawi.com)](https://www.hindawi.com/journals/ijis/2023/4468025/)
# Citation
Wang, Zhifeng, et al. "A unified interpretable intelligent learning diagnosis framework for learning performance prediction in intelligent tutoring systems." International Journal of Intelligent Systems 2023 (2023).

# In Other Papers