# databases_course
This repository contains a couple projects I worked on for my Database Systems course.

# Project 1
In this first project, our objective was to install and get familiar with using MySQL Workbench 8.0 to create tables, import data, and then formulate SQL queries to find specified data.  It takes a little bit of time to get everything installed and get familiar with the Workbench GUI but I enjoyed it. Below are the files from my project:
- 📋 [databases_project1_instructions](https://github.com/espdieg/databases_course/blob/main/Project%201/databases_project1_instructions.docx) - Contains the instructions provided to our class. Disclaimer: I do not own these.
- [SQL_queries](https://github.com/espdieg/databases_course/blob/main/Project%201/SQL_queries.txt) - This text file contains all SQL queries I created myself and executed within MySQL Workbench. (questions related to each query are found in the instructions document)
- [data](https://github.com/espdieg/databases_course/tree/main/Project%201/data) - This folder was provided to our class with data for each table. Our job was to first create each table within Workbench and then import these CSV files into the appropriate tables.
- [Outputs](https://github.com/espdieg/databases_course/tree/main/Project%201/Outputs) - After running each of my queries, the output was saved into CSV files. Here in this folder you can find the output of each individual query I executed.

If you'd like to try this out yourself, the installer for MySQL Workbench can be found here: https://dev.mysql.com/downloads/workbench/ and here I found some really helpful tips on how to install and use Workbench https://www.educative.io/blog/mysql-workbench-tutorial

If you are trying this yourself, very briefly the flow would be as such: install and configure MySQL Workbench, within Workbench create a schema, within this schema create the tables with their attributes, import data into each table, run queries to find desired data, and finally export results onto CSV. 
# Project 2
In this second project, the goal was to create a single python program that would connect to my database, create tables, insert data, and execute queries. The only interaction with MySQL workbench this time was to create the main schema 'project2'. Although this was somewhat tedious, I found this project really enjoyable as I learned a lot about working with python. Below are the files from my project:
- 📋 [databases_projec2_instructions](https://github.com/espdieg/databases_course/blob/main/Project%202/databases_project2_instructions.docx) - Contains the instructions provided. Disclaimer: I do not own these. 
- [output](https://github.com/espdieg/databases_course/blob/main/Project%202/output.txt) - Contains the output of my python program as you would see on the console.
- [project2](https://github.com/espdieg/databases_course/blob/main/Project%202/project2.py) - This is my python program that connects to my database, creates tables, inserts data, and executes queries. You'll have to take my word when I say my password is not just 'password' 😅. 

If you'd like to try this project yourself, you would first start with installing [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) or any [alternative](https://www.bytebase.com/blog/top-mysql-workbench-alternative/) DBMS you may prefer. You would also need to install an IDE that allows for python development. I personally used [Spyder](https://docs.spyder-ide.org/current/installation.html) but there are many options out there. It's worth noting that in your python development environment you may need to install mysql.connector by running "pip install mysql-connector-python". After this you go into Workbench to create a schema and then you can start coding. I would personally recommend starting one step at a time. First verify you can connect to your database, then create tables, then insert data, etc. After each step you can go into Workbench and refresh to see if everything is working correctly. 

