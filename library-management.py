import ast
lst1 = []
lst2 = []

with open("storage_file.txt","r") as f:
    lst11 = f.readline()
    lst22 = f.readline()
    if lst11.strip() != "" :
        lst1 = ast.literal_eval(lst11)
    else:
        lst1 = []
    if lst22.strip() != "" :
        lst2 = ast.literal_eval(lst22)
    else:
        lst2 = []

class book_check:
    def __init__(self,name):
        self.name = name
    def show(self):
        if lst1 != [] :

            for val in lst1:
                if self.name == val["name"] and val["amt"] != 0:
                    return f"{self.name} is available, amount is {val['amt']}, price is {val['price']}"
                else:
                    continue
            else:
                return f"Book not available"
        else:
            return f"Book not available"
        

class book_add:
    def __init__(self,name,amount,price):
        self.name = name 
        self.amount = amount
        self.price = price
    def add(self):
        self.dit = {}
        if lst1 != [] :
            for val in lst1:
                if val["name"] == self.name :
                    val["name"] = self.name
                    val["amt"] += self.amount
                    val["price"] = self.price
                    return f"book added"
            else:
                self.dit["name"] = self.name
                self.dit["amt"] = self.amount
                self.dit["price"] = self.price
                lst1.append(self.dit)
                return f"new book {self.name} was added"
        else:
            self.dit["name"] = self.name
            self.dit["amt"] = self.amount
            self.dit["price"] = self.price
            lst1.append(self.dit)
            return f"new book {self.name} was added"

class book_borrow:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
    def borrow(self):
        if lst1 != [] :
            for val in lst1:
                if self.amount <= 0 and self.name == val["name"] :
                    return f"You can't enter zero or negative amount!"
                elif self.name == val["name"] and self.amount == val["amt"] :
                    val["amt"] -= self.amount
                    return f"You borrowed{self.name} and amount = {self.amount} and price = {val['price']*self.amount}"
                elif self.name == val["name"] and self.amount < val["amt"] and self.amount > 0:
                    val["amt"] -= self.amount
                    return f"You borrowed{self.name} and amount = {self.amount} and price = {val['price']*self.amount}"
                elif self.name == val["name"] and self.amount > val["amt"] :
                    return f"The amount of books you want to borrow is more than we have right now, we have only {val['amt']} books."
                else:
                    continue
            else:
                return f"Book not available"
        else:
            return f"Book not available"

class book_remove:
    def __init__(self,name):
        self.name = name
    def remove(self):
        for val in lst1:
            if self.name == val["name"] :
                lst1.remove(val)
                return f"The book {self.name} was removed"
        else:
            return f"{self.name} wasn't found!"


class member_check:
    def __init__(self,name):
        self.name = name
    def show_members(self):
        for val in lst2:
            if self.name == val["name"] :
                return f"name = {val['name']}, salary = {val['salary']} working hours = {val['working_hour']}"
        else:
            return f"Member not found!"

class member_add:
    def __init__(self,name,salary,working_hour):
        self.name = name
        self.salary = salary
        self.working_hour = working_hour
    def add(self):
        self.dit1 = {}
        for val in lst2:
            if self.name == val["name"] :
                val["salary"] = self.salary
                val["working_hour"] = self.working_hour
                return f"{self.name} data updated!"
        else:
            self.dit1["name"] = self.name
            self.dit1["salary"] = self.salary
            self.dit1["working_hour"] = self.working_hour
            lst2.append(self.dit1)
            return f"new member {self.name} was added!"

class member_remove:
    def __init__(self,name):
        self.name = name
    def remove(self):
        for val in lst2:
            if self.name == val["name"] :
                lst2.remove(val)
                return f"{val["name"]} is removed"
        else:
            return f"{self.name} is not in the library members"

#checking the books or members
ans2 = input("Do you wanna check any books or members or none?(books/members/none)")
ans_2 = ans2.lower()
if ans_2 == "books" :
    ans_22 = "y"
    while ans_22 == "y" :
        ans_second = input("Enter the books name")
        ans_sec = ans_second.lower()
        b_check = book_check(ans_sec)
        print(b_check.show())
        ans22 = input("Do you wanna check any books again?(y/n)")
        ans_22 = ans22.lower()
elif ans_2 == "members" :
    ans_4 = "y"
    while ans_4 == "y" :
        ans_fourth = input("Enter the member's name: ")
        ans_four = ans_fourth.lower()
        m_check = member_check(ans_four)
        print(m_check.show_members())
        ans4 = input("Do you want to check any member of library?(y/n)")
        ans_4 = ans4.lower()
elif ans_2 =="none" :
    print("No checking of books or members\n")


#adding the books or borrowing the books or removing
ans1 = input("DO you want to add books or borrow or remove or none?(add/borrow/remove/none)")
ans_first = ans1.lower()
if ans_first == "add" :
    ans_one = "y"
    while ans_one == "y" :
        in1 = input("Which book you want to enter?")
        in11 = in1.lower()
        in2 = int(input("How many books you want to enter?"))
        in22 = int(input("What is the price of the book?"))
        b_add = book_add(in11,in2,in22)
        print(b_add.add())
        anso = input("DO you want to enter the book again?(y/n)")
        ans_one = anso.lower()
elif ans_first == "borrow" :
    ans_3 = "y"
    while ans_3 == "y" :
        ans_third = input("what book you want to borrow?")
        ans_th = ans_third.lower()
        ans_num = int(input("How many books you want to borrow?"))
        b_borrow = book_borrow(ans_th,ans_num)
        print(b_borrow.borrow())
        ans3 = input("Do you want to borrow the any other books?(y/n)")
        ans_3 = ans3.lower()
elif ans_first == "remove" :
    ans_r = "y"
    while ans_r == "y" :
        ans_r1 = input("which book do you want to remove?")
        ans_r2 = ans_r1.lower()
        b_remove = book_remove(ans_r2)
        print(b_remove.remove())
        ans_r3 = input("Do you want to remove the book again?(y/n)")
        ans_r = ans_r3.lower()

elif ans_first == "none" :
    print("Neither added nor borrowed")


#adding the members or removing 
ans5 = input("Do you want to add the new member or remove?(add/remove/none)")
ans_5 = ans5.lower()
if ans_5 == "add" :
    ans_55 = "y"
    while ans_55 == "y" :
        ans_fifth = input("Enter the members name")
        ans_five = ans_fifth.lower()
        ans_fifth2 = int(input("Enter the members monthly salary"))
        ans_fifth3 = int(input("Enter the members working hours"))
        m_add = member_add(ans_five,ans_fifth2,ans_fifth3)
        print(m_add.add())
        ans555 = input("Do you want to add the new member again?(y/n)")
        ans_55 = ans555.lower()
elif ans_5 == "remove" :
    ans_6 = "y"
    while ans_6 == "y" :
        ans_sixth = input("Enter the name of the member you want to remove.")
        ans_six = ans_sixth.lower()
        m_remove = member_remove(ans_six)
        print(m_remove.remove())
        ans6 = input("Do you want to remove the another member too?(y/n)")
        ans_6 = ans6.lower()


#storing into the output_file.txt file
with open("storage_file.txt","w") as f:
    f.write(str(lst1)+"\n")
    f.write(str(lst2))

#display of books and members
with open("output_file.txt","w") as f:
    f.write("BOOKS"+"\n")
    f.write(f"{'NAME':<40}{'AMOUNT':<25}{'PRICE':<25}"+"\n")
    if lst1 != [] :
        for val in lst1 :
            f.write(f"{val["name"]:<40}{val["amt"]:<25}{val["price"]:<25}"+"\n")
    f.write("\n")
    f.write("\n")
    f.write(f"{"MEMBERS"}"+"\n")
    f.write(f"{'NAME':<40}{'SALARY':<25}{'WORKING HOURS':<25}"+"\n")
    if lst2 != [] :
        for val in lst2:
            f.write(f"{val["name"]:<40}{val["salary"]:<25}{val["working_hour"]:<25}"+"\n")
