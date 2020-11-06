# Clinic

https://open.kattis.com/problems/clinic

*keywords: priority queue, heapq, tombstone*

### This was a good one. 10% acceptance ratio and only 6 accepted Python solutions.

### First iteration
Started out pretty naively with a list of tuples: (priority, name, time, severity). On patient arrival, simply append to the list. On doc ready, recalculate every patient's priority based on their elapsed time, then re-sort and pop. Not surprisingly this was very slow. Didn't implement patient death.

### Second iteration
Insight: patient order in the queue never changes - everyone's priority grows at the same rate over time. No need to recalculate priority every time, just need to figure out where in the queue to put new arrivals. Severity is just an initial boost to their priority.

Changed implementation to heapq. Patient arrival and doc ready are easy, heappush and heappop respectively, but there is no good mechanism to remove an arbitrary item. I ended up using a dict to map patient names to their (priority, name) tuple. Then I treat the heapq as a list and remove the tuple. Finally re-heapify.

This passed all tests except for time-exceeded on the last three, which I think have a lot of patient death events. It worked functionally, but the list.remove() followed by heapify() was just too slow.

### Third iteration
Insight: Don't need all items to be sorted, just need to find the min priority. 

Reimplemented as a dict. Patient arrival and death is straightforward and fast. Doc ready gets the min priority value of the patient dict and pops it. This is O(n) and way too slow. Failed early on in the tests.

### Fourth iteration
Insight: Most of the time we have a sorted list, so use binary search to insert the new arrivals in the right spot.

Went back to a list. The list remains sorted, but rather than calling sort() on it, use bisect() to identify the index at which to insert new patients as they arrive. Doc ready is trivial on a sorted list. Patient death also uses bisect to find and del the right entry.

This is O(nlogn) for cases 1 and 3, and O(1) for case 2. I liked this approach because it makes use of the fact that the list is sorted and should be easy to insert into. Wasn't fast enough, failed same later test cases.

### Fifth iteration
Insight: Quick and dirty is, well... quicker.

Heapq handles prioritization, dict handles tombstones. 

On patient death, rather than try to search and delete from the heapq, only delete from the dict. On doctor ready, When popping from the heapq, if it doesn't also exist in the dict, go back to heapq until you pop someone who's still in line.

In this sense, the data in heapq is dirty - it contains items that shouldn't be there. But every operation is O(n) and all tests pass. So stop being a perfectionist.