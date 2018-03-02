Guass-Markov Theorem and Multiple Regression
==================================================

.. admonition:: Meta
   :class: note

   date: 2016-09-01

   author: OctoMiao

   summary: Gauss-Markov Theorem



Gauss-Markov
---------------------

#. "**Least squares** estimates the parameters :math:`\beta` have the smallest variance among all linear unbiased estimates."
#. **Unbiased estimation** is not always good.
#. ridge regression



Proof of 1
~~~~~~~~~~~~


#. Model is :math:`\theta = a^T \beta`
#. Least square estimate of :math:`\theta`:
   :math:`\hat\theta = a^T \hat \beta = a^T ( \mathbf X^T \mathbf X )^{-1} \mathbf X^T \mathbf y = \mathbf c_0^T \mathbf y`
#. This is unbiased: :math:`E(a^T\hat\beta) = a^T\beta`
#. Gauss-Markov theorem: If we have any other linear estimator
   :math:`\tilde \theta = \mathbf c^T \mathbf y` and
   :math:`E(\mathbf c^T \mathbf y)=a^T \beta`, then
   :math:`Var(a^T\hat \beta)\leq Var(\mathbf c^T \mathbf y)`.
#. To prove it we first write down the general form of a linear
   estimator. **Question:** is the general form of a linear estimator
   :math:`\alpha (X^T X)^{-1} X^T + D`?



Useful functions for the proof:

1. Variance: :math:`Var(X) = E[ (X - \mu)^2 ]`.
2. `On wikipedia <https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem#Proof>`_


1. MSE:
   :math:`MSE(\tilde\theta) = E( (\tilde\theta -\theta)^2 ) = E( (\tilde \theta - E(\theta) + E(\theta) - \theta)^2 ) = E( (\tilde\theta - E(\theta))^2 ) + \cdots`
2. MSE is
   :math:`MSE(\tilde \theta) = Var(\tilde theta) + (E(\theta) -\theta)^2`
   the second term is bias.
3. Least square is good but we can trade some bias to get a smaller
   variance sometimes.
4. Choices are variable subset selection, ridge regression.


1. Suppose new data is biased from the original data by a value
   :math:`\epsilon_0`, the MSE using the original estimator is only the
   original MSE differed by a constant. Eq. 3.22
2. We always have a larger MSE????? I don’t get this.

Multiple Regression
---------------------------

1. Model: :math:`f(X) = \beta_0 + \sum_{j=1}^p X_j \beta`
2. For multiple dimensional inputs, the estimator has no correlations for different features.
