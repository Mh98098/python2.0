#Question 1: 
BillAmount = float(input("Enter the total  bill amount: "))
tip_per = float(input("Enter the tip percentage you want to leave: "))
No_of_People = int(input("Enter the people splitting the bill: "))
total_tip = tip_per*BillAmount/100
billwithTip = total_tip+BillAmount
per_person = billwithTip/No_of_People
print(total_tip)
print(billwithTip)
print(per_person)

#Question 2: 
passw = input("Enter a password: ")
if ((len(passw)) >= 8) and (passw.isupper() == True) and (passw.islower() ==True) and (passw.isdigit() == True):
    print("Password is Strong.")
elif ((len(passw)) >= 6) and ((passw.isdigit() == False) or (passw.isupper() == False)):
    print("Password is Moderate.")
else:
    print("Password is Weak.")

#Question 3: 
Secret = 10
count = 0
while count < 5:
    guess_no = int(input("Guess the Number: "))
    if guess_no < 1 or guess_no > 100:
        print("invalid")
        continue
    elif guess_no == Secret:
        print(" You won!")
        break
    count = count+1
else:
        print("You lost.")

#Question 4: 
full_name = input("Enter full name: ")
a = 0
for i in full_name:
    if i == " ":
        break
    else:
        a = a+1
        string1 = full_name[:a]
print(string1)
b=0
for i in full_name:
    if i != " ":
        b = b+1
        continue
    else:
        string2= full_name[b:]
total = len(full_name)
print("First name:", string2)
print("The initials:", string1[0] ,string2[0])
print(full_name.upper())
print(full_name[::-1])

#Question 5: 
balance = 11000
def deposit(amount):
    global balance
    balance = balance + amount

def withdraw(amount):
    global balance
    if amount > balance:
        print("low balance.")
        return
    balance = balance - amount

deposit(5000)
withdraw(1000)
print("Bank balance:", balance)

#Question 6: 
sentence = input("Enter a sentence: ")
tot_count = len(sentence)
set1 = {*sentence}
unique = len(set1)
print("unique characters:", unique)
print("Set of unique characters:", set1)
print("Total count:" , tot_count)

#Question 7:
dictionary1 = {"Ali" : 45, "Umair" : 97 , "Khan" : 69 , "Amir" : 43}
for name_of_student,score in dictionary1.items():
    if score >= 90:
        print("A grade.")
    elif score >= 80:
        print(" B grade.")
    elif score >= 70:
        print(" C grade.")
    else:
        print(" F grade.")