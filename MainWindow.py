from tkinter import *
from GeneratePassword import generate_password


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

        self.enter_button = Button(self, text='Add', width=50, command=self.add_button_clicked)
        self.enter_button.pack()

        # self.message_label = Label(self, text="No option like that sir! Try again")
        # self.message_label.config(font=("Courier", 10))

    def add_button_clicked(self):
        self.controller.show_frame("AddPasswordFrame")


class AddPasswordFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=100, height=100, padx=30, pady=20,
                       highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0)
        self.controller = controller

        self.website_label = Label(self, text="Website : ", fg="brown")
        self.website_label.config(font=("Courier", 15, "bold"))
        self.website_label.grid(row=0, column=0, sticky=W)

        self.website_edit_text = Entry(self, width=20, font=("Courier", 12))
        self.website_edit_text.grid(row=0, column=1, sticky=W)

        self.email_label = Label(self, text="Email : ", fg="brown")
        self.email_label.config(font=("Courier", 15, "bold"))
        self.email_label.grid(row=1, column=0, sticky=W)

        self.email_edit_text = Entry(self, width=20, font=("Courier", 12))
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
        self.password = StringVar()
        self.password.trace("w", lambda name, index, mode, password=self.password: self.callback())
        self.generated_password_edit_text = Entry(self.frame, width=30, font=("Courier", 12),
                                                  textvariable=self.password)
        self.generated_password_edit_text.grid(row=0, column=0, sticky=E)

        self.copy_password_button = Button(self.frame, text="copy", command=self.copy_password)
        # self.copy_password_button.grid(row=0, column=1, sticky=W)

        self.add_password_button = Button(self, text="Add", command=self.add_password)
        self.add_password_button.grid(row=5, column=0, sticky=E)

        self.back_button = Button(self, text="Back", command=self.back)
        self.back_button.grid(row=5, column=1, sticky=W)

        # self.report_back_button = Button(self, text="Back", command=controller.go_back)
        # self.report_back_button.pack()

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
        pass

    def copy_password(self):
        pass

    def callback(self):
        if self.password.get().strip() == "":
            self.copy_password_button.grid_forget()
            # self.generated_password_edit_text.grid(row=4, columnspan=2)

        else:
            # self.generated_password_edit_text.grid(row=4, column=0)
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

        self.process_coins_frame_title_label = Label(self, text="Process Coins :", fg="brown")
        self.process_coins_frame_title_label.config(font=("Courier", 15, "bold"))
        self.process_coins_frame_title_label.pack()

        self.process_coins_frame_quarter_label = Label(self, text="Enter number of quarters : ", fg="#123333")
        self.process_coins_frame_quarter_label.config(font=("Courier", 15, "bold"))
        self.process_coins_frame_quarter_label.pack()
        self.process_coins_frame_quarter_edit_text = Spinbox(self, width=50, font=("Courier", 12), from_=0, to=100)
        self.process_coins_frame_quarter_edit_text.pack()

        self.process_coins_frame_dimes_label = Label(self, text="Enter number of dimes : ", fg="#123333")
        self.process_coins_frame_dimes_label.config(font=("Courier", 15, "bold"))
        self.process_coins_frame_dimes_label.pack()
        self.process_coins_frame_dimes_edit_text = Spinbox(self, width=50, font=("Courier", 12), from_=0, to=100)
        self.process_coins_frame_dimes_edit_text.pack()

        self.process_coins_frame_nickel_label = Label(self, text="Enter number of nickles : ", fg="#123333")
        self.process_coins_frame_nickel_label.config(font=("Courier", 15, "bold"))
        self.process_coins_frame_nickel_label.pack()
        self.process_coins_frame_nickel_edit_text = Spinbox(self, width=50, font=("Courier", 12), from_=0, to=100)
        self.process_coins_frame_nickel_edit_text.pack()

        self.process_coins_frame_pennies_label = Label(self, text="Enter number of pennies : ", fg="#123333")
        self.process_coins_frame_pennies_label.config(font=("Courier", 15, "bold"))
        self.process_coins_frame_pennies_label.pack()
        self.process_coins_frame_pennies_edit_text = Spinbox(self, width=50, font=("Courier", 12), from_=0, to=100)
        self.process_coins_frame_pennies_edit_text.pack()

        self.process_coins_frame_submit_button = Button(self, text="Submit")
        self.process_coins_frame_submit_button.pack()
        self.process_coins_frame_back_button = Button(self, text="Back")
        self.process_coins_frame_back_button.pack()

        self.process_coins_frame_error = Label(self, text="")
        self.process_coins_frame_error.pack()

    def setup_process_coins(self, machine, drink):
        self.process_coins_frame_title_label.config(text=f"It cost you ${drink.money} sir\nInsert Coins : ")
        self.process_coins_frame_submit_button.config(command=lambda: self.process_coins(machine, drink))
        self.process_coins_frame_back_button.config(command=self.go_back)

    def process_coins(self, machine, drink):
        quarters = 0
        dimes = 0
        nickles = 0
        pennies = 0
        try:
            quarters = int(self.process_coins_frame_quarter_edit_text.get())
            dimes = int(self.process_coins_frame_dimes_edit_text.get())
            nickles = int(self.process_coins_frame_nickel_edit_text.get())
            pennies = int(self.process_coins_frame_pennies_edit_text.get())
        except ValueError:
            self.process_coins_frame_error.config(text="Entered wrong value. Try again")
            self.setup_process_coins(machine, drink)
            # return False

        total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

        if total < drink.money:
            self.reset()
            machine.show_frame("SuccessFrame")
            machine.frames["SuccessFrame"].label_config("Sorry that's not enough money. Money refunded")
        elif total == drink.money:
            machine.add_money(drink.money)
            machine.make_coffee(drink)
            self.reset()
            machine.show_frame("SuccessFrame")
            machine.frames["SuccessFrame"].label_config(f"Here is your {drink.name}. Enjoy!")
        else:
            machine.add_money(drink.money)
            machine.make_coffee(drink)
            self.reset()
            machine.show_frame("SuccessFrame")
            machine.frames["SuccessFrame"].label_config(
                "Here is {:.2f} dollars in change\nHere is your {}. Enjoy!".format(total - drink.money, drink.name))

    def reset(self):
        self.process_coins_frame_quarter_edit_text.delete(0, END)
        self.process_coins_frame_quarter_edit_text.insert(0, 0)
        self.process_coins_frame_dimes_edit_text.delete(0, END)
        self.process_coins_frame_dimes_edit_text.insert(0, 0)
        self.process_coins_frame_nickel_edit_text.delete(0, END)
        self.process_coins_frame_nickel_edit_text.insert(0, 0)
        self.process_coins_frame_pennies_edit_text.delete(0, END)
        self.process_coins_frame_pennies_edit_text.insert(0, 0)

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


# con = sqlite3.connect("day14.db")
# print("Opened database successfully")
# cursor = con.cursor()
# try:
#     cursor.execute("CREATE TABLE COFFEE_MACHINE"
#                    "("
#                    + "date DATETIME,"
#                    + "water INT,"
#                    + "milk INT,"
#                    + "coffee INT,"
#                    + "money INT"
#                      ");")
# except Exception as e:
#     print("Error :", e)
# else:
#     print("Table created")

# dataframe = [(datetime.datetime.now(), 3000, 2000, 1000, 0)]
#
# try:
#     cursor.executemany("INSERT INTO COFFEE_MACHINE VALUES (?,?,?,?,?)", dataframe)
# except Exception as e:
#     print("Error : ", e)
# else:
#     con.commit()
#     print("Data inserted")

# rows = cursor.execute("SELECT * FROM COFFEE_MACHINE")
# water = 0
# milk = 0
# coffee = 0
# money = 0
# for row in rows:
#     print(row[0], row[1], row[2], row[3])
#     water = row[1]
#     milk = row[2]
#     coffee = row[3]
#     money = row[4]

my_machine = MakeTough()

my_machine.geometry("1000x500")
my_machine.title("Make Tough")

my_machine.mainloop()
