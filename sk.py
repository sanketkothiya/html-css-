# for loop 
import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
win.title('LOOP')

labels = ['What is your name : ' , 'What is your age ', 'What is your gender : ', 'Country : ', 'State : ', 'City : ', 'address']



for i in range(len(labels)):
    cur_label = 'label' + str(i) # label0, label1
    cur_label = ttk.Label(win, text = labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

# entry box
name_var = tk.StringVar() 
user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'address' : tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox = 'entry' + i # entryname # entryage
    cur_entrybox = ttk.Entry(win, width=16, textvariable=user_info[i])
    cur_entrybox.grid(column=1, row=counter)
    counter += 1 

def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())

submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=7, columnspan=2)

# name_entry = ttk.Entry(win, width=16, textvariable=name_var)
# name_entry.grid(row=0, column=1)


win.mainloop()





import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk() 

#label frame
label_frame = ttk.LabelFrame(win, text = 'Contact Detail')
label_frame.grid(row=0, column = 0, padx=40, pady=10)

#labels
name_label = ttk.Label(label_frame, text = 'Enter your Name please : ', font=('Helvetica', 14))
age_label = ttk.Label(label_frame, text = 'Enter your age please : ', font=('Helvetica', 14,))

# entry box variables 
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry boxes 
name_entry = ttk.Entry(label_frame, width=36, textvariable = name_var)
age_entry = ttk.Entry(label_frame, width=36, textvariable = age_var)

#grid
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
age_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

def submit():
    # m_box.showwarning('title', 'content of this message box !! ')
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        m_box.showerror('Error', 'Please fill both name and age ')
    else:
        try:
            # age = 'fjasdofj' # value error
            # age = '20'
            age = int(age)
        except ValueError:
            m_box.showerror('title','Only digits are allowed in age field')
        else:
            if age < 18:
                m_box.showwarning('warning', 'you are not 18 , visit this content on your own risk')
            print(f'{name} : {age}')


    

submit_btn = ttk.Button(win, text = 'Submit', command=submit)
submit_btn.grid(row=1, columnspan=2, padx=40)
win.mainloop()



