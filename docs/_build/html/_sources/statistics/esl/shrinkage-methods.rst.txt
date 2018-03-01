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
