from collections import defaultdict
from sklearn.externals import joblib

# d = {'A': [1, 2, 3],
#      'B': [2, 4, 6],
#      'C': [6, 12, 18],
#      'D': [4, 7, 8, 9],
#      'E': [9, 12],
#      'F': [3],
#      'G': [18]}

def sps(start, goal, successors):
    
    frontiers = [[[start]], [[goal]]]
    exploreds = [set(), set()]

    while all(frontiers):
        #breadth first search
        for i, frontier in enumerate(frontiers):    
            path = frontier.pop(0)
            s = path[-1]
            for actor, state in successors(s):
                if state not in exploreds[i]:
                    exploreds[i].add(state)
                    new_path = path + [actor, state]

                    if state in exploreds[abs(i-1)]:
                        for other_path in frontiers[abs(i-1)]:
                            if other_path[-1] == state:
                                return new_path + other_path[:-1][::-1]
                    else:
                        frontier.append(new_path)
    return False

if __name__ == "__main__":
    d = joblib.load('actors.jl')
    print "Loaded"

    inverted = defaultdict(set)
    for k, v in d.items():
        for n in v:
            inverted[n].add(k)

    print "Inverted"
    joblib.dump(inverted, "inverted.jl")

    final = defaultdict(dict)
    for k, v in d.items():
        for n in v:
            final[k][n] = inverted[n]

    print "Final"

    joblib.dump(final, "final.jl")

    def successors(state):
        states = []
        new_nodes = set()
        for k, v in final[state].items():
            for new_state in v:
                if new_state not in new_nodes:
                    new_nodes.add(new_state)
                    states.append((k, new_state))
        return states
    
    print "D", d['Hanks, Tom']
    print "Inverted", inverted['Hanks, Tom']
    print "Final", final['Hanks, Tom']

    print "D", d['Willis, Bruce']
    print "Inverted", inverted['Willis, Bruce']
    print "Final", final['Willis, Bruce']
    print sps('Hanks, Tom', 'Willis, Bruce', successors)


"""
Linked List

0x01 --> [value, 0x02]
0x02 --> [value, 0x72]
0x72 --> [value, 0x01]
0x84 --> [value, '\0']
"""
