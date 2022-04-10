---
title:  Transformative experiences, shifting values and the modular mind
date:   2019-09-13 19:20:32 -0700
excerpt_separator: "<!--more-->"
categories:
  - rationality
  - altruism
layout: page
hidden: false
---
Inspired by rationally speaking 183 with L.A. Paul. combining the idea of the
modular mind and semicoherent rationality.

Rational agents should oppose changes in their values. Should *non*rational
agents, or groups of rational agents? What about groups of rational agents who
gain and lose members?
> Do I contradict myself? Very well, then I contradict myself, I am large, I contain multitudes.
>
> <footer><strong>Walt Whitman</strong> A song of myself </footer>
<!--more-->
{% katexmm %}

To talk about thinking about multi-value agents, read some Elizabeth
Anderson. Specifically [Unstrapping the straightjacket of
'preference'](http://www-personal.umich.edu/%7Eeandersn/andersoncritsen.pdf). She
talks about the role of identity in the expressed preferences of
individuals. Also relevant from her is [Slinging Arrows at
Democracy](https://www.jstor.org/stable/1122890?seq=1). The incommensurability
and non-consequentialist approach is where I'll be getting off that train, I think.

[There's also a strain of buddhist no-self thought that's relevant and in the LessWrong world](https://www.lesswrong.com/posts/W59Nb72sYJhMJKGB8/a-non-mystical-explanation-of-no-self-three-characteristics)

There are schools of thought which consider a person not as an agent with a
single, coherent utility function, but a whole panoply of agents, each with
different goals, with no guarantees that any of the agents last particularly
long. To my knowledge, these are not found frequently in the rationalist
community. Maybe this shouldn't be surprising, given how starkly it flies in
the face of some core assumptions about the relation between consciousness and
rationality. One way to accidentally create such amalgams, however, is through
bounded rationality; each possible way of achieving the overall goal gets
assigned an agent, each optimizing for a different goal, and then interplay
between the agents is set up to approximate net rationality.

Of course, there are also 
(bit discussing other viewpoints)

Let's entertain the notion that

Game theory, and the particular sub-discipline of social choice theory, are the
most formal tools for dealing with decision making involving a group of
rational agents. [Social choice
theory](https://en.wikipedia.org/wiki/Social_choice_theory) is usually used as
a tool to analyze voting systems, and it's most celebrated result is Arrow's
theorem (I'll get there). As a warning, I'll occasionally write "agent $a$
prefers $A$ to $B$" as $A>_a B$, "every individual prefers $A$ to $B$" as
$A>B$, and the aggregate preference of everyone as $\succ$.

What can we say about what a group of agents should do? This runs pretty
quickly into the question of how to integrate multiple utility functions, which
runs around on [Arrow's
theorem.](https://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem). Roughly,
we must break at least one of the following:

* If for each person, $X>Y$, then $X \succ Y$, i.e. everyone prefers $X$ to
  $Y$, then the aggregator prefers $X$ to $Y$. I should hope such a criteria
  is obviously essential for any aggregator purporting to represent any of its
  constituent agents.
* Independence of irrelevant alternatives (iira). Suppose $X\succ Y$. Then
  suppose some subset of people $b$ change their mind on the relative merits of
  $X$ and $Z$. One would hope that $X\succ Y$. This is the axiom that is most
  frequently held as too strong, as there are cases which are
  rock-paper-scissors-like, and thus necessarily tying together more than two
  options.
* No one person's vote determines the outcome, regardless of the other agents.

Turns out, we can't actually have all of these. Probably the most reasonable
conclusion from Arrow's theorem is that any voting scheme with more than two
options and more than 4 people is gamable, so you should vote strategically. To
account for this I'm going to include a 3rd preference indication, $X\gg_aY$,
which means that $a$ truly prefers $X$ to $Y$, and is not just strategically
voting as such, which is what $X>_a Y$ means.

What I want to focus on here isn't the traditional public choice theory
questions. I want to think about in what ways does a collective diverge from
behaving like an agent? The most obvious possibility is that iira can cause the
agent to not behave consistently.
	
# Should we expect value drift over time? #

The case that got me started down this road was thinking about [this rationally
speaking with LA
Paul](http://rationallyspeakingpodcast.org/show/rs-183-l-a-paul-on-transformative-experiences.html)
about transformative life experiences and changing your values. It is an
obvious truism that a fully rational agent has no interest in modifying it's
utility function; that would, by definition, lower it's objective
function. There's more room for boundedly rational agents to have layers of
values, some of which are malleable, and controlled by the higher ones.

What about in the context of the, for lack of a better term, aggregated mind?
In this case, there are two real ways you can modify the aggregator
preferences. One is by causing the strategic votes cast by the sub-agents to
change, be it through mixed equilibria, or through switching between equilibria
by some means (more later). The other, which reflects the actual situation
above somewhat better, is by the introduction of new agents.

## Increase the Horde ##
Will a collection of agents vote to allow new agents? There's still some parts
of this set-up that are vague. For example, without other votes beyond the
inclusion of a new agent, there is no reason for any agent to have preferences
in that election. We will assume that the vote to include new agents is
**purely strategic** in terms of what will happen in the other games. In that
case, any agent will obviously prefer to add a voter with the same preferences
as their own. Another question is whether there is a choice of how many or what
kind of agent to add. If the question is binary, then the concerns of Arrow's
theorem mostly go away. On the other hand, one might guess that if the agents
are allowed to vote on what the new agent looks like, or allowed to choose to
add multiple new agents, they would be more inclined to add new agents. 

So let's say we've just got the inclusion vote and another vote. Further, to
keep it simple, lets consider the excessively gamable first past the post
voting scheme.

## Game theoretic preference shifting ##

{% endkatexmm %}
