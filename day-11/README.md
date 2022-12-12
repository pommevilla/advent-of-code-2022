# Notes

* For Part 2, since we're not dividing worry by 3 every round, the worry levels will get very big very fast over 10,000 rounds. We need to find another way to represent the worry number that still maintains the modular divisibility.
* There's some modulo arithmetic theorem that says that if `x % a = 0` and `x % b = 0`, then `x % lcm(ab) = 0` (or something, my math is rusty lol). 
* In other words, after the operations, we can divide the worry by the lcm of all of the monkeys test to still preserve modulo divisibility.
* There some jankiness with populating the monkey dictionary with who to pass the item to depending on the outcome of the test. I could have made an inner "throw_to" dictionary that had `True` and `False` as the keys to streamline that part of the code.