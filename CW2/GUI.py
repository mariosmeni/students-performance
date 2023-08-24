"""
GUI 
 
"""

# This is my menu in GUI

import testResults as tR
import studentPerformance as sP
import underperformingStudent as uS
import hardworkingStudents as hS
import tkinter as tk





#################################################
#------------------GUI MENU-------------------------#
#################################################





root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 500,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Student Monitoring System')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 100, window=label1)


def exit():
    root.destroy()
   

button1 = tk.Button(text="Find Test Results",command=tR.find_student_results,bg='blue', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 180, window=button1)

button2 = tk.Button(text="Find Student Performance",command=lambda:sP.find_student_performance(), bg='blue', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 220, window=button2)

button3 = tk.Button(text="Find Underperforming Students",command=lambda:uS.find_underperforming_student(), bg='blue', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 260, window=button3)

button4 = tk.Button(text="Find Hardworking Students",command=lambda:hS.hardworking_Students(),bg='blue', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 300, window=button4)

bexit = tk.Button(root,text="Exit",command=exit,bg='red', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 400, window=bexit)




root.mainloop()