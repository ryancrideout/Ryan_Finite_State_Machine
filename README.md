# Finite State Machine
This is an exercise understanding the Finite State Machine, please read below before looking at the code:

## Set up
This repository uses Python (version 3.10 or higher would be ideal, but 3.3+ should be sufficient) and nothing else.

To run the script, type `python run.py`. You DO NOT need to do anything with `main.py`, though you are free to open it up and play around with it.

## Tests
To run all of the unit tests, in this current directory, run `python -m unittest discover` in your console of choice.

## Notes
Normally when I comment code I don't write as much as I did for this repository. I wrote a lot in this case as I felt it was really important to illustrate my thought process for everything.

Also, I know I made a few comments about making changes to increase the performance - with this sort of exercise I don't know how important optimization is. Like, for example, normally when I perform a modulo operator I just do `8 % 3`, but the exercise stated that Finite State Machines are a more efficient way of performing the modulo. So, I can't help but think that if we're at a point where we're tying to optimize a built in python operator, then we REALLY need to be lean when it comes to performance.

In my career experience, I've never had to care about optimizations on this level (normally the issue is much bigger and more easily identifable), but that doesn't mean there couldn't exist situations where we really need to be "as tight as possible" when it comes to efficiency. Like while I get that this could just be construed as a good mental exercise, I could also see value in developing a mathematical operator that's highly efficient, especially if we're doing hundreds of thousands of calculations.
