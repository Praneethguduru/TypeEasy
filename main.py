import random
from tkinter import *
from tkinter import messagebox
correct_word=0
wrong_word=0
timeleft=60
def timer():
    global timeleft,i
    if timeleft>0:
        timeleft-=1
        time_count_Lable.config(text=timeleft)
        time_count_Lable.after(1000,timer)
    else:
        wordEntry.config(state=DISABLED)
        result=correct_word-wrong_word
        instructionLable.config(text=f'Correct words {correct_word}\n Wrong words {wrong_word} \n Final score {result}')
        if result<7:
            emojiLable.config(image=poorpic)
            emoji2Lable.config(image=poorpic)
        if result>10:
            emojiLable.config(image=goodpic)
            emoji2Lable.config(image=goodpic)
        if result>15:
            emojiLable.config(image=propic)
            emoji2Lable.config(image=propic)

        res=messagebox.askyesno('Confrim','Do you want to play again')
        if res:
            i=0
            timeleft=60
            countLable.config(text='60')
            wordEntry.config(state=NORMAL)
            instructionLable.config(text='Type given word and hit enter')
            emojiLable.config(image='')
            emoji2Lable.config(image='')
i=0
def play_game(event):
    global i,correct_word,wrong_word
    i+=1
    countLable.config(text=i)
    instructionLable.config(text='')
    if timeleft == 60:
        timer()

    if wordEntry.get() == word_list_Lable['text']:
        correct_word += 1

    else:
        wrong_word += 1

    random.shuffle(word_list)
    word_list_Lable.config(text=word_list[0])
    wordEntry.delete(0,END)















root=Tk()
root.title('TYPEEASY')
root.iconbitmap('icon.ico')
root.geometry('700x600+250+100')
root.resizable(0,0)
root.config(bg='azure1')
logoImage=PhotoImage(file='logo.png')
logoLabel=Label(root,image=logoImage,bg='azure1')
logoLabel.place(x=280,y=40)
movinglabel=Label(root,text='Type Easy',font=('helvetica',30),bg='azure1')
movinglabel.place(x=250,y=0)


word_list=['python','apple ','banana','cat','dog', 'elephant','fish','gun', 'hitler',' icecream','jam', 'kite','lion','man',' nigga', 'operater','patrick',' queen','rook',' sachin','tiger', 'undecover',' van',' win','xylophone',' yat',' zam', 'my',' honest',' reaction','blunder',' batman',' nolan', 'meow',' ballz',' ass',
'sacrifice',' hello',' morning', 'evening',' afternoon',' night','sigma']
random.shuffle(word_list)
word_list_Lable=Label(root,text=word_list[0],font=('black cooper',38),bg='azure1')
word_list_Lable.place(x=350,y=350,anchor=CENTER)
wordLable=Label(root,text='Words',font=('Casteller',28,'bold'),bg='azure1')
wordLable.place(x=30,y=150)

countLable=Label(root,text='0',font=('Casteller',28),bg='azure1')
countLable.place(x=70 ,y=200)

timerLable=Label(root,text='Timer',font=('Casteller',28,'bold'),bg='azure1')
timerLable.place(x=530,y=150)

time_count_Lable=Label(root,text='60',font=('Casteller',28),bg='azure1')
time_count_Lable.place(x=550 ,y=200)

wordEntry=Entry(root,font=('arial',25,'bold'),bd=8,justify=CENTER)
wordEntry.place(x=180,y=390)
wordEntry.focus_set()

instructionLable=Label(root,text='Type given word and hit enter',font=('Casteller',20),bg='azure1')
instructionLable.place(x=190 ,y=460)

poorpic=PhotoImage(file='poor.png')
goodpic=PhotoImage(file='good.png')
propic=PhotoImage(file='pro.png')
emojiLable=Label(root,bg='azure1')
emojiLable.place(x=80,y=490)

emoji2Lable=Label(root,bg='azure1')
emoji2Lable.place(x=540,y=490)

root.bind('<Return>',play_game)









root.mainloop()


