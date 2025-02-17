x="awesome"         #declares variable x as global variable

def myfunc():       #function: re-assigns the global variable x
    global x        #declares that the global x should be used now
                    # (is only used inside functions. outside of functions, all is global!)
    x="fantastic"   #assigns a new value to the global x

myfunc()            #Run the function above
print("Python is " + x)     #prints something outside a function, so takes global