import tkinter as tk,random as r

def resetGame():
    global RandomNum
    global chances

    chances=5
    RandomNum=r.randint(1,10)

    entry.delete(0,tk.END)
    Result.config(text="",bg="#5766C7")

    button.config(text="Check",width=5,command=checkNumber)
    button.place(x=370)

    destroy.destroy()

def checkNumber():
    global chances
    global Result
    global destroy

    chances-=1
    checkNum=RandomNum

    Result=tk.Label(TK)
    Result.place(x=135,y=220)
    Result.config(width=18,height=10)

    user=entry.get()
    if user.isdigit():
        user=int(user)
        
  
        if 1<=user<=10:

            if user==checkNum:

                button.config(text="Play Again",width=8,command=resetGame)
                button.place(x=335)

                destroy=tk.Button(text="Exit",command=lambda:TK.destroy(),font=("Arial",14),bg="#D5483E")
                destroy.place(x=280,y=140)

                Result.config(text=f"The Number is {checkNum}\nCongratulations!\n You guessed the \nnumber correctly.\n\nin {5-chances} chances",fg="green",font=("Arial",20),bg="#4AD35C")

            elif user<checkNum:
                Result.config(text=f"The number is \nhigher than \n{user}. Try again!\n\n{chances} chances left",font=("Arial",20),bg="#3EA1F7")

            elif user>checkNum:    
                Result.config(text=f"The number is \nlower than \n{user}. Try again!\n\n{chances} chances left",font=("Arial",20),bg="#F7B733")

            else:
                pass

        else:
            Result.config(text=f"Please enter a number \nbetween  1 and 10.\n\n{chances} chances left",font=("Arial",20),bg="#E0CA3E")

    else:
        Result.config(text=f"Invalid input. Please \nenter a valid number.\n\n{chances} chances left",fg="white",bg="#EF382E",font=("Arial",20))
    
    if chances==0:
        
        Result.config(text=f"You've used all \nyour chances!\nThe number was {checkNum}.",fg="white",bg="#EF382E",font=("Arial",20))
        destroy.place(x=280,y=140)        
       
        button.config(text="Play Again",width=8,command=resetGame)
        button.place(x=335)

def main():
    global TK
    global button
    global label
    global entry

    TK.title("Guess The Number")
    TK.geometry("600x600")
    TK.config(bg="#5766C7")
    TK.resizable(0,0)

    label.place(x=160,y=20)
    entry.place(x=130,y=100)

    button.place(x=370,y=140)
    button.config(width=5)

TK=tk.Tk()

RandomNum=r.randint(1,10)
chances=5

label=tk.Label(TK,text="Guess The Number \nBetween 1 - 10",font=("Arial",20),bg="#44DA4B",fg="white")
entry=tk.Entry(TK,font=("Arial",20),bg="#68C954",justify="center")

button=tk.Button(TK,text="Check",font=("Arial",14),bg="#4870D5",fg="white",command=checkNumber)
destroy=tk.Button(TK,text="Exit",command=lambda:TK.destroy(),font=("Arial",14),bg="#D5483E")

if __name__=="__main__":
    main()
    TK.mainloop()

