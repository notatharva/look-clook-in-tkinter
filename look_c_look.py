from heapq import *
from tkinter import *
import tkinter.messagebox


# hp is initial head position
# and requests is the list of requests
# no of cylinders is 200
def num():
    number = e1.get()
    print("" + number)
    global n
    n = int(number, 10)

def head():
    number = e2.get()
    global hp
    hp = int(number, 10)


def req():
    st = e3.get()
    global request
    request = []
    request = list(st.split(" "))
    if (len(request) == n):
        for i in range(0, len(request)):
            request[i] = int(request[i])
    else:
        tkinter.messagebox.showinfo("Error", "number of requests dont match no of i/o requests")
        exit()
    LOOK(hp,request)
    labLook=Label(root,text=""+se).grid(row=5)
    C_LOOK(hp, request)
    labCLook=Label(root,text=""+se2).grid(row=5,column=1)



def do():
    num()
    head()
    req()


def LOOK(hp, reqs):
    global se
    se=""
    requests = reqs.copy()
    pos = hp
    time = 0
    end = max(requests)
    start = min(requests)
    # seek from curr_pos to end which is 200
    for i in range(pos, end + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            se=se+"Seeked : "+str(i)+"\n"
            requests.remove(i)
    for i in range(end, start - 1, -1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            se=se+"Seeked : "+str(i)+"\n"
            requests.remove(i)
    tat1=Label(root,text="Total seek time : "+str(time)).grid(row=6)
    # calculate average seek time
    avg_seek_time = time / n
    atat1=Label(root,text="Average seek time : "+str(avg_seek_time)).grid(row=7)


def C_LOOK(hp, reqs):
    global se2
    se2=""
    requests = reqs.copy()
    pos = hp
    time = 0
    end = max(requests)
    start = min(requests)
    # seek from curr_pos to max of list
    for i in range(pos, end + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            se2=se2+"Seeked : "+str(i)+"\n"
            requests.remove(i)

    time += abs(pos - start)
    pos = start
    # seek to hp from start
    for i in range(start, hp + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            se2=se2+"Seeked : "+str(i)+"\n"
            requests.remove(i)
    tat1=Label(root,text="Total seek time : "+str(time)).grid(row=6,column=1)
    # calculate average seek time
    avg_seek_time = time / n
    atat2=Label(root,text="Average seek time : "+str(avg_seek_time)).grid(row=7,column=1)


root = Tk()
root.geometry("600x300")
l1 = Label(root, text="Provide number of I/O requests").grid(row=0, column=0)
# n is the number of I/O requests
e1 = Entry(root)
e1.grid(row=0, column=1)
l3 = Label(root, text="").grid(row=2, column=0)
l2 = Label(root, text="Provide initial position of disc arm (total cylinders=200)").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
b1 = Button(root, text="Do", command=do).grid(row=3, column=0)
l3 = Label(text="Provide positions to visit : max is 200").grid(row=2)
e3 = Entry(root)
e3.grid(row=2, column=1)
txt=StringVar()
lab=Label(root,textvariable=txt).grid(row=5)
global Var

root.mainloop()
