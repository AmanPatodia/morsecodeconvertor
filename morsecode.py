from tkinter import *
window = Tk()

window.title('Morse Code Convertor')


def encryptor():
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
    English = user_value1.get().upper()
    encrypt_text = ' '
    for letters in English:
        if letters != ' ':
            encrypt_text += MORSE_CODE_DICT.get(letters) + " "
        else:
            encrypt_text += ' '

   # t1.delete("1.0", END)
    t1.insert(END, encrypt_text)


def decryptor():
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
    Morsecode = user_value2.get().upper()
    keys_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    normal = ''
    morse = ''
    for letter in Morsecode:
        if letter != ' ':
            i = 0
            morse += letter
        else:
            i = i+1
            if i == 2:
                normal += ' '
            else:
                normal += keys_list[val_list.index(morse)]
                morse = ''

   # t2.delete("1.0", END)
    t2.insert(END, normal.upper())


W = Label(window, text=''' WELCOME TO MORSE CODE CONVERTOR
''',fg="white",bg="black",height=2,width=35)
e1 = Label(window, text="       Enter Statement For Encryption:",fg="green")
user_value1 = StringVar()
e2 = Entry(window, textvariable=user_value1)
e3 = Label(window, text="       Enter Morse Code For Description:",fg="green")
e4 = Label(window, text="Conversion In Morsecode:",fg='green')
user_value2 = StringVar()
e5 = Entry(window, textvariable=user_value2)
e6 = Label(window, text="Conversion In English:",fg='green')
t1 = Text(window, height=1, width=15)
t2 = Text(window, height=1, width=15)

b1 = Button(window, text="Convert", command=encryptor , fg="white",bg="black")
b2 = Button(window, text="Convert", command=decryptor,fg="white",bg="black")

W.grid(row=0, column=2)
e1.grid(row=1, column=1)
e2.grid(row=1, column=2)
b1.grid(row=1, column=4)
e4.grid(row=2, column=1)
t1.grid(row=2, column=2)
e3.grid(row=4, column=1)
e5.grid(row=4, column=2)
b2.grid(row=4, column=4)
e6.grid(row=5, column=1)
t2.grid(row=5, column=2)

window.mainloop()
