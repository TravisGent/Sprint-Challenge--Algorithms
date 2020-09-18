# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

I would write a algorithm that would essentially pass in values in multiples of ten starting from one. i.e. 1, 10, 100, 1000, 10000 and so on. I would see how many loops it would take before it takes longer than 10 seconds or so. I would probably limit it to only do 10 or 15 multiples because by then the numbers should be big enough to give us good results. I really don't see this causing any real big problems or taking a whole lot of time in my algarithm, but it might take a bit in others. So O(n)
