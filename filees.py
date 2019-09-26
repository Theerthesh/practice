'''fo = open("foo.txt", "wb") #wb is criting in a file
print ("Name of the file: ",fo.name ) 
print ("Closed or not : ", fo.closed) 
print ("Opening mode : ", fo.mode) 
fo.close() '''

#------to write a string in a file

'''fo = open("foo.txt", "w")
fo.write( "experiance\n")
fo.close()''' 

#-----to read a string from a file

'''fo = open("foo.txt", "r+") #r+ is use to read a file
str1 = fo.read(10) #10 charector read from the text
print ("Read String is : ", str1) 
fo.close()'''

#---------- Rename a file from foo1.txt to foo2.txt

'''import os #os module have for methods
os.rename( "foo1.txt", "foo2.txt" ) '''

 
# Delete file test2.txt 
import os 
os.remove("foo2.txt")
