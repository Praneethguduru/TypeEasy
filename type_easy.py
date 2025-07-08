import random
from tkinter import *
from tkinter import messagebox

# Game stats
correct_word = 0
wrong_word = 0
timeleft = 60
i = 0

# Timer Function
def timer():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_count_Label.config(text=str(timeleft))
        time_count_Label.after(1000, timer)
    else:
        wordEntry.config(state=DISABLED)
        result = correct_word - wrong_word
        instructionLabel.config(
            text=f'Correct words: {correct_word}\nWrong words: {wrong_word}\nFinal score: {result}'
        )

        if result < 7:
            emojiLabel.config(image=poorpic)
            emoji2Label.config(image=poorpic)
        elif result <= 15:
            emojiLabel.config(image=goodpic)
            emoji2Label.config(image=goodpic)
        else:
            emojiLabel.config(image=propic)
            emoji2Label.config(image=propic)

        res = messagebox.askyesno('Confirm', 'Do you want to play again?')
        if res:
            restart_game()

# Restart Logic
def restart_game():
    global correct_word, wrong_word, timeleft, i
    i = 0
    correct_word = 0
    wrong_word = 0
    timeleft = 60
    time_count_Label.config(text='60')
    countLabel.config(text='0')
    wordEntry.config(state=NORMAL)
    instructionLabel.config(text='Type the given word and hit Enter')
    wordEntry.delete(0, END)
    word_list_Label.config(text=random.choice(word_list))
    emojiLabel.config(image=blankpic)
    emoji2Label.config(image=blankpic)

# Game Play
def play_game(event):
    global i, correct_word, wrong_word

    if timeleft == 60:
        timer()

    i += 1
    countLabel.config(text=str(i))
    instructionLabel.config(text='')

    typed_word = wordEntry.get().strip()
    target_word = word_list_Label['text'].strip()

    if typed_word == target_word:
        correct_word += 1
    else:
        wrong_word += 1

    word_list_Label.config(text=random.choice(word_list))
    wordEntry.delete(0, END)

# Word List (cleaned)
word_list = [
    'python', 'apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'gun',
    'icecream', 'jam', 'kite', 'lion', 'man', 'ninja', 'operator', 'patrick',
    'queen', 'rook', 'sachin', 'tiger', 'undercover', 'van', 'win', 'xylophone',
    'yacht', 'zebra', 'my', 'honest', 'reaction', 'blunder', 'batman', 'nolan',
    'meow', 'balls', 'sacrifice', 'hello', 'morning', 'evening', 'afternoon',
    'night', 'sigma'
]

# GUI Setup
root = Tk()
root.title('TYPEEASY')
root.iconbitmap('icon.ico')
root.geometry('700x600+250+100')
root.resizable(0, 0)
root.config(bg='azure1')

# Images
logoImage = PhotoImage(file='logo.png')
poorpic = PhotoImage(file='poor.png')
goodpic = PhotoImage(file='good.png')
propic = PhotoImage(file='pro.png')
blankpic = PhotoImage()  # blank image for reset

# Labels and Entry
logoLabel = Label(root, image=logoImage, bg='azure1')
logoLabel.place(x=280, y=40)

titleLabel = Label(root, text='Type Easy', font=('Helvetica', 30, 'bold'), bg='azure1', fg='black')
titleLabel.place(x=250, y=0)

word_list_Label = Label(root, text=random.choice(word_list), font=('Black Cooper', 38), bg='azure1', fg='black')
word_list_Label.place(x=350, y=350, anchor=CENTER)

wordLabel = Label(root, text='Words', font=('Casteller', 28, 'bold'), bg='azure1', fg='black')
wordLabel.place(x=30, y=150)

countLabel = Label(root, text='0', font=('Casteller', 28), bg='azure1', fg='black')
countLabel.place(x=70, y=200)

timerLabel = Label(root, text='Timer', font=('Casteller', 28, 'bold'), bg='azure1', fg='black')
timerLabel.place(x=530, y=150)

time_count_Label = Label(root, text='60', font=('Casteller', 28), bg='azure1', fg='black')
time_count_Label.place(x=550, y=200)

wordEntry = Entry(root, font=('Arial', 25, 'bold'), bd=8, justify=CENTER, fg='black', bg='white')
wordEntry.place(x=180, y=390)
wordEntry.focus_set()

instructionLabel = Label(root, text='Type the given word and hit Enter', font=('Casteller', 20), bg='azure1', fg='black')
instructionLabel.place(x=120, y=460)

emojiLabel = Label(root, bg='azure1')
emojiLabel.place(x=80, y=490)

emoji2Label = Label(root, bg='azure1')
emoji2Label.place(x=540, y=490)

# Bind Enter key to play
root.bind('<Return>', play_game)

# Main loop
root.mainloop()
