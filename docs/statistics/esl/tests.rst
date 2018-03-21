Tests
=======================





Z-score
---------------------

Suppose we have some sample data and we developed a theory for that data. The theory assumes that the mean of the distribution is :math:`\mu_{\bar x}`. However, we calculated the sample mean :math:`\bar x`. The question to ask is to find a measure how well the statistics work.

We calculate

.. math::
   z = \frac{\bar x - \mu_{\bar x}}{\sigma_{\bar x}}.

This z-score tells us the deviations of our sample mean from the actual mean, in unit of standard deviations. For example, if :math:`z=1`, then the deviation of our sample mean from the population mean is of the size one standard deviation.

We do not know the value of standard deviation of the assumed standard deviation :math:`\sigma_{\bar x}`. However, the central limit theorem shows that :math:`\sigma_{\bar x} = \sigma/\sqrt{N}`, where :math:`\sigma` is the standard deviation of the population, and :math:`N` is the sample size.

In principle, we do not really know the population standard deviation :math:`\sigma`. We might be able to approximate this value using the sample standard deviation :math:`\sigma_s`, if the sample size is large enough (larger than 30).

Finally the expression is

.. math::
   \frac{\bar x - \mu_{\bar x}}{ \sigma_s/\sqrt{N} }.

For large sample size (>30), this expression is a z-distribution, which makes the the expression much more easy to understand and meaningful. If the sample size is small (<30), we have a t-distribution. Then we need a t-statistics table to figure out what happens.
