# Python Sales Program 
This project is a full-featured program make for sells, that includes all what I have seen until now.
Implements CRUD functions that you can use in the command line, I have used Click framework for programming facilities.

The program is a little complex so, let's get by parts:

## pv.py
Manage the entry point of the program and define the table that we want to operate.

## setup.py
Interface configuration, in this case assign script command to the word *pb* for initialize program functionalities

Inside *Clients* folder, there are the three core files:

## commands.py
This module define each of the CRUD functions in our program, and assign it to a command keyword for use through Click decorators

## models.py
Template of our client object

## services.py
Allow our command functions to be applied to the client model

## .clients.csv
File that contain clients data

On the project folder, I have two more folders: common and structured_programming, the first contains the functions that I export to use throughout the project, the second consist in a test project which does the same as the original, but only in one module (not work in command line)