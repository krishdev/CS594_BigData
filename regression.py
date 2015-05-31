import numpy as np
import statistics as stat  
import statsmodels.api as sm
from pymongo import MongoClient
from bson.objectid import ObjectId
import matplotlib.pyplot
import pylab
import json
import itertools


x=0
connection = MongoClient("mongodb://localhost:27017/")
db = connection.DataStorage.bData


def getStkRegression():
    my_oid = "5566505ff95f2512e4c7c435"
    
    age =  []
    reputation_score = []
    badge_index = []
    
    for doc in db.find( {'_id': ObjectId(my_oid)}, {"items.age" : 200 }).sort("items.age"): 
        for i in doc['items']:
            age.append(i['age'])
      
    for doc in db.find( {'_id': ObjectId(my_oid)}, {"items.reputation" : 999999 }).sort("items.age"):
        for i in doc['items']:
            reputation_score.append(i['reputation'])
    
    
    for doc in db.find( {'_id': ObjectId(my_oid)}, {"items.badge_counts" : 999999 }).sort("items.age"):
        for j in doc['items']:
            badge_index.append((int(j['badge_counts']['gold']+(0.5*j['badge_counts']['silver'])+(0.5*j['badge_counts']['bronze']))))
            
    x = np.column_stack((age,badge_index))
    x = sm.add_constant(x, prepend=True)
    
    res = sm.OLS(reputation_score,x).fit() #create a model and fit it
    
#     print res.params
#     print "params above"
#     print res.bse
#     print "bse above"
#     print res.summary()
#     print "summary"

   
    yAxis = []
    x1Axis = []
    x2Axis = []
    cordinatesArray = []
    jsonData = {}
    
    c = res.params[0]
    b1 = res.params[1]
    b2 = res.params[2]
       
    stk_ages =  (np.array(age))
    stk_badges = (np.array(badge_index)) 
     
    stk_x1_min= stk_ages.min()
    stk_x1_max= stk_ages.max()
     
    stk_x2_min= stk_badges.min()
    stk_x2_max= stk_badges.max()
     
    stk_reputatn = np.array(reputation_score)
    p = np.percentile(stk_reputatn, 75)
     
    import random
    for x in range(1000):
       x1 =  random.randint(stk_x1_min,stk_x1_max)
       while(x1 < 18):
           x1 =  random.randint(stk_x1_min,stk_x1_max)
           if(x1 >17):
               break;
       x2 = random.randint(stk_x2_min,stk_x2_max)
        
       y = c + (b1*x1) + (b2*x2)
       #if y >= p:
       internal_list =[]
       internal_list.insert(0,y)
       internal_list.insert(1,x1)
       internal_list.insert(2,x2)
        
       cordinatesArray.append(internal_list)
       x1Axis.append(x1)
       x2Axis.append(x2)
       yAxis.append(y)
    
    cordinatesArray = sorted(cordinatesArray)  
    jsonTempArray1 = []
    jsonTempArray2 = []
    jsonstr2 = " "
   # print "reputation "+"| \t"+" age "+"| \t"+" Bagde_index"
    for i in range(len(cordinatesArray)):
#         if cordinatesArray[i][0] >= p:
#            print  str(cordinatesArray[i][0])+"| \t"+str(cordinatesArray[i][1])+"| \t"+str(cordinatesArray[i][2]) 
        jsonStr1 = {'x1':cordinatesArray[i][1], 'y':cordinatesArray[i][0]}
        jsonTempArray1.append(jsonStr1)
        jsonStr2 = {'x2':cordinatesArray[i][2], 'y':cordinatesArray[i][0]}
        jsonTempArray2.append(jsonStr2)
   
    with open('J:\Jyo\MS\CS594\Stk_Histogram1.txt', 'a') as outfile:
        "{}\n".format(json.dump(jsonTempArray1  ,outfile) )
     
    with open('J:\Jyo\MS\CS594\Stk_Histogram2.txt', 'a') as outfile:
        "{}\n".format(json.dump(jsonTempArray2  ,outfile) )
        
        
    scatterArray = []
    for i in range(len(age)):
        internal_list =[]
        internal_list.insert(0,reputation_score[i])
        internal_list.insert(1,age[i])
        internal_list.insert(2,badge_index[i]) 
        scatterArray.append(internal_list)
    
    scatterArray = sorted(scatterArray)    
    jsonTempArray3 = []
    jsonTempArray4 = []
    jsonstr4 = " "
    
    for i in range(len(scatterArray)):
        jsonStr3 = {'x1':scatterArray[i][1], 'y':scatterArray[i][0]}
        jsonTempArray3.append(jsonStr3)
        jsonStr4 = {'x2':scatterArray[i][2] , 'y':scatterArray[i][0]}
        jsonTempArray4.append(jsonStr4)
   
    with open('J:\Jyo\MS\CS594\Stk_Scatter1.txt', 'a') as outfile:
        "{}\n".format(json.dump(jsonTempArray3  ,outfile) )
     
    with open('J:\Jyo\MS\CS594\Stk_Scatter2.txt', 'a') as outfile:
        "{}\n".format(json.dump(jsonTempArray4  ,outfile) )
    
     
    return res


def getPrgRegression():
    age =  []
    reputation_score = []
    badge_index = []
    
    my_oid = "5569479dd699c9b3f77e62aa"

    for doc in db.find( {'_id': ObjectId(my_oid)}, {"items.age" : 200 }).sort("items.age"): 
        for i in doc['items']:
            age.append(i['age'])
         
            
      
    for doc in db.find( {'_id': ObjectId(my_oid)}, {"items.reputation" : 999999 }).sort("items.age"):
        for i in doc['items']:
            reputation_score.append(i['reputation'])
    
    
    for doc in db.find( {'_id': ObjectId(my_oid)}, {"items.badge_counts" : 999999 }).sort("items.age"):
        for j in doc['items']:
            badge_index.append((int(j['badge_counts']['gold']+(0.5*j['badge_counts']['silver'])+(0.5*j['badge_counts']['bronze']))))
    
   
    x = np.column_stack((age,badge_index))
    x = sm.add_constant(x, prepend=True)
    
    res = sm.OLS(reputation_score,x).fit() #create a model and fit it
    
#     print res.params
#     print "params above"
#     print res.bse
#     print "bse above"
#     print res.summary()
#     print "summary"

    
    yAxis = []
    x1Axis = []
    x2Axis = []
    cordinatesArray = []
    jsonData = {}
    
    c = res.params[0]
    b1 = res.params[1]
    b2 = res.params[2]
       
    prg_ages =  (np.array(age))
    prg_badges = (np.array(badge_index)) 
     
    prg_x1_min= prg_ages.min()
    print "min age prg is "+str(prg_x1_min)
    prg_x1_max= prg_ages.max()
    print "max age prg is "+str(prg_x1_max)
     
    prg_x2_min= prg_badges.min()
    prg_x2_max= prg_badges.max()
     
    prg_reputatn = np.array(reputation_score)
    p = np.percentile(prg_reputatn, 75)
     
    
    import random
    for x in range(1000):
       x1 =  random.randint(prg_x1_min,prg_x1_max)
       while(x1 >60):
           x1 =  random.randint(prg_x1_min,prg_x1_max)
           if(x1 <70):
               break;
       x2 = random.randint(prg_x2_min,prg_x2_max)
        
       y = c + (b1*x1) + (b2*x2)
       internal_list =[]
       internal_list.insert(0,y)
       internal_list.insert(1,x1)
       internal_list.insert(2,x2)
       
        
       cordinatesArray.append(internal_list)
       x1Axis.append(x1)
       x2Axis.append(x2)
       yAxis.append(y)
 
   # cordinatesArray = np.array(cordinatesArray)
    cordinatesArray = sorted(cordinatesArray)
    jsonTempArray1 = []
    jsonTempArray2 = []
    jsonstr2 = " "
    print"\n"
    print "reputation "+"| \t"+" age "+"| \t"+" Bagde_index"
    for i in range(len(cordinatesArray)):
        if cordinatesArray[i][0] >= p:
           print  str(cordinatesArray[i][0])+"\t"+str(cordinatesArray[i][1])+"\t"+str(cordinatesArray[i][2]) 
        jsonStr1 = {'x1':cordinatesArray[i][1], 'y':cordinatesArray[i][0]}
        jsonTempArray1.append(jsonStr1)
        jsonStr2 = {'x2':cordinatesArray[i][2],'y':cordinatesArray[i][0],}
        jsonTempArray2.append(jsonStr2)
   
    with open('J:\Jyo\MS\CS594\Prg_Histogram1.txt', 'a') as outfile:
        "{}\n".format(json.dump(jsonTempArray1  ,outfile) )
     
    with open('J:\Jyo\MS\CS594\Prg_Histogram2.txt', 'a') as outfile:
        "{}\n".format(json.dump(jsonTempArray2  ,outfile) )
        
        
        
    scatterArray = []
    for i in range(len(age)):
        internal_list =[]
        internal_list.insert(0,reputation_score[i])
        internal_list.insert(1,age[i])
        internal_list.insert(2,badge_index[i]) 
        scatterArray.append(internal_list)
    
    scatterArray = sorted(scatterArray)    
    jsonTempArray3 = []
    jsonTempArray4 = []
    jsonstr4 = " "
    
    for i in range(len(scatterArray)):
        jsonStr3 = {'x1':scatterArray[i][1],'y':scatterArray[i][0]}
        jsonTempArray3.append(jsonStr3)
        jsonStr4 = {'x2':scatterArray[i][2] , 'y':scatterArray[i][0]}
        jsonTempArray4.append(jsonStr4)
   
    with open('J:\Jyo\MS\CS594\Prg_Scatter1.txt', 'a') as outfile:
        "{}\n".format(json.dump(jsonTempArray3  ,outfile) )
     
    with open('J:\Jyo\MS\CS594\Prg_Scatter2.txt', 'a') as outfile:
        "{}\n".format(json.dump(jsonTempArray4  ,outfile) )
    

    return res


def main():  
    stkResult =  getStkRegression()
    prgResult = getPrgRegression()
    
    print stkResult.summary()
    print prgResult.summary()
#     matplotlib.pyplot.scatter(age,reputation_score)
#     matplotlib.pyplot.show()
#       
#     matplotlib.pyplot.scatter(badge_index,reputation_score)
#     matplotlib.pyplot.show()
  
    #print  json.loads(json.dumps(yAxis))
 
main()