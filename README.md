# Chemistry Interface and Practice Problem Generator

This project is a Python-based tool designed to generate and solve chemistry problems. 
This program helped me deepen my understanding of chemistry concepts and improved my problem-solving speed. 
It also has a chemistry interface to work with compounds, reactions, etc (see ChemFuncts.py).


Link to project website: https://gso47.pythonanywhere.com/ 

## Features

Practice Problem Generation: Generates a variety of chemistry problems modeled after AP Chemistry exams and classroom assignments.\
Chemistry Interface: Using functions in ChemFuncts, it can handle various chemical calculations. \
Web Integration: Converts a terminal-based program into a web interface using Flask for accessibility. 

## Libraries Used

This program uses the following libraries:

- **NumPy**: For linear algebra and polynomial operations.
- **SymPy**: For symbolic mathematics and equation solving.
- **Flask**: To create a simple web-based interface.
- **Math**: For mathematical calculations.
- **Inflect**: For converting numbers to words.
- **Random**: For randomization in problem generation.
- **System** and **IO**: For managing terminal-based operations and file handling.
- **JSON** and **CSV**: For storing and processing problem data.

## How It Works

The first file that gets used is ChemData. In this file, the data that could be necessary get mvoed over from csv and json files into lists and dictionaries that can then be used in the later steps. 

Next, ChemFuncts creates various files and functions that are useful for generating problems. This file is the heart of the chemistry interface, and houses important aspects like the compound and reaction class. 

After that, the problems are created in ChemProblems. Here, each problem type is represented by a function that prints the question to the terminal and returns the answer. 
In order to convert this to Flask, the 'flaskify' function uses the sys and io libraries format the terminal based code for use in the website. 


At this point, there are two options for running the program.

## Installation and Usage

You can either use the program directly from the terminal (easier to set-up and debug), or from the website.

### Terminal

Run the file titled 'chem.py'. This file has instructions and disclaimers about the functionality of the terminal based code.

### Website

This method is identical to the website linked above. To run this version locally, run the file 'ChemFlask.py' locally.

This website is currently very bare bones, although making it more user-friendly is a priority.

You can get a specific type of question by inputting the problem number type (type in 0 for options). This method is not reccomended as it requires intimate knowledge of each function and it's number/useage.

Alternatively, you can go into settings and choose a specific *set* of problems. These are organized by unit. This setting affect the 'Get Random Question' and 'Get Many Questions' buttons. 
In the settings you can also decide what types of reactions are chosen (this setting applies to most, but not all, problems involving reactions. A notable exception are problems related to bonding).
You can also test how well you remember the polyatomic ions by selecting the subset of polyatomic ions you wish to test and clicking 'Polyatomic Ions' on the main page.

The 'Get Many Questions' buttons allows you to generate a pre-determined number of question by changing the value of the slider underneath it. 

## Future Improvements

- There are still many bugs: for example, the thermochemistry reaction sometimes crashes the website.
- Lewis Dot Diagrams are fairly inconsistent, the current version sometimes provides incorrect structures. I am looking into a different way of generating Lewis Dot Diagrams that is more efficient and reliable.
- Electrochemistry is a work in progress. While the functionality for half-reactions is complete, the code for combining them and generating balanaced redox reactions is as of yet incomplete.
- The website needs an improved UI and design.  

