Dispersion Relation
==========================================

A network of neurons forms a field with the field value being the potential and every other valuable measurable quantities. With this concept set up, we could define plane waves on this network and perform linear stability analysis [GErmentrout]_.
Suppose we have a wave of the form :math:`g(c t - x)` travelling, which can be Fourier transformed into many plane waves. If the velocity of the wave doesn't depend on the frequency of each Fourier mode, the wave would remain whatever it started as, which is non-dispersive. However, many waves are dispersive and will disperse as they travels. The reason that the waves disperse is that the velocity of each Fourier modes :math:`A(\omega)e^{-i (\omega t - k x )}` is different such that different Fourier modes will seperate out due to the difference in velocity.

Thus we could find out the velocity as a function of frequency to tell how dispersive the waves are, i.e., :math:`c(\omega)` or :math:`c(k)`, where :math:`\omega` and :math:`k` are the frequency and wave number respectively.

In fact the phase velocity is defined as :math:`c(\omega) = \frac{\omega}{k}` while group velocity is :math:`c_{g}(\omega) = \frac{d\omega}{dk}`. We now established the relations between :math:`\omega` and :math:`k`, e.g., :math:`D(\omega,k)=0`. The relation :math:`D(\omega,k)=0` is dubbed as **dispersion relation**.



Refences and Notes
--------------------

.. [GErmentrout] *Mathematical Foundations of Neuroscience* Chapter 6.
