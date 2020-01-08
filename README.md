Drive Ya Nuts Solver
====================
This program was the result of a weekend with family goofing off with the 
Drive Ya Nuts game. I thought I would throw together a quick solver to 
check for all possible solutions (there's only one). 

The general approach allows each piece gets a chance at the center and all
possible necklace (aka circular) permutations for the outer pieces are generated. 
Each outer piece is rotated so that its side facing the center matches 
the center value, then a check for matching adjacent values is made.
