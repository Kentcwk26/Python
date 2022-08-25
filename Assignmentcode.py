def login():                                   #define the login function
   print("\nWelcome to Tenant Management System Login page.\nPlease enter username and password to proceed.\n") 
   chance = 3                                  #Specify login chances
   while chance > 0:                           #iterate when there are more than 0 chances remaining
      #input login credentials
      username = input("Username: ")
      password = input("Password: ")
      #open file and match for correct login credentials
      with open("user.txt",'r') as userInfo:
         userCheck = userInfo.readlines()
         for record in userCheck:
            listRecord = record.split(",")
            if username == listRecord[0]:
               if password == listRecord[1]:
                  print("\n- Login successful -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                  #check for admin credentials
                  if (username == "john" and password == "1234u-78") or (username == "david" and password == "55467913"):
                     masterKey = True        #activate masterKey
                     UID = None
                  else:
                     with open("currentUser.txt","w") as current:
                        current.write(record)
                     masterKey = False       #deactivate masterKey
                     UID = listRecord[2]
                  menu(masterKey,UID)        #redirect to menu
                  chance=0                   #empty login chances
                  break                      #break loop to avoid running error message
         else:
            chance-=1                        #decrease chances by 1
            print("\nError, incorrect username or password.\n",chance,"chances remaining.\n")

def listIdentifier(listCode):
   if listCode == "t":
      l = "tenant.txt"
   elif listCode == "a":
      l = "Apartment.txt"
   else:
      l = "transaction.txt"
   return l

def appendFile(list,listCode):
   with open (listIdentifier(listCode), "a") as fAppend:
      for item in list:
         fAppend.write(item)
         fAppend.write(", ")
      fAppend.write("\n")

def readFile(listCode):
   with open (listIdentifier(listCode),"r") as fRead:
      string = fRead.readlines()
      for record in string:
            stripped = record.rstrip("\n").rstrip(",")
            splitRecord = stripped.split(",")
            print(splitRecord)

def tenant(masterKey,UID,listCode,code):
   if masterKey == False:
      num = 0
      searchInformation(listCode,num,UID)
   else:
      while True:
         opt = input("[D]-Display tenant Data, [M]-Modify Tenant Data")
         if opt in ["D","d"]:      
            print("Current Tenant Data:")
            readFile(listCode)
         elif opt in ["M","m"]:
            modifyData(masterKey,listCode,code)
         return False

def tenantEntryForm(masterKey,listCode):          #Define tenantEntryForm function
   errorCode = None
   while True:
      if masterKey == True:
         n = input("Number of new tenants: ")
         if n.isdecimal():
            errorCode = None
         else:
            print(type(n))
            errorCode = 0
            message(errorCode)
            continue
      else:
         n = 1
      for tenantList in range(0,int(n)):
         #Get input for tenant data
         UserID  = gettenantID(masterKey)
         name = getname(errorCode,"tenant")
         gender = getgender(errorCode)
         pNum = getpNum(errorCode)
         nationality = getnationality(errorCode)
         startDate = getDate(errorCode,"rental")
         employer = getname(errorCode,"employer")
         income = getincome(errorCode)
         rental = getrental(errorCode,masterKey)
         birthDate = getDate(errorCode,"birth")
         birthCity = getname(errorCode,"city")
         #Apply data to end of list 
         tenantList = [UserID,name,gender,pNum,nationality,startDate,employer,income,rental,birthDate,birthCity]
         appendFile(tenantList,listCode)

def gettenantID(masterKey):
   if masterKey == False:
    #fetch existing UID
      with open("user.txt","r") as uRead:
         userRecord = uRead.read().split(",")
         return userRecord[2]
   else:
    # generate new UID
      UID = dt.datetime.now().strftime("%d%m%Y%H%M%S%f")
      return UID

def getname(code,nameType):                  #define getname()
    specials = specialCharacterList(None)
    while True:
        print("Format: Name Name... or Name-Name Name or Na'me Name")
        if nameType == "tenant":
            name = input("Enter tenant's fullname:\n")
        elif nameType == "employer":
            name = input("Enter tenant's current employer:\n")
        else:
            name = input("Enter tenant's city of birth\n")
        if not name.isnumeric:
            nameList = name.split(" ")
            if len(nameList) >= 2:
                for words in nameList:
                    print("Checking",words)
                    if words[0].isupper() and (words.isalpha() or [character for character in words if(character in specials[12]) or (character in specials[22])]):
                        code = None
                        continue
                    else:
                        code = 2
                        message(code)
                        break
            else:
                code = 3
                message(code)
        else:
            code = 1
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION")
        else:
            print("No errors detected.")
        retry = input("[R]-Retry,[Any other key]-Exit using "+name+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return name

def getgender(code):
    while True:
        gender = input("Format: M/F\nEnter tenant gender:\n")
        if len(gender)== 1:
            if gender.isalpha():
                code = None
            else:
                code = 2
                message(code)
        else: 
            code = 3
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION")
        else:
            print("No errors detected.")
        retry = input("[R]-Retry,[Any other key]-Exit using "+gender+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return gender.upper()

def getpNum(code):
    while True:
        pNum = input("Format: ############\nEnter tenant phone number:\n")
        if 6 > len(pNum) > 16:
            for digit in pNum:
                if digit.isdigit():
                    code = None
                    continue
                else:
                    code = 1
                    message(code)
                    break
        else:
            code = 3
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION")
        else:
            print("No errors detected.")
        retry = input("[R]-Retry,[Any other key]-Exit using "+pNum+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return pNum

def getnationality(code):
    while True:
        nationality = input("Enter tenant nationality: (M: Malaysian/N: non-Malaysian):\n")
        if len(nationality) == 1:
            if nationality.isdigit():
                code = None
            else:
                code = 1
                message(code)
        else: 
            code = 3
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION\n")
        else:
            print("No errors detected.\n")
        retry = input("[R]-Retry,[Any other key]-Exit using "+nationality.upper()+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return nationality.upper()

def getDate(code,dateType):
    specials = specialCharacterList(None)
    while True:
        if dateType == "start":
            path = input("Use current date as rental start date?\n[Y]-Yes\n[Any Other Key]-No\n")
            if path in ["Y","y"]:
                date = dt.date.today().strftime("%Y/%m/%d")
                print("Current date:",date)
            else:
                date = input("Format: YYYY/MM/DD\nEnter Rental start date:\n")
        else:
            date = input("Format: YYYY/MM/DD\nEnter tenant birth date:\n")
        if len(date) == 10:
            if date[4] == date[7] == specials[23]:
                year,month,day = date.split("/")
                try:
                    dt.datetime(int(year),int(month),int(day))
                    code = None
                except ValueError:
                    code = 1
                    message(code)
            else:
                code = 2
                message(code)
        else:
            code = 3
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION\n")
        else:
            print("No errors detected.\n")
        retry = input("[R]-Retry,[Any other key]-Exit using "+date+"\n")
        if retry in ["R","r"]:
            continue
        else:    
            return date

def getincome(code):
    while True:
        income = input("[1]-RM 350~449\n[2]-RM 450~549\n[3]-RM 550~649\n[4]-RM 650~749\n[5]-RM 750~849\n[6]-RM 850~949\n[7]-RM 950~1049\n[8]-RM 1050~1249\n[9]-RM 1250~1500\n[0]-RM > 1500\nChoose tenant income range in Ringgit Malaysia: ")
        if income == 1:
            income = "RM 1500~1599"
        elif income == 2:
            income = "RM 1600~1699"
        elif income == 3:
            income = "RM 1700~1799"
        elif income == 4:
            income = "RM 1800~1899"
        elif income == 5:
            income = "RM 1900~1999"
        elif income == 6:
            income = "RM 2000~2099"
        elif income == 7:
            income = "RM 2100~2199"
        elif income == 8:
            income = "RM 2200~2499"
        elif income == 9:
            income = "RM 2500~3000"
        elif income == 0:
            income = "RM > 3000"
        else:
            code = 0
            message(code)
            continue
        retry = input("[R]-Retry,[Any other key]-Exit using "+income+"\n")
        if retry in ["R","r"]:
            continue
        else:    
            return income

def getrental(masterKey):
    if masterKey == False:
        return "Current"
    else:
        while True:
            rental = input("[P]-Past\n[Any other key]-Current\nChoose tenant rental status(current/past)\n")
            if rental in ["P","p"]:
                rental = "Past"
            else:
                rental = "Current"
            retry = input("[R]-Retry,[Any other key]-Exit using "+rental+"\n")
            if retry in ["R","r"]:
                continue
            else:    
                return rental

def message(code):
   x,y,z="Error, ","Incorrect "," Please try again."
   if code == 0:
      print("\n"+x+y+"input."+z)
   elif code == 1:
      print("\n"+x+y+"data type present."+z)
   elif code == 2:
      print("\n"+x+y+"format."+z)
   elif code == 3:
      print("\n"+x+y+"length."+z)
   elif code == 4:
      print("\n"+x+"data not found."+z)
   elif code == 5:
      print("\n"+x+"zero input."+z)

def specialCharacterList(SCL):
    if SCL == None:
        return ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|",",","\'",".","/","<",">","?",";",":","'",'"'] #0-31
    elif SCL == "SCL1":
        return ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',',','\\','\'','\"','.','/','<','>','?',';',':'] #0-31
    elif SCL == "SCL2":
        return ['~','`','!','@','#','$','%','^','&','*','_','=','+','{','}','[',']','|','\\','\'','\"',',','.','/','<','>','?',':',';'] #0-28

def decision():
   code = None
   while True:
      decisionkey=input("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nAre you sure?\nInsert 'Y' to continue, 'X'to return. PLease think before action: ")
      if decisionkey in ["Y","y"]:
         return False
      elif decisionkey in ["N","n"]:
         return 
      else:
         code = 0
         message(code)
         continue

def confirmation():
   code = None
   menupage = True
   while True:
      confirmationkey=input("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nWe're hearing that you're about to leave soon. Are you sure about that? (Y/N): ")
      if confirmationkey in ["Y","y"]:
         return False
      elif confirmationkey in ["N","n"]:
         return menupage
      else:
         code = 0
         message(code)
         continue

def apartment(masterKey,listCode,code):                        #Define apartment function
   
   print("\n- Apartment info: -\n")
   ApartmentList=[]
   
   #Put sample data
   list1=["Room Info: Standard Room (Triple)","Code: SR1","Dimensions: 140+ sqft","Pricing: RM350","Number of Rooms: 20","Apartment ID: A01-L01-R01 to A01-L01-R21, Date of Acquisition: 03/01/2015, Rental History: 27/02/2015 rent, Status: Available"]
   list2=["Room Info: Standard Room (Twin)","Code: SR2","Dimensions: 120+ sqft","Pricing: RM450","Number of Rooms: 20","Apartment ID: A01-L01-R22 to A01-L01-R41, Date of Acquisition: 10/02/2015, Rental History: 28/03/2015 rent, Status: Available"]
   list3=["Room Info: Standard Room A/C (Triple)","Code: SR3","Dimensions: 150+ sqft","Pricing: RM550","Number of Rooms: 20","Apartment ID: A01-L02-R01 to A01-L02-R21, Date of Acquisition: 21/03/2016, Rental History: 24/04/2016 rent, Status: Available"]
   list4=["Room Info: Standard Room A/C (Twin)","Code: SR4","Dimensions: 130+ sqft","Pricing: RM650","Number of Rooms: 20","Apartment ID: A01-L02-R22 to A01-L02-R41, Date of Acquisition: 02/04/2016, Rental History: 20/05/2016 rent, Status: Available"]
   list5=["Room Info: Deluxe Room (Triple)","Code: DR1","Dimensions: 170+ sqft","Pricing: RM750","Number of Rooms: 20","Apartment ID: A01-L04-R01 to A01-L04-R21, Date of Acquisition: 11/05/2017, Rental History: 21/06/2017 rent, Status: Available"]
   list6=["Room Info: Deluxe Room (Twin)","Code: DR2","Dimensions: 160+ sqft","Pricing: RM840","Number of Rooms: 20","Apartment ID: A01-L04-R22 to A01-L04-R41, Date of Acquisition: 22/06/2017, Rental History: 22/07/2017 rent, Status: Available"]
   list7=["Room Info: Deluxe Room A/C with shared attached bath / toilet (Triple)","Code: DR3","Dimensions: 180+ sqft","Pricing: RM950","Number of Rooms: 20","Apartment ID: A01-L03-R1 to A01-L03-R21, Date of Acquisition: 30/07/2018, Rental History: 25/08/2018 rent, Status: Available"]
   list8=["Room Info: Deluxe Room A/C with shared attached bath / toilet","Code: DR4","Dimensions: 170+ sqft","Pricing: RM1040","Number of Rooms: 20","Apartment ID: A01-L03-R22 to A01-L03-R41, Date of Acquisition: 16/08/2018,, Rental History: 18/09/2018 rent, Status: Available"]
   list9=["Room Info: Compact Premium Single","Code: CPS1","Dimensions: 130+ sqft","Pricing: RM690","Number of Rooms: 20","Apartment ID: A01-L05-R01 to A01-L05-R41, Date of Acquisition: 02/09/2019, Rental History: 29/10/2019 rent, Status: Available"]
   list10=["Room Info: Medium Premium Single","Code: MPS1","Dimensions: 150+ sqft","Pricing: RM750","Number of Rooms: 20","Apartment ID: A02-L01-R01 to A02-L01-R21, Date of Acquisition: 15/10/2019, Rental History: 31/11/2019 rent, Status: Available"]
   list11=["Room Info: Medium Premium Twin","Code: MPT1","Dimensions: 180+ sqft","Pricing: RM890","Number of Rooms: 20","Apartment ID: A02-L02-R01 to A02-L02-R21, Date of Acquisition: 25/11/2020, Rental History: 31/12/2020 rent, Status: Available"]
   list12=["Room Info: Medium Premium with attached bath / toilet (Twin)","Code: MP1","Dimensions: 180+ sqft","Pricing: RM940","Number of Rooms: 20","Apartment ID: A02-L03-R01 to A02-L03-R21, Date of Acquisition: 30/12/2020, Rental History: 31/01/2020 rent, Status: Available"]
   list13=["Room Info: Medium Premium with attached bath / toilet (Single)","Code: MP2","Dimensions: 160+ sqft","Pricing: RM1050","Number of Rooms: 20","Apartment ID: A02-L03-R22 to A02-L03-R41, Date of Acquisition: 16/01/2021, Rental History: 28/02/2021 rent, Status: Available"]
   list14=["Room Info: En-Suite Single (Super Premium - Triple)","Code: ESS3","Dimensions: 160+ sqft","Pricing: RM700","Number of Rooms: 20","Apartment ID: A02-L04-R01 to A02-L04-R41, Date of Acquisition: 25/02/2021, Rental History: 31/03/2021 rent, Status: Available"]
   list15=["Room Info: En-Suite Single (Super Premium - Twin)","Code: ESS2","Dimensions: 140+ sqft","Pricing: RM800","Number of Rooms: 20","Apartment ID: A02-L04-R01 to A02-L04-R41, Date of Acquisition: 31/05/2022, Rental History: Empty, Status: Not Available"]
   list16=["Room Info: En-Suite Twin (Super Premium)","Code: EST2","Dimensions: 200+ sqft","Pricing: RM900","Number of Rooms: 20","Apartment ID: A02-L05-R01 to A02-L05-R41, Date of Acquisition: 26/06/2022, Rental History: Empty, Status: Not Available"]

   #Apply data at the list
   ApartmentList.append(list1)
   ApartmentList.append(list2)
   ApartmentList.append(list3)
   ApartmentList.append(list4)
   ApartmentList.append(list5)
   ApartmentList.append(list6)
   ApartmentList.append(list7)
   ApartmentList.append(list8)
   ApartmentList.append(list9)
   ApartmentList.append(list10)
   ApartmentList.append(list11)
   ApartmentList.append(list12)
   ApartmentList.append(list13)
   ApartmentList.append(list14)
   ApartmentList.append(list15)
   ApartmentList.append(list16)

   for item in ApartmentList:
      print(item)

   with open("Apartment.txt","w") as Ahandler:
      for record in ApartmentList:
         for data in record:
            Ahandler.write(data)
            Ahandler.write(", ")
            Ahandler.write("\n")
         Ahandler.write("\n")
      Ahandler.write("\n")

   if masterKey == True:
      modifyData(masterKey,listCode,code)
   else:
      return False

def modifyData(masterKey,listCode,code):
   modify = True
   while modify == True:
      print("\n- Modification of records: -\n\n1. Add data\n2. Edit Data\n3. Delete Data\n4. Exit\n")
      dataInput=int(input('Please select which operation to perform task (1-4): '))

      if dataInput==1:
         print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n- Add Data -")
         if listCode == "a":
            apartmentAddData()
         elif listCode == "t":
            tenantEntryForm(masterKey,code)
         else:
            print("transactionEntryForm()")

      elif dataInput==2:
         print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n- Edit Data -")
         apartmentEditData()

      elif dataInput==3:
         print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n- Delete Data -")
         #apartmentDeleteData()

      elif dataInput==4:
         print("\n- Exit -")
         return False

      else:
         code=2
         message(code)
         print("\n---------------------------------------------------------------------------------------------------\n\n- Tenant Management System -")
         continue

def apartmentAddData():
   adddatalist = []
   print("\Dear admin, we need your ATTENTION !\n\nFor your information, all the new data will be only stored if Admin insert the information with the correct format for each new data entry provided.\n\nNew room info: only contains alphabets, no numbers and special characters [Except these special characters: '(' ')' '/' '-' ]\nExample: Dual Key Premium Rooms - Single Room\n\nNew room code: only contains alphanumeric (A combination of Uppercased alphabet and number), and no special characters\nExample: DKPRS1\n\nNew Room Dimension (in range sqft): only contains numbers, no special characters (The unit will be provided at the back)\nExample: 300(+sqft)\n\nNew Room Pricing (in RM): only contain numbers, no special characters (The unit will be provided at the front)\nExample: (RM)500\n\nNumber of new rooms: only contains numbers and no special characters\nExample: 10 (Accepted range: 1-99)\n\nNew Apartment ID: A(01)-L(01)-R(01)x(to)xA(99)-L(99)-R(99)\nPlease follow this format as written above (A stands for Apartment Block, L stands for Room Level, R stands for Room Number, x means space)\n\nNew Room Date of Acquisition: dd/mm/yyyy\nNo special characters included, except '/'\n\nNew Room Rental History: (Accepted input: 'dd/mm/yyyy' or 'Empty')\nNo special characters included, except '/'\n\nNew Room Status: (Accepted Input: 'Available' or 'Not Available')\nNo numbers and special characters included\n\n- Now, you are required to enter new data. -\n")
   newroom=newRoom()
   newroomcode=newRoomCode()
   newroomdimension=newRoomDimension()
   newroompricing=newRoompricing()
   newnumberofRooms=newNumberofRooms()
   newroomfirstID=newRoomIDFirst()
   newroomlastID=newRoomIDLast()
   newroomdateofacquisition=newRoomDateofAcquisition()
   newroomrentalhistory=newRoomRentalHistory()
   newroomstatus=newRoomStatus()
   adddatalist=["New Room Info: "+str(newroom),"New Room Code: "+str(newroomcode),"New Room Dimension in range (sqft): "+str(newroomdimension)+'+ sqft',"New Room Pricing: RM"+str(newroompricing),"Number for the new room: "+str(newnumberofRooms),"New room ID: "+str(newroomfirstID+' to '+newroomlastID),"New room Acquisition Date: "+str(newroomdateofacquisition),"New room Rental History: "+str(newroomrentalhistory)+" rent","New room Status: "+str(newroomstatus)]
   print("\nNew Data:",adddatalist)
   apartmentadddataconfirmation(adddatalist)

def newRoom():
   while True:
      code = None
      SCL = 'SCL2'
      specials = specialCharacterList(SCL)
      newRoom=input("New room Info: ")
      if [character for character in newRoom if (character in specials)]:
         code = 2
         message(code)
         print("- New room info does not contain special character(s) -\n")
         continue
      else:
         code = None
      if 0 <= len(newRoom) < 6:
         code = 2
         message(code)
         print("-  Refer to the New Room Info to look for its details and format -\n")
         continue
      else:
         code = None
      if newRoom.isdigit() and any(location.isdigit() for location in newRoom):
         code = 1
         message(code)
         print("- New room info does not contain number(s) -\n")
         continue
      else:
         code = None
      if code == None:
         newRoom.title()
         decisionkey=input("\nAre you sure with your records? (Yes/No): ")
         if decisionkey in ["Yes","yes"]:
            return newRoom
         elif decisionkey in ["No","no"]:
            continue
      else:
         code = 2
         message(code)
         print("- Please fill in the correct format for new Room info. Refer to the New Room Info to look for its details and format -\n")
         continue

def newRoomCode():
   while True:
      code = None
      newRoomCode = input("\nNew Room Code: ")
      if 0 < len(newRoomCode) < 1 :
         code=2
         message(code)
         print("- New Room Code must contain at least 2 or more alphanumeric long -\n")
         continue
      else:
         code = None 
      if newRoomCode.isalnum():
         code = None
      else:
         code=2
         message(code)
         print("- Please noted that new room code is only acceptable when it contains alphanumeric -\n")
         continue
      if code == None:
         return newRoomCode
      else:
         code = 2
         message(code)
         print("- Please fill in the correct format for new Apartment code. Refer to the New Room Pricing to look for its details and format -")
         continue

def newRoomDimension():
   while True:
      code = None
      newRoomDimension=input("New Room Dimension in range (sqft): ")
      if len(newRoomDimension)==0:
         code = 5
         message(code)
         print("- Please fill in the new room dimension, and room dimension must have at least 100 or more sqft -\n")
         continue
      else:
         code = None
      if newRoomDimension.isdigit():
         code = None
      else:
         code = 2 
         message(code)
         print("- New room dimension must consist of number(s) -")
         continue
      if code == None:
         return newRoomDimension
      else:
         code=2
         message(code)
         print("- Please fill in the correct format for new room dimension. Refer to the top description for its details and format -\n")
         continue

def newRoompricing():
   while True:
      code = None
      newRoompricing=input("New Room Pricing (in RM): ")
      if newRoompricing.isdigit():
         nRp=int(newRoompricing)
         if nRp >= 350:
            code = None
      else:
         code = 2
         message(code)
         print("- Please fill in the room pricing, it must be in numeric and the minimum starting price starts from RM350 and above -\n")
         continue
      if code == None:
         return newRoompricing
      else:
         code = 2
         message(code)
         print("- Please follow the correct format for new room pricing. Refer to the desccrition above to know its details and format -\n")
         continue

def newNumberofRooms():
   while True:
      code = None
      newNumberofRooms=input("Number of new rooms: ")
      if len(newNumberofRooms) == 0 or (newNumberofRooms == "0" and newNumberofRooms == "1"):
        code = 5
        message(code)
        print("- Please fill in the number of new rooms -\n")
        continue
      else:
        code = None

      if newNumberofRooms.isdigit():
        code = None
      else:
        code = 3
        message(code)
        print("- Number of new rooms must be in numeric -\n")
        continue

      if code == None :
        return newNumberofRooms
      else:
        code=2
        message(code)
        print("- Please fill in the correct format for the number of new rooms. Refer to the description above to look for its details and format -\n")
        continue

def newRoomIDFirst():
   while True:
      code = None
      SCL='SCL2'
      specials=specialCharacterList(SCL)
      newRoomIDfirst = input("New Room Apartment ID (First): ")

      if len(newRoomIDfirst) == 0:
         code = 5
         message(code)
         print("- Please fill in the new Apartment ID -\n")
         continue
      else:
         code = None

      if 0 < len(newRoomIDfirst) < 10:
         code = 2
         message(code)
         print("- Please follow the format as: A01-L10-R40 ( A stands for Apartment Block, L stands for Level, and R stands for Room (The length must have 11 characters long, including the dash -) -\n")
         continue
      else:
         code = None

      if (newRoomIDfirst[0] == 'A' and newRoomIDfirst[3] == '-' and newRoomIDfirst[4] == 'L' and newRoomIDfirst[7] == '-' and newRoomIDfirst[8] == 'R') and any(location.isdigit() for location in newRoomIDfirst):
         if [character for character in newRoomIDfirst[:] if (character in specials)]:
            code = None
      else:
         code=2
         message(code)
         print("- Please follow the format as: A01-L10-R40, it (A,L,R) must contain uppercases and numbers. -\n")
         continue
            
      if code == None:
         return newRoomIDfirst
      else:
         code=3
         message(code)
         print("- Please fill in the correct format for new room Apartment ID. Refer to the description above to look for its details and format -")
         continue

def newRoomIDLast():
   while True:
      code = None
      SCL = 'SCL2'
      specials=specialCharacterList(SCL)
      newRoomIDlast = input("New Room Apartment ID (Last): ")

      if len(newRoomIDlast) == 0:
         code = 5
         message(code)
         print("- Please fill in the new Apartment ID -\n")
         continue
      else:
         code = None

      if 0 < len(newRoomIDlast) < 10:
         code = 2
         message(code)
         print("- Please follow the format as: A01-L10-R40 ( A stands for Apartment Block, L stands for Level, and R stands for Room (The length must have 11 characters long, including the dash -) -\n")
         continue
      else:
         code = None

      if (newRoomIDlast[0] == 'A' and newRoomIDlast[3] == '-' and newRoomIDlast[4] == 'L' and newRoomIDlast[7] == '-' and newRoomIDlast[8] == 'R') and (location.isdigit() for location in newRoomIDlast):
         if [character for character in newRoomIDlast[:] if (character in specials)]:
            code = None
      else:
         code=2
         message(code)
         print("- Please follow the format as: A01-L10-R40, it (A,L,R) must contain uppercases and numbers. -\n")
         continue
            
      if code == None:
         return newRoomIDlast
      else:
         code=3
         message(code)
         print("- Please fill in the correct format for new room Apartment ID. Refer to the description above to look for its details and format -")
         continue

def newRoomDateofAcquisition():
    while True:
        code = None
        newRoomDateOfAcquisition = input("New Room Date of Acquisition (dd/mm/yyyy): ")
        if any(location.isdigit() for location in newRoomDateOfAcquisition) and len(newRoomDateOfAcquisition) == 10:
            day,month,year = newRoomDateOfAcquisition.split('/')
            ValidDate = True
            try:
               dt.datetime(int(year),int(month),int(day))
               ValidDate = True
            except ValueError:
                ValidDate = False
            if ValidDate == True :
               code = None
               return newRoomDateOfAcquisition
            else:
               code = 2
               message(code)
               print("- New room acquisition date is not valid -\n")
               continue
        else:
            code = 2
            message(code)
            print("- Wrong Date Format (dd/mm/yyyy) -\n")
            continue

def newRoomRentalHistory():
   while True:
        code = None
        newRoomRentalHistory = input("New Room Rental History (dd/mm/yyyy): ")
        if any(location.isdigit() for location in newRoomRentalHistory) and len(newRoomRentalHistory) == 10:
            day,month,year = newRoomRentalHistory.split('/')
            ValidDate = True
            try:
               dt.datetime(int(year),int(month),int(day))
               ValidDate = True
            except ValueError:
               ValidDate = False
            if ValidDate == True :
               code = None
               return newRoomRentalHistory
            else:
               code = 2
               message(code)
               print("- New rental history date is not valid -\n")
               continue
        else:
            code = 2
            message(code)
            print("- Wrong Date Format (dd/mm/yyyy) -\n")
            continue

def newRoomStatus():
   while True:
      code = None
      SCL = None
      specials = specialCharacterList(SCL)
      newRoomStatus = input("New Room Status ( Available / Not Available ): ")
    
      if (0 <= len(newRoomStatus) <= 7) or (len(newRoomStatus) >= 14) :
         code = 5
         message(code)
         print("- Please fill again the new room status and follow the correct format ( Accepted input: Available / Not Available ) -\n")
         continue
      else:
         code = None

      if any(location.isdigit() for location in newRoomStatus) and newRoomStatus.isdigit(): 
         code = 2
         message(code)
         print("- New room status does not contain number(s) -\n")
         continue
      else:
         code = None

      if [character for character in newRoomStatus if (character in specials)]:
         code = 2
         message(code)
         print("- New room status does not have special character(s) -\n")
         continue
      else:
         code = None

      if (0 <= len(newRoomStatus) <= 7 or len(newRoomStatus) >= 14) and (any(location.isdigit() for location in newRoomStatus)):
         code = 2
         message(code)
         print("- New room status does not consists of number(s) -\n")
         continue
      else:
         code = None

      if ([character for character in newRoomStatus if (character in specials)] and any(location.isdigit() for location in newRoomStatus) and [character for character in newRoomStatus if (character in specials)]):
         code = 3
         message(code)
         print("- New room rental history does not contain number(s) and special character(s) -\n")
         continue
      else:
         code = None

      if (0 < len(newRoomStatus) <= 7 or len(newRoomStatus) >= 14) and (any(location.isdigit() for location in newRoomStatus)) and ([character for character in newRoomStatus if (character in specials)]):
         code=3
         message(code)
         print("- Input too short oe long, and also number(s) and special character(s) exist, please follow the correct format ( Accepted input: Available / Not Available ) -\n")
         continue
      else:
         code = None

      if newRoomStatus in ["Available","Not Available"] and (len(newRoomStatus) == 9 or len(newRoomStatus) == 13):
         code = None
      else:
         code = 2
         message(code)
         print("- Room Status can only be accepted either the input is 'Available' or 'Not Available'. -\n")
         continue

      if code == None:
         return newRoomStatus
      else:
         code = 3
         message(code)
         print("Please insert the correct format for new room status. Refer to the top description to let its details and format -\n")
         continue

def apartmentadddataconfirmation(adddatalist):
   modify = True
   listCode = "a"
   while True:
      addDataconfirmation=int(input("\nAre you sure with the records you inserted just now? Enter '1' to save record, Enter '0' to unsave record: "))
      if addDataconfirmation == 1:
         appendFile(adddatalist,listCode)
         print("\n- Data Saved -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
         return modify
      else:
         code=0
         message(code)
         break

def apartmentEditData():
   

# def apartmentDeleteData():

def searchBox():
   while True:                             #Define search function
      print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nWelcome to search box!")
      num = None
      print("\n1. Search room specific details.\n2. Search transaction details.\n3. Search specific tenant details.\n4. Exit search box.\n")
      option=int(input("Please type the search criteria based on the listing above: "))
      if option == 1:
         listCode= "a"
         opt = input("\n[C]-Room code, [P]-Pricing, [N]-Number of Rooms, [A]- Apartment ID, [D]-Date of Acquisition, [R]-Rental \nSearch?  ")     
         if opt in ["C","c"]:
            num = 1
         elif opt in ["P","p"]:
            num = 3
         elif opt in ["N","n"]:
            num = 4
         elif opt in ["A","a"]:
            num = 5
         elif opt in ["D","d"]:
            num = 6
         elif opt in ["R","r"]:
            num = 7
            num = 8
         else:
            code = 0
            message(code)
            continue

      elif option == 2:
         listCode = "p"
         opt = input("\n[R]-Reference number,[D]-Transaction date,[T]-TenantID,[A]-Apartment code,[S]-Amount: ")
         if opt in ["R","r"]:
            num = 0
         elif opt in ["D","d"]:
            num = 1
         elif opt in ["T","t"]:
            num = 2
         elif opt in ["A","a"]:
            num = 3
         elif opt in ["S","s"]:
            num = 4
         else:
            code = 0
            message(code)     
      
      elif option == 3 :
         listCode = "t"
         opt = input("\n[N]-Name,[G]-Gender,[P]-Phone number,[R]-Nationality,[D]-Rental start date,[I]-Income,[S]-Tenant status: ")
         if opt in ["N","n"]:
            num = 0
         elif opt in ["G","g"]:
            num = 1
         elif opt in ["P","p"]:
            num = 2
         elif opt in ["R","r"]:
            num = 3
         elif opt in ["D","d"]:
            num = 4
         elif opt in ["I","i"]:
            num = 5
         elif opt in ["S","s"]:
            num = 6
         else:
            code = 0
            message(code)

      elif option == 4:
         print("\n- Return to main menu -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n- Welcome back ! -")
         return False                                 #return to menu function
      
      else:
         code = 0
         message(code)
      details = None
      searchInformation(listCode,num,details)

def searchInformation(listCode,num,details):                  #Define searchinformation function
   while True:
      if details:
         searchInformation == details
      else:
         searchInformation=input("\nPlease enter text to begin the search: ")
      recordExist = False
      with open(listIdentifier(listCode),"r") as Xhandler:
         print("\nResults:\n")
         for record in Xhandler:
            strippedItem = record.rstrip()
            data=strippedItem.split(",")
            if searchInformation in data[num]:
               print(record.rstrip(",").rstrip("\n"))
               print("\n")
               recordExist = True
            else:
               continue
         if recordExist == True:
            code = 0
            print("- Matching records ends here -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
         else:
            code = 4
            message(code)

      exitSearch=input("\nExit program?\n\n[C] - Continue Program.\n[Any other key] - Exit: ")
      if exitSearch in ["C","c"]:
         continue
      else:
         return False

def menu(masterKey,UID):                                  #Define menu function
   print("\n- Welcome! -")
   menupage = True
   while menupage == True:
      code = None
      if masterKey == False:
         print("\nYou are now entering Tenant Management System (Tenant Page)\n\n[S] - Search box\n\nReview information about:\n\n[A] - Apartment\n[P] - Transaction\n[T] - My Tenant details\n\n[D] - Print my House and Tenant Details\n[E] - Exit\n")
      else:
         print("\nYou are now entering Tenant Management System (Admin Page)\n\n[S] - Search box\n\nReview information about:\n\n[A] - Apartment\n[P] - Transaction\n[T] - Tenant\n[D] - Print Specific House & Tenant Details\n[I] - Inquiry of Past Tenant Details\n[L] - Login History\n[E] - Exit\n")

      opt=input("Please select which operation that you want to do: ")

      if opt in ["S","s"]:
         searchBox()
      #Check for basic Functions
      elif opt in ["A","a"]:
         listCode = "a"
         apartment(masterKey,listCode,code)
      
      elif opt in ["P","p"]:
         listCode = "p"
         print("transaction(masterKey,listCode,code)")
      
      elif opt in ["T","t"]:
         listCode = "t"
         tenant(masterKey,UID,listCode,code)
      #Check for quick functions
      elif opt in ["D","d"]:
         print("tenantAndApartment()")
      
      elif opt in ["I","i"] and masterKey == True:
         details = "past"
         print("searchTenant(details)")

      elif opt in ["L","l"] and masterKey == True:
         print("loginHistory()")

      elif opt in ["E","e"]:
         confirmation()
         print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nExit Tenant Management System\nThank you for using us, have a nice day~\n")
         return False

      else:
         code = 0
         message(code)
         continue

import datetime as dt
login()
