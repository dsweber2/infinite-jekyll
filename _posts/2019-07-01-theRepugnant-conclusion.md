---
title: "A not so repugnant conclusion"
excerpt_separator: "<!--more-->"
categories:
  - rationality
  - altruism
layout: page
hidden: false
---

{% katexmm %} Let's consider a utilitarian value system with equal weights for
all people, a single resource with a fixed amount $R$, and the same utility
function for all people. It is a relatively well known fact that people's
reported happiness scales with the logaritm of the wealth available to
them[^2], so let's take each utility function to be $f(x) =
A\log_b(x+\varepsilon)$; the $\varepsilon$ makes it so that a person doesn't
fear death to the point of murdering everyone they love, so long as it is
positive. If we're looking to maximize total happiness based on the number of
people that exist, we want to choose $N$, the number of people, to maximize
$$
  \sum_{i=1}^N A\log_b\big(\varepsilon + \frac{R}{N}\big) = AN\log_b (N\varepsilon + R) - NA\log_b N
$$
<p align="center">
	...insert calculus...
</p>
$$
	N = \frac{R}{\textrm{e}^{1-\varepsilon}- \varepsilon}
$$
<figure class="align-center">
	<img src="{{ '/images/zeroMatters.png' | absolute_url }}" alt="Looong graph is long.">
</figure> 

This implies that there is some ideal number of people, rather than an
arbitrary race to the bottom. Which makes sense; the part of the logarithm that
is "doing work" in this scenario is actually the part near the origin where a
person's utility is actually negative. It is not clear what a negative utility
means; perhaps it would be better not to exist. Especially if there is any
uncertainty in the amount of resources a person has and the amount of effort
that is necessary to sustain that level of resource, it is certainly plausible
to imagine conditions where starving constantly could be worse than not
existing[^3]. But in that case, the $N$ above achieves a net utility per person of

$$
	A\log_b(\frac{R}{N} + \varepsilon) =
	A\log_b(\frac{R(\textrm{e}^{1-\varepsilon}- \varepsilon)}{R} + \varepsilon)
	= \ldots = A \log_b(\textrm{e}^{1-\varepsilon}) = A\frac{(1-\varepsilon)}{\log(b)}
$$

So it appears that so long as existing eventually becomes worse than not
existing, the population maxes out at a positive utility per person *that is
bounded away from zero utility*; intuitively, one might expect that we would
keep adding people until each hit zero utility, but because each person has a
linear consumption of resources, but the change in resources has a *nonlinear*
effect on their happiness, it's not a good idea to add more. The primary point
of this wasn't to definitely resolve the repugnant conclusion, but to point out
that it depends carefully on the utility functions of the beings that exist. If
we get to introduce arbitrary beings, we're right back where we started; on the
other hand, if they can have arbitrarily high utility, we need to be very
careful about how we use our intuitions.


I made quite a few assumptions in this discussion; some further issues that
I'll consider in upcoming posts, the availability of total resources as a
function of the number of humans and their happiness, what we actually know
about human risk aversion, network effects, and alternatives to real-valued
value systems[^5].  {% endkatexmm %}

# Relevance

There's a fundamental question of whether we actually live in such a world. One
slight problem with the premises is that we *don't* have finite resources, but
that the economy is growing in real monetary terms.

Often the problem with thought experiments is that they sneak in rather massive
assumptions when you're not looking.[^1] The repugnant conclusion doesn't pay
attention to how distributing resources is a problem, or the fact that we can
send people off to other planets. One needs to be careful about

# the role of negatives

People weigh losses more heavily than they weigh an objectively similar gain;
the descriptive psychology of this is known as [Cumulative prospect
theory](https://en.wikipedia.org/wiki/Cumulative_prospect_theory). The actual
level of resources that people get is both never equally distributed, or
constant, so a world just above the zero line, is also one where there are
significantly many people who have crossed the threshold.


[someone seems to have thought of this](https://www.lesswrong.com/posts/Zgwy2QRgYBSrMWDMQ/logarithms-and-total-utilitarianism)


[^1]: for example [the chinese room
    argument](https://plato.stanford.edu/entries/chinese-room/) doesn't specify
    *how* the people do the translation. I hope that the complexity of NLP
    (natural language processing) and the difficulty of creating GTP-2, which
    only vaguely passes this test, convinces you that most of the difficulty
    lies in this part.

[^2]: for a survey within EA, see
    [here](https://80000hours.org/articles/money-and-happiness/). It's unclear
    to what degree this is a necessary consequence of happiness surveys being
    on fixed size scales, while wealth is more or less without an upper
    bound. But this scaling is certainly plausible at the low end.

[^3]: This is in some respects an emperical question, though if we sample
    people in the real world this overweights the case where a significant
    investment of work is necessary for those resources.

[^4]: In this case, the transcendental number that solves
    $A\log_b(\textrm{̌e}^{1-\varepsilon} -\varepsilon)=0$, or more cleanly
    $\varepsilon\textrm{e}^{\varepsilon} = \textrm{e}$, or approximately
    $.557145$

[^5]: The closest example would be if people only have ordinal preferences, and
    if we can say something similar in that case, though one could imagine
    constructing vector-valued utilities, corresponding to non-rational agents.
