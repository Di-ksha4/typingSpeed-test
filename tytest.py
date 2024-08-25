from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error= error+1
        except :
            error = error +1
    return error           
        
def speed_time( time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)
    
        
if __name__ == '__main__':
    while True:
        ck = input("Ready to test your typing speed: yes/no : ")
        if ck == "yes":
            print("")
            test=["All the villagers came running to drive the wolf away. However, they saw no wolf. The boy was amused, but the villagers were not. They told him not to do it again.",
            "The Greek king Midas did a good deed for a Satyr. This prompted Dionysus, the god of wine, to grant him a wish.","A hungry fox once looked everywhere for food. "]
            test1 = r.choice(test)
            print("     **  Typing Speed   ** ")
            print()
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter : ")
            time_2 = time()

            print('Speed : ', speed_time(time_1,time_2,testinput),"w/sec")
            print("Mistakes : ", mistake(test1,testinput))
            print("")
         
        elif ck == 'no' :
            print(" Thank you ")
            break
        else:
           print(" Wrong input ")