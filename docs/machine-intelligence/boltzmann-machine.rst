Boltzmann Machine
================================

Boltzmann machine is much like a spin glass model in physics. In short words, Boltzmann machine is a machine that has nodes that can take values, and the nodes are connected through some weight. It is just like any other neual nets but with complications and theoretical implications.


Boltzmann Machine and Physics
----------------------------------

To obtain a good understanding of Boltzmann machine for a physicist, we begin with Ising model. We construct a system of neurons :math:`\{ s_i\}` which can take values of 1 or -1, where each pair of them :math:`s_i` and :math:`s_j` is connected by weight :math:`J_{ij}`.

This is described as a Boltzmann machine, or spin glass in physics. Spin glass is a type of material that is a composite of many spins pointing in different directions. In principle spin glass is hard to calculate.

Neverthless we can make simplifications to this model. We require each spin to be connected to its nearest neighbours only. Such a model is called Ising model.

Intuitively, those spins can be viewed as tiny magnets that can point up or down only. Each spin interacts with its neighbours. These interactions are calculated in terms of energy,

.. math::
   E = -\sum_{i,j} J_{ij} s_i s_j.

Why do we care about energy? For a physics system, low energy means stable while high energy means unsatble since it might automatically change its configuration into low energy state. That being said, a system of spins is stable if the energy of all the interactions is low.

To find out a low energy state, one of the numerical methods is Monte Carlo method.


.. admonition:: States
   :class: note

   We have been talking about the word state without being specifying the definition of it. In fact we can think of two different pictures of states. For the purpose of this discussion, we consider a system of :math:`N` particles and each of the particle has :math:`m` degrees of freedom.

   The first strategy is to set up a :math:`N\times m` dimension space and describe the state of the whole system with on point in such a space. The distribution of the points can be determined by the corresponding categories of distribution functions. This is dubbed as :math:`\Gamma` space.

   The second strategy is to use a space of :math:`m` dimensions where each particle of the system is a point in such a space. Such a space is called :math:`\mu` space. In :math:`\mu` space, the distribution of each particle state is calculated using BBGKY chain.


   Once the macroscopic propertities of the system is assigned, the all possible states that leads to this macroscopic state show up with equal probability, aka, principle of **equal a priori probabilities**.




.. admonition:: Partition Function
   :class: note

   Partition function :math:`Z` is useful as we calculate the statistical properties of the network,

   .. math::
      Z = \sum e^{-E}.

   With partition function defined, the distribution of states is

   .. math::
      P = \frac{1}{Z} e^{-E}


Minimizing Energy of Ising Model is Hebbian Learning
-------------------------------------------------------

.. admonition:: Hebbian Learning Rule
   :class: note

   Simply put, neurons act similarly at the same time would be more likely to be connected.


A energy minimization procedure would be the same as Hebbian learning rule. Suppose we pick out two spins, :math:`s_3 = 1` and :math:`s_8= 1`, the connected weight would be positive in order to have lower energy :math:`-J_{38}s_3 s_8 = - J_{38}`. For spins with different signs, negative weight would be the choice to make sure the energy is lower. This is similar to Hebbian learning rule.



Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To code a Boltzmann machine, we need a protocal.
