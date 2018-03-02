Introductions (Review) and Several Preliminary Statistical Methods
=========================================================================


.. admonition:: Summary
   :class: note

   Some basics of statistical learning; least squares and k nearest neighbors; statistical decision theory; local methods in high dimensions



Review
-------------

**Skeleton notes**

.. admonition:: Abbreviations
   :class: note

   1. MSE: mean squared error
   2. EPE: expected prediction error
   3. RSS: sum of squares



.. admonition:: Notations
   :class: note

   Fonts:

   1. Vectors or scalars are denoted by italic math font $X$.
   2. Components of vectors are denoted by subscripts $X_i$.
   3. Matrix is denoted by math bold font $\mathbf X$.

   Symbols

   1. $X$ for input variables;
   2. $Y$ for quantitative output;
   3. $G$ for qualitative output;
   4. $\hat {}$ for prediction.


Least Squares and Nearest Neighbors
------------------------------------


Least Squares
~~~~~~~~~~~~~~~~~~~~~~~~

Least square model:

.. math::
   \hat Y = X^T \hat \beta.


Residual sum of squares (RSS):

.. math::
   \mathrm{RSS}(\beta) = (\mathbf y - \mathbf X \beta)^{\mathrm T} (\mathbf y - \mathbf X \beta).


The parameters we need is the set that minimizes RSS, which requires

.. math::
   \frac{d}{d\beta} \mathrm{RSS} = 0.


So we can solve the parameters easily.

Nearest-Neighbor
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. For input data :math:`x`, calculate the Euclidean distance between :math:`x` and other input data :math:`x_j`.
2. Choose the :math:`k` nearest neighbors based on the distance.
3. Output prediction is determined by average of the corresponding outputs of the selected inputs.

   .. math::
      \hat Y = \frac{1}{k} \sum_{N_k} y_i.


.. admonition:: Metric of Distance
   :class: note

   For the calculation of distance, metric must be implemented. The book used examples of Euclidean metric. Another metric that can be inspiring is the hyperbolic space. I talked about this in :ref:`PopularitySimilarity`.



For Which Scenario
~~~~~~~~~~~~~~~~~~~~~~~

1. Least squares: Gaussian-like data set;
2. Nearest-Neighbor: mixture of Gaussians.


.. admonition:: Mixture of Gaussian
   :class: warning

   Mixture of Gaussians can be described by generative model. I am not really sure what that is. It seems to me that the final data is basically generated from Gaussians of different parameters which are generated randomly.



Statistical Decision Theory
-------------------------------------


1. Given input :math:`X` and output :math:`Y`;
2. Following a joint distribution :math:`\mathrm{Pr}(X,Y)`;
3. Based on input and output, we look for a function that predicts the behavior, i.e., :math:`\hat Y = f(X)`;
4. How well the prediction is defined by squared error loss :math:`L(Y,\hat Y) = (Y-\hat Y)^2`.
5. With the distribution, we predict the expected prediction error (EPE) as

   .. math::
      \mathrm{EPE}(f) = E[ ( Y- \hat Y )^2 ] = \int (y - f(x))^2 \mathrm{Pr}(dx, dy).

6. The book derived that the best prediction is :math:`f(x) = E(Y\vert X=x)`.
7. Different loss functions lead to different EPE's.


.. admonition:: About Probability Distribution
   :class: warning

   Question: Can we simply solve the probability distribution and find out the function of prediction? The conclusion says the best prediction of :math:`Y` is the conditional mean. Is it effectively solving $Y$ from the probability distribution?



Nearest-Neighbor
~~~~~~~~~~~~~~~~~~~~~~~~


1. The best prediction based on EPE is conditional mean, Eq. 2.13;
2. Both :math:`k` nearest neighbor and linear regression fits into this framework;
3. Additive models: basically turn the linear :math:`x^T\beta` into a function of :math:`f_j(X_j)`. The summation still holds.
4. The best prediction based on expectation only is conditional median.
5. Categorical variable $G$ also follows the same paradigm but with different loss function.
6. A choice of loss function for categorical case is a matrix. It has to be a matrix because we have to specify penalties a given prediction class compared to the output class. The dimension of this matrix should be the number of categories. It is rank 2.



.. admonition:: Some comments on this section
   :class: note

   1. 0 neighbor indicates an exact classification for the sample data but without the implementation of expectation values at each point since there is only one value at that point in one set of sample data;
   2. :math:`k` nearest neighbor assumed that expectation around a small patch of a point is identical to expectation at the exact point with the corresponding distribution.
   3. In **Monte Carlo method**, calculation of volume in high dimension converges very slowly. The reason is that we need a very large number of sampling points since the dimension is high. The procedure is multiplicative. The same thing might happen here. :math:`k` nearest neighbor is basically some kind of averaging procedure of the volume density. It requires a large number of sample data points to perform an fairly accurate average.
   4. The linear regression is basically a first order Taylor expansion of the approximator :math:`f(x)`, :math:`f(x) = x^T\beta`.



Local Methods in High Dimensions
--------------------------------------------

1. Curse of high dimensions: edge length of a cube of volume :math:`r` is :math:`e_p(r) = r^{1/p}`. An extreme example: :math:`(10^{-10})^{1/10} =0.1`.
2. Small volume leads to high variance.
3. Homogeneous sampling doesn't work in high dimensions. Since most points will fall near the edges.

   .. figure:: assets/10dsphere-volume-vs-radius.png
      :align: center

      Volume of 10D sphere as a function of radius.

4. Requires huge number of sample points in high dimensions.


Statistical Models, Supervised Learning and Function Approximation
---------------------------------------------------------------------

Joint Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Weird SubSection
   :class: note

   I didn't not get the point of this subsection. It seems that the authors are talking about whether it is proper to assume the relation between input and output is deterministic.


Supervised Learning
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. learn by example.


Function Approximation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Linear model;
2. Function as basis (Eq. 2.30): :math:`f_\theta(x) = \sum h_k(x)\theta_k`.
3. Examples of function bases are Fourier expansions, sigmoid, etc.
4. Learning through minimizing sum of squares (RSS), or maximum likelihood estimation, etc.
5. Maximum likelihood estimation:
   1. Likelihood: :math:`L(\theta) = \sum_{i=1}^N \log \mathrm{Pr}_\theta (y_i)`;
   2. Maximized it ("probability of the observed sample is largest")
   3. Minimizing RSS is equivalent to maximum likelihood estimation. Eq. 2.35.
