from tkinter import *
from tkinter import messagebox
import string
import db

# fonts
font_family = 'Script'
title = (font_family, 35, 'bold')
large_text = (font_family, 30)
medium_text = (font_family, 20)
small_text = (font_family, 12)
error_text = (font_family, 15)

# colours
win_bg = 'dark slate blue'
main_bg = 'slate blue'
input_bg = 'light slate blue'
create_bg = 'light slate blue'
welcome_bg = 'light slate blue'

class Win():
    def __init__(self):
        self.win = Tk()
        self.win.title('GUI')
        self.win.resizable(0,0)
        self.win.geometry('400x600')
        self.win.configure(bg=win_bg)

        self.main = Frame(self.win, width=360, height=560, bg=main_bg)
        self.main.grid(row=0, column=0, padx=20, pady=20)

        Label(self.main, text='GUI', font=title, bg=main_bg).grid(row=0, column=0)

        self.validate_user = self.win.register(self.username_check)
        self.validate_pass = self.win.register(self.password_check)

        self.input_frame()

    # sanitise input/s
    def username_check(self, char):
        valid_chars = valid_chars = string.ascii_letters + string.digits
        if len(char) > 1:
            for i in char:
                if i not in char or i not in valid_chars:
                    return False
                
            return True

        return char in valid_chars

    def password_check(self, char):
        valid_chars = string.ascii_letters + string.digits + string.punctuation

        if len(char) > 1:
            for i in char:
                if i not in char or i not in valid_chars:
                    return False
                
            return True

        return char in valid_chars

    # check credentials
    def login(self):
        username = self.user_entry_input.get()
        password = self.pass_entry_input.get()

        if db.check_user(username, password):
            self.error_message_input.configure(text='')
            self.username = username
            self.input_f.destroy()
            self.welcome_frame()
        else:
            self.error_message_input.configure(text='Wrong username or password.')
            
    # create credentials
    def create(self):
        username = self.user_entry_create.get()
        password = self.pass_entry_create.get()
        again = self.again_entry_create.get()

        if len(username) < 5 or len(username) > 16:
            self.error_message_create.configure(text='Username must be between\n5-16 characters.')
            return
        elif len(password) < 8 or len(password) > 64:
            self.error_message_create.configure(text='Password must be between\n8-64 characters.')
            return
        elif password != again:
            self.error_message_create.configure(text='Passwords do not match.')
            return
        
        check = db.add_user(username, password)

        if not check:
            self.error_message_create.configure(text='Username already exists.')
        elif check:
            messagebox.showinfo('Success', f'Made account with username: {username}')
            self.create_f.destroy()
            self.input_frame()

    # login frame
    def input_frame(self):
        self.input_f = Frame(self.main, width=320, height=420, bg=input_bg)
        self.input_f.grid(row=1, column=0, padx=20, pady=20)

        Frame(self.input_f, width=320, height=0, bg=input_bg).grid(row=0, column=0) # sets width

        Label(self.input_f, text='Login', font=large_text, bg=input_bg).grid(row=1, column=0, pady=30)

        Label(self.input_f, text='Enter username:', font=medium_text, bg=input_bg).grid(row=2, column=0)
        self.user_entry_input = Entry(self.input_f, font=small_text, highlightbackground=main_bg, highlightthickness=3, border=False, validate='key', validatecommand=(self.validate_user, '%S'))
        self.user_entry_input.grid(row=3, column=0)

        Label(self.input_f, text='Enter password:', font=medium_text, bg=input_bg).grid(row=4, column=0)
        self.pass_entry_input = Entry(self.input_f, font=small_text, highlightbackground=main_bg, highlightthickness=3, border=False, validate='key', validatecommand=(self.validate_pass, '%S'), show='*')
        self.pass_entry_input.grid(row=5, column=0)

        self.error_message_input = Label(self.input_f, text='', font=error_text, fg='red', bg=input_bg)
        self.error_message_input.grid(row=6, column=0)

        Button(self.input_f, text='Login', font=small_text, bg=input_bg, highlightbackground=main_bg, highlightthickness=3, border=False, width=5, command=self.login).grid(row=7, column=0, pady=10)
        Button(self.input_f, text='Create', font=small_text, bg=input_bg, highlightbackground=main_bg, highlightthickness=3, border=False, width=5, command=self.create_frame).grid(row=8, column=0, pady=10)

    # back button
    def back(self):
        self.create_f.destroy()
        self.input_frame()

    # create frame
    def create_frame(self):
        self.input_f.destroy()

        self.create_f = Frame(self.main, width=320, height=420, bg=create_bg)
        self.create_f.grid(row=1, column=0, padx=20, pady=20)

        Frame(self.create_f, width=320, height=0, bg=create_bg).grid(row=0, column=0) # sets width

        Label(self.create_f, text='Create', font=large_text, bg=create_bg).grid(row=1, column=0, pady=5)

        Label(self.create_f, text='Enter username:', font=medium_text, bg=create_bg).grid(row=2, column=0)
        self.user_entry_create = Entry(self.create_f, font=small_text, highlightbackground=main_bg, highlightthickness=3, border=False, validate='key', validatecommand=(self.validate_user, '%S'))
        self.user_entry_create.grid(row=3, column=0)

        Label(self.create_f, text='Enter password:', font=medium_text, bg=create_bg).grid(row=4, column=0)
        self.pass_entry_create = Entry(self.create_f, font=small_text, highlightbackground=main_bg, highlightthickness=3, border=False, validate='key', validatecommand=(self.validate_pass, '%S'), show='*')
        self.pass_entry_create.grid(row=5, column=0)

        Label(self.create_f, text='Enter password again:', font=medium_text, bg=create_bg).grid(row=6, column=0)
        self.again_entry_create = Entry(self.create_f, font=small_text, highlightbackground=main_bg, highlightthickness=3, border=False, validate='key', validatecommand=(self.validate_pass, '%S'), show='*')
        self.again_entry_create.grid(row=7, column=0)

        self.error_message_create = Label(self.create_f, text='', font=error_text, fg='red', bg=create_bg)
        self.error_message_create.grid(row=8, column=0)

        Button(self.create_f, text='Create', font=small_text, bg=create_bg, highlightbackground=main_bg, highlightthickness=3, border=False, width=5, command=self.create).grid(row=9, column=0, pady=10)
        Button(self.create_f, text='Back', font=small_text, bg=create_bg, highlightbackground=main_bg, highlightthickness=3, border=False, width=5, command=self.back).grid(row=10, column=0, pady=10)

    # log out
    def log_out(self):
        self.welcome_f.destroy()
        self.input_frame()

    # if login is success welcome user
    def welcome_frame(self):
        self.welcome_f = Frame(self.main, width=320, height=420, bg=welcome_bg)
        self.welcome_f.grid(row=1, column=0, padx=20, pady=20)

        Frame(self.welcome_f, width=320, height=0, bg=welcome_bg).grid(row=0, column=0) # sets width

        Label(self.welcome_f, text='GUI', font=large_text, bg=welcome_bg).grid(row=1, column=0, pady=30)

        Label(self.welcome_f, text=f'Welcome, {self.username}!', font=medium_text, bg=welcome_bg).grid(row=2, column=0)

        Button(self.welcome_f, text='Log-out', font=small_text, bg=main_bg, highlightbackground=main_bg, highlightthickness=3, border=False, width=5, command=self.log_out).grid(row=3, column=0, pady=10)

# creates the window
w = Win()

# mainloop
w.win.mainloop()