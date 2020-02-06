gsm_number = input("enter your number")

len(gsm_number)==8

while True:

    try:

        if len(gsm_number)==8:

            if gsm_number[0:2]=="98" or gsm_number[0:2]=="77" or gsm_number[0:2] =="94" or gsm_number[0:2]=="93":

                print("VivaMTS")

                break

            if gsm_number[0:2] =="91" or gsm_number[0:2]== "41" or gsm_number[0:2]=="96":

                print("Veon")

                break

            elif gsm_number[0:2]=="55" or gsm_number[0:2]=="95"or gsm_number[0:2]=="44":

                print("Ucom")

                break

            if len(gsm_number)<8:

                print("try aganin")

                break

    except:gsm_number==str(gsm_number)

    print("wrong format of number")

    break