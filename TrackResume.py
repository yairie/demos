''' @Author: Yelena Irie       
    @Date Created: 06/04/2018  

       Objective: Create a Demo that keeps track of Resume submission  

    This program Creates and Displays the following User Information:
        *Company Name
        *Application Submission Date
        *Job Position

     Input Validation:
     
       company - Company is AlpaNumeric
       date - Is stored in format dd/mm/yyyy
       position - position is Alpha only
       selection- Integer
        
 '''

import sys

def Service(selection):
    submissionRec =[]
    submissionRec.append(Data(company=input("Enter Company Name:"),
                        date=input("Enter Application Submission Date:"),
                        position=input("Enter Application Job Position:")
                       )
              )
    return submissionRec
    
def Display(submissions):
    
    for application in submissions:
        appSubmited = application   #application is a tuple
        print(appSubmited[0])       #print out first element of tuple or field
    
    return
def Data(company,date,position):
    
    return [(company,date,position)]


submissions=[]
while 1:
    
    submissions.append(Service(selection=input("Enter 1  to Add a submitted Application:")))
    Display(submissions)

 
