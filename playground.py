#with open("user.txt","r") as user:
#    rd = user.readlines()
#    for columns in rd:
#        print(columns.rstrip(",").rstrip("\n"))

#Adminkey=False

#def search():
#   while True:
#      category = input("[T-Tenant\n[A-Apartment\n[P-Transaction\n[L-Leave\nChoose a category:")
#      if category in ["T","t":
#         tenantsearch()
#      elif category in  ["A","a":
#         searchbox()
#      elif category in  ["P","p":
#         transactionsearch()
#      elif category in  ["L","l":
#         return False
#      else:
#         code = 0
#         message(code)

#t= "transaction.txt"
#with open(t,"r") as thandler:
#    tread = thandler.readline()
#if tread:
#    print(tread.rstrip(","))
#else:
#    print("record doesnt exist")

#FUNCTION tenantSearch(details):  REPLACED BY UPDATED searchInformation FUNCTION
#    OPEN "tenant.txt" IN READ AS TSearch
#        READ TSearch
#        TSearch STRIP (",")
#        list = JOIN TSearch INTO string(",")
#        FOR record IN list
#            IF record STARTS WITH details THEN
#                PRINT("Found record", record RIGHTSTRIP(",") RIGHTSTRIP(""))
#            ENDIF
#        ENDFOR
#    CLOSEFILE
#ENDFUNCTION
#FUNCTION tenantRead()  REPLACED BY UPDATED readFile FUNCTION
#    OPEN (tenant.txt) IN READ AS fTenant
#        tenantList = READ fTenant LINE-BY-LINE
#        FOR record IN tenantList
#            PRINT(record RIGHTSTRIP(",") RIGHTSTRIP("NEWLINE"))
#        ENDFOR
#    CLOSEFILE
#ENDFUNCTION



# searchInformation = input("Select and enter text to begin search: ") REPLACED BY UPDATED searchInformation FUNCTION
# num=0
# listCode="p"
# if listCode == "p":
#     l="transaction.txt"
# elif listCode=="a":
#     l="apartment.txt"
# elif listCode=="t":
#     l="apartment.txt"    
# with open (l,"r") as Xhandler:
#     for record in Xhandler:
#         strippeditem = record.rstrip(",").rstrip("NEWLINE")
#         data = strippeditem.split(",")
#         if searchInformation in data[num:
#             print("\n Results: \n",record)

#def apartmentSearch(num):      REPLACED BY UPDATED searchInformation FUNCTION
#    displaylist=[]
#    with open ("Apartment.txt", "r") as Tread:
#        acheck = Tread.readlines()
#        for record in acheck:
#            listrec = record.split(",")
#            displaylist.append(listrec[num])
#        print(displaylist)
#with open("Apartment.txt","r") as Ahandler:
#    for item in record:
#        for data in item:
#            print(data.rstrip().rstrip(","))
#a = "0,1,2,3,4,5,6,7,8"
#
#list= a.split(",")
#print(list)

#def apartmentExitProgram(code): SCRAPPED BECAUSE UNUSABLE
#   if code:
#      return True
#   else:
#      print("We are about to exit the program.\n[C]-Continue\nOther keys to exit")
#      exit=input("Do you want to exit?\n")
#      if exit in ["C","c"]:
#         print("\Rerunning\n")
#         return True
#      else:
#         print("\nExiting\n")
#         return False

def getname(code):
    while True:
        code = None
        name = input("Format: Name Name.....\nEnter tenant fullname:\n")
        if type(name) != int:
            nameList = name.split(" ")
            if len(nameList) >= 2:
                for words in nameList:
                    print("Checking",words)
                    if words[0].islower():
                        code = 2
                        message(code)
                        break
                    else:
                        continue
            else:
                code = 3
                message(code)
        else:
            code = 1
            message(code)
        if code:
            print("Error was detected.\n")
        else:
            print("No errors detected.\n")
        retry = input("[R]-Retry,[Any other key]-Exit using "+name+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return name

def getgender(code):
    while True:
        gender = input("Enter tenant gender: (m/f):\n")
        genderCheck = gender
        if len(genderCheck) == 1:
            if type(genderCheck) == int:
                code = 1
                message(code)
                return gender
        else: 
            code = 3
            message(code)

def getpNum(code):
    pNum = input("Enter tenant phone number: (############):\n")
    pNumCheck = pNum
    for digit in pNumCheck:
        if type(digit) == int:
            continue
        else:
            code = 1
            message(code)
    return pNum

def getnationality(code):
    while True:
        nationality = input("Enter tenant nationality: (M: Malaysian/N: non-Malaysian):\n")
        nationalityCheck = nationality
        if len(nationalityCheck) == 1:
            if type(nationalityCheck) == str:
                return False
            else:
                code = 1
                message(code)
        else: 
            code = 3
            message(code)
    return nationality

def getstartDate(code):
   startDate = input("Enter Rental start date: (YYYY,MM,DD):\n")

   return startDate

def getincome(code):
   income = input("Enter tenant income range(RM):\n")

   return income

def getrental(code):
   rental = input("Enter tenant rental status(current/past)\n")
   return rental

def message(code):
    x = "Error,"
    y = "incorrect"
    if code == 0:
        print(x+y+" input.")
    elif code == 1:
        print(x+y+" data type.")
    elif code == 2:
        print(x+y+" format.")
    elif code == 3:
        print(x+y+" length.")
    elif code == 4:
        print(x+"data not found.")
    print("Please try again.")

def tenantEntryForm(tenantList,n):           #Define tenantEntryForm function
    code = None
    for i in range(n):
        #Get input for tenant data
        name = getname(code)
        gender = getgender(code)
        pNum = getpNum(code)
        nationality = getnationality(code)
        startDate = getstartDate(code)
        income = getincome(code)
        rental = getrental(code)
        #Apply data to end of list 
        tenantList.append([name,gender,pNum,nationality,startDate,income,rental])
    #Return the list
    return tenantList

import datetime as dt
list = []
n=2
tenantEntryForm(list,n)
print(list)
