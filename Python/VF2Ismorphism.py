graph1 = []
graph2 = []
class VF2Isomorphism:
    def __init__(self, graph1,graph2):
        self.graph1 = graph1
        self.graph2 = graph2

    def areIsomorphic(self):
        length1 = len(graph1)
        length2 = len(graph2)

        if length1 != length2:
            return False

        if not checkDegreeSequence():
            return False

        visited1 = [False] * length1
        visited2 = [False] * length2
        permutation = [-1] * length1

        return vf2Match(visited1, visited2, permutation )


def vf2Match(visited1, visited2, permutation):
    return vf2Match(0, visited1, visited2, permutation)

def vf2Match(depth, visited1, visited2, permutation):
    length = len(visited1)

    if depth == length:
        return True

    for i in range(length):
        if not visited1[i]:
            for j in range(length):
                if not visited2[j] and isPossible(i, j, permutation):
                    visited1[i] = True
                    visited2[j] = True

                    if vf2Match(depth+1, visited1, visited2, permutation):
                        return True

                    visited1[i] = False
                    visited2[j] = False
                    permutation[i] = -1
            return False
    return False

def isPossible(i, j, permutation):
    if(getDegree(graph1, i) != getDegree(graph2, j)):
        return False

    for k in range(len(graph1)):
        if permutation[i] != -1:
            if graph1[permutation[i]] != graph2[permutation[j]]:
                return False
            if graph1[k][i] != graph2[permutation[k][j]]:
                return False
    return True

def getDegree(graph, vertex):
    degree = 0
    for edge in graph[vertex]:
        degree += edge
    return degree

def checkDegreeSequence():
    degrees1 = getDegrees(graph1)
    degrees2 = getDegrees(graph2)
    degrees1.sort()
    degrees2.sort()
    return degrees1 == degrees2

def getDegrees(graph):
    degrees = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                degrees[i] += 1
    return degrees

