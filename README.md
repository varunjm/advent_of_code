# Introduction

This codebase contains programs to solve the problems presented on [adventofcode.com](https://adventofcode.com/)

Each folder has solutions to problems from problems of that year.

Solutions are named after day. For example

* 9a is a solution to the first problem on day 9
* 9b is a solution to the sencond problem on day 9
* `input/9.in` is the input provided along with the problem (same input for 9a and 9b) 

# Execution instructions

```
$ cd 2019
$ run 9a 9
```

This runs equivalent to 

```
$ python -m cProfile 9a.py input/9.in
```

# Custom Input

Use `input/test.in` or your own `input/<name>.in` file to provide input. Run it like so

```
$ run 9a <name>
```

# Notes

* Tested only with Python 2.7 (and C++11 for 2017)
