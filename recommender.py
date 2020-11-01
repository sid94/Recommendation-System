import numpy as np
import os

class Recommendation:
    def __init__(self,users,items):
        self.users = users + 1
        self.items = items + 1
        self.matrix = [[0 for _ in range(self.items)] for _ in range(self.users)]
        self.similarity = [[]]
        
    def readFile(self):
        if(os.path.isfile("dataset/train.txt")):
            with open("dataset/train.txt", "r") as file:
                for line in file:
                    user,item,rating = line.split()
                    self.matrix[int(user)][int(item)] = int(rating)
                file.close()
                
    def similarity(self):
        self.similarity = []
                
    
                    
        
if __name__ == '__main__':
    
    # user count and item count in total 
    userCount = 943
    itemCount = 1682
    
    # create recommendation instance
    objRec = Recommendation(userCount,itemCount)
    objRec.readFile()
    