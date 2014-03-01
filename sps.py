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
            for action, state in successors(s):
                if state not in exploreds[i]:
                    exploreds[i].add(state)
                    new_path = path + [action, state]

                    if state in exploreds[abs(i-1)]:
                        for other_path in frontiers[abs(i-1)]:
                            if other_path[-1] == state:
                                return new_path + other_path[:-1][::-1]
                    else:
                        frontier.append(new_path)
    return False

both = joblib.load('both.jl')
inverted_both = joblib.load('inverted_both.jl')
print "Files loaded."

def successors(person):
    states = []
    visited_people = set()
    for movie in both[person]:
        people = inverted_both[movie]
        for new_person in people:
            if new_person not in visited_people:
                visited_people.add(new_person)
                states.append((movie, new_person))
    return states

    
if __name__ == "__main__":

    print sps('Watson, Emma (II)', 'Monroe, Marilyn', successors)
