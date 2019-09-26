'''try:    
	fh = open("testfile", "w")    
	fh.write("This is my test file for exception handling!!") 
except IOError:    
	print ("Error: can\'t find file or read data") 
else:    
	print ("Written content in the file successfully")    
fh.close()'''


'''l=[]
try:
	print(l.get())
	print(l[0])
	d=10/0
except AttributeError:
	print("AttributeError list not have get method")
except IndexError:
	print("index Error")
except ZeroDivisionError as e:
	print("you cant divide a number by 0",e)

print("proceed")'''



import math
def sqrt(x):
	if not isinstance(x,(int,float)):
		return TypeError("x must be number")
	elif x<0:
		return ValueError("x cont be negative")
	else:
		return math.sqrt(x)
try:
	print(sqrt("9"))
	print(sqrt(4))
except Exception as e:
	print("error",e)






