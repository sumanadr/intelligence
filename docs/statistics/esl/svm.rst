Support Vector Machines
============================

SVM is a classification method.

1. Support Vector Classifier.
2. Support Vector Machine.


Data has No Overlap - Separable Data
-----------------------------------------


Maximal Margin Classifier: is a optimization problem in the heart.



Non-separable Data and Noisy Data
-----------------------------------

We use soft margins.

Procedures:

Maximize :math:`M`, for :math:`\sum \beta_j^2=1` (unit vector), so that

.. math::
   y_i( \beta_0 + \sum_{k=1}^{p} \beta_{k} x_{ik}  ) \geq (1-\epsilon_i)M,

with :math:`\epsilon_i \geq 0` and :math:`\sum_{i=1}^n \epsilon_i \leq C`. C is a parameter that is chosen to restrict the method.


Feature Expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Construct more variables so that parameter space becomes higher. Effectively, we are constructing a nonlinear hyperplane in the parameter space.

**Mathematically speaking, we are reconstructing the true classifier using it's Taylor expansions.**

We have talked about Support Vector Classifiers. What is the SVM then?

It might be computationial expensive to really work out support vector classfiers. One of the tricks that makes the computation easy is to use inner products.

.. math::
   f(x_k) = \beta_0 + \sum_{i=1}^n \alpha_i \langle x_k, x_i \rangle.

We estimate the parameters :math:`\alpha` and it turns out most of them can be 0. The nonzero ones defines are the actual support vectors that is most important for the classifier. The subset of vectors is selected, by nonzero :math:`\alpha`, and are denoted with :math:`\hat \alpha`.

What is the corresponding formalism for the expanded feature space? The solution is kernel and the method becomes SVM.

.. math::
   K(x_i, x_{i'}) = \left( 1 + \sum_{j=1}^p x_{ij} x_{i'j} \right)^d.

One of the popular kernel is radial kernel:

.. math::
   K(x_i, x_{i'}) = \exp \left(  - \gamma \sum_{j=1}^p (x_{ij} - x_{i'j})^2 \right).



1. SVM is better than Logistic Regression when the data is almost separable.
2. LR with ridge method is better than SVM when it's the other way around.





References and Notes
-----------------------
