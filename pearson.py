import math
import scipy.stats
class Pearson:
    def __init__(self,users,matrix):
        self.similarityMat = [[0 for _ in range(users)] for _ in range(users)]
        self.matrix = matrix
        self.users = users
        # self.dummy = [[0 for _ in range(users)] for _ in range(users)]
    
    def pearson(self,rowi,rowj):
        
        # calculating row mean
        
        def mean(someList):
            total = 0
            n = 0
            for a in someList:
                # if a != 0:
                    total += float(a)
                    n += 1
            mean = total/n
            return mean
        
        def standDev(mean,someList):
            dev = 0.0
            for i in range(len(someList)):
                dev += (someList[i]-mean)**2
            dev = dev**(1/2.0)
            return dev
        
        xMean = mean(rowi)
        yMean = mean(rowj)
        xStandDev = standDev(xMean,rowi)
        yStandDev = standDev(yMean,rowj)
        # r numerator
        rNum = 0.0
        for i in range(len(rowi)):
            rNum += (rowi[i]-xMean)*(rowj[i]-yMean)

        # r denominator
        rDen = xStandDev * yStandDev

        r =  rNum/rDen
        return r
        
        # mean_i = 0
        # mean_j = 0
        
        # def calcMean(row):
        #     rowSum = 0
        #     n = 0
        #     for i,val in enumerate(row):
        #         if(val != 0):
        #             rowSum += val
        #             n += 1
            
        #     return float(rowSum)/n
        
        # mean_i = calcMean(rowi)
        # mean_j = calcMean(rowj)
        
        # numerator = 0
        # denominator1 = 0
        # denominator2 = 0
        # for i in range(len(rowi)):
            
        #     if(rowi[i] != 0 and rowj[i] != 0):
        #         # normalizing
        #         ival = rowi[i] - mean_i
        #         jval = rowj[i] - mean_j
        #         numerator +=  ival*jval 
                
        #     if(rowi[i] != 0):
        #         denominator1 += (rowi[i] - mean_i)**2
            
        #     if(rowj[i] != 0):
        #         denominator2 += (rowj[i] - mean_j)**2
        
        # if(int(denominator1) == 0 or int(denominator2) == 0):
        #     return 0
        
        # denominator = math.sqrt(denominator1) * math.sqrt(denominator2)
        
        # return numerator/denominator
    
    def similarity(self):
        for i in range(1,self.users):
            for j in range(1,self.users):
                self.similarityMat[i][j] = self.pearson(self.matrix[i],self.matrix[j])
                # self.dummy[i][j] = scipy.stats.pearsonr(self.matrix[i],self.matrix[j])[0]
                
        # print(self.dummy)
        return self.similarityMat    