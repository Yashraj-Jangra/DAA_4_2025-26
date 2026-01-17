class FindLen:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, p, q):
        self.parent[self.find(p)] = self.find(q)


class Solution:
    def jobSequencing(self, deadline, profit):
        uf = FindLen(len(deadline) + 1)
        pairs = [(profit[i], deadline[i]) for i in range(len(deadline))]
        pairs.sort(reverse=True)
        total = 0
        count = 0
        for p, d in pairs:
            slotFree = uf.find(d)
            if slotFree > 0:
                uf.union(slotFree, slotFree - 1)
                count += 1
                total += p
        return [count, total]