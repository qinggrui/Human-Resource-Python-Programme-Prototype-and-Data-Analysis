import datetime
import csv
import random
from csv import writer
import string
from datetime import datetime

# START OF PROGRAM


def pythonSales():  # Starts the program
    user = 0
    while True:
        try:  # Direct to user functions, onboarding or hr login
            user = int(input("Welcome to our employee management system. To proceed, please select between 1-10:\n1)To begin new employee registration and onboarding tasks\n2)To access admin accounts and privileges\n3)To view and edit your own current employee data\n4)To manage your salary and allowance\n5)To request for either a leave or a claim\n6)To file a complaint against a department or another employee\n7)To view company rules and regulations\n8)To provide feedback and comments for our company\n9)To view the status of your leave or claim\n10)To declare the amount of sales you made or check if you are eligible for bonus depending on company's performance\nInput: "))
            if (user == 1):
                print("test")
                onboarding()
                break
            elif (user == 2):
                hrLogin()
                break
            elif (user == 3):
                empLogin()
                break
            elif (user == 4):
                salaryAllowanceSystem()
                break
            elif (user == 5):
                leaveSystem()
                break
            elif (user == 6):
                complaints()
                break
            elif (user == 7):
                regulations()
                break
            elif (user == 8):
                feedback()
                break
            elif (user == 9):
                viewLeaveClaimStatus()
            elif (user == 10):
                viewSales()
                break
            else:
                print("Please enter a valid input between 1-8")
        except:
            print("Error. Invalid input. ")
    return None


def hrLogin():  # Function for only hr employees to login.
    hrUsername = input(
        "Please enter the username of your HR personnel account: ")
    hrPassword = input(
        "Please enter the password of your HR personnel account: ")
    with open('HRaccount.csv', 'r') as hrAcc:
        next(hrAcc)
        csv_reader = csv.reader(hrAcc)
        for row in csv_reader:
            if row[0] == hrUsername and row[1] == hrPassword:
                print("Login successful")
                loginFunc = int(input("What would you like to do? \nTo view employee data, press 1.\nTo edit employee data, press 2.\nTo add extra onboarding quizzes for employees, press 3.\nTo rank the performance of employees, press 4.\nTo approve employees' leaves and claims, press 5: \nInput: "))
                if(loginFunc == 1):
                    viewEmployeeData()
                elif(loginFunc == 2):
                    editEmployeeData()
                elif(loginFunc == 3):
                    writeQuiz()
                elif(loginFunc == 4):
                    rankPerformance()
                elif(loginFunc == 5):
                    approveLeaveClaim()
                else:
                    print("Error")
                break
            else:
                print("Invalid username or password. Please try again")
                break
    return None


def empLogin():
    empUsername = input("Please enter your employee ID: ")
    empPassword = input("Please enter your password: ")
    with open('EmployeeInfo.csv', 'r') as empAcc:
        next(empAcc)
        csv_reader = csv.reader(empAcc)
        for row in csv_reader:
            if row[0] == empUsername and row[1] == empPassword:
                print("Login successful")
                editSelfData(row[0])
                break
            else:
                print("Invalid username or password. Please try again")
                break
    return None


def onboarding():  # Starts onboarding process to sign up a new employee
    print("Please fill up the following information")
    address = input("Address: ")
    name1 = input("Name: ")
    name=name1.upper()
    ic = input("IC: ")
    contact = None

    while True:
        try:
            contact = int(input("Contact No.: "))
            break
        except:
            print(
                "{contactNo} is not a valid input, please enter numbers only".format(contactNo=contact))

    while True:
        try:
            date = datetime.strptime(
                input("Date joined (Date format is DD-MM-YYYY): "), '%d-%m-%Y')
            break
        except:
            print("Incorrect date format, should be DD-MM-YYYY")

    while True:
        try:
            genderUser = int(
                input("Gender(1 for male, 2 for female, 3 to prefer not to say): "))
            if genderUser == 1:
                gender = ("male")
                break
            elif genderUser == 2:
                gender = ("female")
                break
            elif genderUser == 3:
                gender = ("Prefer not to say")
                break
            else:
                print("Error. Please enter a number between 1-3")
        except:
            print("Invalid input. Please enter 1,2 or 3")

    citizenship1 = input("Citizenship (eg. Singaporean): ")
    citizenship=citizenship1.upper()
    while True:
        try:
            contractType = int(input(
                "Contract type\nEnter 1 if local\nEnter 2 if expat\nInput: "))
            if contractType in (1, 2):
                break
            print("Invalid contract type entered")
        except:
            print("Invalid input. Please enter 1 or 2 for your contract type")
    print("Thank you. We will now proceed with account creation. Please enter the following information")

    while True:
        try:
            jobGrade = int(input("Please enter your Job Grade (Choose 1-4)\n1: Manager(Sales)\n2:Manager(Admin) \n3:Sales Representative/Associate/Analyst/Consultant\n4:IT/Admin support Representative/Associate/Analyst/Consultant\nInput:"))
            if jobGrade in (1, 2, 3, 4):
                break
            print("Invalid job type entered")
        except:
            print("Invalid input. Please enter a valid job type")

    while True:
        try:
            department = int(input(
                "What is your department?\n1 for Sales\n2 for Admin\n3 for IT\nInput: "))
            if department in (1, 2, 3):
                break
            print("Invalid department entered. Please enter a valid department.")
        except:
            print("Invalid input. Please enter a valid number.")
    username = input("Please enter your username: ")
    employeeID = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=8))  # Generates 8 random characters for EmployeeID
    print("Your Employee ID is: {employeeID}".format(
        employeeID=employeeID))
    print("Your account has been created")
    employeePW = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=10))  # Generates 10 random characters for Password
    print("Your password is: {employeePW}".format(employeePW=employeePW))
    if(department == 1):
        print("Based on your department, our company will provide you with a laptop and a phone.")
    elif(department == 2):
        print("Based on your department, our company will provide you with a laptop.")
    else:
        print(
            "Based on your department, our company will provide you with a desktop and a laptop.")

    while True:  # Employee Skills
        try:
            knowledgeIT = int(input(
                "Please enter your level of IT knowledge, where 1 is low, 2 is average and 3 is high: "))
            if knowledgeIT in (1, 2, 3):
                break
            print("Invalid value. Please input a valid value between 1-3")
        except:
            print("Invalid input. Please enter a valid value between 1-3")

    languages = ["English", "Chinese", "Malay",
                 "Tamil"]  # Language proficiency section
    languageProf = [0, 0, 0, 0]
    while True:
        try:
            confirmLang = input("Aside from the following languages {languages}, do you have any other languages that you are proficient in? Y/N: ".format(
                languages=languages))
            if confirmLang in ("Y", "y", "Yes", "YES", "yes"):
                addLang = input(
                    "Please enter the language that you are proficient in: ")
                languages.append(addLang)
                languageProf.append(0)
            elif confirmLang in ("N", "n", "No", "NO", "no"):
                print("The languages that you are proficient in are as follows: {languages}".format(
                    languages=languages))
                break
            else:
                print("Unconfirmed input. Please enter a valid response.")
        except:
            print("Invalid input. Please enter a valid response.")

    loopController = 0  # Loop to enter proficiency of each language
    while loopController < len(languages):
        try:
            proficiencyLevel = int(input("Please enter your language proficiency for {languages} (0 for do not speak, 1 for poor, 2 for good, 3 for excellent): ".format(
                languages=languages[loopController])))
            if proficiencyLevel in (0, 1, 2, 3):
                languageProf[loopController] = proficiencyLevel
            else:
                print("Invalid number. Please enter a number between 0-3")
            loopController = loopController+1
        except:
            print("Invalid input. Please enter a proper input.")
    while True:  # Loop for years of experience
        try:
            yearsOfExperience = int(
                input("How many years of experience do you have?: "))
            if yearsOfExperience in range(0, 71):
                break
            else:
                print("Invalid. Please enter a valid input from 0-70")
        except:
            print("Invalid input. Please enter a valid input from 0-70")
    print("You will now be directed to understand the rules and regulations of our company. Please carefully read and understand the rules and regulations of our company.")
    regulations()
    print("In order to continue with your onboarding task, please complete the quiz. You must get 8 out of 10 questions correctly, and if you fail you may retry the quiz.")
    rulesQuiz()
    employeeInfo = [employeeID, employeePW, name, gender, department, ic, username, jobGrade, contractType,
                    knowledgeIT, yearsOfExperience, languages, languageProf, contact, address, date, citizenship]
    # Writes employee information from the list into the csv
    print("Creating employee data....")
    with open('EmployeeInfo.csv', 'a+', newline='') as employeecsv:
        csv_writer = writer(employeecsv)
        csv_writer.writerow(employeeInfo)
        employeecsv.close()
    # Opens an empty row in EmployeeKPI to be adjusted and edited later on
    kpiInfo = [employeeID, 0, 0, 0, 0, 0, False, ""]
    with open('EmployeeKPI.csv', 'a+', newline='') as employeeKPI:
        # kpi_writer = writer(employeeKPI)  # If unused, just delete
        csv_writer = writer(employeeKPI)
        csv_writer.writerow(kpiInfo)
        employeeKPI.close()
    # Opens a row in EmployeeLeaveClaim with base days of leave and emloyee claim. Can be adjusted based on their job grade
    leaveDays = 12
    claimBonus = 3000
    if jobGrade in (1, 2):
        leaveDays = 16
        claimBonus = 4000
    leaveClaimInfo = [employeeID, leaveDays, 0, 0, 0, 0, claimBonus, 0, 0, 0]
    with open('EmployeeLeaveClaim.csv', 'a+', newline='') as leaveClaim:
        csv_writer = writer(leaveClaim)
        csv_writer.writerow(leaveClaimInfo)
        leaveClaim.close()
    # For employee's sales and bonuses.
    salesInfo = [employeeID, jobGrade, 0, 0, 0]
    with open('EmployeeSales.csv', 'a+', newline='') as salesWrite:
        csv_writer = writer(salesWrite)
        csv_writer.writerow(salesInfo)
        salesWrite.close()
    # Manage the salary of the employees.
    salary, allowance = 3000, 3000
    if yearsOfExperience > 10:
        salary = 4500
        allowance = 5000
    salaryInfo = [employeeID, contractType, salary, 0, 0, allowance, 0, 0]
    with open('EmployeeSalary.csv', 'a+', newline='') as SalaryManager:
        csv_writer = writer(SalaryManager)
        csv_writer.writerow(salaryInfo)
        SalaryManager.close()
    print("Your account has been created for the company's website.\n")
    print("Your onboarding task is now complete. Thank you.")
    return None


def regulations():
    print("Here are the rules and regulations of our company")
    while True:
        try:
            viewRules = int(input(
                "What rules would you like to read?\n1)Category one rules\n2)Category two rules\n3)Leave entitlement and types of leave\nPress 9 to leave \nInput: "))
            if viewRules == 1:
                with open('categoryOneRules.csv', 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        print(line[0])
            elif viewRules == 2:
                with open('categoryTwoRules.csv', 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        print(line[0])
            elif viewRules == 3:
                with open('categoryLeave.csv', 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        print(line[0])
            elif viewRules == 9:
                print("Thank you for reading the rules and regulations of our company.")
                break
            else:
                print("Invalid input. Please enter a valid input")
        except:
            print("Invalid input. Please enter a number.")
    return None


def rulesQuiz():  # Retrieve list of questions from csv files to quiz the employees
    print("The quiz will now be conducted. Answer the following TRUE or FALSE questions as best as you can. If you scored less than 8 out of 10, the quiz will be repeated. Good luck!")
    with open('rules.csv', 'r') as rules:
        csv_reader = csv.reader(rules, delimiter=',')
        csvr = list(csv_reader)  # Pass the reader into a list
        row_count = len(csvr)
        # Create index of questions in a list
        qstList = list(range(2, row_count))
        # Shuffle the list to randomly generate an index of questions
        random.shuffle(qstList)
        question, correct = 0, 0
        while question < 10:
            question = question+1
            print("You are currently on question number {question} ".format(
                question=question))
            print("What is the answer to the following question?")
            ans = input(csvr[qstList[question]][0]+": ")
            if(ans.upper() == csvr[qstList[question]][1]):
                print("Correct")
                correct = correct+1
            else:
                print("Incorrect")
        if correct < 8:
            print("You have failed the quiz. Please retry the quiz")
            regulations()
            rulesQuiz()
        else:
            print("Congratulations, you have succeeded")
    return None


def writeQuiz():  # Create quiz questions for onboarding quiz
    with open('rules.csv', 'a+', newline='') as quiz:
        csv_writer = writer(quiz)
        question = input("Please enter the question: ")
        answer = input("Please enter the answer: ")
        List = [question, answer]
        csv_writer.writerow(List)
        quiz.close()
    return None


def viewEmployeeData():  # Function to view important data of employee
    with open('EmployeeInfo.csv', 'r') as csvfile:
        next(csvfile)
        csv_reader = csv.reader(csvfile)
        indexctr = 0
        empIdNum1 = input("Please enter the employee ID that you would like to view: ")
        empIdNum=empIdNum1.upper()
        for line in csv_reader:
            if(line[0] in (empIdNum)):
                print("Employee Index number: {indexctr}".format(
                indexctr=indexctr))
                print("Employee ID: {employeeID}".format(employeeID=line[0]))
                print("Employee name: {employeename}".format(employeename=line[2]))
                print("Employee NRIC: {nric}".format(nric=line[5]))
                print("Employee Contact No.: {contact}".format(contact=line[13]))
                print("Employee citizenship: {citizenship}".format(
                citizenship=line[16]))
                print("Employee joined since: {date}".format(
                date=line[15]))
    return None


def editSelfData(empID):  # edit self data for employees
    readfile = open('EmployeeInfo.csv', 'r')
    reader = csv.reader(readfile)
    mylist = list(reader)
    readfile.close
    for row in mylist:
        if empID in row:
            print("Your current employeeID is: {empID}\nYour current name is: {name}\nYour current IC is: {ic}\nYour current address is: {address}\nYour current contact number is: {contact}\nYour current account password is: {pw}".format(
                empID=row[0], address=row[14], ic=row[5], contact=row[13], name=row[2], pw=row[1]))
            choiceEdit = int(
                input("What would you like to edit? \nPress 1 to edit your name\nPress 2 to edit your IC\nPress 3 to edit your address\nPress 4 to edit your contact number\nPress 5 to change your current password: \nInput:  "))
            if choiceEdit == 1:
                editname = input("Please enter your new name: ")
                row[2] = editname.upper()
            elif choiceEdit == 2:
                row[5] = input("Please enter your new ic: ")
            elif choiceEdit == 3:
                row[14] = input("Please enter your new address: ")
            elif choiceEdit == 4:
                row[13] = input("Please enter your new contact number: ")
            elif choiceEdit == 5:
                row[1] = input("Please enter your new password: ")
            else:
                print("Error. Please enter a valid input")
    writefile = open('EmployeeInfo.csv', 'w', newline='')
    csv_writer = csv.writer(writefile)
    csv_writer.writerows(mylist)
    writefile.close()
    return None


def editEmployeeData():  # Function to rewrite the data of employeeinfo.csv with updated fields
    print("Please choose an employee to edit their data")
    readfile = open('EmployeeInfo.csv', 'r')
    reader = csv.reader(readfile)
    mylist = list(reader)
    readfile.close
    while True:
            empIndex = int(
                input("Please enter the index of the employee that you would like to edit: "))
            empInfo = int(input(
                "Please choose which information of the employee that you would like to edit (0-16): \n0)Employee ID \n1)Employee Password \n2)Name \n3)Gender \n4)department \n5)IC \n6)username \n7)Job Grade \n8)Contract Type \n9)IT knowledge \n10)Years of Experience \n11)Languages \n12)Language knowledge \n13)Contact \n14)Address \n15)Date \n16)Citizenship \nInput: "))
            print("The info that you would like to edit is {info}".format(
                info=mylist[empIndex][empInfo]))
            if empInfo in (7, 8, 9, 10, 13):
                empEdit = int(
                    input("Please enter the new value that you would like to change it to: "))
                mylist[empIndex][empInfo] = empEdit
                
            elif empInfo in (0, 1, 2, 3, 4, 5, 6, 11, 12, 14, 15, 16):
                empEdit = input(
                    "Please enter the new value that you would like to change it to: ")
                mylist[empIndex][empInfo] = empEdit
        
            else:
                print("Error. Invalid input")
            break
    mylist[empIndex][empInfo] = empEdit
    writefile = open('EmployeeInfo.csv', 'w', newline='')
    csv_writer = csv.writer(writefile)
    csv_writer.writerows(mylist)
    writefile.close()

    return None


def rankPerformance():  # Function to edit employee KPI. Only accessible from HR/admin account

    readfile = open('EmployeeKPI.csv', 'r')
    reader = csv.reader(readfile)
    mylist = list(reader)
    readfile.close

    kpiInfo = [0, 0, 0, 0, 0, 0, 0, False, ""]
    while True:
        try:
            empIndex = int(input(
                "Please enter the index of the employee that you would like to edit his ratings: "))
            kpiInfo[1] = int(
                input("Please enter the Attendance rating of your selected employee(1-5): "))
            kpiInfo[2] = int(
                input("Please enter the Work Attitude rating of your selected employee(1-5): "))
            kpiInfo[3] = int(input(
                "Please enter the Co-worker evaluation rating of your selected employee(1-5): "))
            kpiInfo[4] = int(
                input("Please enter the Innovation of your selected employee(1-5): "))
            kpiInfo[5] = int(
                input("Please enter the Quality of work of your selected employee(1-5): "))
            kpiInfo[6] = (kpiInfo[5]+kpiInfo[1] +
                          kpiInfo[2]+kpiInfo[3]+kpiInfo[4])/5
            kpiInfo[6] = round(kpiInfo[6], 2)
            break
        except:
            print("Invalid input")
    comments = input("What comments do you have for this employee?")
    kpiInfo[8] = comments
    if int((kpiInfo[6])) > 4.5:
        kpiInfo[7] = True
        print("This employee has a KPI of above 4.5, and has performed well. He will be suggested for a promotion")
    print("Your kpi score average is {sc}".format(sc=kpiInfo[6]))
    kpiInfo[0] = mylist[empIndex][0]
    mylist[empIndex] = kpiInfo
    writefile = open('EmployeeKPI.csv', 'w', newline='')
    csv_writer = csv.writer(writefile)
    csv_writer.writerows(mylist)

    return None


def approveLeaveClaim():  # Function to approve the leave/claim status of pending requests. Only for HR/ADMIN
    readfile = open('EmployeeLeaveClaim.csv', 'r')
    reader = csv.reader(readfile)
    mylist = list(reader)
    readfile.close
    for row in mylist:
        if(row[5] == ("Pending")):
            print("Employee {empid} has requested for a leave of {dur} day(s) starting from {dte} for \"{rsn}\" reasons".format(
                empid=row[0], dur=row[2], dte=row[3], rsn=row[4]))
            while True:
                try:
                    adminChoice = int(input(
                        "Would you like to approve of this employee's leave? To approve, press 1. To save for later, press 2. To Deny, press 3: "))
                    if adminChoice in (1, 2, 3):
                        break
                    else:
                        print("Error. Please enter a value between 1-3")
                except:
                    print("Invalid input. Please enter a valid input")
            if adminChoice == 1:
                row[5] = ("Approved")
            elif adminChoice == 2:
                pass
            elif adminChoice == 3:
                row[5] = ("Rejected")
        if(row[9] == ("Pending")):
            print("Employee {empid} has request for a claim of {clm} for \"{rsn}\" reasons".format(
                empid=row[0], clm=row[7], rsn=row[8]))
            while True:
                try:
                    adminChoice = int(input(
                        "Would you like to approve of this employee's claim? To approve, press 1. To save for later, press 2. To Deny, press 3: "))
                    if adminChoice in (1, 2, 3):
                        break
                    else:
                        print("Error. Please enter a value between 1-3")
                except:
                    print("Invalid input. Please enter a valid input")
            if adminChoice == 1:
                row[9] = ("Approved")
            elif adminChoice == 2:
                pass
            elif adminChoice == 3:
                row[9] = ("Rejected")
        if(row[5] in ("Approved", "Rejected")):
            print("Employee {empid} has requested for a leave of {dur} day(s) starting from {dte} for \"{rsn}\" reasons. The request status is: {status}".format(
                empid=row[0], dur=row[2], dte=row[3], rsn=row[4], status=row[5]))
        if(row[9] in ("Approved", "Rejected")):
            print("Employee {empid} has request for a claim of {clm} for \"{rsn}\" reasons. The status of this request is: {status}".format(
                empid=row[0], clm=row[7], rsn=row[8], status=row[9]))
    writefile = open('EmployeeLeaveClaim.csv', 'w', newline='')
    csv_writer = csv.writer(writefile)
    csv_writer.writerows(mylist)
    return None


def viewLeaveClaimStatus():
   readfile = open('EmployeeLeaveClaim.csv', 'r')
   reader = csv.reader(readfile)
   mylist = list(reader)
   readfile.close
   empIdNum1 = input("Please enter the employee ID that you would like to view: ")
   empIdNum=empIdNum1.upper()
   for row in mylist:
        if(row[0] in (empIdNum)):
            print("Employee {empid} has requested for a leave of {dur} day(s) starting from {dte} for \"{rsn}\" reasons. The request status is: {status}".format(
                empid=[empIdNum], dur=row[2], dte=row[3], rsn=row[4], status=row[5]))
        if(row[0] in (empIdNum)):
            print("Employee {empid} has request for a claim of {clm} for \"{rsn}\" reasons. The status of this request is: {status}".format(
                empid=[empIdNum], clm=row[7], rsn=row[8], status=row[9]))


def viewSales():
    readfile = open('EmployeeSales.csv', 'r')
    reader = csv.reader(readfile)
    mylist = list(reader)
    readfile.close
    empID = input("Please enter your employeeID: ")
    for row in mylist:
        if(empID in row[0]):
            if(int(row[1]) in (1, 3)):
                while True:
                    try:
                        salesMade = int(
                            input("You are part of the sales, so you will earn commission based on your sales\n Please enter the sales that you have achieved this month (inSGD$)): "))
                        comissionEarned = salesMade*0.05
                        print("You have made a commission of {com:.02f}".format(
                            com=comissionEarned))
                        row[2] = salesMade
                        row[3] = comissionEarned
                        break
                    except:
                        print("Invalid input. Please try again.")
            elif(int(row[1]) in (2, 4)):
                while True:
                    try:
                        companyPerfm = int(1000000)
                        if companyPerfm >= 1000000:
                            bonusEarned = companyPerfm*0.0005  # 1mil * 0.05% = 1mil * 0.00005
                            print("The company has successfully reached their quota. You have made a bonus of {bns}".format(
                                bns=bonusEarned))
                            row[4] = bonusEarned
                            break
                        else:
                            bonusEarned = 0
                            print(
                                "Unfortunately the company did not perform well. You did not earn any bonuses.")
                            row[4] = bonusEarned
                            break
                    except:
                        print("Invalid input. Please try again.")
    writefile = open('EmployeeSales.csv', 'w', newline='')
    csv_writer = csv.writer(writefile)
    csv_writer.writerows(mylist)
    return None


def leaveSystem():

    readfile = open('EmployeeLeaveClaim.csv', 'r')
    reader = csv.reader(readfile)
    mylist = list(reader)
    readfile.close
    empID = input("Please enter your employeeID: ")
    for oneD in mylist:
        if(empID in oneD):
            while True:
                try:
                    empChoice = int(
                        input("What would you like to apply for?\n1)Leave\n2)Claim\nInput: "))
                    if empChoice == 1:
                        empLeaveRequest = int(input(
                            "How many days of leave would you like to request for? You have {days} days of leave left: ".format(days=oneD[1])))
                        if empLeaveRequest > 5 and empLeaveRequest < 7:
                            empLeaveRequest = empLeaveRequest-2
                        elif empLeaveRequest > 6:
                            empLeaveRequest = empLeaveRequest-4
                        if empLeaveRequest > int(oneD[1]) or empLeaveRequest > 14:
                            print(
                                "Error. Please enter number of days that do not exceed your amount of remaining days left or select days not longer than 10 days at once.(Weekends are not counted)")
                            break
                        else:
                            oneD[2] = empLeaveRequest
                            oneD[4] = input(
                                "Please submit the reason for your leave. Your leave will be reviewed and approved once it is accepted: ")
                            oneD[1] = int(oneD[1])-empLeaveRequest
                            while True:
                                try:
                                    oneD[3] = datetime.strptime(
                                        input("Leave start date (Date format is DD-MM-YYYY): "), '%d-%m-%Y')
                                    break
                                except:
                                    print(
                                        "Incorrect date format, should be DD-MM-YYYY")
                            oneD[5] = ("Pending")
                            break
                    elif empChoice == 2:
                        empClaimRequest = int(input(
                            "How much claim would you like to receive? You have {claim} in claims left: ".format(claim=oneD[6])))
                        if empClaimRequest > int(oneD[6]):
                            print(
                                "Invalid input. You do not have that much to claim.")
                            break
                        else:
                            oneD[6] = int(oneD[6])-empClaimRequest
                            oneD[7] = empClaimRequest
                            oneD[8] = input(
                                "Please enter the purpose of your claim. It will be reviewed and approved once it is accepted: ")
                            oneD[9] = ("Pending")
                            break
                    else:
                        print("Invalid input. Please enter 1 or 2")
                        break
                except:
                    print("Invalid input. Please try again222 ")
    writefile = open('EmployeeLeaveClaim.csv', 'w', newline='')
    csv_writer = csv.writer(writefile)
    csv_writer.writerows(mylist)
    return None


def salaryAllowanceSystem():
    readfile = open('EmployeeSalary.csv', 'r')
    reader = csv.reader(readfile)
    mylist = list(reader)
    readfile.close
    empID = input("Please enter your employeeID: ").upper()
    with open('EmployeeSalary.csv', 'r') as empAcc:
        next(empAcc)
        csv_reader = csv.reader(empAcc)
        authen = False
        for row in mylist:
            if (row[0] == empID and row[1] == "2"):
                print("Login successful")
                authen = True
                break
            
        if authen == False:
                print("Your employee ID is either not recognized or you are not under the expat contract. Please contact HR if you think this is an error. ")
            
        for row in mylist:
            if row[0] == empID and row[1] == "2":
                try:
                    userInput = int(input(
                "Please enter your function. \n1)For salary conversion\n2)For allowance management: \nInput: "))
                    for row in mylist:                    
                        if userInput in (1, 2):
                            break
                    else:
                        print("Error. Please enter either 1 or 2.")
                except:
                    print("Invalid input. Please try again.")
                if userInput == 1:
                    for i in mylist:
                            if(empID in i):
                                print("Your current salary allocation is: \nSGD: {sgd} \nUSD: {usd} \nMYR: {myr}".format(
                                    sgd=i[2], usd=i[3], myr=i[4]))
                                while True:
                                    try:
                                        amountSwap = int(
                                            input("Please enter the amount of currency that you would like to convert: "))
                                        if amountSwap <= int(i[2]):
                                            print("{amount}SGD of your salary will now be converted".format(amount=amountSwap))
                                            break
                                        else:
                                            print("Invalid value. Please enter a value within your salary range: {salary}".format(salary=i[2]))
                                    except:
                                        print("Invalid input. Please enter a valid input")
                                i[2] = int(i[2])-amountSwap
                                while True:
                                    try:
                                        conv = int(input(
                                            "Please enter the conversion that you would like to process: \n1) SGD to USD(1:0.75)\n2) SGD to MYR(1:3.05)\nInput: "))
                                        if conv == 1:
                                            print("Your amount of SGD: {amount} will now be converted to USD:{usd:0.2f}".format(
                                amount=amountSwap, usd=amountSwap*0.75))
                                            i[3] = amountSwap*0.75
                                            break
                                        elif conv == 2:
                                            print("Your amount of SGD: {amount} will now be converted to MYR{myr:0.2f}".format(
                                amount=amountSwap, myr=amountSwap*3.05))
                                            i[4] = amountSwap*3.05
                                            break
                                        else:
                                            print("Error. Please enter 1 or 2")
                                    except:
                                        print("Error. Please enter a valid input")
                
                elif userInput == 2:
                    for j in mylist:
                        if empID in j:
                            while True:
                                try:
                                    allowAlloc = int(input(
                                        "Your current allowance is SGD{allow}. How much of your allowance would you like to allocate?: ".format(allow=j[5])))
                                    if(allowAlloc <= int(j[5])):
                                        print("Your current allowance of SGD{allow} will now be allocated.".format(
                                allow=allowAlloc))
                                        break
                                    else:
                                        print("Error. Please enter an amount lesser than SGD{allow}".format(
                                allow=allowAlloc))
                                except:
                                    print("Error. Please enter a valid input")
                            j[5] = int(j[5])-allowAlloc
                            while True:
                                try:
                                    allocSegment = int(input(
                            "What would you like to allocate it to?\n1)To allocate towards housing allowance\n2)To allocate it towards schooling allowance: "))
                                    if allocSegment == 1:
                                        j[6] = int(j[6])+allowAlloc
                                        break
                                    elif allocSegment == 2:
                                        j[7] = int(j[7])+allowAlloc
                                        break
                                    else:
                                        print("Error. Please enter 1 or 2")
                                except:
                                    print("Error. Please enter a valid input")
                                break
           

    writefile = open('EmployeeSalary.csv', 'w', newline='')
    csv_writer = csv.writer(writefile)
    csv_writer.writerows(mylist)
    return None


def complaints():
    while True:
        try:
            complaintCateg = int(input(
                "What would you like to complain about?\nEnter 1 to submit a complaint about an employee\nEnter 2 to submit a complaint about a department:\nInput: "))
            if complaintCateg in (1, 2):
                break
            else:
                print("Error. Please enter either 1 or 2")
        except:
            print("Invalid input. Please enter a valid input")
    if complaintCateg == 1:
        complaintTarget = input(
            "Please enter the name of the employee or the ID of the employee: ")
        complaintComment = input(
            "Please enter the complaint that you have against that employee: ")
    elif complaintCateg == 2:
        complaintTarget = input(
            "Please enter the department that you would like to file a complaint against: ")
        complaintComment = input(
            "Please enter the complaint that you have against that department: ")
    print("Input received. We will review your complaints and action will be taken based on our investigation. Thank you.")
    complaintInfo = [complaintCateg, complaintTarget, complaintComment]
    writefile = open('Complaints.csv', 'a+', newline='')
    csv_writer = csv.writer(writefile)
    csv_writer.writerow(complaintInfo)
    return None


def feedback():
    writefile = open ('Feedback.csv', 'a+', newline='')
    csv_writer = csv.writer(writefile)
    anon_id =  input (str("Do you wish to remain anonymous? Please enter 'Yes' or 'Y' or 'No' or 'N': ")).upper()
    while anon_id== "YES" or anon_id== "Y":
        name_type= "Anonymous"
        break
    else:
        name_type=input("Please enter your employee ID: ")
    feedbackTopic = input ("Please enter the feedback you have for the company: ")
    feedbackSuggest = input("Please provide a suggestion for improvement: ")
    feedbackInfo = [anon_id, name_type, feedbackTopic, feedbackSuggest]
    csv_writer.writerow (feedbackInfo)
    
    return None

pythonSales()
