"""
1.2 Test Results

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt




# Finds the all Test Grades for the studentID and plot them

''' This is a function to find the results of all the tests of 
the the given stundentID and them show them in a list and plot them:

- Input the studentID
- Connect to the database and find the table with all the results 
- Set the researchid as the index
- Search from the table for the test results of each test for
the given studentID
- Create a list with all the test names
- Returning the results to a list
- Creating a plot
'''



def find_student_results():

    id = int(input("Enter ID: "))
    
    connection = sqlite3.connect('ResultDatabase.db')

    df = pd.read_sql(""" SELECT *
                     FROM TotalGrades """, connection)

    # Change the index to researchid
    df1 = df.set_index('researchid')



    if id in df1.index:
        
        # Convert the data frame to a list
        y = df1.loc[id].tolist()
        print(y)


        x = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Mock Test', 'Sum Test']

        # Create a bar plot
        plt.bar(x,y)


        plt.xlabel('Test')
        plt.ylabel('Percentage')
        plt.title('Student ' + str(id))
        plt.show()

    else:
        print("Student ID ", id, " not found")

    connection.close()
