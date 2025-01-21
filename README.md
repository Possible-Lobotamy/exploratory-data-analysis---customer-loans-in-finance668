AIcore - Finance Loan Project 

aim of project:
To extract data from an AWS df. 
Then write code in python to clean, transform and viualize the data. 
Then write code in python to analyze and vizualize the data and draw summary conclusions from this analysis. 


Contents:

Milestone 1: line 20 

Milestone 2: line 24

Milestone 3: line 36
Task 1: line 41 
task2: line 50

Milestone 4:

---------------------------------------------------------------

Milestone 1: 
This Milestones aim was to set up a Git, and create the necessary enviroment for the project. 
This was already achieved, in previously lessons, so not much was done here.

Milestone 2:
The aim of this milestone was to 'extract the loans data from the cloud'. 
This involved using a .YAML file with the database (db) credentials, in a engine to connect to the database and then extracting the desired data.
Firstly the credentials file in a .YAML format were downloaded and saved to a .gitignore folder for security. 
Using PyYAML a RDSDatabaseConnector class was designed in python, and the .YAML file safe loaded using SQLalchmey functions.
Then using the loaded credentials, as server connection inputs, an engine to connect to the db was created in the methods. 
Another method in the class, accessing the desired table within the db was added. 
Instance of class was intialized and tested using config_path as parameter, checking to see if engine conected and data extracted.
Data extracted and saved as .CSV file df. 
Columns and thier meanings from the 'loan_payments' database were familiarized with. 
Code refined and git pushed.

Milestone 3:
The aim of this milestone was to gain a deep understanding of and identify any patterns which exist.
Then along this process clean, transfrom and visualize the data in a appropiate way. 

Milestone 3 task 1 - the aim of this task was to convert the columns to the correct pandas (pd) dtype. 
This involved creating a DataFrameTransform class to achieve this.
Firstly a DataFrameTransform class was concieved.
Then a change_dtypes class function which contained code to convert dtype to pd datetime64, boolean & all other.
A dictionary of the columns and desired dtypes to be changed to as key value pairs was then created. 
The .CSV file df was loaded as a pd df, and then intialized as a DataframeTransform class instance.
The class instance along with the change_dtypes function and dictionary was used to transfrom the dtypes.
The new transfromed df was saved as a new .CSV df file. 

Milestone 3 task 2 - 


