from tkinter import *
import sqlite3


conn = sqlite3.connect("calculator.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        expression TEXT,
        result TEXT
    )
""")
conn.commit()

firstnumber = None
operator = None

def digit(value):
    currenttext = resultlabel.cget("text")
    resultlabel.config(text=currenttext + str(value))

def clear():
    global firstnumber, operator
    firstnumber = None
    operator = None
    resultlabel.config(text="")

def setoprater(op):
    global firstnumber, operator
    first_number = resultlabel.cget("text")
    operator = op
    resultlabel.config(text=first_number + op)

def equal():
    try:
        expression = resultlabel.cget("text")
        result = str(eval(expression))
        resultlabel.config(text=result)

        cursor.execute("INSERT INTO history (expression, result) VALUES (?, ?)", (expression, result))
        conn.commit()

    except ZeroDivisionError:
        resultlabel.config(text="Cannot divide by zero",)
    except Exception as e:
        resultlabel.config(text="Error")

def percentage():
    try:
        current_value = float(resultlabel.cget("text"))
        resultlabel.config(text=str(current_value / 100))
    except ValueError:
        resultlabel.config(text="Error")

def delete():
    current_text = resultlabel.cget("text")
    resultlabel.config(text=current_text[:-1])


def insertparentheses():
    currenttext = resultlabel.cget("text")
    opencount = currenttext.count("(")
    closecount = currenttext.count(")")

    if opencount == closecount or currenttext[-1] in "+-*/(":
        resultlabel.config(text=currenttext + "(")
    else:
        resultlabel.config(text=currenttext + ")")

def showhistory():
    if historylabel.cget("text") == "":
        cursor.execute("SELECT * FROM history ORDER BY id DESC LIMIT 5")
        record = cursor.fetchall()

        historytext = "\n".join([f"{i[1]} = {i[2]}" for i in record])
        historylabel.config(text=historytext)
    else:
        historylabel.config(text="")


root = Tk()
root.geometry("326x460")
logo = PhotoImage(file="calculater logo.png")
root.iconphoto(False, logo)
root.title("Calculator")
root.resizable(0,0)
root.configure(background='#D3D3D3')

## Move history label to the top
historylabel = Label(root, text='', bg="#D3D3D3", fg="black", anchor="w",font=('Arial', 12), height=5, width=30, justify=LEFT)
historylabel.grid(row=0, column=0, columnspan=5, padx=0, pady=(0, 0), sticky="ew")

# Move result label below history
resultlabel = Label(root, text='', bg="#D3D3D3", fg="black", anchor="e",width=11, height=2, padx=10, font=('Arial', 18, 'bold'))
resultlabel.grid(row=1, column=0, columnspan=5, pady=(0, 0), padx=0, sticky="ew")

btn_font = ('Arial', 14, 'bold')
btn_width = 6
btn_height = 2

#histroy button
Button(root, text="History", bg="#D3D3D3", fg="black", font=('Arial', 8, 'bold'), height=2, width=5, command=showhistory).place(x=282, y=0)


# Row 1 (Operators)
Button(root, text="%", bg="#D3D3D3", fg="black", font=btn_font,height=btn_height, width=btn_width,command=lambda:percentage()).grid(row=2, column=1)
Button(root, text="CE", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width,command=clear).grid(row=2, column=2)
Button(root, text="()", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width, command=insertparentheses).grid(row=2, column=3)
Button(root, text="/", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width,command=lambda: setoprater("/")).grid(row=2, column=4)

# Row 2 (Numbers & Operators)
Button(root, text="7", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height,width=btn_width,command=lambda: digit("7") ).grid(row=3, column=1)
Button(root, text="8", bg="#D3D3D3", fg="black", font=btn_font,  height=btn_height,width=btn_width,command=lambda: digit("8")).grid(row=3, column=2)
Button(root, text="9", bg="#D3D3D3", fg="black", font=btn_font,  height=btn_height,width=btn_width, command=lambda: digit("9")).grid(row=3, column=3)
Button(root, text="*", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width,command=lambda: setoprater("*")).grid(row=3, column=4)

# Row 3 (Numbers & Operators)
Button(root, text="4", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height,width=btn_width, command=lambda: digit("4")).grid(row=4, column=1)
Button(root, text="5", bg="#D3D3D3", fg="black", font=btn_font,  height=btn_height,width=btn_width,command=lambda: digit("5")).grid(row=4, column=2)
Button(root, text="6", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height,width=btn_width,command=lambda: digit("6")).grid(row=4, column=3)
Button(root, text="-", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width,command=lambda: setoprater("-")).grid(row=4, column=4)

# Row 4 (Numbers & Operators)
Button(root, text="1", bg="#D3D3D3", fg="black", font=btn_font,  height=btn_height,width=btn_width,command=lambda: digit("1")).grid(row=5, column=1)
Button(root, text="2", bg="#D3D3D3", fg="black", font=btn_font,  height=btn_height,width=btn_width,command=lambda: digit("2")).grid(row=5, column=2)
Button(root, text="3", bg="#D3D3D3", fg="black", font=btn_font,  height=btn_height,width=btn_width,command=lambda: digit("3")).grid(row=5, column=3)
Button(root, text="+", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width,command=lambda: setoprater("+")).grid(row=5, column=4)

# Row 5 (Numbers & Actions)
Button(root, text="0", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width, command=lambda: digit("0"),).grid(row=6, column=1)
Button(root, text=".", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width,command=lambda: digit(".")).grid(row=6, column=2)
Button(root, text="Del", bg="#D3D3D3", fg="black", font=btn_font,height=btn_height, width=btn_width,command=lambda:delete()).grid(row=6, column=3)
Button(root, text="=", bg="#D3D3D3", fg="black", font=btn_font, height=btn_height, width=btn_width, command=equal).grid(row=6, column=4)

root.mainloop()
