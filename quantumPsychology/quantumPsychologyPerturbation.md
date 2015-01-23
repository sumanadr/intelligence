
> Read on [StackEdit](https://stackedit.io/viewer#!url=https://raw.githubusercontent.com/emptymalei/quantumPsychology/master/quantumPsychologyPerturbation.md).

$$\newcommand{\ud}[1]{{#1^{\dagger}}} \newcommand{\bra}[1]{\left\langle #1\right|} \newcommand{\ket}[1]{\left| #1\right\rangle} \newcommand\Tr{\mathrm{Tr}} \newcommand{\braket}[2]{\langle #1 \mid #2 \rangle} \newcommand\d{\mathrm{d}} \newcommand\I{\mathbb{I}} \newcommand{\avg}[1]{\left< #1 \right>}$$

## Introduction

As I mentioned in the [previous article](quantumCognition.md), Hamiltonian of two level system can be written in terms of sigmas which makes it really easy to solve.

However, it might be a problem when the system becomes large. Then we might need perturbation theory.

Use $\hat M$ as the operator of a person or system. Suppose we can expand the operator and the state to multiple orders. The first order perturbation,

\begin{align}
\hat M^{(0)} \ket{n^{(1)}} + \hat M^{(1)} \ket{n^{(0)}} = m_n^{(0)} \ket{n^{(1)}} +  m_n^{(1)} \ket{n^{(0)}}
\end{align}

By multiply state vectors on the left we can find out that the perturbations are

|  Order        |  Energy           |   State  |
|:-------------: | :--------------------- |:---------------- |
| 0         |   $m_n^{(0)}$       |   $\ket{n^{(0)}}$   |
|  1     |      $m_n^{(1)} = \bra{n^{(0)}} \hat M^{(1)} \ket{n^{(0)}}$       |  $\ket{n^{(1)}} = \sum_{p \neq n}\frac{\bra{p^{(0)}} \hat M^{(1)} \ket{n^{(0)}} }{m_n^{(0)} - m_p^{(0)}}\ket{p^{(0)}} $     |
|  2    |   $m_n^{(2)}  = \sum_{p\neq n} \frac{ \left\vert \bra{n^{(0)}}\hat M^{(1)} \ket{p^{(0)}} \right\vert ^2}{m_n^{(0)} - m_p^{(0)}}$      |        -        |


It's required in this perturbation method that the system is non degenerate and the perturbation is small, i.e.,

\begin{equation}
\left\vert  \frac{\bra{p^{(0)}} \hat M^{(1)} \ket{n^{(0)}} }{m_n^{(0)} - m_p^{(0)}} \right\vert \ll 1
\end{equation}