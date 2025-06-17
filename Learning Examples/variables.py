x="awesome"                 #defines global variable x and assigns a sting value

def myfunc():               #function: re-assigns the global variable x
    global x                #tells that the global x should be used now
                            #(is only used inside functions. outside of functions, all is global!)
    
    x="fantastic"           #assigns a new value to the global x

myfunc()                    #Runs the function defined above

print("Python is " + x)     #prints something outside a function, so takes global, which is re-assigned
                            # inside the function