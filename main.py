import pandas as pd
from string import ascii_uppercase as alphabet

size = 7
elements = []
for i in range(size):
    elements.append(tuple([alphabet[i], i]))

dsm = {
    elements[0]: [5],
    elements[1]: [0, 2, 3, 6],
    elements[2]: [3, 6],
    elements[3]: [1, 2, 4, 6],
    elements[4]: [0, 3, 5],
    elements[5]: [0, 4],
    elements[6]: [1, 2, 3],
}


def measure(dsm, weight=1):
    points = 0
    for key in dsm:
        for x in dsm[key]:
            point = x - key[1]
            if point < 0:
                points -= weight * point
            else:
                points += point
    return points

    # https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1 :]
        for p in permutation(remLst):
            l.append([m] + p)
    return l


positions = list(range(size))
permutations = permutation(positions)
iterations = len(permutations)

i = 0
winner_points = 999
for permutation in permutations:
    i += 1
    dsm_temp = {}
    for key in dsm:
        connections = dsm[key]
        new_connections = []
        for c in connections:
            new_connections.append(permutation[c])
        dsm_temp[tuple([key[0], permutation[key[1]]])] = new_connections
    points = measure(dsm_temp)
    if points < winner_points:
        winner_points = points
        letters = []
        for i in permutation:
            letters.append(alphabet[i])
        winner = (letters, winner_points)
    print(f"Working... {i}/{iterations}")
print(winner)
