# LatinRoots

This is a work in Progress, its kinda messy, and there is still some functionality I intend to add.

There are two main functions of this program.

1. cleanUpDoc and cleanUpErrors extract the information from the original greek_and_latin_roots2.txt file, and then clean up the extracted information so it can be used in the userNameGen.py script. To do this yourself (though it shouldn't be necessary if you just want to use the word generating function), run cleanUpDoc and then cleanUpErrors respectively.

2. After all information has been extracted and cleaned, the userNameGen.py file should be used without any issues. It works by reading in the roots and definitions files as two separate lists, and then calls two root words at random.
Then, it iterates through all possible ways the two roots can be combined and outputs this to the user, along with the definition for each root.

The user can continue to run the program and then type "Done" when finished.
The favorites/saving functionality have not been added yet.

Original pdf file where all roots and their definitions were extracted from can be found here:
https://www.oakton.edu/user/3/gherrera/Greek%20and%20Latin%20Roots%20in%20English/greek_and_latin_roots.pdf

