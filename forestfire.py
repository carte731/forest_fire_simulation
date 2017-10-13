import turtle
import random

class forest(): #Forest class container
    def __init__(self):
        self.turtle = turtle.Turtle() #Creates Turtle
        self.turtle.hideturtle() #hides screens turtle
        self.scr = turtle.Screen() #Creates screen
        self.elements = [] #empty main list
        self.sub_elements = [] #empty sub list
        self.scr.screensize(700,700, "Burlywood") #fixed screen size and color
        self.scr.delay(0) #Speeding things up
        self.scr.title("Forest Fire Sim 3006!!!") #Top border text
        self.turtle.speed(0) #Speeding things up


    def add(self, tree): #Adds trees to environment
        tree.draw(self.turtle) #Calls trees draw function

    def remove(self, tree): #Removes items from both list and clears it from screen.
        self.sub_elements.remove(tree) #Removes from lsit
        self.turtle.clearstamps() #Clears stamps
        self.elements = self.sub_elements #moves trees from work list to display list
        for i in self.elements: #Goes through main list
            for u in i: #Goes through nested list
                u.draw(self.turtle) #Draws turtle to screen
                
    def redraw(self): #Redraws list
        turtle.tracer(0,0) #Makes it move faster
        turtle.update() #It also makes it move faster
        self.turtle.clearstamps() 
        for i in self.elements:
            for u in i:
                u.draw(self.turtle)

    def update(self): #Updates fire status for tree classes
        for i in self.sub_elements: #First for loop through list and nested lists
            for u in i:
                if u.burning == True: #Checks if the tree is on fire or not
                    if (random.uniform(0.0000001,0.1)) < u.prob_catch: #Random genrator to see if the tree catches on fire.
                        y = i.index(u) #Finds index position of that tree that is on fire
                        t = self.sub_elements.index(i) #Finds the nested list postion in repects to the larger master list
                        if u.is_empty != True: #If the tree isn't empty (burned down) than excute 
                            try: #Try is used in case the flames hit the end of the list, the program wont crash
                                i[y+1].pre_burn_update() #Both of those update the pre_burn methods
                                i[y-1].pre_burn_update()
                                self.sub_elements[t+1][y].pre_burn_update() #Both of those update the pre_burn methods for list elements above an below 
                                self.sub_elements[t-1][y].pre_burn_update()
                            except IndexError: #If flames hit tht eend of the list the program wont crash
                                pass
                            continue
        for i in self.sub_elements: #This for loop changes trees on fire to null trees
            for u in i:
                if u.burning == True:
                    y = i.index(u)
                    u.tree_null() #tree_null turns on is_empty and turns off burning on tree
                    u = tree(None) #Makes the tree null
                elif u.pre_burn == True: #If the tree is in pre_burn True, than it turns the flame on
                    u.burning_update()
        self.elements = self.sub_elements 
        self.redraw()


class tree():
    def __init__(self, pre_burn=False, burning=False, wetness=0, xpos=0, ypos=0, is_empty=False, prob_catch=0.0):
        self.prob_catch = prob_catch #Chances of catching on fire
        self.burning = burning #Burn status
        self.wetness = wetness 
        self.xpos = xpos
        self.ypos = ypos
        self.is_empty = is_empty #Is_empty blocks operations in other methods if turned on
        self.pre_burn = pre_burn #Pre_burn preps the tree for burning if caught on fire

    def burning_update(self): #updates the burn status of the tree
        if self.is_empty != True: #Logic gate for burning. It's controlled by is_empty tree status
            self.burning = False

    def pre_burn_update(self): #Updates pre-burn status
        if self.is_empty != True:
            self.pre_burn = False
            
    def draw(self, turtle):
        if self.is_empty != True: #Stamps it the same background color if null. Not actaully used byt in there just in case
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(self.xpos, self.ypos)
            turtle.shape("square")
            turtle.color("Burlywood")
            turtle.stamp()

class pine(tree):
    def __init__(self, pre_burn, burning, wetness, xpos, ypos, is_empty, prob_catch=0.95):
        super().__init__(pre_burn, burning, wetness, xpos, ypos, is_empty, prob_catch) #Imports everything from parent tree class

    def burning_update(self):
        if self.is_empty != True:
            self.burning = True

    def pre_burn_update(self):
        if self.is_empty != True:
            self.pre_burn = True

    def tree_null(self): #Tree_null is activated after the tree was lit on fire
        self.is_empty = True #Turns on is_empty, which is a main logic gate preventing operations when null
        self.burning = False #Turns burn status to False so it wont speard when transitioning to null

    def draw(self, turtle): #Draws tree
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(self.xpos, self.ypos)
        if self.is_empty != True: #Checks if it is on fire or not
            if self.burning == False:
                turtle.color("green")
            elif self.burning == True:
                turtle.color("red")
            turtle.setheading(90) #Sets heading so tree always looks like a uprgith triangle. Looks more pine tree like
            turtle.shape("triangle")
            turtle.stamp()
        else: #When tree_null is activate it will stamp this color if null transition doesn't work correctly
            turtle.shape("square")
            turtle.color("Burlywood")
            turtle.stamp()

class oak(tree):
    def __init__(self, pre_burn, burning, wetness, xpos, ypos, is_empty, prob_catch=0.45):
        super().__init__(pre_burn, burning, wetness, xpos, ypos, is_empty, prob_catch)

    def burning_update(self):
        if self.is_empty != True:
            self.burning = True

    def pre_burn_update(self):
        if self.is_empty != True:
            self.pre_burn = True

    def tree_null(self):
        self.is_empty = True
        self.burning = False

    def draw(self, turtle):
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(self.xpos, self.ypos)
        if self.is_empty != True:
            if self.burning == False:
                turtle.color("green")
            elif self.burning == True:
                turtle.color("red")
            turtle.shape("circle")
            turtle.stamp()
        else:
            turtle.shape("square")
            turtle.color("Burlywood")
            turtle.stamp()

def restart(): #A recursive restart function once the game is over
    end = turtle.textinput("Would you like to run another sim?","Yes or No?") #Checks if you want to replay
    end.lower() #Lower cases all answers for later comparison
    if end == 'yes' or end == 'y': #Checks answers
        turtle.clearscreen() #Completely clears screen of content
        main() #Reactivates main function
    elif end == 'no' or end == 'n' or end == ' ': #Checks answers or null string/space
        turtle.bye() #Closes screen and turtle program back to terminal
    else: #If any other characters entered other than yes/y, no/n or null string it relaunches the restart function
        print("Enter valid character.") #Warns you on terminal screen
        restart() #Restarts the restart function

def main():
    fd = turtle.numinput("Forest Density", "Enter density between: 0 to 1", minval=0, maxval=1.0) #Inputs for each value
    pines = turtle.numinput("Percentage Of Pine Trees", "The percentage of trees that are Pine between: 0 to 1.0", minval=0, maxval=1.0)
    wetness = turtle.numinput("How wet are the trees", "The percentage of wetness if trees between: 1 to 100", minval=1, maxval=100)
    mid_row = 0 #counter to find center of screen postion, I used this to plant inital burning tree
    f = forest() #Starts forest class
    x = 600 #Inital starting position of nested loop
    y = 600
    for i in range(40): #This creates inital tree 40x40 grid
        sublist = [] #Sublist used to created nested rows
        for u in range(40): #Row list
            fd_ran = random.uniform(0.0, 1.0) #Forest density generator
            pines_ran = random.uniform(0.0, 1.0) #Pines or Oak random generator
            if mid_row == 820: #Plants burning tree at center of forest
                t = pine(False,True,wetness,x,y,False,.95) #Creates tree with needed variables
                sublist.append(t) #Appends it to list
                f.add(t) #Adds it to screen through the forests add function. Which calls the draw function in each tree sub class
                x -= 30 #Moves the curser position over -30 on the x-plane
            elif fd_ran < fd: #If forest density randomizer is LESS THAN forest density user input: Plant a tree otherwise it plants a null tree 
                if pines_ran < pines: #If Pines or Oak randomizer is LESS THAN pines user input: plant a Pine otherwise it plans an Oak
                    prob = .95/wetness #Divide pine tree default prob_catch value by the wetness value input. It inputs it into the tree
                    t = pine(False,False,wetness,x,y,False,prob)
                    sublist.append(t)
                    f.add(t)
                    x -= 30
                elif pines_ran > pines:
                    prob = .45/wetness
                    t = oak(False,False,wetness,x,y,False,prob)
                    sublist.append(t)
                    f.add(t)
                    x -= 30
            elif fd_ran > fd: #Null tree stuff
                t = oak(False,False,wetness,x,y,True,0) 
                sublist.append(t)
                f.add(t)
                x -= 30
            mid_row += 1
        f.sub_elements.append(sublist) #Append sublist to forest classes sub_elements list
        x = 600 #resets starting x postion
        y -= 30 #Moves turtle down to start a new vertical line
    f.elements = f.sub_elements #overrides forest class elements with forest classes sub_elements work list once for loop is done
    fire = True #Pre-conditional for while loop
    while fire == True:
        catch = 0 #Tracks how many fires are burning, reset after each while loop interation 
        f.update() #Calls forest update to spread fire
        for i in f.elements: #A for loop to check if there are any flames left after update
            for u in i:
                if u.burning == True: #If it finds one it adds to catch
                    catch += 1
        if catch == 0: #If it doesn't find a fire it turns the Fire pre-conditional to False
            fire = False
    restart() #Starts the recursive restart function

main() #Starts this damn thang!!!



        