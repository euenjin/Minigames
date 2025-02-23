# Statrts with diskNum disks on first tower
#Goal is to move all disks from self.tower[0] to self.tower [2]
#You cannot place bigger disk above lower disk
#Disk is represented with number
#Number of moved time is recorded.

#Number of disk is chosen by the user input
#Each turn, take begin tower and end tower from user
#If it is valid, it is placed
#Game continues until it is completely moved

class Tower_of_Hanoi:
    def __init__(self,diskNum,count):
        self.diskNum=diskNum
        self.tower=[[],[],[]]
        self.count=count
        self.disk=0
        self.ind=0
#Initialize Tower and Other Features

    def printBoard(self):
        max_height=max(len(tower) for tower in self.tower)
        for i in range(max_height):
            for j in range(3):
                if(self.tower[j][i]==None):
                    print("  *  ", end=" ")
                elif i < len(self.tower[j]):
                    print(f"  {self.tower[j][i]}  ", end=" ")  
            print()
        print(" ___   ___   ___")  

#Function to print tower that first element of the list is printed on top   None is represented with "*"


    def initializeTower(self):

        if(self.diskNum>6): 
            print("Are you sure? It will be hard to complete.")
            keepGoing=input("If you want to challenge your self, enter 'y'. Else press any button")

            if(keepGoing != "y"):
                self.diskNum=int(input("Enter the number of disk you want to try "))

        for i in range(0,self.diskNum,1):
            self.tower[0].append(i+1)
            self.tower[1].append(None)
            self.tower[2].append(None)

#Add numbers from 1 to chosen diskNum for the first tower and Fill None for the other two towers


    def chooseDisk(self,begin):
        if(self.tower[begin][0]!=None):
            self.disk=self.tower[begin][0]
        
        else:    
            for i in range(len(self.tower[begin])-1):
                if((self.tower[begin][i]==None and self.tower[begin][i+1]!=None)):
                    self.disk=self.tower[begin][i+1]
                    self.ind=i
                    break

#For the top disk if it is not none, it is selected
#For other disk, if there is none and !none, then the !none disk is selected.

    def place(self,dest,begin):
        while(self.tower[dest][0]!=None):
            print("Tower is full")
            print("Reenter the index")
            dest=int(input("first tower=0, second tower=1, third tower=2 "))
        # If the top element is filled, it is full.
        
        if(self.tower[dest][self.diskNum-1]==None):
            self.tower[dest][self.diskNum-1]=self.disk

            if(self.tower[begin][0]!=None):
                self.tower[begin][0]=None
            else:    
                self.tower[begin][self.ind+1]=None
            
        # If there is no element in destination tower,this method places disk at the bottom and remove disk from begin tower
        else:
            for i in range(len(self.tower[dest])-1):
                if(self.tower[dest][i] == None and self.tower[dest][i+1] != None):
                    if(self.validateMove(dest,i)):
                        self.tower[dest][i] = self.disk

                        if(self.tower[begin][0]!=None):
                            self.tower[begin][0]=None
                            
                        else:    
                            self.tower[begin][self.ind+1]=None
                            
                    else:
                        print("You can't place higher number above lower number! Choose the tower again!")
                        begin,dest=map(int,input("first tower=0, second tower=1, third tower=2 ").split())
                        self.chooseDisk(begin)
                        self.place(dest,begin)
                    break
        #Based on the return value from validataMove, it is either place disk or ask for input again          

    def validateMove(self,dest,i):
        if(self.tower[dest][i+1]<self.disk):
            return False
        else:
            return True
       #If the disk is higher than disk that is placed already, it returns false. Else, return true.


    def move(self,dest,begin):
        self.chooseDisk(begin)
        self.place(dest,begin)
    #Call chooseDisk and place
                    
            

    def play(self):
        validTower=[]
        for i in range(0,self.diskNum,1):
            validTower.append(i+1)

        while(self.tower[2]!=validTower):
            print("enter the tower you start and tower you want to move.")
            begin,dest=map(int,input("first tower=0, second tower=1, third tower=2 ").split())

            while (begin <0 or begin>2) or (dest <0 or dest>2):
                print("Invalid Input for tower number.")
                begin,dest=map(int,input("first tower=0, second tower=1, third tower=2 ").split())


            self.move(dest,begin)
            
            self.count+=1

            print("This is the current tower.")
            self.printBoard()
            print(f"You moved {self.count} times")
        print("You win! Congrats!")
      #Play until tower[2] is not equal to ideal tower 



def main():
    print("Welcome to the Tower of Hanoi!")
    print("In this game you will choose a disk between 1 to 6")

    diskNum=int(input("Enter the number of disk you want to try "))
    tower_of_hanoi=Tower_of_Hanoi(diskNum,0)
    tower_of_hanoi.initializeTower()

    print("Here is the initiallized Tower.")
    tower_of_hanoi.printBoard()

    print("You need to move all disks from start tower to the tower destination")
    print("higher number can not be placed after lower number")
    tower_of_hanoi.play()
# Main cunction that introduces the game
main()










