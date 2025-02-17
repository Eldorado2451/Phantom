x="awesome"         #declares variable x as global variable

def myfunc():       #defines a function
    global x        #declares that the global x should be used now
                    # (is only used inside functions. outside of functions, all is global!)
    x="fantastic"   #assigns a new value to the global x

myfunc()

print("Python is " + x)     #prints something outside a function, so takes global