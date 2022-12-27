# Project PlayVLCShuffle

**Table of contents**

-   [**Introduction**](#introduction)
-   [**Debugging Utilities**](#debugging-utilities)
-   [**Credits**](#credits)

## Introduction

PlayVLCShuffle consists in a program that, given a determined playlist with songs and its path stored in a xspf file, gets the file songs along its path, shuffles them, prints the shuffled order, calls the VLC programm, and gives it the shuffled playlist to execute and play. Each time the main file (playShuffleVLC.py) is executed, the playlist will be shuffled again and played in a different order.

## Debugging Utilities

Code does not use test cases.
Code uses invariants (preconditions and postconditions) to check the status of the data structures that are modified. As well as functions to check the validity of the data returned by the routines with the main responsibilities.

## Credits

Code from [dfleta](https://github.com/dfleta/playVLCshuffle).  

I just refactored and organized the project.
