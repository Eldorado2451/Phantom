from time import sleep          #import sleep for the delay

i = 0                           # i is declared globally
while i < 5:                    # This is the same as while(i<5){...}
    print("ON")
    sleep(1)                    #delays 1 sec
    print("OFF")
    sleep(1)
    i += 1                      #increments i with 1. while is NOT A FUNCTION, so i can be used without declaring "global i" before the increment