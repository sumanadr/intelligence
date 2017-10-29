Time Scale in Memory
=================================



.. _memory:

Memory
------------------------------------


1. Three categories of memory: [Tetzlaff2012]_

   1. Working memory: processing information and usually requires with atention.
   2. Short-term memory
   3. Long-term memory

2. Evidence of plasticity (Martin et al 2000):

   1. Detectability: measured change in synapse when animals is learning or momorizing.
   2. Mimicry: replicate the synapse change from one animal to another would result in similar memory or behavior. Not yet experimentally realized.
   3. Anterograde alteration: disable synaptic plasticity and learning and memory should stop working.
   4. Retrograde alteration: modify synapse weight and the memory should be changed.



.. admonition:: Why Do We Care about Time Scales
   :class: warning

   Memory works on many different time scales. This is extremely important for life forms because they need to work out correlations between events in the past and current status.

   I would think of permenant memory would serve the purpose of finding out the casalities. However it won't be optimized to work on small time scales. The suitation might be quite similar to computers.

   In the end, there are memories on different time scales as mentioned before.


.. index:: working memory

Working Memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. What is working memory? Remember the current state of a ongoing plan.
2. Where: probably prefrontal cortex
3. Small capacity
4. Chunking: store chunks of information elsewhere and load the link to working memory.
5. Tiny time scale: ms to minutes
6. Not persistent: requires constant rehearsal or attention

.. index:: short-term memory

Short-term Memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Short-term memory time scale: minutes to days
3. Where: hippocampus, but amygdala has influence on memory through emotions. Some theories developed context based brain area storage.
4. Possibly related to synaptic plasticity



.. index:: long-term memory

Long-term Memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Short-term memory can be consolidated to long-term memory during **sleeping**.
2. Long-term memory time scale: days to years
3. Where: mainly in prefrontal cortext but distributed cortical network
4. Related to both synaptic plasticity and structural plasticity




From STM to LTM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The relation between STM and LTM is not clear yet [Tetzlaff2012]_.

.. admonition:: Questions
   :class: note

   Several questions from [Tetzlaff2012]_

   1. Does LTM come from STM?



Learning
-----------------


Correlation-based Learning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conditioning



Reward-based Learning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reward-based learning, aka. reinforment learning, figure out which choice is better by comparing the results.


Supervised Learning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Memory is probably required.



Models of Memory and Learning for Different Time Scales
---------------------------------------------------------------

.. figure:: assets/physiological-mechanisms.png
   :align: center

   Physiological mechanisms for different time scales. From [Tetzlaff2012]_.





Memory Consolidation and Synapse Scaling
-----------------------------------------------

Long-term memory requires memory consolidation, which consolidates the synapse locally to enhence memory or transfers momories to other area.

At the region that connects hippocampus and cortex, LTS (Long-term storage) and STS (Short-term storage) happens at the same time. This indicates that neurons in this cross-section mentains two different types of dynamics, one of which responds to consolidation (i.e., synapse weight change), while the other doesn't.


.. admonition:: #TIL# Recall momory can destablize the corresponding memory itself
   :class: note

   In the paper by Tetzlaff [Tetzlaff2013]_, they mentioned it.




Tetzlaff et al found a solution to this time scale problem [Tetzlaff2013]_. In principle, :math:`\frac{d w^{+}_{ij}}{dt}` can be Taylor expanded to have all orders of :math:`w^{+}_{ij}`. In this work by Tetzlaff, they included a simple plasticity (zeroth order in Taylor expansion)

.. math::
   \mu F_{i} F_{j},

as well as a synapse scaling (second order in Taylor expansion)

.. math::
   \frac{\mu}{\kappa} (F^T - F_i) \left( w^{+}_{ij} \right)^2.


We put those two together,

.. math::
   \frac{d w^{+}_{ij}}{dt} = \mu \left( F_{i} F_{j} +  \kappa (F^T - F_i) \left( w^{+}_{ij} \right)^2 \right).



Such a updating rule for weights contains dynamics of bifurcation. For a region of input frequencies, activity and weights exhibit bistability, thus leading to neurons evolve to different states. Neurons recieved strong inputs have larger weights due to plasticity. Those neurons with large weights evolve into equilibrium points of LTS for the corresponding frequency.


.. [Tetzlaff2012] Tetzlaff, C., Kolodziejski, C., Markelic, I., & Wörgötter, F. (2012). Time scales of memory, learning, and plasticity. Biological Cybernetics, 106(11–12), 715–726. https://doi.org/10.1007/s00422-012-0529-z
.. [Tetzlaff2013] Tetzlaff, C., Kolodziejski, C., Timme, M., Tsodyks, M., & Wörgötter, F. (2013). Synaptic Scaling Enables Dynamically Distinct Short- and Long-Term Memory Formation. PLoS Computational Biology, 9(10), e1003307. https://doi.org/10.1371/journal.pcbi.1003307
