import time
import random
fileread = open("password.txt","r")

read = fileread.readlines()

pas = read[3]
pas = pas.strip()





def password(b,c):
    while b>0:

        print("Enter Password:")

        a = input()



        if a == pas:
            print("Correct.....Unlocked!!")


            exit()

        else:
            print("Wrong...Try Again!!")

        if b<=5:
            print("Hint: ",read[1])

        b = b-1
        if b == 0:
            print("Wait for",c," sec")

            time.sleep(c)


            break

def forgotpassword():

    c = read[5].replace("name:","").strip()
    d = read[6].replace("text:","").strip()

    e = input("enter name: ")
    f = input("enter text file name: ")
    if e==c:
        if f==d:
            filewrite = open("forgotpass.txt","a")
            #opt
            lenght = 6
            sstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

            otpass = ''.join(random.choices(sstr, k=lenght))

            #

            filewrite.write(otpass)
            filewrite = open("forgotpass.txt", "w")
            filewrite.write("")


            print("we have send a otp in forgotpass.txt")


            g = 1
            while g>0:
                otp = input("Enter otp")
                if otp==otpass:
                    print("Unlocked!!")
                    print("Change password")
                    chgpass = input("Enter New password: ")


                    lines = open("password.txt", 'r').readlines()
                    lines[3] = chgpass+"\n"
                    out = open("password.txt", 'w')
                    out.writelines(lines)
                    print("Password Changed!!")

                    break
                else:
                    print("Invalid OTP")
                g= g-1







        else:
            print("Invalid Identity")
    else:
        print("Invalid Identity")



def passwordlasttime(b):

    while b > 0:

        print("Enter Password:")

        a = input()

        if a == pas:
            print("Correct.....Unlocked!!")

            exit()

        else:
            print("Wrong...Try Again!!")

        if b <= 5:
            print("Hint: ", read[1])

        b = b - 1
        if b==0:
            print("EMERGENCY!!!.....unknown user")
            print("Access Denied")




password(2,2)
x = input("Forgot pass?(yes/no) ")
if x=="yes":
    forgotpassword()
else:
    password(2,2)
    passwordlasttime(2)

