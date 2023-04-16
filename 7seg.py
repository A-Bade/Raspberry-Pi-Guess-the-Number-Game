# Write your code here :-)
import RPi.GPIO as GPIO
import time
import random
import os, sys, gc
import threading
from rpi_lcd import LCD


#import machine
lcd = LCD()



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#setup output pins
GPIO.setup(35, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

seg1a = 24
seg1b = 11
seg1c = 7
seg1d = 8
seg1e = 10
seg1f = 0
seg1g = 13

seg2a = 15
seg2b = 16
seg2c = 18
seg2d = 19
seg2e = 21
seg2f = 22
seg2g = 23

GPIO.setup(seg1a, GPIO.OUT)
GPIO.setup(seg1b, GPIO.OUT)
GPIO.setup(seg1c, GPIO.OUT)
GPIO.setup(seg1d, GPIO.OUT)
GPIO.setup(seg1e, GPIO.OUT)
#GPIO.setup(seg1f, GPIO.OUT)
GPIO.setup(seg1g, GPIO.OUT)

GPIO.setup(seg2a, GPIO.OUT)
GPIO.setup(seg2b, GPIO.OUT)
GPIO.setup(seg2c, GPIO.OUT)
GPIO.setup(seg2d, GPIO.OUT)
GPIO.setup(seg2e, GPIO.OUT)
GPIO.setup(seg2f, GPIO.OUT)
GPIO.setup(seg2g, GPIO.OUT)



GPIO.setup(29, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_UP)


#define 7 segment digits
digitclr=[1,1,1,1,1,1,1]
digit0=[0,0,0,0,0,0,1]
digit1=[1,0,0,1,1,1,1]
digit2=[0,0,1,0,0,1,0]
digit3=[0,0,0,0,1,1,0]
digit4=[1,0,0,1,1,0,0]
digit5=[0,1,0,0,1,0,0]
digit6=[0,1,0,0,0,0,0,]
digit7=[0,0,0,1,1,1,1]
digit8=[0,0,0,0,0,0,0]
digit9=[0,0,0,1,1,0,0,]

a = [1,1,1,1,1,1,0]
b = [1,1,1,1,1,0,1]
c = [1,1,1,1,0,1,1]
d = [1,1,1,0,1,1,1]
e = [1,1,0,1,1,1,1]
f = [1,0,1,1,1,1,1]
g = [0,1,1,1,1,1,1]

pattern =[b,c,d,e,f,g]

displayer = [digit0,digit1,digit2,digit3,digit4,digit5,digit6,digit7,digit8,digit9]
gpin=[35,12,36,33,32,38,40]
gpin1 = [seg1a,seg1b,seg1c,seg1d,seg1e,seg1f,seg1g]
gpin2 = [seg2a,seg2b,seg2c,seg2d,seg2e,seg2f,seg2g]



num2 = random.randint(0,9)
num3 = random.randint(0,9)
num4 = random.randint(0,9)
num5 = random.randint(0,9)
num6 = random.randint(0,9)
num7 = random.randint(0,9)
num8 = random.randint(0,9)
num9 = random.randint(0,9)
num10 = random.randint(0,9)


#routine to display digit from 0 to 9
def loop_pattern1():
     GPIO.output(35, False) # a
     GPIO.output(12, True) # b
     GPIO.output(36, True) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, True) # f
     GPIO.output(40, True) # g

     time.sleep(0.06)

     GPIO.output(35, True) # a
     GPIO.output(12, False) # b
     GPIO.output(36, True) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, True) # f
     GPIO.output(40, True) # g

     time.sleep(0.06)

     GPIO.output(35, True) # a
     GPIO.output(12, True) # b
     GPIO.output(36, False) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, True) # f
     GPIO.output(40, True) # g

     time.sleep(0.06)

     GPIO.output(35, True) # a
     GPIO.output(12, True) # b
     GPIO.output(36, True) # c
     GPIO.output(33, False) # d
     GPIO.output(32, True) # e
     GPIO.output(38, True) # f
     GPIO.output(40, True) # g

     time.sleep(0.06)

     GPIO.output(35, True) # a
     GPIO.output(12, True) # b
     GPIO.output(36, True) # c
     GPIO.output(33, True) # d
     GPIO.output(32, False) # e
     GPIO.output(38, True) # f
     GPIO.output(40, True) # g

     time.sleep(0.06)

     GPIO.output(35, True) # a
     GPIO.output(12, True) # b
     GPIO.output(36, True) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, False) # f
     GPIO.output(40, True) # g

     time.sleep(0.06)

def base():
     GPIO.output(35, True) # a
     GPIO.output(12, True) # b
     GPIO.output(36, True) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, True) # f
     GPIO.output(40, True) # g

def loop_pattern2():
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, True) # b
     GPIO.output(seg2c, True) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, True) # g

     time.sleep(0.06)

     GPIO.output(seg2a, True) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, True) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, True) # g

     time.sleep(0.06)

     GPIO.output(seg2a, True) # a
     GPIO.output(seg2b, True) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, True) # g

     time.sleep(0.06)

     GPIO.output(seg2a, True) # a
     GPIO.output(seg2b, True) # b
     GPIO.output(seg2c, True) # c
     GPIO.output(seg2d, False) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, True) # g

     time.sleep(0.06)

     GPIO.output(seg2a, True) # a
     GPIO.output(seg2b, True) # b
     GPIO.output(seg2c, True) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, False) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, True) # g

     time.sleep(0.06)

     GPIO.output(seg2a, True) # a
     GPIO.output(seg2b, True) # b
     GPIO.output(seg2c, True) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, False) # f
     GPIO.output(seg2g, True) # g

     time.sleep(0.06)

#the_choice = ["a","b","c","d","e","f","g","h","i","j"]
arr1 = [13]
arr2 = [12]

def SevenSeg(x): # Define function 'SevenSeg' which calls function 'one' 'two' or 'three' depending on 'x'
 if x == 1:
     #del arr1[]:
     GPIO.output(seg2a, True) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, True) # g
     arr1[0] = 1
     #print(arr1[0])
 elif x == 2:
     #del arr1[0]
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, True) # c
     GPIO.output(seg2d, False) # d
     GPIO.output(seg2e, False) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, False) # g
     arr1[0] = 2
     #print(arr1[0])
 elif x == 3:
     #del arr1[0]
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, False) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, False) # g
     arr1[0] = 3
     #print(arr1[0])
 elif x == 4:
     #del arr1[0]
     GPIO.output(seg2a, True) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, False) # f
     GPIO.output(seg2g, False) # g
     arr1[0] = 4
     #print(arr1[0])
 elif x == 5:
     #del arr1[0]
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, True) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, False) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, False) # f
     GPIO.output(seg2g, False) # g
     arr1[0] = 5
     #print(arr1[0])
 elif x == 6:
     #del arr1[0]
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, True) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, False) # d
     GPIO.output(seg2e, False) # e
     GPIO.output(seg2f, False) # f
     GPIO.output(seg2g, False) # g
     arr1[0] = 6
     #print(arr1[0])
 elif x == 7:
     #del arr1[0]
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, True) # f
     GPIO.output(seg2g, True) # g
     arr1[0] = 7
     #print(arr1[0])
 elif x == 8:
     #del arr1[0]
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, False) # d
     GPIO.output(seg2e, False) # e
     GPIO.output(seg2f, False) # f
     GPIO.output(seg2g, False) # g
     arr1[0] = 8
     #print(arr1[0])
 elif x == 9:
     #del arr1[0]
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, True) # d
     GPIO.output(seg2e, True) # e
     GPIO.output(seg2f, False) # f
     GPIO.output(seg2g, False) # g
     arr1[0] = 9
     #print(arr1[0])
 elif x == 10:
     #del arr1[0]
     GPIO.output(seg2a, False) # a
     GPIO.output(seg2b, False) # b
     GPIO.output(seg2c, False) # c
     GPIO.output(seg2d, False) # d
     GPIO.output(seg2e, False) # e
     GPIO.output(seg2f, False) # f
     GPIO.output(seg2g, True) # g
     arr1[0] = 10
     #print(arr1[0])


def SevenSeg1(x):
 if x == 1:
     #del arr2[0]
     GPIO.output(35, True) # a
     GPIO.output(12, False) # b
     GPIO.output(36, False) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, True) # f
     GPIO.output(40, True) # g
     arr2[0] = 1

     return arr2
 elif x == 2:
     #del arr2[0]
     GPIO.output(35, False) # a
     GPIO.output(12, False) # b
     GPIO.output(36, True) # c
     GPIO.output(33, False) # d
     GPIO.output(32, False) # e
     GPIO.output(38, True) # f
     GPIO.output(40, False) # g

     arr2[0] = 2
     return arr2
 elif x == 3:
     #del arr2[0]
     GPIO.output(35, False) # a
     GPIO.output(12, False) # b
     GPIO.output(36, False) # c
     GPIO.output(33, False) # d
     GPIO.output(32, True) # e
     GPIO.output(38, True) # f
     GPIO.output(40, False) # g
     arr2[0] = 3
     return arr2
 elif x == 4:
     #del arr2[0]
     GPIO.output(35, True) # a
     GPIO.output(12, False) # b
     GPIO.output(36, False) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, False) # f
     GPIO.output(40, False) # g
     arr2[0] = 4
     #print(arr2[0])
     return arr2
 elif x == 5:
     #del arr2[0]
     GPIO.output(35, False) # a
     GPIO.output(12, True) # b
     GPIO.output(36, False) # c
     GPIO.output(33, False) # d
     GPIO.output(32, True) # e
     GPIO.output(38, False) # f
     GPIO.output(40, False) # g
     arr2[0] = 5
     return arr2
 elif x == 6:
     #del arr2[0]
     GPIO.output(35, False) # a
     GPIO.output(12, True) # b
     GPIO.output(36, False) # c
     GPIO.output(33, False) # d
     GPIO.output(32, False) # e
     GPIO.output(38, False) # f
     GPIO.output(40, False) # g
     arr2[0] = 6
     return arr2
 elif x == 7:
     #del arr2[0]
     GPIO.output(35, False) # a
     GPIO.output(12, False) # b
     GPIO.output(36, False) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, True) # f
     GPIO.output(40, True) # g
     arr2[0] = 7
     return arr2
 elif x == 8:
     #del arr2[0]
     GPIO.output(35, False) # a
     GPIO.output(12, False) # b
     GPIO.output(36, False) # c
     GPIO.output(33, False) # d
     GPIO.output(32, False) # e
     GPIO.output(38, False) # f
     GPIO.output(40, False) # g
     arr2[0] = 8
     return arr2
 elif x == 9:
     #del arr2[0]
     GPIO.output(35, False) # a
     GPIO.output(12, False) # b
     GPIO.output(36, False) # c
     GPIO.output(33, True) # d
     GPIO.output(32, True) # e
     GPIO.output(38, False) # f
     GPIO.output(40, False) # g
     arr2[0] = 9
     return arr2
 elif x == 10:
     #del arr2[0]
     GPIO.output(35, False) # a
     GPIO.output(12, False) # b
     GPIO.output(36, False) # c
     GPIO.output(33, False) # d
     GPIO.output(32, False) # e
     GPIO.output(38, False) # f
     GPIO.output(40, True) # g
     arr2[0] = 10
     return arr2
store = 0

def loop1():
    count = 0
    state = 0
    while True:
        for t in range (0,10,1):

            if count == 0 and GPIO.input(37) == True:
                     GPIO.output(seg2a, True) # a
                     GPIO.output(seg2b, True) # b
                     GPIO.output(seg2c, True) # c
                     GPIO.output(seg2d, True) # d
                     GPIO.output(seg2e, True) # e
                     GPIO.output(seg2f, True) # f
                     GPIO.output(seg2g, True) # g
                     time.sleep(0.5)
                     count = count +1
                     state = 1
                     t = t+1
            time.sleep(0.01)

            if count == 1 and GPIO.input(37) == False:
                    SevenSeg(1)
                    store = SevenSeg(1)
                    time.sleep(0.5)
                    count = count +1
                    state = 1
                    t = t+1
            time.sleep(0.01)


            if count == 2 and GPIO.input(37) == False:
                     SevenSeg(2)
                     store = SevenSeg(2)
                     time.sleep(0.5)
                     count = count +1
                     state = 2
                     t = t+1
            time.sleep(0.01)

            if count == 3 and GPIO.input(37) == False:
                SevenSeg(3)
                store = SevenSeg(3)
                count = count +1
                time.sleep(0.5)
                state = 3
                t = t+1
            time.sleep(0.01)

            if count == 4 and GPIO.input(37) == False:
                SevenSeg(4)
                store = SevenSeg(4)
                count = count +1
                time.sleep(0.5)
                state = 4
                t = t+1
            time.sleep(0.01)

            if count == 5 and GPIO.input(37) == False:
                SevenSeg(5)
                store = SevenSeg(5)
                count = count +1
                time.sleep(0.5)
                state = 5
                t = t+1
            time.sleep(0.01)

            if count == 6 and GPIO.input(37) == False:
                SevenSeg(6)
                store = SevenSeg(6)
                count = count +1
                time.sleep(0.5)
                state = 6
                t = t+1
            time.sleep(0.01)

            if count == 7 and GPIO.input(37) == False:
                SevenSeg(7)
                store = SevenSeg(7)
                count = count +1
                time.sleep(0.5)
                state = 7
                t = t+1
            time.sleep(0.01)

            if count == 8 and GPIO.input(37) == False:
                SevenSeg(8)
                store = SevenSeg(8)
                count = count +1
                time.sleep(0.5)
                state = 8
                t = t+1
            time.sleep(0.01)

            if count == 9 and GPIO.input(37) == False:
                SevenSeg(9)
                store = SevenSeg(9)
                count = count +1
                time.sleep(0.5)
                state = 9
                t = t+1
            time.sleep(0.01)

            if count == 10 and GPIO.input(37) == False:
                SevenSeg(10)
                store = SevenSeg(10)
                count = count +1
                time.sleep(0.5)
                state = 10
                t = t+1
            time.sleep(0.01)

            if count == 11 and GPIO.input(37) == False:
                count = 1
                time.sleep(0.5)
            time.sleep(0.01)


def loop3():
    determine = 3
    while True:
        ###CHECK 1
        for u in range (0,3):
            if GPIO.input(26) == False and determine == 3:

                    print(determine)
                    determine = determine - 1
                    if arr1[0] == arr2[0]:
                        print("Success!!")
                        lcd.text("CORRECT!!!", 1)
                        lcd.text("   :D", 2)
                        time.sleep(5)
                        lcd.text("Restarting...",1)
                        time.sleep(3)
                        lcd.clear()
                        time.sleep(2)
                        os.execv(sys.executable, ['python'] + sys.argv)
                    if arr1[0] != arr2[0]:

                        #u = u - 1
                        lcd.text("WRONG!!!", 1)
                        lcd.text("   :(  Lives = " + format(determine), 2)
                        #time.sleep(0.001)
                        time.sleep(3)
                        lcd.clear()

            if GPIO.input(26) == False and determine == 2:

                    print(determine)
                    determine = determine - 1
                    if arr1[0] == arr2[0]:
                        print("Success!!")
                        lcd.text("CORRECT!!!", 1)
                        lcd.text("   :D", 2)
                        time.sleep(10)
                        lcd.text("Restarting...",1)
                        time.sleep(3)
                        lcd.clear()
                        time.sleep(2)
                        os.execv(sys.executable, ['python'] + sys.argv)
                    if arr1[0] != arr2[0]:

                        #u = u - 1
                        lcd.text("WRONG!!!", 1)
                        lcd.text("   :(  Lives = " + format(determine), 2)
                        #time.sleep(0.001)
                        time.sleep(3)
                        lcd.clear()





            if GPIO.input(26) == False and determine == 1:
                    if arr1[0] == arr2[0]:
                        print("Success!!")
                        lcd.text("CORRECT!!!", 1)
                        lcd.text("   :D", 2)
                        time.sleep(10)
                        lcd.text("Restarting...",1)
                        time.sleep(3)
                        lcd.clear()
                        time.sleep(2)
                        os.execv(sys.executable, ['python'] + sys.argv)
                    if arr1[0] != arr2[0]:
                        lcd.text("GAME OVER!!!", 1)
                        lcd.text("     >:(", 2)
                        time.sleep(10)
                        lcd.text("Restarting...",1)
                        time.sleep(3)
                        lcd.clear()
                        time.sleep(2)
                        os.execv(sys.executable, ['python'] + sys.argv)



def loop2():
    BS1 = False
    BS2 = False
    counter = 0
    while True:

        for s in range (0,2):

            if counter == 0 and GPIO.input(29) == True:
                #print( "The game has started...")
                        #digdisp(displayer[num2])
                SevenSeg1(random.randint(1,10))
                lcd.text("Game has...", 1)
                lcd.text("     STARTED!!", 2)
                time.sleep(3)
                lcd.text("Choose with Blk", 1)
                lcd.text("Compare with Y", 2)
                time.sleep(100000000)
                s = s+1



            else:

                base()
                lcd.text("Welcome to Guess", 1)
                lcd.text("The Number Game!", 2)
                time.sleep(1.5)
                lcd.text("Hold Grn Button", 1)
                lcd.text("To Start Game!!!", 2)
                time.sleep(1.5)




thread1 = threading.Thread(target=loop1)
thread1.start()

thread2 = threading.Thread(target=loop2)
thread2.start()

thread2 = threading.Thread(target=loop3)
thread2.start()



