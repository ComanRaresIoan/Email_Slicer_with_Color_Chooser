import tkinter as tk
from tkinter import colorchooser

window = tk.Tk()
window.geometry("800x600")
window.config(bg="#004080")
window.resizable(width=False, height=False)
window.title('Simple Email Slicer')

def result():
    try:
        email = entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index('@')]
        domain = inp_email[inp_email.index('@') + 1:]
        text_box.delete('1.0', tk.END)
        msg = 'Email entered was: {}\nYour email username is {}\nAnd your email domain server is {}'
        msg_formatted = msg.format(email, username, domain)
        text_box.insert(tk.END, msg_formatted)
        entry.delete(0, 'end')
    except:
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, "ERROR!")


def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')


def pick_color():
    color = colorchooser.askcolor(title="Select Color")
    if color[1] is not None:
        print("Selected color: ", color[1])
        window.config(bg=color[1])


# Labels
greeting = tk.Label(text="Welcome to the Email Slicer!", font=(12), foreground="white", background="black")
Info = tk.Label(foreground="white", background="#BE361A", font=(10),
                text="Enter your email id click the done button!\n The application will extract your username and domain name.")
entry_label = tk.Label(foreground="white", font=(10), background="black", text="Enter Your Email Id: ")
result_label = tk.Label(font=(10), foreground="white", background="black", text="The results are as follows:")
empty_label0 = tk.Label(background="#0080ff")
empty_label1 = tk.Label(background="#0080ff")
empty_label2 = tk.Label(background="#0080ff")
empty_label3 = tk.Label(background="#0080ff")
empty_label4 = tk.Label(background="#0080ff")
empty_label5 = tk.Label(background="#0080ff")

# Entry
e1 = tk.StringVar()
entry = tk.Entry(font=(11), width=50, justify='center', textvariable=e1)

# Buttons
button = tk.Button(text="Done!", command=result, font=(11))
reset = tk.Button(text="Reset!", command=reset_all, font=(11))
color_button = tk.Button(text="Pick Color", command=pick_color, font=(11))

# Result
text_box = tk.Text(height=5, width=50)

# Packing Everything Together
empty_label0.pack()
greeting.pack()
Info.pack()
empty_label1.pack()
entry_label.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
button.pack()
empty_label5.pack()
reset.pack()
color_button.pack()
empty_label3.pack()
result_label.pack()
text_box.pack()

window.mainloop()
