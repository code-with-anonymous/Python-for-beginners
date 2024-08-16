marks={
    "harry":87,
    "ali":89,
    "aslam":98
}
print(marks.items(),type(marks)) #display the whole items of dictionry
print(marks.keys(),type(marks)) 
marks.update({"harry":100,"rayyan":99})#update the previous value or add the new value
print(marks)
print(marks.get("harrry"))#return none when key is not found
print (marks["harrry"])#return error when key is not found


