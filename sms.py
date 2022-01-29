from tkinter import *
from tkinter import ttk
import pymysql  # mysql for large number of data


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="skyblue", fg="darkblue")
        title.pack(side=TOP, fill=X)

        ####################### variable ##############################
        self.name_var = StringVar()
        self.roll_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.dob_var = StringVar()
        self.contact_var = StringVar()

        ####################### Manage Frame ###############################

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=590)

        m_title = Label(Manage_Frame, text="Manage Students", font=("times new roman", 25, "bold"), bg="crimson",
                        fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        name = Label(Manage_Frame, text="Name", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        name.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        ##########################

        roll = Label(Manage_Frame, text="Roll no.", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        roll.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        txt_roll = Entry(Manage_Frame, textvariable=self.roll_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        ##########################

        email = Label(Manage_Frame, text="Email", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        email.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        ##########################

        gender = Label(Manage_Frame, text="Gender", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        s_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 15, "bold"),
                                state='readonly')
        s_gender["values"] = ("Male", "Female", "others")
        s_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        ##########################

        contact = Label(Manage_Frame, text="Contact", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        contact.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        ##########################

        dob = Label(Manage_Frame, text="D.O.B", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        dob.grid(row=6, column=0, pady=10, padx=20, sticky='w')

        txt_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        ##########################

        address = Label(Manage_Frame, text="Address", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        address.grid(row=7, column=0, pady=10, padx=20, sticky='w')

        self.text_address = Text(Manage_Frame, width=30, height=4, font=("", 10))
        self.text_address.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        ####################### Btn Frame ###############################

        Btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        Btn_Frame.place(x=10, y=510, width=430)

        Add = Button(Btn_Frame, text="Add", width=10, command=self.add_student, bg="white", fg="darkblue").grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
        update = Button(Btn_Frame, text="Update", width=10, bg="white", fg="darkblue").grid(row=0, column=1, padx=10,
                                                                                         pady=10)
        delete = Button(Btn_Frame, text="Delete", width=10, bg="white", fg="darkblue").grid(row=0, column=2, padx=10,
                                                                                         pady=10)
        clear = Button(Btn_Frame, text="Clear", width=10, bg="white", fg="darkblue").grid(row=0, column=3, padx=10,
                                                                                        pady=10)

        ####################### data Frame ##############################

        Data_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Data_Frame.place(x=500, y=100, width=780, height=590)

        search = Label(Data_Frame, text="Search By", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        s_search = ttk.Combobox(Data_Frame, width=10, font=("times new roman", 15, "bold"), state='readonly')
        s_search["values"] = ("Roll no.", "Name", "Contact")
        s_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')

        txt_search = Entry(Data_Frame, width=15, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        searchbtn = Button(Data_Frame, text="Search", width=10, pady='5', bg="white", fg="darkblue").grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=10,
                                                                                                          pady=10)
        Showall = Button(Data_Frame, text="Show All", width=10, pady='5', bg="white", fg="darkblue").grid(row=0,
                                                                                                          column=4,
                                                                                                          padx=10,
                                                                                                          pady=10)

        ####################### Table Frame ##############################

        Table_Frame = Frame(Data_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=750, height=500)
        Scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        Scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        Student_table = ttk.Treeview(Table_Frame,
                                     columns=('Name', 'Roll no.', 'Email', 'Gender', 'Contact', 'D.O.B', 'Address'))

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=Student_table.xview)
        Scroll_y.config(command=Student_table.yview)
        Student_table.heading('Name', text='Name')
        Student_table.heading('Roll no.', text='Roll no.')
        Student_table.heading('Email', text='Email')
        Student_table.heading('Gender', text='Gender')
        Student_table.heading('Contact', text='Contact')
        Student_table.heading('D.O.B', text='D.O.B')
        Student_table.heading('Address', text='Address')
        Student_table.column('Name', width=10)
        Student_table.column('Roll no.', width=100)
        Student_table.column('Email', width=100)
        Student_table.column('Gender', width=100)
        Student_table.column('Contact', width=100)
        Student_table.column('D.O.B', width=100)
        Student_table.column('Address', width=150)

        Student_table['show'] = 'headings'
        Student_table.pack(fill=BOTH, expand=1)

        ####################### variable ##############################
        self.var_choice = StringVar()

    ##################

    def add_student(self):
        con = pymysql.connect(host="localhost", user="root", password="candycrush001", database="stp")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.name_var.get(),
                                                                         self.roll_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.text_address.get('1.0', END)
                                                                         ))
        con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()
