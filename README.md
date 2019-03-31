# to-dos
A simple Django todo app

## Usage

* To create a task click on the "I need to..." field and type in your task description. Note, that maximum number of charachters
is 100. If you are done just hit <kbd>enter</kbd> or <kbd>return</kbd>, otherwise if you need to specify the priority, 
use the selector that is placed next to the task text field and hit the "create" button.
* To edit the task description click on it's text and do your corrections. After you are done just 
click anyware outside the text field and it will be updated automatically.
* To delete a task click on the trash button next to the priority selector.
* To sort your tasks select the field you want to sort by and click arrow up or arrow down buttons (that denote ascending and 
descending orderings accordingly) next to the field selector.

## Installation

If you are running under OS X you just have to clone the repository into the folder of your choice and run the development 
server from the root of the project. Otherwise, at first you have to create a virtual environment with python3.6 and install all the requrements listed in the requirements.txt.

## Future improvements
* Make the app multiuser compatible
* Implement the ability to add tags
* Add pagination
* Implement complex filtering (multifield)
* Add deadlines
* etc.
