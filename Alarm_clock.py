import time

current_time = time.localtime()

hour = current_time.tm_hour
minute = current_time.tm_min


if (hour>7) or (hour==7 and minute>29):
    print('IT IS TIME TO GET UP')
    print('RISE AND SHINE')
    print('THE EARLY BIRD GETS THE WORM')
print('The time is', hour,':',minute)    # This statement is always performed
