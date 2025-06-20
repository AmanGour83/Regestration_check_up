import pandas as pd
import numpy as np
while True:
   sheet=pd.read_csv(r"C:\Users\pc-1\Desktop\tiwari\model_loc.csv",index_col='Admission Number')
   alpha=pd.DataFrame(sheet)
   print(alpha)
   
   while True:
      print("-------List of Candidates-------")
      print("For Details of a particular student")
      print("please enter the student's Admission Number")
      admn_no=int(input())
      details=sheet.loc[admn_no]
      print(details)
      while True:
        edit=input("do you want to edit details? Y/N: ").upper()
        if edit == "Y":
            print("1.Student's name")
            print("2.Father's name")
            print("3.Mother's name")
            print("4.Date of birth")
            print("5.Aadhar card number")
            print("6.Gender")
            print("7.Caste")
            print("8.Mobile number")
            print("9.Annual Income")
            print("10.Only Child")
            print("11.PwD")
            det=int(input("choose the detail which is to be corrected: "))
            if det==1:
                while True:
                    value=input("please enter the correct Name of the Student: ")
                    choice=input("do you want to save?\n Y/N\n").upper()
                    if choice=="Y":
                      abc = admn_no
                      alpha.Name_Of_The_Student[abc]=value
                      print("Data Updation Successfully Completed")
                      break
                    elif choice=="N":
                        print("the data is not saved")
                    else:
                        print("Invalid input")
            if det==2:
                value =input("please enter the correct Name of the father")
                choice=input("do you want to save?\n Y/N\n").upper()
                    if choice=="Y":
                      abc = admn_no
                      alpha.Name_Of_The_Studen[abc]=value###continued
                      
                      print("Data Updation Successfully Completed")
                      break
                    elif choice=="N":
                        print("the data is not saved")
                    else:
                        print("Invalid input")
            if det==3:
                value=input("please enter the correct Name of the mother")
                print("Working")
            if det==4:
                value =input("please enter the correct Date of birth")
                print("Working")
            if det==5:
                value=input("please enter the correct Aadhar card number")
                print("Working")
            if det==6:
                value=input("please enter the correct Gender")
                print("Working")
            if det==7:
                value=input("please enter the correct caste")
                print("Working")
            if det==8:
                value=input("please enter the correct mobile number")
                print("Working")
            if det==9:
                value=input("please enter the correct Annual income")
                print("Working")
            if det==10:
                value=input("please enter the correct option for ony child Y/N")
                print("Working")
            if det==11:
                value=input("please enter the correct option for PwD")
                print("Working")
        elif edit == "N":
         print("Thank you ")
         print("-------END-------")
         break
        else:
            print("Enter a valid input")
