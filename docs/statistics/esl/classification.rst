Classification
=========================


1. Qualitative variables: such as

   .. math::
      \text{eye color} \in \{ \text{brown, blue, green} \}

2. Given features and tell if the response falls in to the qualitative variables, sometimes by calculating the probabilities.


Logistic Regression
----------------------


We take two variables case as an exmple, linear regression may result in any kind of values, including negative values, which is not good for the classification probability problem. So we use logistic values.

We need a relation that is easy for our regression which guarantees that the probabilities doesn't go over 1 or below 0. It indicates that we need

.. math::
   P(X) ( 1- P(X) )  \leq 0,

or

.. math::
   \frac{P(X)}{ 1- P(X) }  \leq 0.

We notice that the first expression is also bounded within 1. It's more complicated than the second version since **the second version is monotonic but the first one is not**. So we will try to use the second approach,

.. math::
   \log \left( \frac{P(X)}{ 1- P(X) }  \right) = \beta_0 + \beta_1 X

Mathematically speaking, logistic regression is

.. math::
   P(X) =  \frac{ e^{\beta_0 + \beta_1 X} }{ 1 +  e^{\beta_0 + \beta_1 X} }.


Maximum Likelihood
---------------------------

For a bunch of independent variables, we simply multiple all the probabilities and 1-probabilities together to get a joint likelihood.



Multivarible Logistic Regression
----------------------------------------


We simply add more basis to the variable space


.. math::
   P(X) =  \frac{ e^{\beta_0 + \sum_i\beta_i X_i} }{ 1 +  e^{\beta_0 + \sum_i \beta_i X_i} }.


Note that the correlations between variables can alter the signs and make the signs of coefficients very different from single variable case.




References and Notes
-------------------------


1. https://lagunita.stanford.edu/courses/HumanitiesSciences/StatLearning
