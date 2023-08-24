import testResults as tR
import studentPerformance as sP
import underperformingStudent as uS
import hardworkingStudents as hS



    

def display_menu():
     """
     Building Menu Options
     
     """
     print ("\n")
     print ("**********************")
     print ("*------Menu----------*")
     print ("**********************")
     print ("Please select an option below")
     print ("1. Test Results")
     print ("2. Student Performance")
     print ("3. Underperforming Students")
     print ("4. Hardworking Students")
     print ("5. Exit")


while True:
    display_menu()
    menuoption=input("Enter Choice(1/2/3/4): ") 
    
    if menuoption=="1":
        print(tR.find_student_results()) 
   
    if menuoption=="2":
        print(sP.find_student_performance()) 
        
    if menuoption=="3":
        print(uS.find_underperforming_student()) 
   
    if menuoption=="4":
        print(hS.hardworking_Students())
    
    if menuoption=="5":
        break


