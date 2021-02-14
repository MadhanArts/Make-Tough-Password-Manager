import json
from tkinter import *
from GeneratePassword import generate_password
import pyperclip
from functools import partial


class MakeTough(Tk):
    def __init__(self):
        super().__init__()

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuFrame, AddPasswordFrame, SearchPasswordFrame, SuccessFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuFrame")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

    def go_back(self):
        self.show_frame("MenuFrame")


class MenuFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=100, height=100, padx=30, pady=20,
                       highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
        self.controller = controller

        self.welcome_label = Label(self, text="****** Make Tough ******", fg="brown")
        self.welcome_label.config(font=("Courier", 15, "bold"))
        self.welcome_label.pack()

        # self.menu_label = Label(self, text="What would you like? ([1] espresso/[2] latte/[3] cappuccino)",
        # fg="#123333") self.menu_label.config(font=("Courier", 15, "bold")) self.menu_label.pack()

        # self.choice_edit_text = Entry(self, width=50, font=("Courier", 12))
        # self.choice_edit_text.pack(pady=10)

        self.add_button = Button(self, text='Add', width=50, command=self.add_button_clicked)
        self.add_button.pack()

        self.search_button = Button(self, text='Search', width=50, command=self.search_button_clicked)
        self.search_button.pack()

        # self.message_label = Label(self, text="No option like that sir! Try again")
        # self.message_label.config(font=("Courier", 10))

    def add_button_clicked(self):
        self.controller.show_frame("AddPasswordFrame")

    def search_button_clicked(self):
        self.controller.show_frame("SearchPasswordFrame")


class AddPasswordFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=100, height=100, padx=30, pady=20,
                       highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0)
        self.controller = controller

        self.website_label = Label(self, text="Website : ", fg="brown")
        self.website_label.config(font=("Courier", 15, "bold"))
        self.website_label.grid(row=0, column=0, sticky=W)

        self.website_text = StringVar()
        self.website_edit_text = Entry(self, width=20, font=("Courier", 12), textvariable=self.website_text)
        self.website_edit_text.grid(row=0, column=1, sticky=W)
        self.website_edit_text.focus()

        self.email_label = Label(self, text="Email : ", fg="brown")
        self.email_label.config(font=("Courier", 15, "bold"))
        self.email_label.grid(row=1, column=0, sticky=W)

        self.email_text = StringVar()
        self.email_edit_text = Entry(self, width=20, font=("Courier", 12), textvariable=self.email_text)
        self.email_edit_text.grid(row=1, column=1, sticky=W)

        self.password_length_label = Label(self, text="Password length : ", fg="brown")
        self.password_length_label.config(font=("Courier", 15, "bold"))
        self.password_length_label.grid(row=2, column=0, sticky=W)

        self.password_length = IntVar()
        self.password_length_spinbox = Spinbox(self, width=20, font=("Courier", 12), text=self.password_length,
                                               from_=0, to=100)
        self.password_length_spinbox.grid(row=2, column=1, sticky=W)

        self.generate_password_button = Button(self, text="Generate Password", command=self.generate_password)
        self.generate_password_button.grid(row=3, columnspan=2)

        self.frame = Frame(self)
        self.frame.grid(row=4, columnspan=2)
        self.password_text = StringVar()
        self.password_text.trace("w", lambda name, index, mode, password=self.password_text: self.callback())
        self.generated_password_edit_text = Entry(self.frame, width=30, font=("Courier", 12),
                                                  textvariable=self.password_text)
        self.generated_password_edit_text.grid(row=0, column=0, sticky=E)

        self.copy_password_button = Button(self.frame, text="copy", command=self.copy_password)
        # self.copy_password_button.grid(row=0, column=1, sticky=W)

        self.add_password_button = Button(self, text="Add", command=self.add_password)
        self.add_password_button.grid(row=5, column=0, sticky=E)

        self.back_button = Button(self, text="Back", command=self.back)
        self.back_button.grid(row=5, column=1, sticky=W)

    def back(self):
        self.reset()
        self.controller.show_frame("MenuFrame")

    def generate_password(self):
        temp_password = generate_password(self.password_length.get())
        print(temp_password)
        if self.generated_password_edit_text.get() != "":
            self.generated_password_edit_text.delete(0, END)
        self.generated_password_edit_text.insert(0, temp_password)

    def add_password(self):
        file = open("passwords.json", "r")
        items = []
        # print(file.read())
        if file.read() != "":
            file.seek(0)
            items = json.load(file)
        file.close()

        file = open("passwords.json", "w")
        item = {
            'website_name': self.website_text.get(),
            'mail_id': self.email_text.get(),
            'pass_str': self.password_text.get()
        }
        items.append(item)
        print("Items : ", items)
        json.dump(items, file, indent=4)
        file.close()
        self.reset()

    def copy_password(self):
        pyperclip.copy(self.password_text.get())

    def callback(self):
        if self.password_text.get().strip() == "":
            self.copy_password_button.grid_forget()
        else:
            self.copy_password_button.grid(row=0, column=1)

    def reset(self):
        self.website_edit_text.delete(0, END)
        self.email_edit_text.delete(0, END)
        self.generated_password_edit_text.delete(0, END)
        self.password_length_spinbox.delete(0, END)
        self.password_length_spinbox.insert(0, 0)


class SearchPasswordFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=100, height=100, padx=30, pady=20,
                       highlightbackground="blue", highlightcolor="blue", highlightthickness=1,
                       bd=0)
        self.controller = controller

        self.search_password_frame_title_frame = Frame(self)
        self.search_password_frame_title_frame.pack()
        self.search_password_frame_title_label = Label(self.search_password_frame_title_frame, text="Search Password",
                                                       fg="brown")
        self.search_password_frame_title_label.config(font=("Courier", 15, "bold"))
        self.search_password_frame_title_label.grid(row=0)

        self.search_password_frame_search_box_frame = Frame(self)
        self.search_password_frame_search_box_frame.pack()
        self.search_text = StringVar()
        self.search_password_frame_search_edit_text = Entry(self.search_password_frame_search_box_frame, width=30,
                                                            font=("Courier", 12), textvariable=self.search_text)
        self.search_password_frame_search_edit_text.grid(row=0, column=0)

        self.search_password_frame_search_by_website_button = Button(self.search_password_frame_search_box_frame,
                                                                     text="Search by Website",
                                                                     command=self.search_by_website)
        self.search_password_frame_search_by_website_button.grid(row=0, column=1)
        self.search_password_frame_search_by_username_button = Button(self.search_password_frame_search_box_frame,
                                                                      text="Search by username",
                                                                      command=self.search_by_username)
        self.search_password_frame_search_by_username_button.grid(row=0, column=2)

        self.search_password_frame_search_result_list_frame = Frame(self, highlightbackground="green",
                                                                    highlightcolor="green",
                                                                    highlightthickness=1, bd=0, width=500, height=400)
        self.search_password_frame_search_result_list_frame.pack()

    def search_by_website(self):
        url = self.search_text.get()
        file = open("passwords.json", "r")
        items = json.load(file)
        file.close()
        # search_result_list = Listbox(self.search_password_frame_search_result_list_frame)
        print("Search by result")
        for child in self.search_password_frame_search_result_list_frame.winfo_children():
            child.destroy()
        i = 0
        for item in items:
            if item['website_name'].lower().strip().__contains__(url.lower().strip()):
                # print("URL is : ", item['website_name'])
                # print("mail id is : ", item['mail_id'])
                # print("Password is : ", item['pass_str'])

                search_password_frame_search_list_item_frame = Frame(
                    self.search_password_frame_search_result_list_frame,
                    highlightbackground="blue",
                    highlightcolor="blue",
                    highlightthickness=1, bd=0, width=500
                    )
                search_password_frame_search_list_item_frame.pack(padx=10, pady=10, fill="both", expand=True)
                search_password_frame_search_list_item_frame.grid_rowconfigure(0, weight=1)
                search_password_frame_search_list_item_frame.grid_columnconfigure(0, weight=1, minsize=300)
                search_result_website_label = Label(search_password_frame_search_list_item_frame,
                                                    text=item['website_name'])
                search_result_website_label.grid(row=0, column=0)
                search_result_email_label = Label(search_password_frame_search_list_item_frame,
                                                  text=item['mail_id'])
                search_result_email_label.grid(row=1, column=0)
                search_result_show_password_button = Button(search_password_frame_search_list_item_frame,
                                                            text="Show Password", command=partial(self.change, i))
                search_result_show_password_button.grid(row=0, column=1)
                i += 1

    def search_by_username(self):
        pass

    def show_password(self, i):
        print("id", i)

    def change(self, i):
        print(i)

    def reset(self):
        pass

    def go_back(self):
        self.reset()
        self.controller.show_frame("MenuFrame")


class SuccessFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=100, height=100, padx=30, pady=20,
                       highlightbackground="blue", highlightcolor="blue", highlightthickness=1,
                       bd=0)
        self.controller = controller
        self.success_frame_label = Label(self, fg="brown")
        self.success_frame_label.pack(side="top", fill="x", pady=10)
        self.success_frame_back_button = Button(self, text="Go to main menu",
                                                command=lambda: controller.show_frame("MenuFrame"))
        self.success_frame_back_button.pack()

    def label_config(self, text):
        self.success_frame_label.config(font=("Courier", 15, "bold"), text=text)


my_machine = MakeTough()

my_machine.geometry("1000x500")
my_machine.title("Make Tough")

my_machine.mainloop()
