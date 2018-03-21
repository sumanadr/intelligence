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


.. admonition:: Fermi-Dirac Distribution
   :class: warning

   This is the Fermi-Dirac distribution in statistical mechanics.


Maximum Likelihood
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a bunch of independent variables, we simply multiple all the probabilities and 1-probabilities together to get a joint likelihood.



Multivarible Logistic Regression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


We simply add more basis to the variable space


.. math::
   P(X) =  \frac{ e^{\beta_0 + \sum_i\beta_i X_i} }{ 1 +  e^{\beta_0 + \sum_i \beta_i X_i} }.


Note that the correlations between variables can alter the signs and make the signs of coefficients very different from single variable case.

Case-Control Sampling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In reality, we might not be able to really monitor some experiment through out too many years. One of the techniques that allows us to learn something is to use the case-control sampling. We choose some cases and controls and work out the statistics.

The regression parameters for logistic regress is calculated

.. math::
   \hat\beta^*_0 = \hat \beta_0 + \log \frac{\pi}{1-\pi} - \log \frac{\tilde \pi }{ 1-\tilde \pi },

where :math:`\hat\beta^*` is the corrected interception in the model, :math:`\hat \beta_0` is the intercept that is obtained by fitting the data, :math:`\tilde \pi ` is the number of cases over the sum of cases and control. For example, if we have 10 cases and 90 controls, we calculate :math:`\tilde \pi=10/(10+90)=0.1`. The value of :math:`\pi` might be obtained by some other study that shows the actual prevalence among the population.

We usually need more controls to really fit the model, for example we probably need five times more controls than cases.

.. admonition:: For Rare Situation
   :class: warning

   Case-control works well for situation such as diseases, spam emails, etc. It doesn't work for the situation where the prior probilities for two classes are almost the same.


More than two classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fit models with more than two classes, softmax probability has been developed.

.. math::
   P_k = \frac{ e^{\beta_{0k} + \sum_i\beta_{ik} X_i} }{ \sum_k e^{\beta_{0k} + \sum_i \beta_{ik} X_i} },

where :math:`k` indicates which class we are calculating.

This is basically a Boltzmann distribution, and the summation is the partition function.


Linear Discriminant Analysis
-----------------------------

Bayes Theorem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Everyboday knows it.

But here we are going to rewrite it.

.. math::
   P_k = \frac{ \pi_i f_i(x)  }{ \sum \pi_l f_l(x) },

where :math:`P_k = P(\text{Prediction for class k} | \text{Variables }x)`, :math:`\pi_k` is the probability for class k, :math:`f_k(x)` is the probability density for class k.

1. DA is good even when the classes are well seperated, or small number of samples, but logistic regression fails;
2. Also works well for multiple classes.



Gaussian Discriminant Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The density can be chosen to be the Gaussian distribution,

.. admonition:: Gaussian Distribution
   :class: note

   .. math::
      f_k(x) =  \frac{ 1 }{ \sqrt{2\pi} \sigma_k } e^{ -\frac{1}{2} \left( \frac{x-\mu_k}{\sigma_k} \right)^2 }.

In principle we can plug in the distribution to calculate the probabilities. However, we are mostly interested in the largest probabilities, which is related to a quantity called **discriminant function**. Probabilities can be reconstructed using it.

It can also be done for multivariable statistics.

Quadratic Discriminant Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Naive Bayes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





References and Notes
-------------------------


1. https://lagunita.stanford.edu/courses/HumanitiesSciences/StatLearning
