Random Walks
====================


There exists several simple models of random walks. It can be either fixed stepsize but random directions or varying stepsize.



Fixed Stepsize
----------------------

A simple model is that we assume each step is a step of size :math:`\epsilon`, but with random directions. The position of this random walker at step :math:`N` is the summation of all the steps (vectors),

.. math::
   \vec X = \sum_i^N x_i,

where :math:`x_i` is the vector that represents step i.

What we want to find out is the places that the random walker explored after :math:`N` steps. The corresponding quantity that represents it is :math:`\sqrt{\langle \vec X^2 \rangle}`.

From the idea of random walk, we know that

.. math::
   \langle \vec x_i \rangle =& 0 \\
   \langle \vec x_i \cdot \vec x_j \rangel =& 0.

Thus

.. math::
   \langle \vec X^2 \rangle = & \sum_i \vec x_i\cdot \vec x_i \\
   =& N \epsilon^2.

Then we find out that

.. math::
   \bar X = \sqrt{\langle \vec X^2 \rangle} = \sqrt{N}\epsilon.
   :label: eqn-rms-distance


Significance of Dimension
--------------------------------------


From the root-mean-squared distance Eq. :eq:`eqn-rms-distance` we can define the density of points. Suppose we have a continues version of this random walk. After time :math:`t`, the random walker walked a distance :math:`vt`. Meanwhile the random walker explored a region of radius :math:`\sqrt{t}v`, which corresponds to a volume :math:`V \propto \sqrt{t}v`. The density of walked points is defined as

.. math::
   \rho \propto \frac{t}{\sqrt{t}^d} = t^{1-d/2},

where :math:`d` is the dimension of the space.

We spot this critical dimension :math:`d=2`.

1. :math:`d<2`: the density of points at :math:`t\to\infty` becomes :math:`\rho\to \infty`. This called recurrent behavior. We are sure that after infinite time, we are going back to a point that we visited before.
2. :math:`d=2`: the density of points at :math:`t\to\infty` becomes :math:`\rho\to \mathrm{Constant}`. **This derivation is wrong about this critical case.** It should be :math:`\rho\to \ln t`
3. :math:`d>2`: the density of points at :math:`t\to\infty` becomes :math:`\rho\to 0`. This is called transit behavior. We are not sure that we could go back to a point that we visited before.







Refs & Notes
-------------------

1. `Sid Redner's Lectures @ Santa Fe Institute <https://www.santafe.edu/engage/learn/courses/random-walks>`_
