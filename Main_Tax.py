from copy import deepcopy
from tabnanny import check
from Node_Tax import *
from Payer import *
from Linklist_Tax import *


class Main:
    Mylist = mylist()

# 1.
    def load_data_from_file(self, file: str, delimiter: str = ";"):
        while True:    
            try:
                with open(file, "r") as f:
                    for i in map(
                        lambda lst: map(lambda char: char.strip(), lst),
                        map(lambda line: line.split(delimiter),
                            filter(None, f.read().splitlines()))
                    ):
                        # lst = tuple(i)
                        code, name, income, deduction = i
                        code, name, income, deduction = (
                            code,
                            name,
                            float(income),
                            float(deduction),

                        )
                        node = Node(Payer(code, name, income, deduction))
                        self.Mylist.add_to_End(node)
                print("Loading file successfully!!!")
                return self.Mylist
            except:
                print(f'File: "{file}" not found')
                break
            

# 2.
    def add_Last(self):
        while True:
            try:
                code = input("Enter the code for tax payer: ").strip()
                if code == "":
                    break
                elif self.search_Code(code) != "Can't find":
                    print(f"Already have this {code} code payer in system")
                    continue
                name = input('Enter the name of tax payer: ').strip()
                income = float(
                    input("Enter the income of this payer: ").strip())
                deduction = float(
                    input("Enter the deduction for this payer: ").strip())
                if deduction > income:
                    continue
                payer = Payer(code, name, income, deduction)
                self.Mylist = self.addData_last(payer)
                return True
            except:
                print("Something wrong")
                break
        return True

    def addData_last(self, payer: Payer):
        node = Node(payer)
        self.Mylist.add_to_End(node)
        return self.Mylist

# 3.
    def display(self):
        space = 15
        first_line = "| {} | {} | {} | {} | {} |".format("Code".center(8), "Name".center(20), "Income".center(10),
                                                         "Deduction".center(12), 'Tax'.center(10))
        separate_line = "-" * space * 5
        detail = ""
        for node in self.Mylist:
            code = node.data.code
            name = node.data.name
            income = node.data.income
            deduction = node.data.deduction
            tax = node.data.tax
            detail += f"|{code.center(10)}|{name.center(22)}|{str(income).center(12)}|{str(deduction).center(14)}|{str(tax).center(12)}|\n"
        table = f"{first_line}\n{separate_line}\n{detail}"
        return table
# 4.
    #####load another file
    def save_Data(self, filename: str):
        with open(filename, "w") as f:
            f.write(self.display())
            print("Save file successfully!!!")
        return f

# 5.
    def search_Code(self, code: str):
        find = self.Mylist.Search(code)
        if find:
            return ("| {} | {} | {} | {} | {} |".format(find.code.center(8), find.name.center(20), str(find.income).center(10), str(find.deduction).center(12), str(find.tax).center(10)))
        return "Can't find"
# 6.

    def deleteData_Code(self, code: str):
        d = self.Mylist.del_by_Code(code)
        if code == '':
            return True
        if not self.Mylist.Search(code):
            return (f"Delete {d.code} sucessful")
        else:
            return "Can't delete"

# 7.
    def sort_code(self):
        temp = deepcopy(self.Mylist)
        self.Mylist.sort_by_Code()
        print(self.display())
        self.Mylist = temp

# 8.
    def add_First(self):
        while True:
            try:
                code = input("Enter the code for tax payer: ").strip()
                if code == "":
                    break
                elif self.search_Code(code) != "Can't find":
                    print(f"Already have this {code} code payer in system")
                    continue
                name = input('Enter the name of tax payer: ').strip()
                income = float(
                    input("Enter the income of this payer: ").strip())
                deduction = float(
                    input("Enter the deduction for this payer: ").strip())
                if deduction > income:
                    continue
                payer = Payer(code, name, income, deduction)
                self.Mylist = self.addData_first(payer)
                return True
            except:
                print("Something wrong")
                break
        return True

    def addData_first(self, payer: Payer):
        node = Node(payer)
        self.Mylist.add_to_Begin(node)
        return self.Mylist

# 9.
    def addAfterk(self, payer: Payer, key):
        node = Node(payer)
        self.Mylist.addAfterIndex(node, key)
        return self.Mylist

    def addDT_after_k(self, key):
        while True:
            try:
                code = input("Enter the code for tax payer: ").strip()
                if code == "":
                    break
                elif self.search_Code(code) != "Can't find":
                    print(f"Already have this {code} code payer in system")
                    continue
                name = input('Enter the name of tax payer: ').strip()
                income = float(
                    input("Enter the income of this payer: ").strip())
                deduction = float(
                    input("Enter the deduction for this payer: ").strip())
                if deduction > income:
                    continue
                payer = Payer(code, name, income, deduction)
                self.Mylist = self.addAfterk(payer, key)
                return True
            except:
                print("Something wrong")
                break
        return True

# 10.
    def del_k(self, key):
        self.Mylist.DelIndex(key)
        return self.Mylist


linklist = Main()
Mylist = mylist()


# display
List = '''
    1. Load data from the file 
    2. Input & add to the end
    3. Display data
    4. Save data to the file
    5. Search by code
    6. Delete by code
    7. Sort by code
    8. Input & add to the beginning
    9. Add after position k
    10. Delete position k
    0. Exit
'''
print()
print("      Income tax calculation         ")


while True:
    print(List)
    choice = str(input('Your selection (0 -> 10): '))
    print()
    if choice == '0':
        print("Thank you")
        print()
        break

    elif choice == '1':
        check1=[]
        while True:    
            file = input("Enter file name: ")
            if file not in check1:
                linklist.load_data_from_file(file)
                print()
                check1.append(file)
                break
            elif file in check1:
                continue
            
    elif choice == '2':
        linklist.add_Last()
        print("Add successfully")
        print()
    elif choice == '3':
        print(linklist.display())
        print()

    elif choice == '4':
        filename = input("Enter filename to save: ")
        linklist.save_Data(filename)
        print()

    elif choice == '5':
        search = input("Enter the code of payer you want to search: ")
        print(linklist.search_Code(search))
        print()

    elif choice == '6':
        dele = input('Enter the code of payer you want to delete: ')
        print(linklist.deleteData_Code(dele))
        print()

    elif choice == '7':
        print("List after sort:")
        print()
        linklist.sort_code()
        print()

    elif choice == '8':
        linklist.add_First()
        print()

    elif choice == '9':
        while True:
            try:
                key = int(input("Enter the position k: "))
                linklist.addDT_after_k(key)
                print("Add successfully")
                print()
                break
            except:
                print("Invalid input")
                break

    elif choice == '10':
        while True:
            try:
                key1 = int(input('Enter the position k: '))
                linklist.del_k(key1)
                print(f" List after deleting node at position {key1}: ")
                print()
                print(linklist.display())
                print()
                break
            except:
                print("Invalid input")
                break
