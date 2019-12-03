using Plots
using LaTeXStrings
t = 0:.001:.999999
N = 1 ./(exp.(1 .- t) .- t)
plot(t, N,label="", yaxis="ideal population (log scale)",xaxis=L"\varepsilon")
yaxis!(:log)
savefig("zeroMatters.jpg")
