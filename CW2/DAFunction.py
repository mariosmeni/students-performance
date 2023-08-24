'''
TotalGrades Table

'''



import sqlite3
import pandas as pd




### Create Table for all the ID's with only the results of each test


connection = sqlite3.connect('ResultDatabase.db')

# Selecting the ID and the Grades from Test 1
first = pd.read_sql(""" SELECT researchid,Grade AS 'Test 1'
                       FROM dfFormattedCleanTest_1""", connection)

# Selecting the ID and the Grades from Test 2
second = pd.read_sql(""" SELECT researchid,Grade AS 'Test 2'
                       FROM dfFormattedCleanTest_2""", connection)

# Selecting the ID and the Grades from Test 3             
third = pd.read_sql(""" SELECT researchid,Grade AS 'Test 3'
                       FROM dfFormattedCleanTest_3""", connection)

# Selecting the ID and the Grades from Test 4
fourth = pd.read_sql(""" SELECT researchid,Grade AS 'Test 4'
                       FROM dfFormattedCleanTest_4""", connection)

# Selecting the ID and the Grades from MockTest
mockt = pd.read_sql(""" SELECT researchid,Grade AS 'Mock Test'
                       FROM dfFormattedClean_MockTest""", connection)

# Selecting the ID and the Grades from SumTest
sumt = pd.read_sql(""" SELECT researchid,Grade AS 'Sum Test' 
                       FROM dfFormattedClean_SumTest""", connection)

# Creating a new table with all the Grades for all the Tests
a = pd.merge(first, second, on='researchid', how='outer')
b = pd.merge(a, third, on='researchid', how='outer')
c = pd.merge(b, fourth, on='researchid', how='outer')
d = pd.merge(c, mockt, on='researchid', how='outer')
TotalGrades = pd.merge(d, sumt, on='researchid', how='outer')

# Replace na with 0
TotalGrades = TotalGrades.fillna(0)

# Sort TestGrades 
TotalGrades.sort_values(by=['researchid'], inplace=True)

# Create a table in the database with all the Grades for each student id
TotalGrades.to_sql("TotalGrades", connection, if_exists="replace", index=False)

connection.close()

