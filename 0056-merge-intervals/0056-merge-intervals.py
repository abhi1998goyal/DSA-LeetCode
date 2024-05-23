class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        ans=[sorted_intervals[0]]

        for i,inv in enumerate(sorted_intervals):
            start=ans[-1][0]
            end=ans[-1][1]
            start1=inv[0]
            end1 = inv[1]
            if(start1<=end):
                new_end=max(end1,end)
                ans[-1][0]=start
                ans[-1][1]=new_end
            else:
                ans.append(inv)
        return ans
            

