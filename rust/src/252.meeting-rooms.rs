
//  Definition of Interval:
 #[derive(Debug, Clone)]
 pub struct Interval {
     pub start: i32,
     pub end: i32,
 }

 impl Interval {
     pub fn new(start: i32, end: i32) -> Self {
         Interval { start, end }
     }
 }

use std::slice;
use crate::Solution;

impl Solution {
    pub fn can_attend_meetings(mut intervals: Vec<Interval>) -> bool {
        intervals.sort_by_key(|i| i.start);
        intervals.windows(2)
            .all(|w|w[0].end <= w[1].start)
    }
}