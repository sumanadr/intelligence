Alternatives to Least Squares
=================================


For data with a huge amount of feature, we need **feature selection**, aka, which set of features that is our best chance of fitting the data well.

1. Subset selection;
2. Shrinkage Methods;
3. Dimension reduction.



Subset Selection
--------------------------

Best Subset Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first idea that we can think of, is to try out all the possible combinations of the features. Then out of all these models, we choose the model that works the best.

How do we define the best models? We might be able to check the RSS, etc. But do remember that we should cross validate our data instead of selecting models based on the training data only.

Stepwise Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The problem of best subset, however, is that it requires a large amount of calculation. Meanwhile, selection from all the possible combinations would usually lead to overfitting.

.. admonition:: Tip
   :class: note

   Usually we do not use best subsect selection if the dimension of the feature excedes 10 to 20. Do remember that best subset is not always the best strategy even when we can do it.


Forward stepwise selection:

1. Add in one feature each time.
2. Do not explore all the possible combinations but only test all the possible feature to add in each step.
3. Work out untill we have all the features.

.. admonition:: Computation Complexity
   :class: note

   The number of models to be tested in best subset selection is a power to the number of features. However, stepwise selection is proptional to the number of features squared.







Shrinkage Methods
------------------------

.. admonition:: Meta
   :class: note

   date: 2016-09-23
   author: OctoMiao
   summary: Shrinkage methods



Shrinkage methods
----------------------

1. Why? Some variables might be redundant. Shrink the model.


Ridge Regression
~~~~~~~~~~~~~~~~~~~~~~


Lasso
~~~~~~~~~~~~~

1. Small constraint $t$ cause some of the coefficients reduce exactly to 0: this is **variable selection**, while producing **sparse model**.
2. Convex optimization.




**Why would lasso leads to exact 0 coefficients?**

Would spot the reason as long as you plot out the constraints and the RSS. Fig. 3.11.


Compare Lasso and Ridge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For sparse models, lasso is better. Otherwise, lasso can make the fitting worse than ridge.

No rule of thumb.


Generalization
~~~~~~~~~~~~~~~~~~~~
Ridge and lasso can be generalized. Replace the distance calculation
with other definitions, i.e., :math:`\sum \lvert \beta_j \rvert^q`.

1. :math:`q=0`: subset selection
2. :math:`q=1`: lasso
3. :math:`q=2`: ridge

Smaller :math:`q` leads to tighter selection.

.. code-block:: text

   Plot[Evaluate@Table[(1 - x\ :sup:`(q))`\ (1/q), {q,
   0.5, 4, 0.5}], {x, 0, 1}, AspectRatio -> 1, Frame -> True, PlotLegends
   -> Placed[Table[“q=” <> ToString@q, {q, 0.5, 4, 0.5}], {Left, Bottom}],
   PlotLabel -> “Shrinkage as function of L-q norm disance”, FrameLabel ->
   {“!(*SubscriptBox[([Beta]), (i)])“,”!(*SubscriptBox[([Beta]), (j)])“}]



.. figure:: assets/shrinkage-methods/shrinkage-lq-norm.png
   :align: center

   Shrinkage as a function of L-q norm distance.
