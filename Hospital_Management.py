import os #importing os library in python application for clearing the screen
import sys #importing sys library in python application for terminating the prg
import time #importing time library in python application for delaying the display screen
import mysql.connector #importing MYSQL Connector in python application
import maskpass #importing maskpass library in python application for hiding the inputted password
from datetime import date #importing datetime library in python application
import base64 #importing base64 library in python application for decoding and encoding of password
import pandas as pd #importing pandas library in python application




# =============================================================================
#                                    ADMIN
# =============================================================================

class Admin:
    def __init__(self):   #CONSTRUCTOR
        #EXCEPTION HANDLING
        try: 
            self.mydb = mysql.connector.connect(host="localhost",user="root",password="",database="apollohospital")  #MYSQL Connection Request
        except:
            print("\nFailed to make connection with server.\n") #Printing the error message
            sys.exit()  #Exiting the System



# =============================================================================
#                                    PATIENT
# =============================================================================

class Patient(Admin): # INHERITING THE ADMIN CLASS
    def patient_appointment(self):
        connect = self.mydb.cursor() # Encapsulating the cursor
        print("\n\n\n\n\n\n\t\t\t", end="")
        print("|------------- GET APPOINMENT IN APOLLO-HOSPITAL  --------------|")

                                   #INPUT FIELDS
        self.__name = input ("\n\n\t\t\t\tENTER NAME OF PATIENT       : ")
        self.__symp = input ("\t\t\t\tENTER SYMPTOMS OF PATIENT   : ")
        self.__mob =  input ("\t\t\t\tENTER MOBILE NUMBER         : ")
        self.__add =  input ("\t\t\t\tENTER ADDRESS OF THE PATIENT: ")
        self.__stat = input ("\t\t\t\tENTER STATUS OF THE PATIENT : ")
        self.__today = str(date.today())  #Retrives Current date
        # EXCEPTION HANDLING
        try:
            connect.execute("Insert into patient(Name,Symptoms,Mobile,Address,Status,Admiting)" +
                        "values('"+self.__name+"','"+self.__symp +"','"+self.__mob+"','"+self.__add+"','"+self.__stat+"','"+self.__today+"')") #MYSQL Query
            self.mydb.commit() # Commiting to the DataBase
            print("\n\n\t\t\t\t Patient Added Succesfully \n")
        except:
            self.mydb.rollback()  # Roll Back if any error is generated
            print("\n\n\t\t\t\t Issue in adding Patient. TRY AGAIN ! \n") # Printing the error message

    def display_patient(self):
        connect = self.mydb.cursor() # Encapsulating the cursor
        #EXCEPTION HANDLING
        try:
            connect.execute("select * from patient")  #MYSQL Query
            self.__rs = connect.fetchall() #Fetching the data accoring to the MYSQL Query
            print("\n\n\n\n\n\t\t\t", end="")
                                    # Displaying the Data
            print("|----------------  APOLLO-HOSPITAL PATIENT LIST  ---------------|")
            print("\n\n\tID     Name          Symptoms           Mobile            Status          Admiting Date")
            print("\t============================================================================================\n")
            j=0; i=0
            for row in self.__rs:
                print("\t%-7d%-14s%-19s%-19d%-15s%-12s"%(row[0],row[1],row[2],row[3],row[4],row[5])) # d% and s% is used for printing values
                if(row[4] == 'hold'):
                    j+=1
                else:
                    i+=1
            print("\n\n\t\tOn Hold case     : ",j) #Number of On Hold Cases
            print("\t\tAdmitted Patient : ",i) #Number Admitted Patients
        except:
            print("\n\n\t\t\tUNABLE TO FETCH DATA! \n") # Printing the Error Message

    def search_patient(self):
        print("\n\n\n\n\n\n\t\t\t", end="")
        print("|---------------- SEARCH PATIENT APOLLO-HOSPITAL  ---------------|")
                                    # INPUT FIELD
        self.__id = input("\n\n\t\t\t\tENTER ID OF THE PATIENT: ")
        os.system('cls')  # Clearing the previously loaded screen
        connect = self.mydb.cursor() # Encapsulating the cursor
        # EXCEPTION HANDLING
        try:
            connect.execute("select * from patient where idpatient='" + self.__id + "'") #MYSQL Query
            self.__rs = connect.fetchall() # Fetching the data according to the given MYSQL Query
            print("\n\n\n\n\n\t\t\t", end="")
                                    # INPUT FIELD
            print("|----------------  APOLLO-HOSPITAL PATIENT LIST  ---------------|")
            print("\n\n\tID     Name          Symptoms           Mobile            Status          Admiting Date")
            print("\t============================================================================================\n")
            for row in self.__rs:
                print("\t%-7d%-14s%-19s%-19d%-15s%-12s"%(row[0],row[1],row[2],row[3],row[4],row[5])) # # d% and s% is used for printing values
        except:
            print("\n\n\t\t\t\tUNABLE TO FETCH DATA! \n") # Printing the Error Message

    def update_patient_info(self):
        connect = self.mydb.cursor() # Encapsulating the cursor
        print("\n\n\n\n\n\n\t\t\t", end="")
        print("|------------- UPDATE PATIENT INFO APOLLO-HOSPITAL  -------------|")
                                # INPUT FIELDS
        self.__id = input("\n\n\t\t\t\tENTER ID OF PATIENT: ")
        self.__st = input("\t\t\t\tENTER PATIENT STATUS: ")
        # EXCEPTION HANDLING
        try:
            connect.execute("update patient set Status = '" + self.__st + "' where idpatient='" + self.__id + "'") #MYSQL Query
            self.mydb.commit() #Commiting to the Database
            print("\n\n\t\t\t\tStatus Set Succesfully...\n")
        except:
            self.mydb.rollback()  # Roll Back if any error generates
            print("\n\n\t\t\t\tUNABLE TO UPDATE THE STATUS! ")

    def generate_invoice(self):
        print("\n\n\n\n\n\n\t\t\t", end="")
        print("|--------------- PATIENT INVOICE APOLLO-HOSPITAL  ---------------|")
                                # INPUT FIELDS
        self.__id = input("\n\n\t\t\t\tENTER ID OF THE PATIENT: ")
        os.system('cls') #Clearing the previously loaded screen
        connect = self.mydb.cursor() # Encapsulating the cursor
        # EXCEPTION HANDLING
        try:
            connect.execute("select * from patient where idpatient='" + self.__id + "'") #MYSQL Query
            self.__rs = connect.fetchall() # Fetching the data according to the given Query
            print("\n\n\n\n\n\n\t\t\t", end="")
            print("|--------------- PATIENT INVOICE APOLLO-HOSPITAL  ---------------|")
            for row in self.__rs:

                # Calculating the number of days between 2 dates
                self.d = str(row[5])
                self.prev = str(row[5])
                self.to = str(date.today())
                f_date = date(int(self.prev[0:4]),int(self.prev[5:7]),int(self.prev[8:10]))
                l_date = date(int(self.to[0:4]),int(self.to[5:7]),int(self.to[8:10]))
                delta = l_date - f_date
    
                d = delta.days
                if d == 0:
                    f = 0
                else:
                    f = d*1000 + 200000


                # Updating the excel sheet with Patient's Details
                df = pd.read_excel("Patient_details.xlsx")
                id = row[0]
                nm = row[1]
                symp = row[2]
                mob = row[3]
                stat = row[4]
                admit = row[5]
                address = row[6]

                # Arranging the data in JSON ( JavaScript Object Notation ) Format
                tmpdata = {
                    "ID": id,
                    "Name": nm,
                    "Symptoms": symp,
                    "Mobile": mob,
                    "Status": stat,
                    "Admiting Date": admit,
                    "Address": address
                }

                df = df.append(tmpdata, ignore_index=True)  # Appending the data to the df
                writer = pd.ExcelWriter("Patient_details.xlsx", engine="xlsxwriter") # Mentioning the Filename and the engine used for writing the data
                df.to_excel(writer, sheet_name='Sheet1', index=False) # Writing to the excel sheet
                writer.save() # Saving the data

                                                        #DISPLAY
                print("\n\n\t\t\t_________________________________________________________________")
                print("\t\t\t|                                                               |")
                print("\t\t\t|                        APOLLO HOSPITAL                        |")
                print("\t\t\t|                                                               |")
                print("\t\t\t|---------------------------------------------------------------|")
                print("\t\t\t|Admiting Date: %-6s             Status  : %-15.9s|"%(self.d[0:10],row[4]))
                print("\t\t\t|Patient Id   : %-11d            Name    : %-15.9s|"%(row[0],row[1]))
                print("\t\t\t|Mobile no    : %-11d            Symptoms: %-15.8s|"%(row[3],row[2]))
                print("\t\t\t|                                                               |")
                print("\t\t\t|---------------------------------------------------------------|")
                print("\t\t\t|Total Amount : %-12d                                    |"%f)
                print("\t\t\t|                                                               |")
                print("\t\t\t|_______________________________________________________________|")




                self.__myc.execute("delete from patient where idpatient='" + self.__id + "'") # Deleting from the database using MYSQL Query
                self.__mydb.commit() # Commiting to the database

        except:
            print("\n\n\n\n\t\t\t\tUNABLE TO FETCH DATA! \n")




# =============================================================================
#                                    DOCTOR
# =============================================================================

class Doctor(Admin): # INHERITING THE ADMIN CLASS
    def sign_in(self):
        print("\n\n\n\n\n\n\t\t\t", end="")
                                        # DISPLAY
        print("                               Sign in                           ")
        print("\t\t\t-----------------------------------------------------------------")

                            # DECRYPTING THE PASSWORD
        self.__user = input("\n\n\n\n\n\t\t\t\t\t\tUsername : ")
        self.__pwd = maskpass.askpass("\t\t\t\t\t\tPassword : ")
        self.__ecdpwd = base64.b64encode(self.__pwd.encode("utf-8")) # Encoding the Entered Password
        self.__ecdpwd = str(self.__ecdpwd) # Converting the encoded password with base64 to String
        connect=self.mydb.cursor() # Encapsulating the cursor
        # EXCEPTION HANDLING
        try:
            connect.execute("select password from admin where username='"+self.__user+"'") # MYSQL Query
            result=connect.fetchall() # Retriving the data according to the given MYSQL Query
            for row in result:
                self.__result = row[0]
            if(self.__ecdpwd ==  self.__result): # Comparing the Entered Password with the stored encoded Password in the database
                return "Right"
            else:
                pass
        except:
            print("\n\t\t\t\t\tNo Data Found with \'Username\' : %s\n"%self.__user)
        
    def display_doctors(self):
        connect=self.mydb.cursor() # Encapsulating the cursor
        # EXCEPTION HANDLING
        try:
            connect.execute("select * from doctor") # MYSQL Query
            result=connect.fetchall() # Fetching data according to the given MYSQL Query
            print("\n\n\n\n\n\t\t\t", end="")
                                            # DISPLAY
            print("|----------------  APOLLO-HOSPITAL DOCTORS LIST  ---------------|")
            print("\n\n\tID          Name                Department                       Mobile            Status ")
            print("\t============================================================================================\n")
            j=0; i=0
            for row in result:
                print("\t%-12d%-20s%-33s%-18d%-12s"%(row[0],row[1],row[2],row[3],row[4]))
                if(row[4] == 'pending'):
                    j+=1
                else:
                    i+=1
            print("\n\n\t\tPending case     : ",j) # Number of Pending Cases
            print("\t\tPermanent Doctor : ",i) # Number of Permanent Doctors
        except:
            print("\n\t\t\tOops! Unable to fetch the data.\n")

    def search_doctor(self):
        connect=self.mydb.cursor() # Encapsulating the cursor
        print("\n\n\n\n\n\n\t\t\t", end="")
                                        # DISPLAY
        print("|---------------- SEARCH DOCTOR APOLLO-HOSPITAL  ---------------|")
                                       # INPUT FIELDS
        self.__name = input("\n\n\t\t\t\t\tEnter Name : ")
        self.__id = input("\t\t\t\t\tEnter ID   : ")
        os.system('cls') # Clearing the previously Loaded Screen
        # EXCEPTION HANDLING
        try:
            connect.execute("select * from doctor where id='"+self.__id+"' and name='"+self.__name+"'") # MYSQL Query
            result=connect.fetchall() # Fetching data according to MYSQL Query
            print("\n\n\n\n\n\t\t\t", end="")
                                        # DISPLAY
            print("|----------------  APOLLO-HOSPITAL DOCTORS LIST  ---------------|")
            print("\n\n\tID          Name                Department                       Mobile            Status ")
            print("\t============================================================================================\n")
            for row in result:
                print("\t%-12d%-20s%-33s%-18d%-12s"%(row[0],row[1],row[2],row[3],row[4]))
                
        except:
            print("\n\t\t\t\tOops! Unable to fetch the data.\n")

    def remove_doctor(self):
        connect=self.mydb.cursor() # Encapsulating the cursor
        print("\n\n\n\n\n\n\t\t\t", end="")
                                        # DISPLAY
        print("|---------------- DELETE DOCTOR APOLLO-HOSPITAL  ---------------|")
                                        # INPUT FIELDS
        self.__id = input("\n\n\n\t\t\t\t\t\tEnter ID   : ")
        os.system('cls') # Clearing the previously Loaded Screen
        # EXCEPTION HANDLING
        try:
            connect.execute("select * from doctor where id='"+self.__id+"'") # MYSQL Query
            result=connect.fetchall() # Fetching the data according to the MYSQL Query
            print("\n\n\n\n\n\t\t\t", end="")
                                        # DISPLAY
            print("|----------------  APOLLO-HOSPITAL DOCTORS LIST  ---------------|")
            print("\n\n\tID          Name                Department                       Mobile            Status ")
            print("\t============================================================================================\n")
            for row in result:
                print("\t%-12d%-20s%-33s%-18d%-12s"%(row[0],row[1],row[2],row[3],row[4]))
            try:
                print("\n\n\t\t\t________________________________________________________")
                print   ("\t\t\t|                                                       |")
                print   ("\t\t\t|        Are you sure want to delete above data ?       |")
                print   ("\t\t\t|                                                       |")
                print   ("\t\t\t|              [YES]                [NO]                |")
                print   ("\t\t\t|_______________________________________________________|")
                                # INPUT FIELD
                ch = input("\n\t\t\tEnter your choice(y/n) : ")
                                # CONDITIONAL STATEMENT
                if(ch=="YES" or ch=="yes" or ch=="Y" or ch=="y"):
                    connect.execute("delete from doctor where id='"+self.__id+"'") # MYSQL Query to delete the data from database
                    self.mydb.commit() # Commiting to the database
                    print("\n\t\t\tCandidate removed Successfully.\n\n")
                else:
                    self.mydb.rollback() # Roll Back if the choice is NO
                    print("\n\t\t\tCandidate has not been removed...\n\n")
            except:
                self.mydb.rollback() # Roll Back if any error occurs
        except:
            print("\n\n\t\t\t\tOops! Unable to fetch the data.\n")

    def update_doctor_info(self):
        connect=self.mydb.cursor() # Encapsulating the cursor
        print("\n\n\n\n\n\n\t\t\t", end="")
                                        # DISPLAY
        print("|------------- UPDATE DOCTOR INFO APOLLO-HOSPITAL  -------------|")
                                        # INPUT FIELDS
        self.__name = input("\n\n\t\t\t\t\tEnter Name : ")
        self.__id = input("\t\t\t\t\tEnter ID   : ")
        os.system('cls') # Clearing the previously Loaded Screen
        # EXCEPTION HANDLING
        try:
            connect.execute("select * from doctor where id='"+self.__id+"' and name='"+self.__name+"'") # MYSQL Query
            result=connect.fetchall() # Fetching data according to the given MYSQL Query
            print("\n\n\n\n\n\t\t\t", end="")
                                        # DISPLAY
            print("|----------------  APOLLO-HOSPITAL DOCTORS LIST  ---------------|")
            print("\n\n\tID          Name                Department                       Mobile            Status ")
            print("\t============================================================================================\n")
            for row in result:
                print("\t%-12d%-20s%-33s%-18d%-12s"%(row[0],row[1],row[2],row[3],row[4]))                
            if(row != None):   
                print("\n\n\t\t\t\tChoose from below option to Update: \n")
                print("\n\t\t\t\t1.Update_ID             4.Update_Mobile")
                print("\t\t\t\t2.Update_Name           5.Update_Status")
                print("\t\t\t\t3.Update_Department     6.Update_All")
                                        # INPUT FIELD
                ch = int(input("\n\n\t\t\t\tEnter Your Choice : "))                
                if(ch == 1):
                    try:
                        self.__upid = input("\n\n\t\t\t\tEnter new ID : ")
                        connect.execute("update doctor set id='"+self.__upid+"' where id='"+self.__id+"'") # MYSQL Query
                        self.mydb.commit() # Commiting to the database
                        print("\n\t\t\tRecord Updated Succesfully...\n\n")
                    except:
                        self.mydb.rollback() # Roll Back if any error occurs
                        print("\n\t\t\tOops! Unable to update the data...\n")    
                elif(ch == 2):
                    try:
                        self.__upname = input("\n\n\t\t\t\tEnter new Name : ")
                        connect.execute("update doctor set name='"+self.__upname+"' where id='"+self.__id+"'") # MYSQL Query
                        self.mydb.commit() # Commiting to the database
                        print("\n\t\t\tRecord Updated Succesfully...\n\n")  
                    except:
                        self.mydb.rollback() # Roll Back if any error occurs
                        print("\n\t\t\tOops! Unable to update the data...\n")                       
                elif(ch == 3):
                    try:
                        self.__updpt = input("\n\n\t\t\t\tEnter new Department : ")
                        connect.execute("update doctor set department='"+self.__updpt+"' where id='"+self.__id+"'") # MYSQL Query
                        self.mydb.commit() # Commiting to the database
                        print("\n\t\t\tRecord Updated Succesfully...\n\n")
                    except:
                        self.mydb.rollback() # Roll Back if any error occurs
                        print("\n\t\t\tOops! Unable to update the data...\n")                       
                elif(ch == 4):
                    try:
                        self.__upphone = input("\n\n\t\t\t\tEnter new Mobile no : ")
                        connect.execute("update doctor set mobile='"+self.__upphone+"' where id='"+self.__id+"'") # MYSQL Query
                        self.mydb.commit() # Commiting to the database
                        print("\n\t\t\tRecord Updated Succesfully...\n\n")
                    except:
                        self.mydb.rollback() # Roll Back if any error occurs
                        print("\n\t\t\tOops! Unable to update the data...\n")                       
                elif(ch == 5):
                    try:
                        self.__upstatus = input("\n\n\t\t\t\tEnter new Status : ")
                        connect.execute("update doctor set status='"+self.__upstatus+"' where id='"+self.__id+"'") # MYSQL Query
                        self.mydb.commit() # Commiting to the database
                        print("\n\t\t\tRecord Updated Succesfully...\n\n")
                    except:
                        self.mydb.rollback() # Roll Back if any error occurs
                        print("\n\t\t\tOops! Unable to update the data...\n")                        
                elif(ch == 6):
                    try:
                        self.__upid = input("\n\t\t\t\tEnter new ID         : ")
                        self.__upname =input("\t\t\t\tEnter new Name       : ")
                        self.__updpt = input("\t\t\t\tEnter new Department : ")
                        self.__upphone = input("\t\t\t\tEnter new Mobile no  : ")
                        self.__upstatus = input("\t\t\t\tEnter new Status     : ")
                        #MYSQL Query
                        connect.execute("update doctor set id='"+self.__upid+"', name='"+self.__upname+"',department='"+self.__updpt+"',mobile='"+self.__upphone+"', status='"+self.__upstatus+"' where id='"+self.__id+"'")
                        self.mydb.commit() # Commiting to the database
                        print("\n\t\t\tRecord Updated Succesfully...\n\n")
                    except:
                        self.mydb.rollback() # Roll Back if any error occurs
                        print("\n\t\t\tOops! Unable to update the data...\n")
                else:
                    print("\n\t\t\tWrong choice entered, choose within 1 to 6..\n")
            else:
                print("\n\t\t\tNo Data Found to Update....\n\n")
        except:
            print("\n\t\t\tOops! Unable to fetch the data.\n")

    def doctor_application(self):
        connect=self.mydb.cursor() # Encapsulating the cursor
        # EXCEPTION HANDLING
        try:
            print("\n\n\n\n\n\n\t\t\t", end="")
                                    # DISPLAY
            print("|-------------- APPLY FOR JOB IN APOLLO-HOSPITAL  --------------|")
                                    # INPUT FIELDS
            self.__name = input("\n\n\t\t\t\t\tEnter Name       : ")
            self.__dpt = input("\t\t\t\t\tEnter Department : ")
            self.__phone = input("\t\t\t\t\tEnter Mobile no  : ")
            self.__status = "pending"

            connect.execute("Insert into doctor(name,department,mobile,status)"+
                       "values('"+self.__name+"','"+self.__dpt+"','"+self.__phone+"','"+self.__status+"')") # MYSQL Query
            self.mydb.commit() # Commiting to the database
            print("\n\n\t\t\t\tRecord Added Succesfully\n\n")
        except:
            self.mydb.rollback() # Roll Back if any error occurs
            print("\n\n\t\t\t\tOops! Unable to Record the data.\n")    

    def add_doctor(self):
        connect=self.mydb.cursor() # Encapsulating the cursor
        # EXCEPTION HANDLING
        try:
            print("\n\n\n\n\n\n\t\t\t", end="")
                                            # DISPLAY
            print("|---------------- ADD DOCTOR IN APOLLO-HOSPITAL  ----------------|")
                                        # INPUT FIELDS
            self.__name = input("\n\n\t\t\t\t\tEnter Name       : ")
            self.__dpt = input("\t\t\t\t\tEnter Department : ")
            self.__phone = input("\t\t\t\t\tEnter Mobile no  : ")
            self.__status = input("\t\t\t\t\tEnter Status     : ")
            
            connect.execute("Insert into doctor(name,department,mobile,status)"+
                       "values('"+self.__name+"','"+self.__dpt+"','"+self.__phone+"','"+self.__status+"')") # MYSQL Query
            self.mydb.commit() # Commiting to the database
            print("\n\n\t\t\t\tRecord Added Succesfully\n\n")
        except:
            self.mydb.rollback() # Roll Back if any error occurs
            print("\n\t\t\t\tOops! Unable to Record the data.\n")    




# =============================================================================
#                                  Driver part
# =============================================================================
while(True):
    d = Doctor()
    p = Patient()
    os.system('cls') # Clearing the previously Loaded Screen
    print("\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t", end="")
                                    # DISPLAY
    print("|----------------   WELCOME TO APOLLO-HOSPITAL   ---------------|")
    time.sleep(3) # TIME INTERVAL OF 3 SECONDS
    os.system('cls') # Clearing the previously Loaded Screen
    r = d.sign_in()
    os.system('cls') # Clearing the previously Loaded Screen
    while(True):
        
        if(r == "Right"):
            print("\n\n\n\n\n\n\t\t\t", end="")
                                        # DISPLAY
            print("|----------------   WELCOME TO APOLLO-HOSPITAL   ---------------|")
                                        # INPUT FIELDS
            print("\n\n\n\n\n\t\t\t\t\tChoose From Below :\n")
            print("\n\t\t\t\t\t1. Doctor")
            print("\t\t\t\t\t2. Patient")
            print("\t\t\t\t\t3. Exit")
            ch = int(input("\n\n\t\t\t\t\tEnter your choice : "))
            os.system('cls') # Clearing the previously Loaded Screen
            if ch == 1:
                while(True):
                    os.system('cls') # Clearing the previously Loaded Screen
                    print("\n\n\n\n\n\n\t\t\t", end="")
                                                    # DISPLAY
                    print("|----------------   WELCOME TO APOLLO-HOSPITAL   ---------------|")
                                                # INPUT FIELDS
                    print("\n\n\n\n\n\t\t\t\tChoose From Below :\n")
                    print("\n\t\t\t\t1. View All Doctor           2. Search Doctor")
                    print("\t\t\t\t3. Remove Doctor             4. Update Doctor")
                    print("\t\t\t\t5. Add Doctor                6. Apply for Job")
                    print("\t\t\t\t7. Main menu")
                        
                    dch = int(input("\n\n\t\t\t\tEnter your choice : "))
                    os.system('cls') # Clearing the previously Loaded Screen
                    if dch == 1:
                        d.display_doctors()
                    elif dch ==2:
                        d.search_doctor()
                    elif dch ==3:
                        rd = d.sign_in()
                        if rd == "Right":
                            os.system('cls') # Clearing the previously Loaded Screen
                            d.remove_doctor()
                        else:
                            print("\n\n\t\t\t\tWrong password entered...\n")
                    elif dch ==4:
                        d.update_doctor_info()
                    elif dch ==5:
                        d.add_doctor()
                    elif dch ==6:
                        d.doctor_application()
                    elif dch ==7:
                        break
                    else:
                        print("\n\n\n\n\n\t\t\t\tYou have entered wrong choice...\n")
                    choice = input("\n\nEnter any key to \'Go Back\' = ")
                    
            elif ch ==2:
                while(True):
                    os.system('cls') # Clearing the previously Loaded Screen
                    print("\n\n\n\n\n\n\t\t\t", end="")
                                                    # DISPLAY
                    print("|----------------   WELCOME TO APOLLO-HOSPITAL   ---------------|")
                                                    # INPUT FIELDS
                    print("\n\n\n\n\n\t\t\t\tChoose From Below :\n")
                    print("\n\t\t\t\t1. View All Patient           2. Search Patient")
                    print("\t\t\t\t3. Patient Appointment        4. Update Patient")
                    print("\t\t\t\t5. Invoice                    6. Main Menu")
                    
                    pch = int(input("\n\n\t\t\t\tEnter your choice : "))
                    os.system('cls') # Clearing the previously Loaded Screen
                    if pch == 1:
                        p.display_patient()
                    elif pch ==2 :
                        p.search_patient()
                    elif pch ==3:
                        p.patient_appointment()
                    elif pch ==4:
                        p.update_patient_info()
                    elif pch ==5:
                        p.generate_invoice()
                    elif pch ==6:
                        break
                    else:
                        print("\n\n\n\n\n\t\t\t\tYou have entered wrong choice...")
                    choice = input("\n\nEnter any key to \'Go Back\' = ")
            elif ch ==3:
                sys.exit() # Exit the Python Application
            else:
                print("\n\n\n\n\n\n\t\t\t\t\tYou have entered wrong choice...")
                time.sleep(3) # TIME INTERVAL OF 3 SECONDS
                os.system('cls') # Clearing the previously Loaded Screen
        
        else:
            print("\n\n\n\n\t\t\tEither password or username is wrong....")
            sys.exit() # Exit the Python Application