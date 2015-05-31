from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import csv

connection = MongoClient("mongodb://localhost:27017/")


def countSTkTags():
    db = connection.DataStorage.bData
    map = open('mapTags.js','r').read()
    reduce = open('reduceTag.js','r').read()
     
    results = db.map_reduce(map,reduce,"stk_tags_count")
    
    return results
     
#     for result in results.find():
#         print(result['_id'],result['value'])
        
def countPrgTags():
    db = connection.DataStorage.PrgQuestions
    map = open('mapTagsPrg.js','r').read()
    reduce = open('reduceTagPrg.js','r').read()
     
    results = db.map_reduce(map,reduce,"prg_tags_count")
    
    return results
     
#     for result in results.find():
#         print(result['_id'],result['value'])
        
def main():
    stkResults = countSTkTags()
    prgResults = countPrgTags()
    
    jsonTempArray1=[]
    jsonTempArray2=[]
    jsonTempArray3=["tag stkCnt PrgCnt"+"\n"]
    
  
    for result in stkResults.find():
        for result1 in prgResults.find():
            if(result['_id'] == result1['_id']):
                jsonStr = str(result['_id'])+"\t"+str(result['value'])+"\t"+ str(result1['value'])+"\n"
                jsonTempArray3.append(jsonStr)
                
    print jsonTempArray3
    
    file = open('J:\\Jyo\\MS\\CS594\\tagsCount.tsv', 'a');
    for i in range(len(jsonTempArray3)):
        file.write(jsonTempArray3[i])
    file.close()
    

            
  
#     for result in stkResults.find():
#         jsonStr1 = {'tag':result['_id'],'count':result['value']}
#         jsonTempArray1.append(jsonStr1)
#     
#     with open('J:\Jyo\MS\CS594\Stk_Tags.txt', 'a') as outfile:
#         "{}\n".format(json.dump(jsonTempArray1  ,outfile) )
#         
#     for result in prgResults.find():
#         jsonStr2 = {'tag':result['_id'],'count':result['value']}
#         jsonTempArray2.append(jsonStr2)
#     
#     with open('J:\Jyo\MS\CS594\Prg_Tags.txt', 'a') as outfile:
#         "{}\n".format(json.dump(jsonTempArray2  ,outfile) )
#         
    print "done"
    
main()