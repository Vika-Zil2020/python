input_num = int(input("enter number check prime or not"))
def prime(input_num):
    if (input_num==1):
        return False
    elif (input_num==2):
        return True
    else:
        for i in range(2,input_num):
            if(input_num % i==0):
                return False
        return True             
print(prime(input_num))
