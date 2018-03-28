Tree-Based Methods
============================



Regressioin
---------------------------


It might be a overfit if we have a huge tree since we have fitted the model so well to the training data set. We need a termination condition, or we simple build a large tree then prune it to a smaller one.

Cost complexity pruning: add a punishment to the cost function

.. math::
   \sum_{t} \sum_i (y_i - \tilde y_i)^2 + \alpha t

where :math:`\alpha` can be determined from cross validation.


Categorical
----------------------

1. Gini index: purity
2. Cross entropy



Tree vs Linear Regression
------------------------------

1. Trees are box based



Bagging
-------------------------

Bootstrap aggregation


For categorical

1. Majority voting: most frequent categorical predictions
2. Average





References and Notes
---------------------------
