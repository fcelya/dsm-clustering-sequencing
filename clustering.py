from string import ascii_uppercase as alphabet

size = 7
num2let = []
let2num = {}
for i in range(size):
    num2let.append(alphabet[i])
    let2num[alphabet[i]] = i

dsm_original = {
    num2let[0]: ["F"],
    num2let[1]: ["A", "C", "D", "G"],
    num2let[2]: ["D", "G"],
    num2let[3]: ["B", "C", "E", "G"],
    num2let[4]: ["A", "D", "F"],
    num2let[5]: ["A", "E"],
    num2let[6]: ["B", "C", "D"],
}


def measure(dsm_num, weight=1):
    points = 0
    for key in dsm_num:
        for x in dsm_num[key]:
            point = x - key
            if point < 0:
                points -= weight * point
            else:
                points += point
    return points


def measure2(dsm_num):
    permutation = list(dsm_num.keys())
    points = 0
    for i in range(len(permutation)):
        for n in range(1, len(permutation) - i):
            points += count_square(dsm_num, i, n + 1) / cluster_size(n + 1)
    return -points


def count_square(dsm, corner, n):
    count = 0
    for i in range(n):
        element = corner + i
        for x in dsm[element]:
            if x in list(range(corner, corner + n)):
                count += 1
    return count


def cluster_size(n):
    return n * n - n


# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
# Algorithm to generate permutations obtained from the above page
def permutation_generator(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1 :]
        for p in permutation_generator(remLst):
            l.append([m] + p)
    return l


def letdsm2numdsm(dsm_orginal, permutation, let2num):
    dsm_num = {}
    for key in dsm_original:
        l = []
        for item in dsm_original[key]:
            l.append(permutation[let2num[item]])
        dsm_num[permutation[let2num[key]]] = l
    return dsm_num


positions = list(range(size))
permutations = permutation_generator(positions)
iterations = len(permutations)

i = 0
winner = {"letters": [], "points": 999, "dsm": {}}
for permutation in permutations:
    i += 1
    dsm_temp = letdsm2numdsm(dsm_original, permutation, let2num)
    points = measure2(dsm_temp)
    if points < winner["points"]:
        winner["points"] = points
        letters = list(range(size))
        for j in range(size):
            letters[permutation[j]] = num2let[j]
        winner["letters"] = letters
        winner["dsm"] = dsm_temp
print(winner)
