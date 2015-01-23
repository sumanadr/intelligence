

> This is my notes on [Quantum Structure in Cognition](http://arxiv.org/abs/0805.3850).
> **Read on** [StackEdit](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/emptymalei/quantumPsychology/master/quantumCognition.md).


### TO DO

1. ~~Meaning of observable $\hat L$ in the [quantum love model](#quantum-love-as-a-joke).~~ (Results [here](#description-of-items).)
2. Meaning and representation of $A\land B$.
3. Meaning of **imaginary part** of off diagonal elements in operators.
4. Meaning of eigenvalues.
4. Two eigenvectors will present sometimes. Two eigenvectors? Once measured collapse to one of them? Needs more proof.
4. Application of Statistical Mechanical stochastic matrix or similar ones.
 

$$\newcommand{\ud}[1]{{#1^{\dagger}}}
\newcommand{\bra}[1]{\left\langle #1\right|}
\newcommand{\ket}[1]{\left| #1\right\rangle}
\newcommand\Tr{\mathrm{Tr}}
\newcommand{\braket}[2]{\langle #1 \mid #2 \rangle}
\newcommand\d{\mathrm{d}}
\newcommand\I{\mathbb{I}}
\newcommand{\avg}[1]{\left< #1 \right>}$$


### James A. Hampton

Hampton's result：

* For the item **Cuckoo**, 


| Item        | Concept           | Weight  |
| ------------- | ------------- | ----- |
| Cuckoo      |  Bird     |    1   |
|             |   Pet        |  0.575       |
|       |   Bird & Pet        |     0.842    |
| ------ | -------- | --------- |

* For the item **Ashtray**


| Item      | Concept      |    Weight    |
| --------- | ----------- | ----------- |
| Ashtray   |  Home Furnishing     |  0.7  |
|        |  Furniture     |  0.3  |
|        |  Home Furnishing or Furniture     |  0.25    |
| ------ | -------- | --------- |


### Math Representations of Guppy Effect

Two concepts A and B, their weights are $\mu(A)$ and $\mu(B)$. The conjunction and disjunction of them are A and B ($A \land B$), A or B (A$\lor$B) respectively. The weights are $\mu(A\land B)$ and $\mu(A\lor B)$.

* Conjunction minimum rule deviation

\begin{equation}
\Delta_c = \mu(A\land B) - min(\mu(A),\mu(B))
\end{equation}

* Disjunction maximum rule deviation

\begin{equation}
\Delta_d = max(\mu(A),\mu(B)) - \mu(A\lor B)
\end{equation}


### Quantum Representation of Concepts


Now kets stands for concepts.

> But why Hermition operators? Real eigen values? Wait and see.

To explain Hampton's experiment, we use two orthogonal concept states $\ket{A}$ and $\ket{B}$ (**why orthogonal? Not nessarily**). For a specific experiment $\hat M$, we have

\begin{align}
\mu(A) & = \bra{A}\hat M\ket{A} \\
\mu(B) & = \bra{A}\hat M\ket{A} \\
\mu(A\lor B) & = \frac{\bra{A}+\bra{B} }{\sqrt{2}}\hat M  \frac{\ket{A}+\ket{B}}{\sqrt{2}}
\end{align}



#### Description of Items

**The key point is that operators are items while concepts are states.**

Here we use the idea I proposed several month ago to interpret this method. I need a boy or girl description of a human being $\hat I_D$, which is an operator. So the bases are $\ket{B}$ and $\ket{G}$.

Suppose we have some measurement results that the expectation value of me to be a girl is $\mu(G)$ and that of me to be a boy is $\mu(B)$, and that of me to be a boy and girl is $\mu(G\lor B)$. In the Boy-Girl basis, we can write down the representations of states and operators.

\begin{align}
\hat I_D & \rightarrow \begin{pmatrix} a & c \\ c^* & b \end{pmatrix} \\
\ket{G} & \rightarrow \begin{pmatrix} 1 \\ 0 \end{pmatrix} \\
\ket{B} & \rightarrow \begin{pmatrix} 0 \\ 1 \end{pmatrix} 
\end{align}

So the expectation value of me to be a girl,

\begin{align}
\mu(G)& := \bra{G}\hat I_D \ket{G} = \cdots (\text{insert identity}) = a \\
\mu(B)& :=\bra{B}\hat I_D \ket{B} = \cdots (\text{insert identity}) = b \\
\mu(G\lor B) &:= \frac{1}{2}(\bra{G} + \bra{B})\hat I_D (\ket{G} + \ket{B}) = \cdots (\text{insert identity}) \\
& \phantom{} = a+b+2\mathrm {Re}(c)
\end{align}

If we can get the measurement results of $\mu(G)$, $\mu(B)$, $\mu(G\lor B)$, the elements of the human being operator under Boy-Girl representation can be calculated except the imaginary part.

1. **We can show that the imaginary part of off diagonal elements doesn't change any of the expectation values of the Hermition operator, so for expectation values, the imaginary part is of no importance.**
2. **The "problem" of this formalism is that the eigenvectors of operators could have negative elements which makes it hard to interpret the meaning. But the probability is alright because the probability is the square of the coefficient.**
3. Notice that Pauli matrices together with identity matrix form the orthonormal complete basis of any two energy level system. So we can use Pauli matrices to write down the operators for two level system in psychology.

#### Measurement Experiments

To get the data of the expectation values, repeat the **Hampton experiment**.





### Quantum Love As A Joke


In the case of love stories, we have Boy and Girl which are two items. Then we have a "experiment", which is the relationship between the two.

~~So we have two states $\ket{B}$ and $\ket{G}$ and an observable $\hat L$. **The meaning of this observable is not clear.**~~

Suppose we have a girl and a boy without a third person, the bases become the direct product of the bases the boy and the bases of the girl, $\ket{S_B}\otimes \ket{S_G}$, $\ket{S_B}\otimes \ket{L_G}$, $\ket{L_B}\otimes \ket{S_G}$, $\ket{L_B}\otimes \ket{L_G}$. It's obvious that for such a system, the square of the element at the bottom right corner of the system operator matrix is the weight of the two being in love with each other.







