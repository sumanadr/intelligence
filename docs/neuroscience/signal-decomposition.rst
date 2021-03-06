Signal Decomposition
=====================

.. admonition:: Acknowledgement
   :class: warning

   I had some of the ideas when Han Lu was explaining an experiment after one of my lunch. We share some of the ideas.

Signals, electric potential or stimulations, are usually decomposed into different modes to study a system. The most prominant application is the measured signals, but stimulations should also be decomposed to study the response.

Why would we expect the decomposition of signal in a brain to have any significance? **For a neural system of tiny elements to really work out a complicated problem, I expect that some of the neurons have to work collectively in order to solve the problem.** Such collective phenomona might generate observable signals in fMRI etc if the collective neurons are clustering in space. In this case a spherical harmonic decomposition would be able to detect some of the features. Well, this is a little doubtful because the activities might not be global.



Measurement
-------------------


Application of spherical harmonics to EEG have resulted in interesting experiments [Sivakumar2016]_.

However, [Sivakumar2016]_ only used it to decompose the surface of the brain, which is not the complete information. A full map of signal should be a field of 3 dimensional sphere. At each point, we can have information about

1. electric potential,
2. current with direction (flux of charge),
3. electric field with direction.

For electric potential, we can set up a reference point and measure it, which means it's a scalar and we have a number at each point. But for the other two with directions, they are vectors.

The decompositions can be done in different ways, according to the information we want to extract.

1. Globally decomposite the signal with spherical harmonics :math:`Y_{}` at different radius, a multiple expansion for the whole brain; It requires **spin weighted spherical harmonics** etc for vector fields.
2. Locally expand the signal at each point using spherical harmonics; Only need the spherical harmonics.




.. [Sivakumar2016] Sivakumar SS, Namath AG and Galán RF (2016) `Spherical Harmonics Reveal Standing EEG Waves and Long-Range Neural Synchronization during Non-REM Sleep <http://journal.frontiersin.org/article/10.3389/fncom.2016.00059/full>`_ . Front. Comput. Neurosci. 10:59. doi: 10.3389/fncom.2016.00059


Stimulation
--------------------------

Stimulations could also be done in a similar way. We apply different modes and check if each mode plays a different role in the brain.

Theoretically, we might think the brain activity might be related to the modes, since each mode stands for different levels of activity in different regions. For example, if we have only :math:`l=0` mode at different radius we might not be doing anything, since an isotropic brain is very likely to be a dead one. One of the regions have large activities means we have higher modes excited and since the brain has a fixed anatomy structure, a certain mode indicates activities in different regions.

It's the same for stimulations. Generating a certain mode of electric field or potential will cause a stimulation in different regions.



Thearetical Investigation
--------------------------------------


We could find the conservation laws of a popularition in multiple expansion and identify the conserved quantities from population theory. This could be useful for simulations.
