class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row)//2
        couples = [[] for _ in range(N)]
        for seat, num in enumerate(row):
            couples[num//2].append(seat//2)
        adj = [[] for _ in range(N)]
        for couch1, couch2 in couples:
            adj[couch1].append(couch2)
            adj[couch2].append(couch1)

        result = 0
        for couch in range(N):
            if not adj[couch]: continue
            couch1, couch2 = couch, adj[couch].pop()
            while couch2 != couch:
                result += 1
                adj[couch2].remove(couch1)
                couch1, couch2 = couch2, adj[couch2].pop()
        return result

val=Solution()
edges=int(input())
rows=list(map(int,input().split()))
print(val.minSwapsCouples(rows))
