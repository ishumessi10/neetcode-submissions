class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        new_list= []
        i = 0
        res = []

        for x1, y1 in points:
            dist = x1*x1 + y1*y1
            new_list.append((dist, (x1, y1)))
            i += 1

        heapq.heapify(new_list)

        while len(res) < k:
            res.append(heapq.heappop(new_list)[1])

        return res

        