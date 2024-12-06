AIcore - Finance Loan Project 

What is the aim of this project?


Contents:
Milestone 1:
Milestone 2:
Milestone 3:
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
Instance of class is intialized and tested using config_path as parameter, checking to see if enging conected and data extracted.
Refinement and error handling performed. 

Pushed to Git. 

Columns and thier meanings from the 'loan_payments' database are to be familiarized with. 

Code refined and made more robust FROM * removed, and all the column names of the loan_payments df. 
