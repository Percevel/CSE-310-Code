#class named item, this represents every item on the todo list.
class item():
    def __init__(self, val):
        self.val = val
        self.checkmark = False

    def getVal(self):
        #returns value or the thing todo on the list
        return self.val
    
    def isCheck(self):
        #returns whether the list itself is checked off
        return self.checkmark
    
    def retCheck(self):
        #returns the value of the checkmard if it is checked
        if self.checkmark:
            return "✓"
        else:
            return " "

    def check(self):
        #checks off the list as done
        self.checkmark = True
