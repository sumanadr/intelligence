Nonlinear Models
============================


What we are really doing in statistical learning is to find a approximator for the data.

Suppose we have a model for some data :math:`X`, which describes the data as

.. math::
   Y = F(X),

where :math:`F(X)` is some function of data and :math:`Y` is the prediction. In principle, it can be any function since data can be very complicated. However, Taylor expansion tells us that

.. math::
   F(X) = \hat \beta_0  + \hat \beta_1 x_1 +\hat \beta_2 x_2 +\cdots.

Think about linear regression. It's just an approximator that neglects the higher orders. In principle we could put in higher orders for the data. These models with higher orders are called polynomial regression.

In general, we could think of other forms, such as fourier series, wavelets, step functions, etc.

Polynomial Regression
----------------------

.. admonition:: Tails in Polynomial Regression
   :class: note

   Polynomials are wiggly at the tails. We usually discard them.



Step Functions
---------------------------
