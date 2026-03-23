#Make Normal Dictionary
Result = {
    "Name" : "Shravani Ajay Yadav",
    "Subject Marks" : {
        "Physics" : 86,
        "Chemistry" : 68,
        "Maths" : 79,
    }
}

#.key Method
#for printing keys 
print(Result.keys())

#List of Keys
print(list(Result.keys()))

#.values method
#printing values under the keys
print(Result.values())

#printing list of values under the keys
print(list(Result.values()))

#measuring length of values under the keys
print(len(Result.values()))

#.items method
#printing all info given in Dict in Tuple Form = ()
print(Result.items())

#printing list of info given in Dict in Tuple Form = ()
print(list(Result.items()))

#.get Method
#name2 is not available in our dict > shows error
#we have used .get > no error we will show > shows : None 
info = {
    "name" : "Shravani Ajay Yadav",
}

print(info.get("name2"))

#.update Method
#Adds Any Key
Result.update({"City" : "Pune"})
print(Result)