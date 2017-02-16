Green's Function Method
*******************************



Green's Function Method
==================================

In this section, we demonstrate Green's function method of solving differential equations.


Cable Equation
-------------------

The cable equation is written as [Gerstner2002]_

.. math::
   \frac{\partial}{\partial t} u(t,x) = \frac{\partial^2}{\partial x^2} u(t,x) - u(t,x) + i_{e}(t,x),
   :label: eqn-cable-equation-potential


or

.. math::
   \frac{\partial}{\partial t} i(t,x) = \frac{\partial^2}{\partial x^2} i(t,x) - i(t,x) + \frac{\partial}{\partial x} i_e (t,x),
   :label: eqn-cable-equation-current


where :math:`t`, :math:`x`, :math:`i`, :math:`i_e` are all renormalized unit less quantities. For the meaning and definition of them, ref. page 55 of Gerster 2002 [Gerstner2002]_.



Solutions to Cable Equation
---------------------------------


Stationary Solution
~~~~~~~~~~~~~~~~~~~~~~~~

Equation :eq:`eqn-cable-equation-potential` can be solved for stationary case, which is

.. math::
   \frac{\partial^2}{\partial x^2} u(t,x) - u(t,x) =- i_{e}(t,x) .
   :label: eqn-cable-equation-stationary-equation-potential


While many methods can be used to solve second order nonhonogenerous differential equations, Green's function is the most general and useful one.



.. admonition:: Definition of Green's Function
   :class: note

   The idea of Green's function is very simple. TO solve a general solution of equation

   .. math::
      \frac{d^2}{d x^2} y(x) + y(x) = f(x),
      :label: eqn-green-function-example

   where :math:`f(x)` is the source and some given boundary conditions. To save ink we define

   .. math::
      \hat L_x = \frac{d^2}{dx^2} + 1,

   which takes a function :math:`y(x)` to :math:`f(x)`, i.e.,

   .. math::
      \hat L_x y(x) = f(x).
      :label: eqn-green-function-example-1


   Now we define the Green's function to be the solution of equation :eq:`eqn-green-function-example-1` but replacing the source with delta function :math:`\delta(x-z)`

   .. math::
      \hat L_x G(x,z) = \delta(z-x).


   Why do we define this function? The solution to equation :eq:`eqn-green-function-example` is given by

   .. math::
      y(x) = \int G(x,z) f(z) dz.


   To verify this conclusion we plug it into the LHS of equation :eq:`eqn-green-function-example`

   .. math::
      & \left(\frac{d^2}{dx^2} +1 \right) \int G(x,z) f(z) dz \\
      =& \int \left[ \left(\frac{d^2}{dx^2} +1 \right) G(x,z) \right] f(z) dz \\
      =& \int \delta(z-x) f(z) dz \\
      =& f(x),

   in which we used one of the properties of Dirac delta distribution

   .. math::
      \int f(z) \delta(z-x) dz = f(x).

   Also note that delta function is even, i.e., :math:`\delta(-x) = \delta(x)`.

   So all we need to do to find the solution to a standard second differential equation

   .. math::
      \left( \frac{d^2}{dx^2} + p(x) \frac{d}{dx} + q(x) \right)y(x) = f(x)

   is do the following.



   1. Find the general form of Green's function (GF) for operator for operator :math:`\hat L_x`.
   2. Apply boundary condition (BC) to GF. This might be the most tricky part of this method. Any ways, for a BC of the form :math:`y(a)=0=y(b)`, we can just choose it to vanish at :math:`a` and :math:`b`. Otherwise we can move this step to the end when no intuition is coming to our mind.
   3. Continuity at :math:`n-2` order of derivatives at point :math:`x=z`, that is

   .. math::
      G^{(n-2)}(x,z) \vert_{x<z} = G^{(n-2)} \vert _{x>z} ,\qquad \text{at } x= z.

   4. Discontinuity of the first order derivative at :math:`x=z`, i.e.,

      .. math::
         G^{(n-1)}(x,z)\vert_{x>z} - G^{(n-1)}(x,z)\vert_{x<z} = 1, \qquad \text{at } x= z.


      This condition comes from the fact that the integral of Dirac delta distribution is Heaviside step function.

   5. Solve the coefficients to get the GF.
   6. The solution to an inhomogeneous ODE  :math:`y(x)=f(x)` is given immediately by

      .. math::
         y(x) = \int G(x,z) f(z) dz.


      If we haven't done step 2 we know would have some unkown coefficients which can be determined by the BC.





.. admonition:: How to Find Green's Function
   :class: note

   So we are bound to find Green's function. Solving a nonhonogeneous equation with delta as source is as easy as solving homogeneous equations.

   We do this by demonstrating an example differential equation. The problem we are going to solve is

   .. math::
      \left(\frac{d^2}{dx^2} + \frac{1}{4}\right) y(x) = f(x),

   with boundary condition

   .. math::
      y(0) = y(\pi) = 0.
      :label: eqn-green-function-example2-bc



   For simplicity we define

   .. math::
      \hat L_x = \frac{d^2}{dx^2} + \frac{1}{4}.


   **First of all we find the GF associated with**

   .. math::
      \hat L_x G(x,z) = \delta(z-x).


   We just follow the steps.

   1. The general solution to

      .. math::
         \hat L_x G(x,z) = 0

      is given by

      .. math::
         G(x,z) = \begin{cases}
         A_1\cos (x/2) + B_1 \sin(x/2), & \qquad x \leq z, \\
         A_2\cos (x/2) + B_2 \sin(x/2), & \qquad x \geq z.
         \end{cases}

   2. Continuity at :math:`x=z` for the 0th order derivatives,

      .. math::
       G(z_-,z) = G(z_+,z),

      which is exactly

      .. math::
         A_1\cos(z/2) + B_1 \sin(z/2) = A_2 \cos(z/2) + B_2\sin(z/2).
         :label: eqn-green-function-example2-continuity

   3. Discontinuity condition at 1st order derivatives,

      .. math::
         \left.\frac{d}{dx} G(x,z)  \right\vert_{x=z_+} - \left.\frac{d}{dx} G(x,z)  \right\vert_{x=z_-} = 1,

      which is

      .. math::
         -\frac{A_2}{2}\sin\frac{z}{2} + \frac{B_2}{2} \cos\frac{z}{2} - \left( -\frac{A_1}{2}\sin\frac{z}{2} + \frac{B_1}{2}\cos\frac{z}{2} \right) = 1
         :label: eqn-green-function-example2-discontinuity


      Now we combine :eq:`eqn-green-function-example2-continuity` and :eq:`eqn-green-function-example2-discontinuity` to eliminate two degrees of freedom. For example, we can solve out :math:`A_1` and :math:`B_1` as a function of all other coefficients. Here we have

      .. math::
         B_1 &= \frac{ - 2/\sin(z/2) }{\tan(z/2) + \cot(z/2)} + B_2 , \\
         A_1 &= A_2 + B_2(\tan(z/2)-1) + \frac{2}{\sin(z/2) + \cot(z/2)\cos(z/2)}.

   4. Write down the form solution using :math:`y(x) = \int G(x,z) f(z) dz`. Then we still have two unknown free coefficients :math:`A_2` and :math:`B_2`, which in fact is to be determined by the BC equation :eq:`eqn-green-function-example2-bc`.








The stationary equation :eq:`eqn-cable-equation-stationary-equation-potential` can be written as

.. math::
   \hat L_x u(x) = - i_e(t,x),

where :math:`\hat L_x = \frac{d^2}{dx^2} -1`. The boundary condition is the vanishing wave at infinity :math:`u(\pm\infty)=0`. As we are talking about stationary equation, the source should be time-independent, thus we take only a one dimension Dirac distribution :math:`\delta(x)` to solve for GF.

The general Green's function is [1]_

.. math::
   G(x,x') = \begin{cases}
   C_1 e^{-x} + D_1 e^{x}, & \qquad x\leq z,\\
   C_2 e^{-x} + D_2 e^{x}, & \qquad x\geq z.
   \end{cases}



.. admonition:: Solving Homogeneous Equation
   :class: note

   The corresponding homogeneous equation is

   .. math::
      \frac{d^2}{dx^2} u(x) - u(x) = 0.


   To find the general solution we assume it has the form

   .. math::
      u(x) = A e^{\omega x},

   which is then plugged back into the equation,

   .. math::
      (\omega^2 - 1) u(x) = 0.


   We require :math:`\omega^2-1=0` to make the solution most general, which leads to

   .. math::
      \omega = \pm 1.


   Finally we write down the general solution to this homogeneous equation,

   .. math::
      u(x) = C e^{x} + D e^{-x}.




In this simple case, BC can be applied to Green's function first [2]_, which means

.. math::
   G(-\infty,x') &= 0, \\
   G(\infty,x') &= 0.


These conditions can significantly simplify the GF,

.. math::
   G(x,x') = \begin{cases}
   D_1 e^{x}, & \qquad x<x',\\
   C_2 e^{-x}, & \qquad x>x'.
   \end{cases}


Then we use the continuity condition and discontinuity condition,

.. math::
   G(x'_-,x') - G(x'_+,x') &= 0\\
   \left.\frac{d}{dx}G(x,x')\right\vert_{x=x'_+} - \left.\frac{d}{dx}G(x,x')\right\vert_{x=x'_-} &= 1,

which is basically

.. math::
   D_1 e^{x'} - C_2 e^{-x'} &= 0,\\
   - C_2 e^{-x'} - D_1 e^{x'} & =1.


Solving out the coefficients, we get

.. math::
   D_1 & = \frac{1}{2}e^{-x'},\\
   C_2 &= \frac{1}{2}e^{x'}.


Then we reached the complete and final GF,

.. math::
   G(x,x') = \begin{cases}
   \frac{1}{2}e^{x-x'}, & \qquad x<x'\\
   \frac{1}{2}e^{x' - x}. & \qquad x>x'
   \end{cases}


Given any general source :math:`-i_e(t,x)`, we can write down the solution

.. math::
   u(x) = \int G(x,x') (-i_e(t,x') ) dx'.


As a verification, we integrate out for :math:`i_e(t,x) = 1`,

.. math::
   u(x) = -\int_{-\infty}^{x}  \frac{1}{2}e^{x'-x} dx' - \int_{x}^{\infty} \frac{1}{2}e^{x - x'} dx' = 1,

which is exactly the solution given by Mathematica and makes sense.

.. [1] In fact this is can be obtained by using the Fourier transform method.
.. [2] Because the only possibility to make the integral :math:`u(\pm\infty)=\int G(\pm\infty,x') dx'=0` satisfy :math:`u(\pm\infty)=0` is to make sure GF vanish on the boundaries.


Physical Meaning
~~~~~~~~~~~~~~~~~~~~

So far we have been dealing with math. What is the actual meaning of GF? To dive into this question we need to review the equation for GF, in this case,

.. math::
   \left(\frac{d^2}{dx^2} -1\right) u(x) = \delta(x'-x).


On the RHS, source term is a delta function, which is just a stimulation to the system at point :math:`x'`. The textbook shows a graph [3]_ for the case :math:`x'=0`, where we see the stimulation is given for point :math:`x'=0` and the potential drops as we deviate from the stimulated point.

In a stimulation-response system, one of the most important properties is the resonance width, or reaction width, which means the deviation required for the amplitude to drop to :math:`1/e` of the peak value. In this stationary solution, the distance is 1 in renormalized unit. To transform back to to SI unit, recall that the characteristic length is this problem is :math:`\lambda = \sqrt{\frac{r_T}{r_L}}`.

Just to build a picture, this length is around [4]_

.. math::
   \lambda = \sqrt{ \frac{r_T}{r_L}} = \sqrt{ \frac{30\mathrm{k\Omega\cdot cm^2}/(2\pi \rho)}{ 100 \mathrm{k\Omega\cdot cm}/(2\pi \rho) } } = \sqrt{ \frac{5\times 10^{11} \mathrm{\Omega \cdot \mu m} }{ 3\times 10^{5} \mathrm{\Omega \cdot \mu m^{-1}}  } } = 1.2\mathrm{mm}



.. [3] Wulfram Gerstner and Werner M. Kistler, Spiking Neuron Models, (2002), Fig. 2.17.
.. [4] Since opening of ion channesl can significantly change the transverse conductivity, this estimation can change significantly in different situations.



Non-stationary Solution
~~~~~~~~~~~~~~~~~~~~~~~~~

To solve the most general non-homogeneous cable equation even for non-stationary case, we have to introduce a two-dimensional Dirac distribution :math:`\delta^2(t,x) = \delta(t)\delta(x)`.

Green's function for the most general case should satisfy [Gerstner2002]_

.. math::
   \frac{\partial}{\partial t} G(t,t';x,x') - \frac{\partial^2}{\partial x^2}  G(t,t';x,x') +  G(t,t';x,x') = \delta(t'-t)\delta(x'-x).


Again to save ink we define

.. math::
   \hat L_{t,x} = \hat L_t - \hat L_x,

where :math:`\hat L_t = \frac{\partial}{\partial t}` and :math:`\hat L_x = \frac{\partial^2}{\partial x^2} - 1`.

The trick is to solve for time dependence first by Fourier transforming the equation to frequency space. To achieve that, we define

.. math::
   G(t,t';x,x') = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty G(t,t';k,x')e^{ikx}dk.
   :label: eqn-green-function-fourier-transform


On the other hand, Dirac delta is Fourier transformed to

.. math::
   \delta(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty \delta(\bar x) e^{- ik \bar x} d\bar x = \frac{1}{\sqrt{2\pi}} ,
   :label: eqn-dirac-delta-fourier-transform

which infact gives one of the representations of Dirac delta distribution

.. math::
   \delta(\bar x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty \frac{1}{\sqrt{2\pi}} e^{ik \bar x} dk .


Applying the transforms of :eq:`eqn-green-function-fourier-transform` and :eq:`eqn-dirac-delta-fourier-transform` to the equation we have

.. math::
   \hat L_{t,x}\left( \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty G(t,t';k,x')  e^{i kx} dk \right) = \delta(t'-t) \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty \frac{1}{\sqrt{2\pi}}  e^{i k(x'-x)} dk,

which becomes

.. math::
   &\frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty \frac{\partial}{\partial t}  G(t,t';k,x') e^{ikx}dk - \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty  G(t,t';k,x') \frac{\partial^2}{\partial x^2} e^{ikx}dk  \\
   &+  \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty G(t,t';k,x')e^{ikx}dk = \delta(t'-t) \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty \frac{1}{\sqrt{2\pi}} e^{ik(x'-x)} dk,

which is then simplified by removing the integral and common parts

.. math::
   \frac{\partial}{\partial t} G(t,t';k,x')  + k^2 G(t,t';k,x') + G(t,t';k,x') = \delta(t'-t) \frac{1}{\sqrt{2\pi}} .


Then we solve this first order differential equation.



.. [Gerstner2002] Wulfram Gerstner and Werner M. Kistler, Spiking Neuron Models, (2002).
