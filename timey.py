import time  #import the library
current_time = time.localtime()  # get the time value
hour = current_time.tm_hour  #Get the hour value
minute = current_time.tm_min
it_is_time_to_get_up = (hour >7) or (hour==7 and minute>29)    #Set the flag value

if it_is_time_to_get_up:                #is the flag value true?
    print("IT IS TIME TO GET UP")        #if so, print the message

else:
    print('Go back to bed')
