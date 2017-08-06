Binary Human Model
=======================

Han has been discussing with me about building human dynamics by making analogy to neural systems.

The idea is to treat every human as an activation function which is connected to each other to form a large network. The trouble was how to deal with information input and output from outside of the group which is similar to external stimulation in neural systems.

A Simplified Model
----------------------

Here we develop a model for wechat groups instead of general human dynamics. We assume everyone share all the information in the group.


There are several aspects to be defined.

0. One way to simplify the model is to set up a external pool of information and opinions which we denote as :math:`\mathscr P`.
1. An opinion is plugged into the pool :math:`\mathscr P` initially.
2. Everyone will take information and output information to this poll :math:`\mathscr P`.
3. Each human would either output null (being silent) or 1 (agreement) or 0 (disagreement). Each of the outputs in the pool is denoted as :math:`P_i`.
4. The output of each human depends on the pool, the nature of the human, and the relation with other people. We approximate each human using a binary input/output function.


Such a general model seems to be good enough. However, we have to define all different types of human first.

1. Being average: takes in all the opinions of other participants and work out an average.

   .. math::
      \Theta(\frac{\sum_{1}^N P_i}{N}-0.5),

   where :math:`\Theta` is the step function or Heaviside function.
2. Being extreme: exaggerates whatever is obtained from average。

   .. math::
      \Theta(\alpha\frac{\sum_{1}^N P_i}{N}-0.5),

   where :math:`\alpha` is the extreme factor. For linear summations (euclidean metric), this is effectively pessimism (:math:`\alpha<1`) or optimism (:math:`\alpha>1`).
3. Synchronized to other people. The simplest case is to synchronize to one of the members in the group.


Numerical Model
~~~~~~~~~~~~~~~~~~~~~~

We need to build a program to calculate an example and see if it makes sense.




.. code:: python

    import numpy as np

.. code:: python

    # Define Heaviside function; returns 0 if x<0.5, otherwise returns 1

    def hsh(x):
        #return (0.5 * (np.sign(x-0.5) + 1))
        return int(np.piecewise(x, [x < 0.5, x >= 0.5], [0, 1]) )



.. code:: python

    # Test of functions

    print hsh(0.1), hsh(0.5), hsh(0.6)


.. parsed-literal::

    0 1 1




In this example, we simulate the opinion stream of each person as well
as the whole system which is determined by the pool.

For convinience we establish a group of 4 person.

.. code:: python

    # Define the pool

    pool = np.random.randint(2, size=4).tolist();
    print pool


.. parsed-literal::

    [1, 0, 0, 1]


.. code:: python

    # Define four characters of the group

    ## First character is an averagist

    def avgist(x):

        return hsh( np.sum(x)/len(x) )

    ## The second character is pessimist

    def pesist(x,alpha=0.6):

        return hsh( alpha * np.sum(x)/len(x) )


    ## The third character is a optimist
    def optist(x,alpha=2):

        return hsh( alpha * np.sum(x)/len(x) )

    ## The fourth synchronizes with the first character, i.e., averagist

    def synist(x):

        return x[0]

.. code:: python

    # Test characters

    print avgist(pool), pesist(pool), optist(pool), synist(pool)
    print np.array([avgist(pool), pesist(pool), optist(pool), synist(pool) ])


.. parsed-literal::

    0 0 1 1
    [0 0 1 1]


.. code:: python

    # Define iterator

    def iter(initpool,n): # initpool: the inital pool; n: number of iterations

        poolM = np.array(initpool);
        stateM = np.array([poolM]);


        for i in range(n):
            poolM = np.array( [ avgist(poolM), pesist(poolM), optist(poolM), synist(poolM) ] )
            stateM = np.append( stateM, np.array([poolM]) ,axis=0 )

        return stateM

.. code:: python

    print(iter([1,1,0,1],10), \
        iter([1,1,0,1],10), \
          iter([1,0,1,1],10)
         )


.. parsed-literal::

    (array([[1, 1, 0, 1],
           [0, 0, 1, 1],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]), array([[1, 1, 0, 1],
           [0, 0, 1, 1],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]), array([[1, 0, 1, 1],
           [0, 0, 1, 1],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]))
