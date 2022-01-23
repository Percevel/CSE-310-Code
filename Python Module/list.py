from item import item

class list():
    def __init__(self):
        self.lenList = 0
        self.tdList =[]
        self.openList()
        self.start(True)
            
    def start(self, kG):
        #starts the list program
        keepGoing = kG
        if keepGoing == False:
            return False

        print("Welcome to the ToDoList! Here are some options for you:\n")
        print("1. print your todolist")
        print("2. check items off your list")
        print("3. add / remove items to your list")
        print("4. start a new list")
        print("5. exit\n")

        #asks for your choice and then uses a match case to decide the action
        choice = input("your choice?: ")
        print("\n")
        match choice:
            case "1":
                self.printList()
            case "2":
                self.checkItem()
            case "3":
                print("1. add to the list")
                print("2. remove from the list")
                choice = int(input("your choice?: "))

                match choice:
                    case 1:
                        self.addItem()
                    case 2:
                        self.remItem()
            case "4":
                self.tdList = []
            case "5":
                print("Come again!")
                self.saveList()
                keepGoing = False
        self.start(keepGoing)

        

    def checkItem(self):
        #asks for an input for the new item
        checkPos = int(input("Which item would you like to be checked"))
        self.tdList[checkPos].check()

        #asks the user if they wanna keep on goin
        print("would you like to keep on going?")
        print("1 for yes, 2 for no")
        ans = int(input("wanna keep on checking? "))
        match ans:
            case 1:
                self.checkItem()
            case 2:
                print("Back to main")

    def addItem(self):
        adder = input("what's the todo task you want to add?: ")

        new = item(adder)
        self.tdList.append(new)

        print("would you like to keep on going?")
        print("1 for yes, 2 for no")
        ans = int(input("wanna keep on adding? "))
        match ans:
            case 1:
                self.addItem()
            case 2:
                print("Back to main")

    def remItem(self):
        #asks what item you want away
        remPos = int(input("What item u want away homie"))
        self.tdList.pop(remPos)

        #asks if the user wants to continue
        print("would you like to keep on going?")
        print("1 for yes, 2 for no")
        ans = int(input("wanna keep on removing? "))
        match ans:
            case 1:
                self.remItem()
            case 2:
                print("Back to main")
    
    def printList(self):
        #prints the list
        for line in self.tdList:
            print(f'{self.tdList.index(line)}. [{line.retCheck()}] - {line.getVal()}')

    def saveList(self):
        data = ""

        #writes the save data for the readme.txt. The items are split with ", " and the ":" splits the items and the checkmarks up
        for line in self.tdList:
            data += f'{line.getVal()}, '
        
        data += ":"
        for line in self.tdList:
            data += f'{line.isCheck()}, '

        f = open("TODOLIST.txt", "w")
        f.write(data)
        f.close()
    
    def openList(self):
        #opens up the TODOLIST.txt file and reads thru it
        with open("TODOLIST.TXT") as f:
            contents = f.read()
        
        #splits the list in to halves, one side is the item value, and the others is wether the item is checked off.
        tempList = contents.split(":")
        #splits each of the two halves up and puts them into lists
        listItems = tempList[0].split(", ")
        isChecked = tempList[1].split(", ")

        #these fill the list up to be used for the program, and goes thru the list and checks if the items are checked off
        for thing in listItems:
            self.tdList.append(item(thing))

        ind = 0
        for thing in isChecked:
            if thing == "True":
                self.tdList[ind].check()
            ind += 1

        #there's a straggler at the end so I'm removing it
        self.tdList.pop()