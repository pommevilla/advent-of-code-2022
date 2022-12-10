# Notes

* Instantiating `tree = forest[i][j]` can be avoided by doing `for i, row in enumerate(forest): for j, tree in enumerate(row): ...`, but I don't like instantiating row since we're not using it except for enumeration in the outer loop.