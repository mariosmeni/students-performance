'''
1.4 Underperforming Students

'''



import sqlite3 
import pandas as pd


# Finds the all the underperformance students based on all tests

''' This is a function to find the the underperformance students based
in all tests they had

- Connect to the database and finds all students with their total test grades
- Select the students who score less than 50%
- Finds the average of all the tests that each student attempt
- Select only the students who have less than 50% in the average
- Exclude the students who didn't attempt more than 3 tests
- Find for each student the lowest test grade
'''




def find_underperforming_student():

    connection = sqlite3.connect('ResultDatabase.db')

    df = pd.read_sql(""" SELECT *
                     FROM TotalGrades """, connection)


    # Find all the students who got less than 50% in their Summary Test
    df = df.loc[df['Sum Test'] < 50]

    # Create a new column which contains the average for each student of all tests
    df['Average all student tests'] = df.mean(axis = 1)

    # We choose the students now who's average is below 50%
    df = df.loc[df['Average all student tests'] < 50]


    #Search how many zeros has every student 
    zeros = (df == 0).sum(axis=1)

    # Creating a dataframe which includes how many zeros has each students in his test
    dfz = pd.DataFrame(zeros)

    # Finding the students who didn’t 3 or more tests
    dfz = dfz.loc[dfz[0] >= 3]

    # Exclude students who didn’t 3 or more tests
    x = df.drop(dfz.index)
    
    # Sort by SumTest
    x = x.sort_values(by=['Sum Test'])
    
    # Create a new column and add the lowest grade all formative tests of each student
    x['Lowest Grade'] = x.apply(lambda x: x.drop(['researchid', 'Sum Test']).loc[x>0].min(), axis=1)
    
    print(x)

    connection.close()