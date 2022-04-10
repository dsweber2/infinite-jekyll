abstract type aggregator end

struct BordaCount <: aggregator end
struct BordaCount <: aggregator end

struct agentPreference
function BordaCount(A)
    nCandid = max(A[1])
    Votes = zeros(nCandid)
    for x in A
        
    end
end
using Random
A = [randperm(10) for i=1:15]

