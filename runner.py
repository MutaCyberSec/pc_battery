import os,sys,time
print('''
What Would You Like To Do?
[1] Get Battery info Notification
[2]Encrypt P.D.F Document
[3] Sleep Computer

''')
direction = input("Your Option >> ")

def battery():
    print("Welcome Want To Cheack You Battery power")
    print("After How long Would You Like To Recive A Remaining Battery Reminder Notification?")
    time_wai = input("Time Between Notifications >> ")
    time_wait = int(time_wai)
    os.system("python pc_battery.py")
    for x in range(1000000):
        time.sleep(60*time_wait)
        os.system("python pc_battery.py")
    return

def encrypt_pdf():
    print("Welcome To PDF Encryption")
    os.system("python pdf_encrypt.py")
    return


def sleep_comp():
    time_wai = input("Time to Wait In Minutes >> ")
    time_wait = int(time_wai)
    time.sleep(60*time_wait)
    os.system("shutdown -h")
    
    
if direction == "1":
    battery()
if direction == "2":
    encrypt_pdf()
if direction == "3":
    sleep_comp()
