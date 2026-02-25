# priocomp

A simple Python library that lets you check comparisons in order of priority (importance).

This is my third python library :D

Commands:

priocomp.pc.get() # Returns True if the comparison with the highest importance is true, and False if false.

priocomp.pc.add("comparison",importance) # Adds a comparison with a set importance.

priocomp.pc.clear() # Removes all comparisons.

priocomp.pc.remove(index) # Removes a specific comparison, but the next comparison added will be one index higher than this (if it was the latest). Use priocomp.pc.clear() to restart index from 0 (also erases all comparisons).

priocomp.pc.peek() # Returns the comparison with the highest importance.

priocomp.pc.size() # Returns how many comparisons (that arent removed) are left.

priocomp.pc.is_empty() # Returns True if there are no comparisons, False if there are comparisons left.


!NB!

Use: pip install priocomp

But, to import it to python: import priocomp
