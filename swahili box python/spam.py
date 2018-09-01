''''spam = 0 
while spam < 5:
  print("hello world")
  spam = spam + 2 # this will loop three times'''
spam = 0
while spam < 5:
  	spam = spam + 1
  	if spam == 4:
  		continue
  	print('spam is ' + str(spam))