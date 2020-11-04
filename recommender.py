# import numpy as np
import os
import numpy as np
from pearson import Pearson
from sklearn.model_selection import train_test_split
import pickle
import math

class Recommendation:
    def __init__(self,users,items):
        self.users = users + 1
        self.items = items + 1
        self.input = np.array([[0,0,0]])
        self.matrix = [[0 for _ in range(self.items)] for _ in range(self.users)]
        self.similarityMat = [[]]
        self.out = [[0 for _ in range(self.items)] for _ in range(self.users)]
        self.accFlag = True
        self.test = None
        
    def readFile(self):
        
        if(not self.accFlag):
            if(os.path.isfile("dataset/train.txt")):
                with open("dataset/train.txt", "r") as file:
                    for line in file:
                        user,item,rating = line.split()
                        self.matrix[int(user)][int(item)] = int(rating)
                    file.close()
        else:
            self.inputToNpArray()
            self.input = np.delete(self.input, (0), axis=0)
            np.random.shuffle(self.input)
            x_train ,x_test = train_test_split(self.input,test_size=0.2)
            # print(len(x_train))
            # print(len(x_test))
            self.test = x_test
            
            for i,j,rate in x_train:
                self.matrix[int(i)][int(j)] = int(rate)
        # self.printRowByRow(self.matrix)
                
    def similarity(self):
        objPearson = Pearson(self.users,self.matrix)
        self.similarityMat = objPearson.similarity()
        with open("simi.pkl", "wb") as file:
            pickle.dump(self.similarityMat,file)
            file.close()
        # self.printRowByRow(self.similarityMat)
        
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
        print("prediction start")
        file = open('simi.pkl', 'rb')
        self.similarityMat = pickle.load(file)
        for i in range(1,self.users):
            mean_i = self.mean(self.matrix[i])
            for j in range(1,self.items):
                if(self.matrix[i][j] == 0):
                    s1 = 0
                    s2 = 0
                    for k in range(1,self.users):
                        if(self.matrix[k][j] != 0):
                            s1 +=  self.matrix[k][j] * self.similarityMat[i][k]
                            s2 +=  self.similarityMat[i][k]
                        
                    if(s2 == 0 or s2 == 0.0):
                        self.out[i][j] = round(mean_i,0)
                    else:
                        self.out[i][j] = round(s1/s2, 0)
                        
                    print((i,j))
                else:
                    self.out[i][j] = self.matrix[i][j]
                    print((i,j))
    
    def write(self):
        with open("output.txt", "w+") as file:
            for i in range(1,len(self.out)):
                for j in range(1,len(self.out[0])):
                    file.write("{} {} {}\n".format(i,j,self.out[i][j]))
            file.close()
        
        # self.printRowByRow(self.out)
        
    def accuracy(self):
        total = 0
        N = len(self.test)
        diffSqrSum = 0
        for i,j,rate in self.test:
            print(int(self.out[i][j]), "   " ,int(rate))
            diffSqrSum += (int(rate) -  int(self.out[i][j]))**2
            if(int(self.out[i][j]) == int(rate)):
                total += 1
        
        print("RMSE = ", math.sqrt(diffSqrSum/N))
        print("accuracy = ", (total/len(self.test)) * 100 )
                
    def inputToNpArray(self):
        if(os.path.isfile("dataset/train.txt")):
            with open("dataset/train.txt", "r") as file:
                for line in file:
                    user,item,rating = line.split()
                    arr = [int(user),int(item),int(rating)]
                    self.input = np.append(self.input,[arr],axis=0)
                file.close()
        
        
        
if __name__ == '__main__':
    
    # user count and item count in total 
    userCount = 943
    itemCount = 1682
    
    # userCount = 4
    # itemCount = 7
    
    # create recommendation instance
    objRec = Recommendation(userCount,itemCount)
    objRec.readFile()
    objRec.similarity()
    objRec.predict()
    objRec.accuracy()
    objRec.write()
    # objRec.predict()