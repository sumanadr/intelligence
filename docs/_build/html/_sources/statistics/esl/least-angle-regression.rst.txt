Least Angle Regression
============================================

.. admonition:: Meta
   :class: note

   date: 2016-09-29
   author: OctoMiao
   summary: Least angle regression, aka, LAR



Least Angle Regression
--------------------------

1. Algorithm 3.2
2. We want to change :math:`\beta` so that the prediction is closer to
   data :math:`y`, i.e., we require the change of :math:`\beta`
   decreases :math:`X\beta = y - r`. So the change should be
   $:raw-latex:`\propto `X^T r $.
3. Why this works? It reduces the MSE.
4. LAR is similar to lasso.
5. Modified LAR Algorithm 3.2a leads to lasso result.
6. LAR(lasso) is efficient. It takes :math:`\mathrm{min}(p,N-1)` steps
   where lasso itself might take more than p steps.
7. LAR and lasso are almost identical if we use the geometric meaning of
   the algorithms. But when some coefficient crosses 0, the differences
   pop up.
