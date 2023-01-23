# Domino and Tromino Tiling
A bit of mathematical analysis of one tiling problem on leetcode. 

There is  a problem on [leetcode] (https://leetcode.com/problems/domino-and-tromino-tiling/) .

You have two types of tiles: dominoes (1x2) and trominoes (2x2 without one corner). 

It is required to write a program to calculate the number of ways to tile a 2xn rectangle. 

## Solution
It is easy to show that a tilling can only start in one of the following ways:
![](tiling.svg2)
The space between trominoes can only be tiled in one way.

Hence we can write a recurrent relation for the number of ways to tile a 2xn rectangle.

```math
\begin{align*}
f_{n}&=f_{n-1}+f_{n-2}+(f_{n-3}+f_{n-5}+...)+(f_{n-4}+f_{n-6}+...)+(f_{n-3}+f_{n-5}+...)+(f_{n-4}+f_{n-6}+...) \\
&=f_{n-1}+f_{n-2}+2(f_{n-3}+f_{n-4}+...)
\end{align*}
```
The initial terms of this recurrent sequence are as follows $f_{0}=1,f_{1}=1,f_{1}=2$.

Sequential calculation of the members of this recurrent sequence requires $\mathcal{O}(n)$ memory and $\mathcal{O}(n^2)$ operations.

We can replace the tail with a more compact expression

```math
f_{n}=f_{n-1}+f_{n-2}+2f_{n-3}+f_{n-1}-f_{n-2}-f_{n-3}=2f_{n-1}+f_{n-3}
```
Sequential evaluation of the members of the recursive sequence in this form requires $\mathcal{O}(1)$ memory and $\mathcal{O}(n)$ operations.

As
```math
f_{n}=2f_{n-1}+f_{n-3}\geqslant 2f_{n-1}
```
then the sequence grows faster than $2^{n}$.

To get more accurate information about $f_{n}$ consider the characteristic equation
```math
p(x)=x^{3}-2x^{2}-1=0
```
As
```math
(p(x),p'(x))=1
```
then the equation has no multiple roots.

We denote the roots of this equation $x_{1},x_{2},x_{3}$.

Then 
```math
f_{n}=c_{1}x_{1}^n+c_{2}x_{2}^n+c_{3}x_{3}^n
```
for some $c_{i}$.

As $f_{n}$ grows faster than $2^{n}$, then there is at least one root modulo greater than 2.

On the other hand, since
```math 
x^3+1< 2x^2
```
on interval $\left(1, \varphi\right)$
, $\varphi$ – Golden ratio, then, by Roche's theorem, the equation has two roots with modulus less than or equal to 1.

Therefore $f_{n}$  grows as  $c_{1}x_{1}^n$ where $x_{1}$ is the only root modulo >2.

As $f_{n}>0$, since $x_{1}$ is real and positive and $c_{1}>0$.

Discriminant of the equation > 0.

Therefore, the equation has one real root $\left(x_{1}\right)$ and two complex conjugated $\left(x_{3}= \bar{x_{2}}\right)$.

According to the Vieta theorem, the free term is equal to the product of the roots
```math
1=x_{1}*x_{2}*x_{3}=x_{1}*|x_{2}|^2
```
this implies
```math
|x_{2}| = \sqrt{\frac{1}{x_{1}}}<\sqrt{0.5}<0.71
```
Those. for sufficiently large n
```math
f_{n}= round(c_{1}x_{1}^n)
```
and the calculation of $f_{n}$ in this case looks like this 
```python
return math.round(math.exp(c1log+x1log*n))
```
where `c1log`, `x1log` are the natural logarithms of $c_{1}$ and $x_{1}$, which exist because $c_{1}$ and $x_{1}$ are positive. 

Formula evaluation requires $\mathcal{O}(1)$ memory and $\mathcal{O}(1)$ operations. True, these operations are fatter than addition and multiplication of integers. 


Applying the Cordano formula, we now calculate the roots of the characteristic equation 
```math
\begin{align*}
x_{1} = &\left ( 2 + \sqrt[3]{(43 - 3 \sqrt{177})/2} + \sqrt[3]{(43 + 3 \sqrt{177})/2} \right )/3\\
x_{2} = &\left(2 + 1/2 (-1+i\sqrt{3}) \sqrt[3]{(43 - 3 \sqrt{177})/2} - 1/2 (1 + i \sqrt{3}) \sqrt[3]{(43 + 3 \sqrt{177})/2)}\right )/3\\
x_{3} = & \bar{x_{2}}
\end{align*}
```

We now solve the system of equations for $c_{i}$ and find 
```math
\begin{align*}
c_{1}= &\left(59 + \sqrt[3]{(3481-177 \sqrt{177})/2} + \sqrt[3]{(3481+177 \sqrt{177})/2}\right) /177
\\
c_{2} = &\left(59 - (1 + i \sqrt{3})/2 \sqrt[3]{(3481-177 \sqrt{177})/2} - (1 - i \sqrt{3})/2 \sqrt[3]{(3481+177 \sqrt{177})/2}\right)/177
\\
c_{3}= &\bar{c_{2}}
\end{align*}
```

It is easy to show that 
```math
|x_{2}||c_{2}|=|x_{3}||c_{3}| <0.182
```
therefore 
```math
|f_{n}-c_{1}x_{1}^n|<|x_{2}||c_{2}|+|x_{3}||c_{3}|<0.37
```
т. е. 
```math
f_{n}= round(c_{1}x_{1}^n)
```
for all positive n. 

In conclusion,  look a little bit on at the bit depth of calculations. 
 
In order for the approximate value c1x1**n to give the same value f(n) as c1x1**n, it is necessary that the closest integer to the approximate value is the same as to the exact one.  
The exact value is close enough to the integer 

|f(n)-c1x1**n|=|c2x2**n+c3x3**n| <2|c2||x2|**n
Therefore, for the correct calculation of round 
calculation accuracy must be no worse 
0.5-2|c2||x2|**n
For large n, this is close to 0.5. 
In other words, we need to compute c1x1**n with a fixed precision (of the order of 0.5). 
Therefore, the binary bit depth of calculations grows with n as n * log2x1. 
For the example, the standard bit depth of double is enough for the first 40 terms. 
If we want to calculate values of n < 1000, then we need to have 100 exact digits. 

