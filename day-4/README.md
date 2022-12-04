# Notes

* Python has shorthand to see if a number is contained in an interval. If you want to test if `x` is in the interval `[a, b]`, you can do `if a <= x <= b...` instead of breaking it up with an `and`
* Potential optimization is to read the lines character by character, which will allow for some potential short-circuit evaluations for containment/overlap. I want to practice writing iterators, type hints, and doc tests, though, so I'll keep doing it this way.