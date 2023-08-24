'''
1.5 Hardworking Students

'''



import sqlite3 
import pandas as pd



# Finds the hardworking students

''' This is a function to find all the hardworking students:

- Connect to the database and find the Summary Test
- Read the StudentRate csv as a dataframe 
- Select the columns that we want and rename them
- Merge the df of the Sum Test and the csv file with the Rates
- Select only the "Below beginner" and "Beginner"
- Choose only the Students who got grater than 60% in the Sum Test

'''



def hardworking_Students():

    connection = sqlite3.connect('ResultDatabase.db')

    df = pd.read_sql(""" SELECT researchid,Grade
                         FROM dfFormattedClean_SumTest""",connection)


    # Choosing the StudentRate to select the "researchid" and the "Knowledge"
    StudentRate = pd.read_csv('Data Files/StudentRate.csv')

    # Selecting the columns "researchid" and the "Column with the knowledge"
    dfstudents = StudentRate.iloc[:,[0,3]]
    
    
    # Renaming the columns
    dfstudents.rename(columns = {"What level programming knowledge do you have?":
                    "Knowledge" , "research id": "researchid"}, inplace = True)
      

    # Merge the two dataframes
    Students = pd.merge(df, dfstudents, on='researchid', how='outer')   
        
    # Select only the "Below beginner" and "Beginner"
    Students = (Students.loc[Students['Knowledge'].isin(['Below beginner','Beginner'])])


    # Selecting the Student who got grater than 60% in the Sum Test
    Results = Students.loc[Students['Grade'] > 60]
    
    print(Results)

    connection.close()



