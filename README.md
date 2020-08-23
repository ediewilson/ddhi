# DDHI Database creating script
### Last updated 23 August 2020 by Edie Wilson
Python scripts and database for consistent place name visualizations

## Getting started 
Open the Terminal application on your Mac
Type `which brew`

- If `/usr/local/bin/brew` is the output that shows up when you type that command, use
`brew update`.
- If that is **NOT** the output, run `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
- If at any point a popup appears and asks you to fill in your password in order to update system, do it.

After you complete these steps, type the following into the Terminal window, pressing return and waiting for the command to complete after each line:


`brew install python3`


`pip3 install pyqt5`

Hopefully all went well... you now have python3 on your computer!


![](https://media.giphy.com/media/2lbhL8dSGMh8I/giphy.gif)

## Tackling git on Terminal
I promise, it's not **too** bad!

First, we need to get this repository onto your computer. To do this, all you need to do is open up Terminal and use this command: 
`git clone https://github.com/ediewilson/ddhi.git`


The repository is now on your computer, and we can go into it by typing 

`cd ddhi`

Next step is to add the file that you want to edit. Go to your Finder application and search `ddhi`. 

The folder that your git repository lives in should be right there, and you'll want to drag and drop your CSV file with ONLY the place names into the subfolder **CSVs**. 

Give yourself a pat on the back! You're ready to run that program! 


![](https://media.giphy.com/media/s2qXK8wAvkHTO/giphy.gif)

## Using the program
Before you start make !!!SURE!!! that you use the command 

`git pull` 

to update the dictionary from the repository! If you don't do this... there will be... merge conflicts 
![](https://media.giphy.com/media/117gK0K7OZ8UcE/giphy.gif)

**Okay, let's get started.**
To begin running the program, make sure you are in the right folder on terminal (`cd ddhi`), and run 

`python3 ddhi.py`


There are 3 types of prompts that you will get.
1. Enter interviewee's last name: 
2. Enter the name of the file you're processing: .... ie. lovely_placeName.csv
3. The information prompts for when a place is new. This goes through all of the categories (address, city, etc), so just fill them out and press return. If there is no answer for that portion, just press return. 


When you've finished going through all of the new places, you'll be able to find your new file in the newCSVs folder in the ddhi folder! 

## Adding your changes to the database
Last step! 
Run the following commands within the ddhi directory on your terminal after you run the program. 


`git add .`


`git commit -m "Some message about your change, could be anything`


`git push`


And with that you're DONE!
