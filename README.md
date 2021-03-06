############################## DESCRIPTION OF THE PROGRAM ##############################

There is a collection of strings and queries.
The purpose is to determine for each query how many times it occurs in the list of strings.

There are 3 way to use the program :

-> With 0 argument in command line :
The program use the environments variables for both strings and queries

-> With 1 argument in the command line :
The argument given is the queries, strings is an environment variable

-> With 2 arguments in the command line :
The arguments given are first the strings and second the queries


############################## How to run the program ##############################

"python -m main" will run the program with 0 argument in command line, environment variables will be used

"python -m main ab,c" will run the program with 1 argument in command line, queries will be 'ab' and 'c', strings
will be based on the value of the environment variable

"python -m main ab,c ab,ab,d" will run the program with 2 arguments in command line, queries will be 'ab' and 'c',
strings will be 'ab', 'ab' and 'd'

############################## EXPLICATION OF THE FILES ##############################

The project is composed of 2 files :

->SparseArray.py
This script contains the method that count how many times each query occurs in the list of strings

-> main.py
The main script get the environment variables and check how many arguments there is on the command line.
Depending of this number it will send the appropriates values to the method contain in SparseArray

-> Dockerfile
This file allow the possiblity to create a python image

############################## DOCKER ##############################

-> how to run the program with docker ?
"docker run -t test_mdm ab,abc,bc" allow you to launch the program with "ab", "abc" and "bc" as queries.
On the same way, you can provide 0,1 or 2 arguments depending of what you want

-> If you don't have image
"docker build . -t test_mdm" create an image of python 3.7 named test_mdm

############################## FLASK + SWAGGER ##############################

-> how to use this ?
"python server.js" launch the server, then you need to go on your navigator and type : 127.0.0.1:5000/api/ui

You have different options :

-> GET (/dict) return all the queries of the dictionary
-> POST create a new query and add it to the dictionary
-> DELETE, delete the query typed
-> GET(/dict{queries}) return the query typed
-> PUT modify the value "strings" of the query typed