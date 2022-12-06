# Notes

* Popping and appending to either side of a deque is [approximately O(1)](https://docs.python.org/3/library/collections.html#collections.deque). On the other hand, lists are a lot slower when popping or appending left as [each element has to be shifted over](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues), meaning that these operatiosn are closer to  O(n).
* An improvement would be to instantiate the counter right off the bat and incremement and de-increment the appropriate letter whenever a new one is read and one is popped. This will prevent having to recount everything all the time. Since the counter is a subclass of a dictionary, which are implemented as a hashmap, this is probably a more efficient implementation.
* Timing results after implementing the improved algorithm:

    ```
    ------Timing Part One------
    Average time for part_one over 10000 trials: 0.00067569
    Average time for part_one_improved over 10000 trials: 0.00064139
    ------Timing Part Two------
    Average time for part_two over 10000 trials: 0.00567510
    Average time for part_two_improved over 10000 trials: 0.00086254
    ```

* So it looks like there isn't a big difference when `n` is small (where `n` is the number of characters that have to be different) as seen in the timings in Part 1. In Part 2, though, implementing the second method outlined above gave us approximately a 6.5 increase in speed.
* You can run the timing tests yourself by doing `python day-6.py -m timing`

