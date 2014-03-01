from sklearn.externals import joblib
from collections import defaultdict

d = joblib.load('actresses.jl')
print "Loaded"

inverted = defaultdict(set)
for k, v in d.items():
    for n in v:
        inverted[n].add(k)

print "Inverted"
joblib.dump(inverted, "actresses_inverted.jl")

final = defaultdict(dict)
for k, v in d.items():
    for n in v:
        final[k][n] = inverted[n]

print "Final"

joblib.dump(final, "actresses_final.jl")

