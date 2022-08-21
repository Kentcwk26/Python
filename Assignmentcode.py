def login():                                 #define the login function
   print("\nWelcome to Tenant Management System Login page.\nPlease enter username and password to proceed.\n") 
   chance = 3                                  #Specify login chances
   while chance>0:                           #iterate when there are more than 0 chances remaining
      #input login credentials
      username = input("Enter username:")
      password = input("Enter password:")
      #open file and match for correct login
      with open("user.txt",'r') as userInfo:
         userCheck = userInfo.readlines()
         for record in userCheck:
            listRecord = record.split(",")
            if username == listRecord[0]:
               if password == listRecord[1]:
                  print("\nLogin successful\n")
                  #check for admin credentials
                  if (username == "john" and password == "1234u-78") or (username == "david" and password == "55467913"):
                     masterKey = True        #activate masterKey
                  else:
                     masterKey = False       #deactivate masterKey
                  menu(masterKey)            #redirect to menu
                  chance=0                   #empty login chances
                  break                      #break loop to avoid running error message
         else:
            chance-=1                        #decrease chances by 1
            print("\nError, incorrect username or password.\n",chance,"chances remaining.\n")

def tenant(masterKey,UID):
   if masterKey == False:
      print("tenantSearch(UID)")
   else:
      
      n = input("Number of new tenants: ")
      tenantList=[]
      tenantList = tenantEntryForm(tenantList,n)
      print(tenantList)

def tenantEntryForm(tenantList,n):           #Define tenantEntryForm function
   for i in range(n):
      #Get input for tenant data
      name = getname()
      gender = getgender()
      pNum = getpNum()
      nationality = getnationality()
      startDate = getstartDate()
      income = getincome()
      rental = getrental()
      #Apply data to end of list 
      tenantList.append(name,gender,pNum,nationality,startDate,income,rental)
   #Return the list
   return tenantList

def getname():
  while True:
      name = input("Enter tenant name: Firstname Familyname Lastname\n")
      nameCheck = name
      nameCheck.split(",")
      for words in nameCheck:
         if words[0].isupper:
            break
         else:
            code = 2
            message(code)
      return name

def getgender():
   gender = input("Enter tenant gender: (m/f):\n")
   genderCheck = gender
   if genderCheck.len == 1:
      if type(genderCheck) != str:
         code = 1
         message(code)
   else: 
      code = 3
      message(code)
   return gender

def getpNum():
   pNum = input("Enter tenant phone number: (############):\n")
   pNumCheck = pNum
   for digit in pNumCheck:
      if type(digit) != int():
         continue
      else:
         code = 1
         message(code)
   return pNum

def getnationality():
  while True:
      nationality = input("Enter tenant nationality: (M: Malaysian/N: non-Malaysian):\n")
      nationalityCheck = nationality
      if len(nationalityCheck) == 1:
         if type(nationalityCheck) == str:
            continue
         else:
            code = 1
            message(code)
      else: 
         code = 3
         message(code)
      return nationality

def getstartDate():
   startDate = input("Enter Rental start date: (YYYY,MM,DD):\n")

   return startDate

def getincome():
   income = input("Enter tenant income range(RM):\n")

   return income

def getrental():
   rental = input("Enter tenant rental status(current/past)\n")
   return rental

def message(code):
   if code == 0:
      print("Incorrect input")
   elif code == 1:
      print("Incorrect data type present")
   elif code == 2:
      print("Format error")
   elif code == 3:
      print("Length error")
   print("Please try again.")

def adminApartment():                        #Define apartment function
   
   print("\nApartment info:\n")
   record=[]         
   #Put sample data
   list1=[["Standard Room (Triple)"],["Code: SR1"],["Dimensions: 140+ sqft"],["Pricing: RM350"],["Number of Rooms: 20"],["Apartment ID: A01-L1-R1 to A01-L1-R21"]]
   list2=[["Standard Room (Twin)"],["Code: SR2"],["Dimensions: 120+ sqft"],["Pricing: RM450"],["Number of Rooms: 20"],["Apartment ID: A01-L1-R22 to A01-L1-R41"]]
   list3=[["Standard Room A/C (Triple)"],["Code: SR3"],["Dimensions: 150+ sqft"],["Pricing: RM550"],["Number of Rooms: 20"],["Apartment ID: A01-L2-R1 to A01-L2-R21"]]
   list4=[["Standard Room A/C (Twin)"],["Code: SR4"],["Dimensions: 130+ sqft"],["Pricing: RM650"],["Number of Rooms: 20"],["Apartment ID: A01-L2-R22 to A01-L2-R41"]]
   list5=[["Deluxe Room (Triple)"],["Code: DR1"],["Dimensions: 170+ sqft"],["Pricing: RM750"],["Number of Rooms: 20"],["Apartment ID: A01-L4-R1 to A01-L4-R21"]]
   list6=[["Deluxe Room (Twin)"],["Code: DR2"],["Dimensions: 160+ sqft"],["Pricing: RM840"],["Number of Rooms: 20"],["Apartment ID: A01-L4-R22 to A01-L4-R41"]]
   list7=[["Deluxe Room A/C with shared attached bath / toilet (Triple)"],["Code: DR3"],["Dimensions: 180+ sqft"],["Pricing: RM950"],["Number of Rooms: 20"],["Apartment ID: A01-L3-R1 to A01-L3-R21"]]
   list8=[["Deluxe Room A/C with shared attached bath / toilet"],["Code: DR4"],["Dimensions: 170+ sqft"],["Pricing: RM1040"],["Number of Rooms: 20"],["Apartment ID: A01-L3-R22 to A01-L3-R41"]]
   list9=[["Compact Premium Single"],["Code: CPS"],["Dimensions: 130+ sqft"],["Pricing: RM690"],["Number of Rooms: 20"],["Apartment ID: A01-L5-R1 to A01-L5-R41"]]
   list10=[["Medium Premium Single"],["Code: MPS"],["Dimensions: 150+ sqft"],["Pricing: RM750"],["Number of Rooms: 20"],["Apartment ID: A02-L1-R1 to A02-L1-R21"]]
   list11=[["Medium Premium Twin"],["Code: MPT"],["Dimensions: 180+ sqft"],["Pricing: RM890"],["Number of Rooms: 20"],["Apartment ID: A02-L2-R1 to A02-L2-R21"]]
   list12=[["Medium Premium with attached bath / toilet (Twin)"],["Code: MP1"],["Dimensions: 180+ sqft"],["Pricing: RM940"],["Number of Rooms: 20"],["Apartment ID: A02-L3-R1 to A02-L3-R21"]]
   list13=[["Medium Premium with attached bath / toilet (Single)"],["Code: MP2"],["Dimensions: 160+ sqft"],["Pricing: RM1050"],["Number of Rooms: 20"],["Apartment ID: A02-L3-R22 to A02-L3-R41"]]
   list14=[["En-Suite Single (Super Premium - Triple)"],["Code: ESS3"],["Dimensions: 160+ sqft"],["Pricing: RM700"],["Number of Rooms: 20"],["Apartment ID: A02-L4-R1 to A02-L4-R41"]]
   list15=[["En-Suite Single (Super Premium - Twin)"],["Code: ESS2"],["Dimensions: 140+ sqft"],["Pricing: RM800"],["Number of Rooms: 20"],["Apartment ID: A02-L4-R1 to A02-L4-R41"]]
   list16=[["En-Suite Twin (Super Premium)"],["Code: EST2"],["Dimensions: 200+ sqft"],["Pricing: RM900"],["Number of Rooms: 20"],["Apartment ID: A02-L5-R1 to A02-L5-R41"]]

   #Apply data at the list
   record.append(list1)
   record.append(list2)
   record.append(list3)
   record.append(list4)
   record.append(list5)
   record.append(list6)
   record.append(list7)
   record.append(list8)
   record.append(list9)
   record.append(list10)
   record.append(list11)
   record.append(list12)
   record.append(list13)
   record.append(list14)
   record.append(list15)
   record.append(list16)
   
   with open("Apartment.txt","w") as Ahandler:
      for item in record:
         for data in item:
            for element in data:
               Ahandler.write(element)
            Ahandler.write(", ")
         Ahandler.write("\n")
       
   with open("Apartment.txt","r") as Ahandler:
      for item in record:
         for data in item:
            for element in data:
               Ahandler.write(element)
            Ahandler.write(", ")
         Ahandler.write("\n")
         for item in Ahandler:
            print(item.rstrip().rstrip(","))

   modifyData()

def modifyData():
  while True:
      print("\n1. Add data\n2. Edit Data\n3. Delete Data\n4. Exit\n")
      dataInput=int(input('Please select which operation: '))

      if dataInput==1:
         print("\nAdd Data\n")
         apartmentAddData()

      elif dataInput==2:
         print("\nEdit Data\n")
         apartmentEditData()

      elif dataInput==3:
         print("\nDelete Data\n")
         apartmentDeleteData()

      elif dataInput==4:
         print("Exit")
         return False

      else:
         print("Error!")

def apartmentAddData(record):
   adddatanum=int(input('How many records that you decide to add? '))
   adddata=[]
   print("\nNow, you are required to enter the new data\n")
   for i in range(0,adddatanum):
      newapartment=str(input("Apartment: "))
      newapartmentcode=input("Code: ")
      newapartmentdimension=input("Dimension (Range): ")
      newapartmentpricing=input("Pricing in RM: ")
      newapartmentnumberofrooms=str(input("Number of rooms: "))
      newapartmentID=input("Apartment ID: ")
      adddata.append(newapartment)
      adddata.append("Code: ",newapartmentcode)
      adddata.append("Dimensions: "+newapartmentdimension+"sqft")
      adddata.append("Pricing: "+"RM"+newapartmentpricing)
      adddata.append("Number of Rooms: ",newapartmentnumberofrooms)
      adddata.append("Apartment ID: ",newapartmentID)
      print("\n",adddata,"\n")
      record.extend(adddata)

def apartmentEditData():
   editdatanum=int(input('How many records that you decide to edit? '))

def apartmentDeleteData():
   deletedatanum=int(input('How many records that you decide to add? '))

def apartmentExitProgram():
   
  while True:
      exitoption=str(input("We are about to exit to the program. \nAre you sure that you want to exit? Enter 'C to continue, Enter''X' to exit: "))
      if exitoption=='C':
         print("\nContinue\n")
      elif exitoption=='X':
         print("\nExit program, return to main menu\n")
         return False
      else:
         print("\nInvalid input\n")

def tenantApartment():                       #Define apartment function
   
   print("\nApartment info:\n")
   record=[]         
   #Put sample data
   list1=[["Standard Room (Triple)"],["Code: SR1"],["Dimensions: 140+ sqft"],["Pricing: RM350"],["Number of Rooms: 20"],["Apartment ID: A01-L1-R1 to A01-L1-R21"]]
   list2=[["Standard Room (Twin)"],["Code: SR2"],["Dimensions: 120+ sqft"],["Pricing: RM450"],["Number of Rooms: 20"],["Apartment ID: A01-L1-R22 to A01-L1-R41"]]
   list3=[["Standard Room A/C (Triple)"],["Code: SR3"],["Dimensions: 150+ sqft"],["Pricing: RM550"],["Number of Rooms: 20"],["Apartment ID: A01-L2-R1 to A01-L2-R21"]]
   list4=[["Standard Room A/C (Twin)"],["Code: SR4"],["Dimensions: 130+ sqft"],["Pricing: RM650"],["Number of Rooms: 20"],["Apartment ID: A01-L2-R22 to A01-L2-R41"]]
   list5=[["Deluxe Room (Triple)"],["Code: DR1"],["Dimensions: 170+ sqft"],["Pricing: RM750"],["Number of Rooms: 20"],["Apartment ID: A01-L4-R1 to A01-L4-R21"]]
   list6=[["Deluxe Room (Twin)"],["Code: DR2"],["Dimensions: 160+ sqft"],["Pricing: RM840"],["Number of Rooms: 20"],["Apartment ID: A01-L4-R22 to A01-L4-R41"]]
   list7=[["Deluxe Room A/C with shared attached bath / toilet (Triple)"],["Code: DR3"],["Dimensions: 180+ sqft"],["Pricing: RM950"],["Number of Rooms: 20"],["Apartment ID: A01-L3-R1 to A01-L3-R21"]]
   list8=[["Deluxe Room A/C with shared attached bath / toilet"],["Code: DR4"],["Dimensions: 170+ sqft"],["Pricing: RM1040"],["Number of Rooms: 20"],["Apartment ID: A01-L3-R22 to A01-L3-R41"]]
   list9=[["Compact Premium Single"],["Code: CPS"],["Dimensions: 130+ sqft"],["Pricing: RM690"],["Number of Rooms: 20"],["Apartment ID: A01-L5-R1 to A01-L5-R41"]]
   list10=[["Medium Premium Single"],["Code: MPS"],["Dimensions: 150+ sqft"],["Pricing: RM750"],["Number of Rooms: 20"],["Apartment ID: A02-L1-R1 to A02-L1-R21"]]
   list11=[["Medium Premium Twin"],["Code: MPT"],["Dimensions: 180+ sqft"],["Pricing: RM890"],["Number of Rooms: 20"],["Apartment ID: A02-L2-R1 to A02-L2-R21"]]
   list12=[["Medium Premium with attached bath / toilet (Twin)"],["Code: MP1"],["Dimensions: 180+ sqft"],["Pricing: RM940"],["Number of Rooms: 20"],["Apartment ID: A02-L3-R1 to A02-L3-R21"]]
   list13=[["Medium Premium with attached bath / toilet (Single)"],["Code: MP2"],["Dimensions: 160+ sqft"],["Pricing: RM1050"],["Number of Rooms: 20"],["Apartment ID: A02-L3-R22 to A02-L3-R41"]]
   list14=[["En-Suite Single (Super Premium - Triple)"],["Code: ESS3"],["Dimensions: 160+ sqft"],["Pricing: RM700"],["Number of Rooms: 20"],["Apartment ID: A02-L4-R1 to A02-L4-R41"]]
   list15=[["En-Suite Single (Super Premium - Twin)"],["Code: ESS2"],["Dimensions: 140+ sqft"],["Pricing: RM800"],["Number of Rooms: 20"],["Apartment ID: A02-L4-R1 to A02-L4-R41"]]
   list16=[["En-Suite Twin (Super Premium)"],["Code: EST2"],["Dimensions: 200+ sqft"],["Pricing: RM900"],["Number of Rooms: 20"],["Apartment ID: A02-L5-R1 to A02-L5-R41"]]

   #Apply data at the list
   record.append(list1)
   record.append(list2)
   record.append(list3)
   record.append(list4)
   record.append(list5)
   record.append(list6)
   record.append(list7)
   record.append(list8)
   record.append(list9)
   record.append(list10)
   record.append(list11)
   record.append(list12)
   record.append(list13)
   record.append(list14)
   record.append(list15)
   record.append(list16)
   
   with open("Apartment.txt","r") as Ahandler:
      for item in Ahandler:
         print(item.rstrip().rstrip(","))

def searchBox():                             #Define search function
   print("\nWelcome to search box!")
   while True:
      print("\n1. Search room specific details.\n2. Search transaction details\n3. Search specific tenant details\n\n4. Exit search box\n")
      option=int(input("Please type the search number based on the listing above:"))
      print("\n Please type the search criteria based on the keywords below:")
      if option == 1:
         listCode= "a"
         opt = input("\n[A]-Apartment code, [P]-Pricing\n")     
         if opt in ["A","a"]:
            print("\nSR1,SR2,SR3,SR4,DR1,DR2,DR3,DR4,CPS,MPS,MPT,MP1,MP2,ESS3,ESS2,EST2")
            num = 1
         elif opt in ["P","p"]:
            print("\nRM350,RM450,RM550,RM650,RM690,RM700,RM750,RM800,RM840,RM890,RM900,RM940,RM950,RM1040,RM1050")
            num = 3
         else:
            code = 0
            message(code)
      
      elif option == 2:
         listCode = "p"
         opt = input("NEWLINE [R]-Reference number,[D]-Transaction date,[T]-TenantID,[A]-Apartment code,[S]-Amount")
         if opt in ["R","r"]:
            num = 0
         elif opt in ["D","d"]:
            num = 1
         elif opt in ["T","t"]:
            num = 2
         elif opt in ["A","a"]:
            print("NEWLINE SR1,SR2,SR3,SR4,DR1,DR2,DR3,DR4,CPS,MPS,MPT,MP1,MP2,ESS3,ESS2,EST2.... NEWLINE Please enter the apartment code to begin the search: ")
            num = 3
         elif opt in ["S","s"]:
            num = 4
         else:
            code = 0
            message(code)     
      
      elif option =='3':
         listCode = "t"
         opt = input("NEWLINE [N]-Name,[G]-Gender,[P]-Phone number,[R]-Nationality,[D]-Rental start date,[I]-Income,[S]-Tenant status")
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
         print("\nReturn to main menu\n\n--------------------------------")
         return False                                 #return to menu function
      
      else:
         code = 0
         message(code)
      searchInformation(listCode,num)

def searchInformation(listCode,num):                  #Define searchinformation function
   if listCode == "p":
      l="transaction.txt"
   elif listCode=="a":
      l="Apartment.txt"
   else:
      l="tenant.txt"   
   while True:
      searchinformation=input("Select and enter text to begin search: ")

      with open(l,"r") as Xhandler:
         for record in Xhandler:
            strippeditem=record.rstrip()
            data=strippeditem.split(", ")
            if searchinformation in data[num]:
               print("\nResults:\n",record)

      exitSearch=input("Exit program? Enter any key to exit, Enter 'C' to continue.")
      if exitSearch in ["C","c"]:
         continue
      else:
         return False

def menu(masterKey):                                  #Define menu function
   print("\n- Welcome back, you are now entering Tenant Management System -")
   while True:
      print("\n[S]-Search box\nReview information about:\n")

      if masterKey == False:
         print("[A]-Apartment\n[P]-Transaction\n[T]-My Tenant details\n\n[D]-Print my House and Tenant Details\n[E]-Exit\n")
      else:
         print("[A]-Apartment\n[P]-Transaction\n[T]-Tenant\n\n[D]-Print Specific House & Tenant Details\n[I]-Inquiry of Past Tenant Details\n[L]-Login History\n[E]- Exit\n")

      opt=input("\nPlease select which operation that you want to do: ")

      if opt in ["S","s"]:
         searchBox()
      #Check for basic Functions
      elif opt in ["A","a"]:
         if masterKey == False:
            tenantApartment()
         else:
            adminApartment()
      
      elif opt in ["P","p"]:
         print("transaction(masterKey)")
      
      elif opt in ["T","t"]:
         tenant(masterKey)
      #Check for quick functions
      elif opt in ["D","d"]:
         print("tenantAndApartment()")
      
      elif opt in ["I","i"] and masterKey == True:
         details = "past"
         print("searchTenant(details)")
      
      elif opt in ["L","l"] and masterKey == True:
         print("loginHistory()")

      elif opt in ["E","e"]:
         print("\nThank you for using, have a nice day~\n")
         return False

      else:
         code = 3
         message(code)


login()
