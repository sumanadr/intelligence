Mean-field Method
===========================

Mean-field is a concept in statistical mechanics to approximately treat the many body problem. It is an effective theory.


Paramagnetic Material
-------------------------------

In paramagnetic materials, the "polarized" spins :math:`\{s_i\}` determine the overall "magnetization" of the material. When the spins are all aligned, we get the maximium "magnetization". If the directions of the spins are completely random, the material is not "magnetized". In other words, we can use a quantity :math:`m=\langle s \rangle`, which is called magnetization, to represent how well the overall "magnetization" of the material is.

For simplicity, we assume that the spins can only be up (s=1) or down (s=-1).

**The idea of mean-field is to treat each spin as a mean-field** :math:`m` **and the fluctuations around this mean-field**. Mathematically speaking

.. math::
   s_i = m + \delta s_i,

where :math:`\delta s_i = s_i -m` is the so called fluctuations. This treatment of the material requires the material to be homogeneous. Under the condition of homogeneous material, we can think of all the spins are the same. Thus we can look at one spin :math:`s_\alpha` and all other spins become a background environment of this particular spin. This background environment is called mean-field which provides a potential field to interact with.

On the other hand, the average of spins :math:`\langle s \rangle` is equivalent to the ensemble average of this particular spin :math:`\langle s_\alpha \rangle`

.. math::
   \langle  s \rangle = \langle s_\alpha \rangle_{ensemble} = \sum P(E_\alpha) s_\alpha,

where :math:`P(E_\alpha)` is calculated by the Boltzmann distribution,

.. math::
   P(E_\alpha) = \frac{e^{\beta E_\alpha} }{  \sum e^{\beta E_\alpha} }.

So we need to calculate the energy of the spin first. Using the Hamiltonian for spins

.. math::
   E_\alpha = - s_\alpha H_{total},

where :math:`H_{total}` is the total magnetic field including the mean-field. This energy finally becomes

.. math::
   E_\alpha &= - s_\alpha \left( H_{ext} + J \sum_{i, near \alpha} s_i \right) \\
   &= -s_\alpha \left( H_{ext} + J \sum_{i, near \alpha} ( m + (s_i - m) ) \right) \\
   & = -s_\alpha \left( H_{ext} + J z m + J \sum_{i, near \alpha} ( s_i - m ) \right),

where :math:`z` is the number of spins interacting with :math:`s_\alpha`.

**Mean-field theory assume a homogeneous background, the summation of fluctuations**, :math:`\sum_{i, near \alpha} ( s_i - m)` **should be 0**.

Then energy is calcuated as

.. math::
   E_\alpha = - s_\alpha (z J m + H).

Using this we get the ensemble average of spin :math:`\alpha`,

.. math::
   \langle s_\alpha \rangle &= \sum_{s_\alpha}  s_\alpha \frac{e^{\beta E_\alpha} }{  \sum e^{\beta E_\alpha} } \\
   &= \tanh \left( \beta (z J m + H) \right).

By definition, we know that

.. math::
   m = \langle s \rangle = \langle s_\alpha \rangle_{ensemble} = \tanh \left( \beta (z J m + H) \right).

Such a transcendental equation tells us the magnetization of the material.



Neuroscience
----------------------------


Mean-field theory is also applied to networks of neurons. Since it is an effective theory, we can only talk about the statistical features of neuron networks as mean-field is applied.


This method is explained in [Deco2008]_. This section is an interpretation of it if not a rewritten.


Two Phase Spaces
~~~~~~~~~~~~~~~~~~~~~

Similar to the :math:`\mu` space (6 D) and :math:`\Gamma` space (6N D) in statistical mechanics, it takes a lot of dimensions if we would like to describe a neuron network using a point in a phase space (:math:`\Gamma` space of network).

To see this, consider a network of :math:`N` neurons, each neuron requires :math:`\zeta` variables :math:`\{ \xi_1, \xi_2,\cdots, \xi_\zeta\}` for a complete description (say, PSP :math:`V`, current :math:`I`, :math:`\mathcal T`, as mentioned in [Deco2008]_). If we would like to describe the network using these :math:`\zeta` variables, it is represented as a bunch of points in such a phase space, which we name :math:`\mu` space. On the other hand, we can construct a :math:`N\zeta` dimensional phase space, where each dimension is a variable of a certain neuron. Suppose the neurons are given ids :math:`{}_i`. The dimensions are :math:`\xi_{j,i}` which stands for the :math:`\xi_j` variable of neuron i.

We could imagine how convoluted the new phase space (:math:`\Gamma` space) has become.

In any case, the evolution of the network is mapped to the motion of a point in :math:`\Gamma` space or motion of :math:`N` points in :math:`\mu` space.

Equation of Motion
~~~~~~~~~~~~~~~~~~~~~~

The dynamics of the system is described using Fokker-Planck equation,

.. math::
   \partial_t p = - \nabla\cdot (f-D \nabla) p,

where :math:`p` is the density of points in phase space. This is a statistical formalism.


.. admonition:: Drift and Diffusion
   :class: note

   The two terms on the RHS are dubbed as drift term and diffusion term for the physics they are describing.



[Deco2008]_ uses leaky integrate-and-fire model, which is used to find out the evolution of the membrane potential :math:`V_i` of neuron :math:`i`, which has a solution

.. math::
   V_i = V_L + \sum_{j=1}^N J_{ij} e^{-(t-t_j^{(k)})/\tau} \sum_k \Theta(t-t_j^{(k)}),

where :math:`\Theta` is the Heaviside function. The complication of this model comes from the fact that all neurons are potentially coupled.



.. admonition:: Leaky Integrate-and-fire Model
   :class: toggle

   LIF is a model utilizing capacitors and resistors to describe the evolution of membrane potential. The point of a capacitor is to reset the potential when it reaches the threshold.

   The EoM is

   .. math::
      \tau \frac{d}{dt} V = - (V - V_L) + IR,

   where :math:`I` is the total synaptic current input of the neuron, :math:`V_L` is the leak.

   For a neuron :math:`i` in a network, :math:`I` comes from all the synaptic delta pulse inputs of other neurons :math:`j`,

   .. math::
      I_i R = \tau \sum_{j=1}^N J_{ij} \sum_k \delta(t-t_j^{(k)}),

   where :math:`t_j^{(k)}` denotes the time for kth spike of neuron :math:`j`.

   The equation can be solved using Green's function method.



Following the idea of phase space, the authors of [Deco2008]_ derived Fokker-Planck equation for spiking neuron models. We could imagine that the :math:`\Gamma` space for LIF models would be a :math:`N` dimensional one :math:`\{V_i\}`, where :math:`N` is the number of neurons. On the other hand, :math:`\mu` space description requires only 1 D, which is potential. In :math:`\mu` space, we define a probability density :math:`p(v,t)`, which gives us the probability of neuron falls in a potential range :math:`[v,v+dv]` when multiplied by the size of the phase space :math:`dv`.

The Chapman-Kolmogorov equation describes the evolution of such a density function

.. math::
   p(v,t+dt) = \int_{-\infty}^\infty p(v-\epsilon,t)\rho(\epsilon\vert v-\epsilon) d\epsilon,

where :math:`\rho(\epsilon\vert v-\epsilon)` is the probability of neuron to be with potential :math:`v` at :math:`t+dt` given neuron potential at :math:`t` to be :math:`v-\epsilon`. But this integral form is not always useful. Kramers-Moyal expansion of it gives us the differential form

.. math::
   \partial_t p(v,t) = \sum_{k=1}^\infty \frac{ (-1)^k }{k!} \frac{\partial^k}{\partial v^k} \left( p(v,t) \lim_{dt\to 0} \frac{ \langle \epsilon^k\rangle_v }{dt} \right),
   :label: eqn-prob-density-equation-with-kramers-moyal-expansion

where

.. math::
   \langle \epsilon^k\rangle_v = \int_{-\infty}^\infty \epsilon^k\rho(\epsilon\vert v) d\epsilon,

which is an average.

The plan is to find method to calcualte :math:`\langle \epsilon^k \rangle_v` which is an average with respect to :math:`v`.


Mean-field Approximation
~~~~~~~~~~~~~~~~~~~~~~~~


By assuming each neurons are identical in this network, we face the same situation as in the paramagnetic material. By saying so we are going to assume that the time average (system average, in paramagnetic materials) is the same as the ensemble average, which treats all other neurons as a background and consider only one neuron.

The key of this practice is that :math:`\langle \epsilon^k \rangle_v = \langle \epsilon^k \rangle_{ensemble}`. On the other hand, we know that :math:`\langle \epsilon^k \rangle_{ensemble} = dV`, if we find this :math:`dV` that calculates the change of potential.

We need to find a quantity that is useful to describe the network, which should be similar to our magnetization :math:`m`. The choice can either be average potential of each neuron :math:`V_{avg}` or the total membrane potential :math:`V=NV_{avg}`. The authors in [Deco2008]_ choose the average membrane potential.


We denote mean firing rate as :math:`A`. The equation of :math:`V` is

.. math::
   dV = \langle J\rangle N A dt - \frac{V-V_L}{\tau} dt,

where :math:`\langle J\rangle` is the avarage synaptic weight and mean firing rate or population activity is

.. math::
   A = \lim_{dt\to 0} \frac{ \text{number of spikes within time } [t,t+dt] }{dt} \frac{1}{N}.

Since :math:`\epsilon=dV`, we plug it in to Eq. :eq:`eqn-prob-density-equation-with-kramers-moyal-expansion`. To save keystrokes, we calcualte the moments first.

.. math::
   M^{(k)} &= \lim_{dt\to 0} \frac{1}{dt}\langle \epsilon\rangle_v \\
   & = \lim_{dt\to 0} \frac{1}{dt}\langle \epsilon\rangle_{ensemble} \\
   & = \lim_{dt\to 0} \frac{1}{dt} dV \\
   & = \cdots \\
   & = \langle J^k \rangle N A.

In the derivation we dropped all terms that contains order of infinitesimal varibales :math:`\mathcal O (dt^2)`.

The diffusion approximation will help us drop the :math:`k>2` moments. This is a Taylor expansion anyway.

.. admonition:: A Simple Argument for Diffusion Approximation?
   :class: warning

   There should be one.

   Regardless of real understanding or not,

   .. math::
      M^{(1)} &= \frac{\mu(t)}{\tau} - \frac{ v-V_L }{\tau} \\
      M^{(2)} &= \frac{\sigma^2(t)}{\tau},

   are related to the drift coefficient :math:`\mu(t)` and the diffusion coefficient :math:`\sigma(t)`.



Then we obtain the Fokker-Planck equation

.. math::
   \partial_t  p(v,t) = \frac{1}{2\tau} \sigma^2(t) \partial^2_v p(v,t) + \partial_v \left[ \frac{ v - V_L - \mu(t) }{\tau} p(v,t) \right],

where :math:`\sigma(t)` is diffusion coefficient and :math:`\mu(t)` is drift coefficient.








References and Notes
--------------------------

.. [Deco2008] Deco, G., Jirsa, V. K., Robinson, P. A., Breakspear, M., & Friston, K. (2008). `The Dynamic Brain: From Spiking Neurons to Neural Masses and Cortical Fields <https://doi.org/10.1371/journal.pcbi.1000092>`_. PLoS Computational Biology, 4(8), e1000092.
