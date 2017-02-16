Functional Connectivity
============================================

Biological neural networks are quite complicated in the sense maps. Given some input the network generates a output, which is a map of the complicated kind. However, we could also feel the simplicity of such complicated networks. The building blocks of such network are simple neurons which are filters of information.

As a physicist, we have been working with harmonic oscillators. Single oscillators have its frequency of oscillations. Coupled oscillators have their eigenmode, which are hidden collective behaviors of the oscillators. It seems that each oscillator is oscillating chaotically. As we find the eigenmodes, we find the collective patterns. Each oscillator joins some if not all of the collective patterns.

This idea inspires us. If we look at the spiking of each neuron, we might not be able to identify the patterns. However, for coupled neurons, we have to find their collective modes to really SEE the hidden patterns. This idea works for very small networks, the eigenvalues and eigenvectors of which can be found easily. For super large networks, it becomes mission impossible.

In any case, we can persue the idea that the network is composed of basic functional units. There are many levels and aspects of brain connectivity [BrainConnectivity]_.

1. Graph theory:
   - clustering techniques
   - community detection, **which is quite interesting**.
2. Morphometric methods
3. Functional brain connectivity:
   - computing cross-correlations in the time or frequency domain;
   - mutual information;
   - spectral coherence.


.. admonition:: Community Detection
   :class: note

   The article [BrainConnectivity]_ mentioned that **eigenspectrum** is used in community detection.

   In social science and complex networks, community detection is a well researched field. A bunch of methods have been developped.

   - Q modularity [Newman2016]_;
   - Hyperbolic mapping [Boguna2010]_;
   - Statistical mechanics method such as Gibbs distribution [Zhang2014]_;
   - ...

   .. [Newman2016] Newman, M. E. J. (2016). `Community detection in networks: Modularity optimization and maximum likelihood are equivalent <http://arxiv.org/abs/1606.02319>`_. ArXiv 1606.02319, 1–8.
   .. [Zhang2014] Zhang, P., & Moore, C. (2014). `Scalable detection of statistically significant communities and hierarchies using message passing for modularity <http://doi.org/10.1073/pnas.1409770111>`_, 111(51), 18144–18149.
   .. [Boguna2010] Boguna, M., Papadopoulos, F., & Krioukov, D. (2010). `Sustaining the Internet with Hyperbolic Mapping. Nature Communications <http://doi.org/10.1038/ncomms1063>`_, 1(6), 1–8.


Here are some facts about brain network.

1. It's similar to small world network [BrainConnectivity]_.
2. There are functional hubs [BrainConnectivity]_.
3. Segregation and integration might be key to a functional neural network [BrainConnectivity]_.


References
--------------------

.. [BrainConnectivity] `Brain connectivity <http://www.scholarpedia.org/article/Brain_connectivity>`_
