Factor Graph
=================================

In the propagation of information, we are usually dealing with such relations that some system (factor) :math:`f` is related to some inputs (variable) :math:`x`.

Factor graph builds such networks of relations. In such a graph, we use boxes to represent factors, and circles to represent variables.

.. figure:: assets/factor-graph/factor-graph-wikipedia.jpg
   :align: center

   From `Factor Graph @ Wikipedia <https://en.wikipedia.org/wiki/Factor_graph#/media/File:Factorgraph.jpg>`_.

Suppose we need to find out the probability of factor :math:`f_4`, we have to take in the two variables :math:`X_2` and :math:`X_3`.

One important question is that we can actually calculate the probability of a specific configuration of the variables, which is

.. math::
   P \propto f_1(X_1) + f_2(X_1,X_2) + f_3(X_1,X_2) + f_4(X_2,X_3).

In general, we can assign weights :math:`w_i` to each factors :math:`f_i`, so that the probability of each set of variables is

.. math::
   P(X_1,X_2,X_3,X_4) \propto w_1 f_1(X_1) + w_2 f_2(X_1,X_2) + w_3 f_3(X_1,X_2) + w_4 f_4(X_2,X_3).

The normalization is the partition function, i.e., the summation of all the possible combinations of variables,

.. math::
   Z = \sum_{\{X_1,X_2,X_3,X_4\}} P(X_1,X_2,X_3,X_4).

As an example, we consider :math:`X_i` is 0 or 1. The combinations are (partially) listed below.


.. table:: List of Possible Configurations of Variables
   :widths: auto

   +-------------+---+---+---+---+-----+
   | :math:`X_1` | 0 | 1 | 1 | 1 | ... |
   +-------------+---+---+---+---+-----+
   | :math:`X_2` | 0 | 0 | 1 | 1 | ... |
   +-------------+---+---+---+---+-----+
   | :math:`X_3` | 0 | 0 | 0 | 1 | ... |
   +-------------+---+---+---+---+-----+
   | :math:`X_4` | 0 | 0 | 0 | 0 | ... |
   +-------------+---+---+---+---+-----+



References and Notes
-----------------------


1. `Factor Graph @ Wikipedia <https://en.wikipedia.org/wiki/Factor_graph>`_.
2. `DeepDive Docs <http://deepdive.stanford.edu/assets/factor_graph.pdf>`_.
