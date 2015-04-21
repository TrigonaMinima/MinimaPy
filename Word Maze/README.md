Word-maze
======

### Usage:

This files generates a word-maze of 12X12 matrix size from a list of given words. Just run the below line in the same directory as that of this file (```wordmaze.py```).

```
python3.4 wordmaze,py
```

The output of the above command is shown in the ```results.txt```.

For a different set of words you can edit line 11. You can't change the size of the matrix though. If you want to display the matrix without filling with any random characters then uncomment the line 137 and rerun the above specified instruction. It'll print both matrices.



### Assumptions

- It is assumed that user will enter the whole sentence with a mix of letters, digits and special characters. The code handles all of them to get the text out and generate the puzzle.
- The algorithm used here to generate the matrix is not practical at all. Once the pattern is seen one can easily find the while path.
- While displaying the end point coming on the left hand side and at the bottom are not considered. Both were making the code messy.