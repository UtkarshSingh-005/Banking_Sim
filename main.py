import pandas as pd
df = pd.read_excel('banking data sim.xlsx')
Accnumber = list(df.AccNumber)
Name = list(df.Name)
Balance = list(df.Balance)
Pin = list(df.Pin)
#df.drop('Pin',axis=1)
#df.drop('AccNumber',axis=1)
#df.drop('Balance',axis=1)
#df.drop('Name',axis=1)
#keys = ['AccNumber','Name','Balance','Pin']
#values = list(zip(Accnumber, Name, Balance, Pin))
#my_dup = dict(zip(keys, values))
print("\n\n""\t\t""Welcome to A Banking Simulator""\n\n")
termi =1
while termi==1:
  number = int(input("Enter Your *6 digit* Account Number : "))
  for i in range(99):
    if (int(Accnumber[i]) == number):
      print("\n\n""\t\t""Welcome! ",Name[i],"\n")
      print("Our Services :""\n""1. Withdrawl""\n""2. Deposit""\n""3. Balance Enquiry""\n""4. Close""\n")
      num = input("Please enter your service number : ")
      if num=='1':
        print("\n\n""processing...""\n""please wait""\n""Your request for withdrawl is processing...""\n")
        amt = int(input("Amount : "))
        secpin = int(input("Enter your pin : "))
        if secpin == Pin[i]:
           print("\n""Please collect your money""\n\n""\t\t""Have a nice day :) ")
           amt = int(Balance[i])-amt
           Balance[i]=str(amt)
        else:
          rng = [2,1,0]
          for i in rng:
            print("Invalid Transaction")
            print(i," attempts left..")
            if i==0:
              print("Sorry transaction Failed :( ")
            else:
              secpin = int(input("Enter your pin : "))
              if secpin == Pin[i]:
                print("\n""Please collect your money""\n\n""\t\t""Have a nice day :) ")
                amt = int(Balance[i])-amt
                Balance[i]=str(amt)
                break
              else:
                continue
      elif num=='2':
        print("\n\n""processing...""\n""please wait""\n""Your request for deposit is processing...""\n")
        amt = int(input("Amount : "))
        secpin = int(input("Enter your pin : "))
        if secpin == Pin[i]:
           print("\n""Thanks for deposit ""\n\n""\t\t""Have a nice day :) ")
           amt = int(Balance[i])+amt
           Balance[i]=str(amt)
        else:
          rng = [2,1,0]
          for i in rng:
            print("Invalid Transaction")
            print(i," attempts left..")
            if i==0:
              print("Sorry transaction Failed :( ")
            else:
              secpin = int(input("Enter your pin : "))
              if secpin == Pin[i]:
                print("\n""Thank you Your Transaction is processed sucessfuly :) ""\n\n""\t\t""Have a nice day :) ")
                amt = int(Balance[i])-amt
                Balance[i]=str(amt)
                break
              else:
                continue
      elif num=='3':
        secpin = int(input("Enter your pin : "))
        if secpin == Pin[i]:
          print("Your available balance : ", Balance[i])
        else:
           rng = [2,1,0]
           for i in rng:
             print("Invalid Transaction")
             print(i," attempts left..")
             if i==0:
               print("Sorry transaction Failed :( ")
             else:
               secpin = int(input("Enter your pin : "))
               if secpin == Pin[i]:
                 print("\n""Thank You.. :) ""\n\n""\t\t""Have a nice day :) ")
                 amt = int(Balance[i])-amt
                 Balance[i]=str(amt)
                 break
               else:
                 continue
      else:
        print("\n\n""Thank for your visit :) ")
        break
    else:
      continue
  coun = input("\n\n""Do you want to continue ?""\n""Press any key to continue & 1 to stop : ")
  if coun != '1':
    termi = 1
  else:
    termi = 0
print("\n\n\n""Please visit again...  :) ")
#df = pd.DataFrame(my_dup)
#file_path = '/content/drive/MyDrive/banking sim/banking data sim.xlsx'
#df.to_excel(file_path,index= False)
