#...............conditional statement.......................

#..1.......for tickent booking..........
age = int(input("enter the age:"))
if age < 12:
    print("Your ticket is free")
elif age > 12 and age < 60:
    member = input("Do you have a membership card, yes/no?")
    if member == "yes":
        print("Your ticket cost Rs. 150")
    else:
        print("Your ticket cost Rs. 200")  
else:
    print("congratulation!! You got a senior citizen discout and your ticket cost Rs. 100")



#....2...for electricity bill...........
usage = int(input("Enter your electricity usage in units:"))
if(usage <= 100):
    amount = usage*5
elif(usage > 100 and usage < 300 ):
    use = usage - 100
    amount = use*8 + 100*5
else:
    billUse = usage - 300
    amount = 100*5 + 200*8 + billUse*10
print(f"the rate for {usage} units is: {amount}")


#.......3.........resturant bill................
total_bill = int(input("Enter the total bill:"))
premium_customer = input("Are you a premium customer, yes/no? ")
if(total_bill >= 1000 and total_bill < 2000):
    if(premium_customer == "yes"):
      amount = total_bill - (total_bill*(15/100))
    else:
      amount = total_bill - (total_bill*(10/100))
    print(f"Your bill amount of {total_bill} is {amount}")
elif(total_bill >= 2000):
    if(premium_customer == "yes"):
        amount = total_bill - (total_bill*(20/100))
    else:
        amount = total_bill - (total_bill*(15/100))
    print(f"Your bill amount of {total_bill} is {amount}")
else:
   amount = total_bill
   print(f"Your bill amount of {total_bill} is {amount}")


#.....4...online shopping discount system...........
purchase_amount = int(input("Enter the purchase amount:"))
prime_member = input("Are you a prime member, yes/no ? ")
if(purchase_amount > 2000 and purchase_amount < 5000):
    if(prime_member == "yes"):    
        price = purchase_amount - (purchase_amount*(10/100))
    else:
        price = purchase_amount - (purchase_amount*(5/100))    
   
elif(purchase_amount > 5000):
    if(prime_member == "yes"):
        price = purchase_amount - (purchase_amount*(20/100))
    else:
        price = purchase_amount - (purchase_amount*(10/100))   
else:
    price = purchase_amount
print(f"Your bill with discounted price of {purchase_amount} is {price}")
   

#.....5.....grading system...........
marks = int(input("Enter your marks: "))
project_work = input("Do you have a project work, yes/no ? ")
if(project_work == "yes"):
    marks += 5
    if(marks >=90):
        print('You are graded by "A" grade')
    elif(marks >= 75 and marks < 90):
        print('You are graded by "B" grade')
    elif(marks >=60 and marks < 75):
        print('You are graded by "C" grade')
    else:
        print("You are failed")
else:
    if(marks >=90):
        print('You are graded by "A" grade')
    elif(marks >= 75 and marks < 90):
        print('You are graded by "B" grade')
    elif(marks >=60 and marks < 75):
        print('You are graded by "C" grade')
    else:
        print("You are failed")


#......6.......mobile recharge offer........
recharge_amount = int(input("Enter your rechanrge amount: "))
vip = input("Are you a VIP user, yes/no ? ")
if(recharge_amount >= 1000):
    if(vip == "yes"):
        amount = recharge_amount + (recharge_amount*(20/100))
    else:
        amount = recharge_amount + (recharge_amount * (10/100))
else:
    if(vip == "yes"):
        amount = recharge_amount + (recharge_amount * (5/100))
    else:
        print("You have no extra talk time")
print(f"your talk time is for Rs.{amount}")


#....7.......Hotel room booking system..........
stay_night = int(input("Enter the number of nights you stay on hotel:"))
room_type = input("Enter your room type, deluxe/standard ? ")
if(room_type == "deluxe"):
    if(stay_night > 5):
        charge = stay_night * 5000
        total_charge = charge - (charge*(20/100))
    else:
        total_charge = stay_night*5000
else:
    if(stay_night > 5):
        charge = stay_night * 3000
        total_charge = charge - (charge * (10/100))
    else:
        total_charge = stay_night * 3000
print(f"You stayed {stay_night} in our hotel your total charge is {total_charge} ")


#....8.......vehicle insurance premium calculator.............
vehicle_type = input("What is your vehicle type, Car/Bike ? ")
time = input("Is your vehicle is more than 5 years, yes/no ? ")
owner_claim = input("Have you a claim bonus, yes/no ? ")
if(vehicle_type == "Car"):
    if(time == "yes"):
        if(owner_claim == "yes"):
            premium = 4000 + (4000 * (10/100))
        else:
            premium = 4000 - (4000 * (20/100))
    else:
        premium = 4000
else:
    if(time == "yes"):
        if(owner_claim == "yes"):
            premium = 2000 + (2000 * (10/100))
        else:
            premium = 2000 - (2000 * (20/100))
    else:
        premium = 2000
print(f" Your final premium is {premium}")


#.............income tax calculator.............

# income = input("Say what's your income is: ")
# i have confusion in question
