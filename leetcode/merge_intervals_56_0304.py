from pickle import SHORT_BINSTRING

from pyparsing import sglQuotedString


# -*- coding: utf-8 -*-
class Solution:
    def merge(self,intervals):
        result = []
        # 每一个startbound，每个interval里的第一个值，x对应inteval的第一个值index所对应的数值去做sorting
        intervals.sort(key = lambda x: x[0])

        i = 0
        while i < len(intervals):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            #check if overlapping
            if result:
                #-1读 collection里最后一个数值
                prev_start,prev_end = result[-1]
                #min end,max statt
                # [[1,4],[2,3]]，hi = 3,lo = 2,lo < hi:,可以merge
                #[[1,4],[4,5]]hi = 4,low = 4,lo = hi 可以merge
                #[[1,4],[5,6]],hi = 4,lo = 5 lo > hi: 不能merge，有gap
                hi = min(prev_end,cur_end)
                lo = max(prev_start,cur_start)
                #如果最小的后端，大于最大的前段,就说明可以做merge
                if lo <= hi:
                    if cur_end > prev_end:
                        #start point已经排序了 ,只需要update endbound
                        result[-1][1] = cur_end
                else:
                    result.append(intervals[i])
           # result为空，没有interval
            else:   
                result.append(intervals[i]) 
            i += 1
        return result                 





