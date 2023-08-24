'''
1.3 Student Performance

'''

import sqlite3 
import pandas as pd
import matplotlib.pyplot as plt



# Finds the all the questions results for the given test and studentID and plot them

''' This is a function to find the results of all quesions of 
the the given test and stundentID, calculate the absolute and relative performance
and then show them in plots.

- Input the studentID and the Test
- Connect to the database and checks if the ID or test exist
- If both studentID and test exist then it finds all the results for the selected student (Absolute)
- Search from the table for the test results of all students and calculates the Average
- Then it calculate the Relative performance
- Plot both Absolute and Relative performance in a plot

'''




def find_student_performance():


    
      L = ['dfFormattedCleanTest_1', 'dfFormattedCleanTest_2', 'dfFormattedCleanTest_3',
         'dfFormattedCleanTest_4', 'dfFormattedClean_MockTest', 
         'dfFormattedClean_SumTest']



      id = input("Enter StudentID: ")
     
     
      # Menu which the user will choose the test he wants
      print("Tests: ")
      print("(1) Test 1 ")
      print("(2) Test 2 ")
      print("(3) Test 3 ")
      print("(4) Test 4 ")
      print("(5) Mock Test ")
      print("(6) Sum Test ")
     
     
      menuoption = input("Please select a Test: ")
    

      options =  ['1','2','3','4','5','6']
    
      if menuoption in options:
             test = L[int(menuoption)-1]
      else:
             return 'Invalid student ID or Test'   
      
    
    



      connection = sqlite3.connect('ResultDatabase.db')


      # Open the database and checks if the input studentID or the test are both exist
      A = pd.read_sql(""" SELECT *
         FROM """  + test + 
         """ WHERE researchid == """ + id , connection)



      if (test in L) and (A.empty == False):

        # Dropping the text columns to see the Total marks for each question for a single student (Absolute)
        Absolute = A.drop(['researchid', 'Startedon', 'Completed','Grade' ], axis=1).max().round(decimals=2)


        # Go to the database and finds all the students results for the test
        df = pd.read_sql(""" SELECT *
                             FROM """  + test , connection)


        # Dropping the text columns to calculate the Average of each question for all students
        df_drop = df.drop(['researchid', 'Startedon', 'Completed','Grade' ], axis=1)
        
        
        # Find the average of each question
        Average = df_drop.iloc[:].mean()
 
        # Calculate the Relative performance and round to two decimals
        Relative = (Absolute - Average).round(decimals=2)

        

        # Create two bar plots for Absolute and Relative performance

        Absolute.plot.bar()
        plt.axhline(0, color="k");
        plt.ylabel('Score')
        plt.title(f'Absolute Performance for student {id}')
        plt.show()

        Relative.plot.bar()
        plt.axhline(0, color="k");
        plt.ylabel('Score')
        plt.title(f'Relative Performance for student {id}')
        plt.show()

        print(f"Test {menuoption}")
        print("Absolute performance: \n" ,Absolute.to_dict() ,"\n \nRelative performance: \n", Relative.to_dict())


        
        connection.close()
