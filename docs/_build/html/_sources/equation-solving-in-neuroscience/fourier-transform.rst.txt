Fourier Tranform
****************************************************

Fourier Serious and Continuous Fourier Transform
==============================================================================

A function :math:`f(x)` defined on :math:`x\in [-L, L]` can be decomposed into Fourier series

.. math::
   f(x) = \sum_{-\infty}^\infty A_n e^{i n k_0 x },

where

.. math::
   k_0 = 2 \pi/ 2 L = \pi/L.



A continuous Fourier transform is not very different from Fourier series for equation solving. A function :math:`f(x)` can be written as a convolution of another function :math:`g(x)`,

.. math::
   f(x) = \int_{-\infty}^\infty g(t) e^{2\pi i x t} dt,
   :label: eqn-fourier-transform-original-1

where :math:`f(x)` is the Fourier transform of :math:`g(t)`. It is called a **transform** because we have a change of variable from t to x. This form is not convinient for the purpose of equation solving. We usually write it as

.. math::
   f(x) = \frac{1}{2\pi}\int_{-\infty}^\infty g(k) e^{i k x} dk,

which is derived by plug :math:`k=2\pi t` in to Eq. (:eq:`eqn-fourier-transform-original-1`).


.. admonition:: Some Tips about Differential Equations
   :class: toggle

   It's useful to try out Fourier series and Fourier transform on some frequently used operators.

   For Fourier series

   .. math::
      \frac{d}{dx}f(x) = \frac{d}{dx}\sum_{-\infty}^\infty A_n e^{i n k_0 x } = \sum_{-\infty}^\infty A_n \frac{d}{dx} e^{i n k_0 x } = \sum_{-\infty}^\infty (i n k_0) A_n  e^{i n k_0 x }.

   As we apply Fourier transform,

   .. math::
      \frac{d}{dx}f(x) = \frac{1}{2\pi}\int_{-\infty}^\infty g(t) \frac{d}{dx} e^{i x t} dt = \frac{1}{2\pi} \int_{-\infty}^\infty g(t) (i x t)e^{i x t} dt,

   which is more or less similar to the result from Fourier series.


Application in Equation Solving
=====================================

**We provide two examples. The first one is a homogenous equation that is NOT solved using this method. The second equation is a inhomogenous one.**


In the first example, we apply Fourier series and Fourier transform to the differential equation of harmonic oscillators,


.. math::
   \ddot x(t) = - \omega^2 x(t),
   :label: eqn-harmonic-oscillator-eom

where :math:`\dot {} = \frac{d}{dt}`.

The second example will be a damped oscillator, which is

.. math::
   \ddot x(t) = - \omega^2 x(t) + f(t).
   :label: eqn-damped-harmonic-oscillator-eom


Homogeneous Equations
------------------------------------------

We'll find out that homogenous differential equations doesn't have solutions of the Fourier series type. The reason is that the transform of the solution to a homogeneous equation diverges. However, we still love this example because it shows us that using this method doesn't garantee that we will find a solution.


Using Fourier Series
~~~~~~~~~~~~~~~~~~~~~~~~~~

Insert Fourier series of :math:`x(t) = \sum_{-\infty}^{\infty} A_n e^{i n k_0 t }` into equation of harmonic oscillator (:eq:`eqn-harmonic-oscillator-eom`),

.. math::
   \ddot \sum_{-\infty}^{\infty} A_n e^{i n k_0 t } = - \omega^2 \sum_{-\infty}^{\infty} A_n e^{i n k_0 t }.

The derivatives will only apply to term :math:`e^{i n k_0 t }`, so that the equations becomes,

.. math::
   \sum_{-\infty}^{\infty} (i n k_0)^2 A_n e^{i n k_0 t } = - \omega^2 \sum_{-\infty}^{\infty} A_n e^{i n k_0 t }.

We move everything to the left side and combine the summations,

.. math::
   \sum_{-\infty}^{\infty} \left( (i n k_0)^2   +  \omega^2   \right)A_n e^{i n k_0 t } = 0.

The only possible solution to this equation is that the coefficient is zero, i.e.,

.. math::
   (i n k_0)^2   +  \omega^2  =0,

which has a solution of interest

.. math::
   k_0 =\pm \omega /n.

This result is the dispersion relation like solution to the system. However, we can not construct the original solution from this relation only. The reason is that the equation is homogeneous.


Using Fourier Transform
~~~~~~~~~~~~~~~~~~~~~~~~~~

We assume that the function :math:`x(t)` that we are looking for is a Fourier transform of another function :math:`\hat x(\tau)`

.. math::
   x(t) = \frac{1}{2\pi} \int_{-\infty}^\infty \hat x(k) e^{i k t} dk.

Insert this transform into the equation of harmonic oscillator (:eq:`eqn-harmonic-oscillator-eom`),

.. math::
   \frac{d^2}{dt^2} \frac{1}{2\pi} \int_{-\infty}^\infty \hat x(k) e^{i k t} dk = - \omega^2 \frac{1}{2\pi} \int_{-\infty}^\infty \hat x(k) e^{i k t} dk,

which is simplified to

.. math::
   \frac{1}{2\pi} \int_{-\infty}^\infty \left(  (i k  )^2  + \omega^2 \right) \hat x(\tau) e^{ik t} dk .

We find ourselves in the same situation as the Fourier series solution. No solution is found.


Inhomogeneous Equations
------------------------------

For an inhomogeneous equation (:eq:`eqn-damped-harmonic-oscillator-eom`), we can apply the same trick. However, we use Fourier transform for generality. Please note that the Fourier transform requires the solution to be defined on a range of the argument.

Before we actually work out the case, here are some tricks. We always use hat to denote the inverse Fourier transformed equation. Fourier transform of the equation actually will be a replacement of the following,

.. math::
   f(t)\to \hat f(k) \\
   x(t)\to \hat x(k) \\
   \dot x(t) \to (ik )\hat x(k) \\
   \dot x(t) \to (ik )^2\hat x(k).

Using these rules, we find out the Fourier transform equation of (:eq:`eqn-damped-harmonic-oscillator-eom`),

.. math::
   (ik )^2 \hat x(k) + \omega^2  \hat x(k) = \hat f(k),

which has a solution

.. math::
   \hat x(k) = \frac{ \hat f(k) }{ -k^2 + \omega^2 },

so that the final solution we are looking for becomes

.. math::
   x(t) =& \frac{1}{2\pi}\int_{-\infty}^\infty \hat x(k) e^{i k t} dk \\
   =& \frac{1}{2\pi}\int_{-\infty}^\infty  \frac{ \hat f(k) }{ -k^2 + \omega^2 } e^{i k t} dk.

We know :math:`f(t)` so :math:`\hat f(k)` can be calculated.




Application to Neuroscience
==========================================
