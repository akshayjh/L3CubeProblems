###Write a program to list duplicate files from hard drive

The aim of this assignment is to list all the duplicate files from the hard drive and give user option to remove them or merge them.

You have to provide full (absolute path) for the directory where the duplicate filesare to be checked for

Compile as:   <br>
`javac prog3.java`

Run as:   <br>
`java prog3`

**Note**: For merging I have adopted this method:

If the duplicates files contains `hello`, then after merging, the 2nd file contents shall be appended to the 1st file and the second file shall be deleted.
Like:
```
hello
hello
```
