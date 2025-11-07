class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        
        n = len(stations)
        left, right = 0, k + sum(stations)
        while left <= right:
            x = (left + right) // 2
            use = 0
            # v is the stations after adding
            v = stations.copy()
            # s means the power of city i
            # at first, it record the sum of v[0,r)
            s = sum(stations[0: r])
            for i in range(n):
                # add to t if needed
                t = n - 1 if n - 1 < i + r else i + r
                # update s
                # find a city should be added
                if i + r < n: s += v[i+r]
                # find a city should be removed
                if i - r > 0: s -= v[i-r-1]
                # mising power stations
                diff = x - s if x - s > 0 else 0 
                v[t] += diff
                s += diff
                use += diff
            
            if use <= k:
                left = x + 1
            else:
                right = x - 1
        return right