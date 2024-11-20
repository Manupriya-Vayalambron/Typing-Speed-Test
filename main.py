import tkinter as tk
from tkinter import ttk
import ttkthemes as tt
import time as tm
import threading
import random
import pyttsx3

# Initial Variables

timelimit=60
rem=timelimit
elapsed=0
total=0
wrong=0
wpm=0
acc=0
melo=pyttsx3.init()

def start_timer():
    global elapsed

    entry.focus()
    entry.config(state='normal')
    btn_start.config(state='disabled')
    for time in range(1,timelimit+1):
        elapsed=time

        updatedrem= rem-elapsed
        lbl_remTimer['text']=updatedrem

        tm.sleep(1)
        window.update()

    entry.config(state='disabled')
    btn_reset.config(state='normal')
    melo.say("Time Over")
    melo.runAndWait()

def count():
    global wrong
    global elapsed
    global total
    global wpm
    global acc

    #paragraph given
    para_words=lbl_para['text'].split()
    while(elapsed != timelimit):
        #words entered by user
        entered=entry.get(1.0,'end-1c').split()
        total=len(entered)

    #comparing each word of para with the word entered by user
    for pair in list(zip(para_words,entered)):
        if pair[0] != pair[1]:
            wrong+=1

    wpm = total - wrong
    grosswpm=total
    acc=(wpm/grosswpm)*100
    lbl_wpm['text']=wpm

    lbl_acc['text']=round(acc,2)

    lbl_total['text']=total

    lbl_wrong['text']=wrong

def start():
    thread1=threading.Thread(target=start_timer)
    thread1.start()

    thread2=threading.Thread(target=count)
    thread2.start()

def reset():
    global rem
    global elapsed

    btn_reset.config(state='disabled')
    btn_start.config(state='normal')

    entry.config(state='normal')
    entry.delete(1.0,tk.END)
    entry.config(state='disabled')

    rem=timelimit
    elapsed=0

    lbl_remTimer['text']=rem
    lbl_wpm['text']=0
    lbl_total['text']=0
    lbl_acc['text']=0
    lbl_wrong['text']=0
    
#changing paragraph
with open('paragraph.txt') as f:
    paragraphs=f.readlines()
    selected_paragraph=random.choice(paragraphs)







#******************************************************GUI**********************************************
window= tt.ThemedTk()
window.get_themes()
window.set_theme("radiance")
window.title("Typo Speed")
window.geometry("1100x900+400+20")
window.resizable(False,False)
#Main Frame
main_frame=tk.Frame(window,bg="white",bd=4)  
#Title frame
frame_title=tk.Frame(main_frame,bg="orange",relief="flat")
lbl_title=tk.Label(frame_title,text="Typo Speed Test",font='Algerian 35 bold',bg="yellow",fg="black",relief="flat",bd=10,width=30)
lbl_title.grid(row=0,column=0,pady=10)
frame_title.grid(row=0,column=0)

#Test Frame
frame_test=tk.LabelFrame(main_frame,text="Test",bg="white",relief="groove")
#Paragraph
lbl_para=tk.Label(frame_test,text=selected_paragraph,wraplength=1000,justify="left")
lbl_para.grid(row=0,column=0,pady=5)
#InputBox
entry=tk.Text(frame_test,height=8,width=110,bd=2)
entry.grid(row=1,column=0,pady=5,padx=5)
entry.config(state="disabled")
frame_test.grid(row=1,column=0)

#Output Frame
frame_output=tk.Frame(main_frame,bg="white",relief="flat")
frame_labels=tk.Frame(frame_output,bg="white")

#remaining time
lbl_rem=tk.Label(frame_labels,text="Remaining Time",font="Tahoma 10 bold",fg="red",bg="white")
lbl_remTimer=tk.Label(frame_labels,text="60",font="Tahoma 10 bold",fg="black",bg="white")
lbl_rem.grid(row=0,column=0,padx=10,pady=10)
lbl_remTimer.grid(row=0,column=1,padx=10,pady=10)
#wpm
lbl_wpm_title=tk.Label(frame_labels,text="Words Per Minute",font="Tahoma 10 bold",fg="red",bg="white")
lbl_wpm=tk.Label(frame_labels,text="0",font="Tahoma 10 bold",fg="black",bg="white")
lbl_wpm_title.grid(row=0,column=2,padx=10,pady=10)
lbl_wpm.grid(row=0,column=3,padx=10,pady=10)
#accuracy
lbl_acc_title=tk.Label(frame_labels,text="Accuracy",font="Tahoma 10 bold",fg="red",bg="white")
lbl_acc=tk.Label(frame_labels,text="0",font="Tahoma 10 bold",fg="black",bg="white")
lbl_acc_title.grid(row=0,column=4,padx=10,pady=10)
lbl_acc.grid(row=0,column=5,padx=10,pady=10)
#total words
lbl_total_title=tk.Label(frame_labels,text="Total Words",font="Tahoma 10 bold",fg="red",bg="white")
lbl_total=tk.Label(frame_labels,text="0",font="Tahoma 10 bold",fg="black",bg="white")
lbl_total_title.grid(row=0,column=6,padx=10,pady=10)
lbl_total.grid(row=0,column=7,padx=10,pady=10)
#wrong words
lbl_wrong_title=tk.Label(frame_labels,text="Wrong Words",font="Tahoma 10 bold",fg="red",bg="white")
lbl_wrong=tk.Label(frame_labels,text="0",font="Tahoma 10 bold",fg="black",bg="white")
lbl_wrong_title.grid(row=0,column=8,padx=10,pady=10)
lbl_wrong.grid(row=0,column=9,padx=10,pady=10)

frame_control=tk.Frame(frame_output,bg="white")
#START BUTTON
btn_start=ttk.Button(frame_control,text="Start",command=start)
btn_start.grid(row=0,column=0,padx=10)
#RESET BUTTON
btn_reset=ttk.Button(frame_control,text="Reset",command=reset)
btn_reset.grid(row=0,column=1,padx=10)
btn_reset.config(state="disabled")

frame_control.grid(row=1)

frame_labels.grid(row=0)
frame_output.grid(row=2,column=0)
#Keyboard Frame

frame_keyboard=tk.Frame(main_frame,bg="white")
#1-0
frame_1_0=tk.Frame(frame_keyboard,bg="white")
lb_1=tk.Label(frame_1_0,text="1",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_2=tk.Label(frame_1_0,text="2",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_3=tk.Label(frame_1_0,text="3",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_4=tk.Label(frame_1_0,text="4",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_5=tk.Label(frame_1_0,text="5",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_6=tk.Label(frame_1_0,text="6",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_7=tk.Label(frame_1_0,text="7",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_8=tk.Label(frame_1_0,text="8",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_9=tk.Label(frame_1_0,text="9",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_0=tk.Label(frame_1_0,text="0",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)

lb_1.grid(row=0,column=0,padx=10,pady=5)
lb_2.grid(row=0,column=1,padx=10,pady=5)
lb_3.grid(row=0,column=2,padx=10,pady=5)
lb_4.grid(row=0,column=3,padx=10,pady=5)
lb_5.grid(row=0,column=4,padx=10,pady=5)
lb_6.grid(row=0,column=5,padx=10,pady=5)
lb_7.grid(row=0,column=6,padx=10,pady=5)
lb_8.grid(row=0,column=7,padx=10,pady=5)
lb_9.grid(row=0,column=8,padx=10,pady=5)
lb_0.grid(row=0,column=9,padx=10,pady=5)

frame_1_0.grid(row=0)
#q-p

frame_q_p=tk.Frame(frame_keyboard,bg="white")
lb_q=tk.Label(frame_q_p,text="q",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_w=tk.Label(frame_q_p,text="w",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_e=tk.Label(frame_q_p,text="e",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_r=tk.Label(frame_q_p,text="r",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_t=tk.Label(frame_q_p,text="t",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_y=tk.Label(frame_q_p,text="y",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_u=tk.Label(frame_q_p,text="u",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_i=tk.Label(frame_q_p,text="i",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_o=tk.Label(frame_q_p,text="o",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_p=tk.Label(frame_q_p,text="p",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)

lb_q.grid(row=1,column=0,padx=10,pady=5)
lb_w.grid(row=1,column=1,padx=10,pady=5)
lb_e.grid(row=1,column=2,padx=10,pady=5)
lb_r.grid(row=1,column=3,padx=10,pady=5)
lb_t.grid(row=1,column=4,padx=10,pady=5)
lb_y.grid(row=1,column=5,padx=10,pady=5)
lb_u.grid(row=1,column=6,padx=10,pady=5)
lb_i.grid(row=1,column=7,padx=10,pady=5)
lb_o.grid(row=1,column=8,padx=10,pady=5)
lb_p.grid(row=1,column=9,padx=10,pady=5)

frame_q_p.grid(row=1)
#a-l

frame_a_l=tk.Frame(frame_keyboard,bg="white")
lb_a=tk.Label(frame_q_p,text="a",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_s=tk.Label(frame_q_p,text="s",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_d=tk.Label(frame_q_p,text="d",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_f=tk.Label(frame_q_p,text="f",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_g=tk.Label(frame_q_p,text="g",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_h=tk.Label(frame_q_p,text="h",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_j=tk.Label(frame_q_p,text="j",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_k=tk.Label(frame_q_p,text="k",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_l=tk.Label(frame_q_p,text="l",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)

lb_a.grid(row=2,column=0,padx=10,pady=5)
lb_s.grid(row=2,column=1,padx=10,pady=5)
lb_d.grid(row=2,column=2,padx=10,pady=5)
lb_f.grid(row=2,column=3,padx=10,pady=5)
lb_g.grid(row=2,column=4,padx=10,pady=5)
lb_h.grid(row=2,column=5,padx=10,pady=5)
lb_j.grid(row=2,column=6,padx=10,pady=5)
lb_k.grid(row=2,column=7,padx=10,pady=5)
lb_l.grid(row=2,column=8,padx=10,pady=5)

frame_a_l.grid(row=2)
#z-m

frame_z_m=tk.Frame(frame_keyboard,bg="white")
lb_z=tk.Label(frame_z_m,text="z",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_x=tk.Label(frame_z_m,text="x",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_c=tk.Label(frame_z_m,text="c",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_v=tk.Label(frame_z_m,text="v",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_b=tk.Label(frame_z_m,text="b",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_n=tk.Label(frame_z_m,text="n",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)
lb_m=tk.Label(frame_z_m,text="m",bg="black",fg="white",relief="groove",width=5,height=2,bd=10)

lb_z.grid(row=3,column=0,padx=10,pady=5)
lb_x.grid(row=3,column=1,padx=10,pady=5)
lb_c.grid(row=3,column=2,padx=10,pady=5)
lb_v.grid(row=3,column=3,padx=10,pady=5)
lb_b.grid(row=3,column=4,padx=10,pady=5)
lb_n.grid(row=3,column=5,padx=10,pady=5)
lb_m.grid(row=3,column=6,padx=10,pady=5)

frame_z_m.grid(row=3)
#space
frame_space=tk.Frame(frame_keyboard,bg="white")
lb_space=tk.Label(frame_space,bg="black",fg="white",relief="groove",width=40,height=2,bd=10)
lb_space.grid(row=0,padx=10,pady=5,column=0)
frame_space.grid(row=4)

frame_keyboard.grid(row=3,pady=10)
main_frame.grid(row=0,column=0)
main_frame.pack(expand=True, fill='both')


#Key Bindings

def changebg(widget):
    bg="black"
    widget.configure(background="blue")
    widget.after(100,lambda color=bg:widget.configure(background=color))

labels_numbers=[lb_1,lb_2,lb_3,lb_4,lb_5,lb_6,lb_7,lb_8,lb_9,lb_0]
labels_alpha=[lb_a,lb_b,lb_c,lb_d,lb_e,lb_f,lb_g,lb_h,lb_i,lb_j,lb_k,lb_l,lb_m,lb_n,lb_o,lb_p,lb_q,lb_r,lb_s,lb_t,lb_u,lb_v,lb_w,lb_x,lb_y,lb_w]
labels_space=[lb_space]

binding_numbers=['1','2','3','4','5','6','7','8','9','0']
binding_capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
binding_small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for number in range(len(binding_numbers)):
    window.bind(f"{binding_numbers[number]}",lambda event,label=labels_numbers[number]: changebg(label))

for cap in range(len(binding_capital)):
    window.bind(f"{binding_capital[cap]}",lambda event,label=labels_alpha[cap]: changebg(label))

for small in range(len(binding_small)):
    window.bind(f"{binding_small[small]}",lambda event,label=labels_alpha[small]: changebg(label))

window.bind("<space>",lambda event,label=labels_space[0]: changebg(label))

window.mainloop()
