Normalizer
==========

Program that normalizes a directory.

Directions for usage:

In commandline, you must first CD to the directory that contains the file "normalize.py".
Afterwards, type in "python normalize.py arg", with arg being the directory that you want to normalize.
Example: "python normalize.py foo/./bar" will print:
foo/bar

For multiple directories to normalize, separate the arguments with a space. 
Example: "python normalize.py foo/./bar foo//bar" will print:
foo/bar
foo//bar

Happy usage! Thanks for checking out my small tool!
