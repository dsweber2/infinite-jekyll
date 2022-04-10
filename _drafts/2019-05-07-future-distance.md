---
title: "The future is much closer than you think"
excerpt_separator: "<!--more-->"
categories:
  - rationality
layout: page
hidden: false
---

When thinking about what the future, often we are drawn to trying to
extrapolate from the past. One of the principle difficulties with doing this is
that exponential growth is difficult to really grok seriously. There's a quote
in the defense community[^1] that <q>Quantity has a quality all of it's
own.</q> Shoot one bullet a minute, and you've got a bunch of lines pointed at
each other firing. Shoot 500 bullets a minute and you've got trench
warefare. 

<!--more-->
{% katexmm %}

The same is true elsewhere, so we should expect to see major qualitative
changes as we pass by various orders of magnitude.

Over the past 10 years, a certain amount of growth has occurred. In the linear
case, we should expect to see the same amount of change happen in another 10
years. But in the exponential case, 10 years of progress happens in
significantly less than 10 years. Supposing we have growth rate \\(r\\), and we
want to know how long until the future experiences what took us heretofore 10
years to achieve. We can write this as
\begin{align}
	P(0) - P(-10) &= P(t) - P(0)\\\
	A_0 - A_0(1+r)^{-10} &= A_0 (1+r)^{10 + t} - A_0(1+r)^{10}\\\
	\ldots\\\
	t &= \textrm{log}_{1+r}\big(2 - (1+r)^{-10}\big)
\end{align}

To be more concrete, supposing that we consider a growth rate of $$r=.03$$;
then we need only look 7.7 years in the future.
<figure class="align-center">
	<img src="{{ '/images/futureDistance1.png' | absolute_url }}" alt="Looong graph is long.">
</figure> 


Take a gander. 2015 is 3 years out, which doesn't seem that drastic. On the
other hand, to get as much growth as happened *SINCE THE END OF WORLD WAR 1* we
only need to look out to about 22 years. If we assume the far less modest 7%,
we plateau out at 11 years; in general, the asympote will be
$$\log_{1+r}2$$. For 3% this is 23.5 years and for 7% this is 10.2 years. It's
worth noting that this horizon is *very* sensitive to small differences in
percent near zero.

So how to interpret this? Part of this is that we're using an absolute measure
of difference to measure a process that is fundamentally about multiplicative
difference. On the other hand, that there is a plateau at all does tell us
something useful. To the degree that quantity makes quality, we quickly run out
of a scope where anyone has ever seen this much growth.

I would like to point out that this has actually been true for a large part of
the last 200 something years, so it is not actually a new phenomina that the
future is going to change more than anyone has ever experienced. While no one
before has experienced this much growth, several generations now have *that*
experience. [It might explain some things](https://xkcd.com/1227/)


*[anyone]: even the undead, with their infinite longevity and poor planning skills.

How long until we've gained as much as we did in the past 10 years?

[^1]: It has also been attributed to Stalin, [apparently
	incorrectly](https://www.quora.com/Who-said-Quantity-has-a-quality-all-its-own).


Exponential growth, despite its ubiquity is surprisingly difficult to think
about. I want to try to develop a simple way of compar
{% endkatexmm %}