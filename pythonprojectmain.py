#Expense Tracker Project

expensesList = [] #list of expenses in form of dictionary
print(" Welcome to Expense Tracker : Khrcha kam kiya karo ")

while True:
    print ("====MENU====")
    print ("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice : "))

#ADD Expense    
    if (choice ==1):
        date= input("Kis date par khrcha kiya tha?: ")
        category= input("Kis type ka khrcha kiya? (Food, Travel, Makeup, Books): ") 
        description= input("Aur detail dedo: ")
        amount= float(input("Enter the amount:"))

        expense = {  
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }

        expensesList.append(expense)
        print(" \n DONE bro. Expense is added successfully")

# 2. VIEW ALL EXPENSES
    elif(choice == 2):
        if (len(expensesList)==0 ):
            print("No Expenses Added. Jao pehle khrcha karo. ")
        else:
            print("=====Ye h apka sara expense =====")
            count=1
            for eachkhrcha in expensesList:
                print(f"khrcha Number {count} -> {eachkhrcha["date"]}, {eachkhrcha["category"]}, {eachkhrcha["description"]}, {eachkhrcha["amount"]}")
                count= count+1 
# 3. View TOtal Spending
    elif (choice == 3):
        total= 0
        for eachKhrcha in expensesList:
            total = total + eachkhrcha["amount"]
        
        print("\n TOTAL KHRCHA = ", total)

# 4. EXIT
    elif(choice == 4):
        print("Dhanyawad aapne humara system use kiya")
        break

    else:
        print("INVALID CHOICE, TRY AGAIN")