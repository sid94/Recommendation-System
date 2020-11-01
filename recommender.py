import numpy as np
import os
from pearson import Pearson

class Recommendation:
    def __init__(self,users,items):
        self.users = users + 1
        self.items = items + 1
        self.matrix = [[0 for _ in range(self.items)] for _ in range(self.users)]
        self.similarityMat = [[]]
        self.out = [[]]
        
    def readFile(self):
        if(os.path.isfile("dataset/testtrain.txt")):
            with open("dataset/testtrain.txt", "r") as file:
                for line in file:
                    user,item,rating = line.split()
                    self.matrix[int(user)][int(item)] = int(rating)
                file.close()
        self.printRowByRow(self.matrix)
                
    def similarity(self):
        objPearson = Pearson(self.users,self.matrix)
        self.similarityMat = objPearson.similarity()
        self.printRowByRow(self.similarityMat)
        
    def printRowByRow(self,matrix):
        
        for row in matrix:
            print(row)
        print("\n")
        
    def mean(self,someList):
            total = 0
            n = 0
            for a in someList:
                # if a != 0:
                    total += float(a)
                    n += 1
            mean = total/n
            return mean
        
    def predict(self):
        for i in range(self.users):
            mean_i = self.mean(self.matrix[i])
            for j in range(self.items):
                if(self.matrix == 0):
                    
                else:
                    self.out[i][j] = self.matrix[i][j]
                
                
        return
        
if __name__ == '__main__':
    
    # user count and item count in total 
    # userCount = 943
    # itemCount = 1682
    
    userCount = 4
    itemCount = 7
    
    # create recommendation instance
    objRec = Recommendation(userCount,itemCount)
    objRec.readFile()
    objRec.similarity()
    # objRec.predict()