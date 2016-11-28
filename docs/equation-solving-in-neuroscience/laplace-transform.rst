Laplace Tranform
****************************************************


Laplace Transform
====================


Laplace transform is useful in equation solving. By definition, Laplace transform transforms a function :math:`f(x)` defined on :math:`x\geq 0` into another function by calculating the convolution

.. math::
   F(s) = \int_0^\infty e^{-s x} f(x) dx,

or symbolically,

.. math::
   F(s) = \mathcal L_s (f(x)).




A table of important Laplace transforms can be found on `mathworld.wolfram.com <http://mathworld.wolfram.com/LaplaceTransform.html>`_. Here we steal some of the commonly used.

.. math::
   \mathcal L_s (1) =& \frac{1}{s}\\
   \mathcal L_s (x^n) =& \frac{n!}{s^{n+1}}\\
   \mathcal \sin(kx) =& \frac{k}{k^2+s^2} \\
   \mathcal \cos(kx) =& \frac{s}{k^2+s^2}.

It can also be applied to differentials.

.. math::
   \mathcal L_s \left(\frac{d f(x)}{dx}\right) =& s \mathcal L_s (f(x)) - f(0) \\
   \mathcal L_s \left(\frac{d^2f(x)}{dx^2}\right) =& s^2 \mathcal L_s (f(x)) - s f(0) - \left.\frac{df(x)}{dx}\right\vert_{x=0}.

.. admonition:: Laplace Transform of Differentials
   :class: toggle

   The general form is

   .. math::
      \mathcal L_s (f^{(n)}(x)) = s^n \mathcal L (f(x)) - \sum_{m=1}^n s^{n-m} f^{(m-1)}(0).


Integrals with upper limit as argument also transform nicely.

.. math::
   \mathcal L_s \left( \int_0^x f(x') dx'  \right) = \frac{\mathcal L_s(f)}{s}.

Laplace transform is useful in solving differential equations because it transforms many equations into fractions and polynomials. A simple example is the harmonic osicllators. The equation of motion is

.. math::
   \ddot x(t) = - \omega^2 x(t),


which is transformed into

.. math::
   s^2 X(s) - s x(0) - \dot x(0) = - \omega^2 X(s).

The solution to it is

.. math::
   X(s) = \frac{ s x(0) + \dot x(0)}{s^2 + \omega^2} = x(0)\frac{ s }{s^2 + \omega^2} + \frac{\dot x(0)}{\omega} \frac{\omega}{s^2 + \omega^2}.

We can spot sin and cos from the solution, or more generally perform an inverse Laplace transform,

.. math::
   x(t) = x(0) \cos(\omega t) + \frac{\dot x(0)}{\omega} \sin(\omega t).


This example is too simple sometimes naive. However, it shows the spirit.

.. admonition:: Caveats
   :class: warning

   Laplace transform has a lot of counter intuitive expressions.

   1. Laplace transform of product of two functions :math:`f(x)g(x)` is **NOT** the product of the Laplace transforms :math:`\mathcal L_s(f)\mathcal L_s(g)`. However, if one of the functions is a constant, say :math:`f(x)=5`, we can prove that the Laplace transform of :math:`5g(x)` is :math:`5\mathcal L_s(g)`.
   2. The product of two Laplace transforms :math:`\mathcal L_s(f)\mathcal L_s(g)` is the Laplace transform of a convolution

      .. math::
         \int_0^x f(x') g(x-x') dx'.

   3. Small s corresponds to large x, due to the nature of the exponential suppression in Laplace transform. For example, for small argument x, the function :math:`e^{k t}` becomes almost 1, meanwhile, the Laplace transform of the function :math:`1/(s - k)` becomes :math:`1/s` under large s. We can see that the two limits are consistant since the Laplace transform of 1 is :math:`1/s`.
   4. In so many circumstance the Laplace transform doesn't exist simple because the integral doesn't converge. Please beware of this and use the transform only when it exists.


.. admonition:: Inverse Laplace Transform
   :class: toggle

   We do not usually use the general form of inverse Laplace transform since we can find it in the table. Nevertheless we write it down here.

   .. math::
      f(x) = \frac{1}{2\pi i} \int_{-i\infty}^{i \infty} F(s) e^{sx}ds.

   By defining :math:`s=i s^\dagger`, we can rewrite the formula

   .. math::
      f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(is^\dagger) e^{is^\dagger x} ds^\dagger .



The more interesting application is to solve matrix differential equations. For any equations

.. math::
	\partial_x \mathbf f(x) = \mathbf A \mathbf f(x),

Laplace transform takes it to the form

.. math::
	s \mathbf F(x) - f(0) = \mathbf A \mathbf F(s).

The solution is

.. math::
	\mathbf F(x) = \frac{1}{s \mathbf I - \mathbf A} \mathbf f(0) .

So the final solution for :math:`f(x)` is

.. math::
	\mathbf f(x) = \mathcal L^{-1} \left(\frac{1}{s \mathbf I - \mathbf A} \right)\mathbf f(0).


We could work out the Taylor expansion of solution,

.. math::
	\frac{1}{s \mathbf I - \mathbf A} = \frac{\mathbf I}{s}+ \frac{\mathbf A}{s^2} + \frac{\mathbf A^2}{s^3} \cdots.

The inverse Laplace transform can be done simply term by term,

.. math::
	\mathcal L^{-1} \left(\frac{1}{s \mathbf I - \mathbf A} \right) = \mathbf I + x \mathbf A + \frac{1}{2!} (x \mathbf A)^2 + \cdots = e^{x \mathbf A}.


Finally we obtain the formal solution of the system, which is


.. math::
	\mathbf f(x) = \exp\left( x \mathbf A \right)\mathbf f(0).


.. admonition:: Only Works for Constant Coefficients
	:class: warning

	This result only works for constant coefficients. In general, if the matrix :math:`A` depends on the argument :math:`x`, the solution can be systematically calculated using the so called `Magnus Expansion <https://en.wikipedia.org/wiki/Magnus_expansion>`_. However, it is as tedious as a numerical solution.



Application to Neuroscience
================================================
