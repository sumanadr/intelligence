Unsupervised Learning
=========================


Principle components analysis
----------------------------------------

Given a set of features,

.. math::
   X = \begin{pmatrix}
   X_1 \\
   X_2 \\
   \cdots \\
   X_n
   \end{pmatrix},

we define a transformation matrix which relates the features to a new set of features,

.. math::
   Z_i = X_j U_{ji} .

The transformation matrix is normalized,

.. math::
   \operatorname{Diag}(U U^{\mathrm T}) = ( 1, 1, ... , 1 )

The coefficients are called loadings.

The first principal component is the :math:`Z_1` that has the largest variance, where we have to adjust the coefficients or loadings to make it ture. The coefficients :math:`U_{i1}` are the elements of the loading vector.

To make it clear, we take an example where each feature has N sample data points. The values for the first principal compunent is

.. math::
   z_{n1}  = x_{n m} U_{m1},

where I have used the Einstein summation notation. The variance of the first principal component is

.. math::
   \frac{1}{n}\sum_{n=1}^N z_{n1},

which should be maximized.


.. admonition:: Relation between PCA and Linear Regression
   :class: note

   The ESL has a very nice explanation of this geometrically.




Clustering
----------------------

K-means Clustering
~~~~~~~~~~~~~~~~~~~~~~~~~


Algorithm:

1. Assign data points to a group
2. Iterate through until no change:
   1. Find centroid
   2. Find the point that is closest to the centroids. Assign that data point to the corresponding group of the centroids.

.. admonition:: How Many Groups
   :class: warning

   The art of chosing K.


Hierarchical Clustering
~~~~~~~~~~~~~~~~~~~~~~~~~


Bottom-up hierarchical groups can be read out from dendrogram.


References and Notes
-------------------------
