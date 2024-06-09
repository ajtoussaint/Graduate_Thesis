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

# Models
- [[LDM-ID]]
- [[LDM-HMI]]


# Link
[A Unified Interpretable Intelligent Learning Diagnosis Framework for Learning Performance Prediction in Intelligent Tutoring Systems (hindawi.com)](https://www.hindawi.com/journals/ijis/2023/4468025/)
# Citation
Wang, Zhifeng, et al. "A unified interpretable intelligent learning diagnosis framework for learning performance prediction in intelligent tutoring systems." International Journal of Intelligent Systems 2023 (2023).

# In Other Papers