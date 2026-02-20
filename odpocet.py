def odpocet(n):
    if n<=0:
        print("bummmm")
        return
    else:
        print ("odpocet"+str(n))
        odpocet(n-1)
    odpocet(5)