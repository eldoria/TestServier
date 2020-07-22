There is a collection of strings and queries.
The purpose is to determine for each query how many times it occurs in the list of strings.

There are 3 way to use the program :

-> With 0 argument in command line :
The program use the environments variables for both strings and queries

-> With 1 argument in the command line :
The argument given is the queries, strings is an environment variable

-> With 2 arguments in the command line :
The arguments given are first the strings and second the queries


-> How to run the program

"python -m main" will run the program with 0 argument in command line, environment variables will be used

"python -m main ab,c" will run the program with 1 argument in command line, queries will be 'ab' and 'c', strings
will be based on the value of the environment variable

"python -m main ab,c ab,ab,d" will run the program with 2 arguments in command line, queries will be 'ab' and 'c',
strings will be 'ab', 'ab' and 'd'


The project is composed of 2 files :

->SparseArray.py
This script contains the method that count how many times each query occurs in the list of strings

-> main.py
The main script get the environment variables and check how many arguments there is on the command line.
Depending of this number it will send the appropriates values to the method contain in SparseArray