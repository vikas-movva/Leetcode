#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])
        
        rooms = 0
        end_ptr = 0
        for start in start_times:
            if start < end_times[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1
        return rooms
# @lc code=end