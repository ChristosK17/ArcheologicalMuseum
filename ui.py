#Import necessary modules
import sqlite3
import tkinter as tk
from tkinter import ttk
import db_handler as handler
from timer import timeIt
import customtkinter
from customtkinter import *

#Main Interface
class MainLayout:
    def __init__(self, root):
        self.names = ['Person', 'Request','Event','Employee','Visits','Event ticket', 'Visit ticket','Event Room', 'Exchange Request',
                      'Research Request', 'Event Request','Room Request','Exhibit','Position', 'Category', 'Dimensions',
                      'Plans', 'Refers to research', 'Refers to exchange', 'Approve', 'Request refers to room']
        self.root = root
        #dimensions of the main window
        self.root.geometry("550x300")
        self.root.title('Archaeological DB Menu')
        self.root.resizable(width=True, height=False)
        self.combo_box= ""

        #Create UI elements
        self.create_combo_box()
        self.create_buttons()
        self.create_text_box()

    #Create a combo box element so that the user can choose the desired table on which he will execute CRUD operations
    def create_combo_box(self):
        self.selected_item = tk.StringVar(value='Choose one of the following tables')
        self.combo_box = ttk.Combobox(
            self.root,
            values=self.names,
            font=('Arial Bold', 14),
            state='readonly',
            textvariable=self.selected_item)
        self.combo_box.pack(expand=False, fill='both')
        
    #Create a text box with instructions
    def create_text_box(self):
        self.text_box = tk.Label(self.root, text="Select an Entity from the dropdown list in \n the combobox and press the desired button\n to execute one of the CRUD opperations",
                                 font=("Arial", 16))   
        self.text_box.place(x=120, y=140)
        
    #Create buttons for CRUD operations
    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill='both', pady=5)

        button1=customtkinter.CTkButton(master=self.root, text='Create',corner_radius=8, command=self.insert_button_click,width=120, height=10)
        button2=customtkinter.CTkButton(master=self.root, text='Read', corner_radius=8,command=self.read_button_click,width=120, height=10)
        button3=customtkinter.CTkButton(master=self.root, text='Update', corner_radius=8,command=self.update_button_click,width=120, height=10)
        button4=customtkinter.CTkButton(master=self.root, text='Delete', corner_radius=8,command=self.delete_button_click,width=120, height=10)
        button5=customtkinter.CTkButton(master=self.root, text='Exit',corner_radius=8, command=self.root.destroy,width=120, height=12)
        
        button6= customtkinter.CTkButton(master=self.root, text='Exhibit by Category',corner_radius=8, command=self.exhibitbycategory_button_click,width=120, height=10)
        button7=customtkinter.CTkButton(master=self.root, text='Exhibit Position',corner_radius=8, command=self.exhibit_position_button_click,width=120, height=10)
        button8=customtkinter.CTkButton(master=self.root, text='Event Categories',corner_radius=8, command=self.event_categories_button_click,width=120, height=10)
        button9=customtkinter.CTkButton(master=self.root, text='Exhibit Categories',corner_radius=8, command=self.exhibit_categories_button_click,width=120, height=10)
        
        #CRUD buttons
        button1.place(relx=0.02, rely=0.2, anchor=tk.W)
        button2.place(relx=0.28, rely=0.2, anchor=tk.W)
        button3.place(relx=0.52, rely=0.2, anchor=tk.W)
        button4.place(relx=0.76, rely=0.2, anchor=tk.W)
        
        #Custom queries buttons
        button6.place(relx=0.02, rely=0.3, anchor=tk.W)
        button7.place(relx=0.28, rely=0.3, anchor=tk.W)
        button8.place(relx=0.52, rely=0.3, anchor=tk.W)
        button9.place(relx=0.76, rely=0.3, anchor=tk.W)
        
        #Exit button
        button5.place(relx=0.75, rely=0.96, anchor=tk.SW) 
    
    #Handle button clicks for inserting data
    def insert_button_click(self):
        selected_item = self.combo_box.get()
        self.root.destroy()
        if (selected_item == "Person"):
            insert_form = Create("Person", "PERSON", ["id","firstName","lastName","phone","email"])
            insert_form.run()
        if (selected_item == "Request"):
            insert_form = Create("Request", "REQUEST", ["id","description","submitionDate","startDate","endDate","personId"])
            insert_form.run()
        if (selected_item == "Event"):
            insert_form = Create("Event", "EVENT", ["id", "category", "description" ,"startDate", "endDate","eventRoomId"])
            insert_form.run()
        if (selected_item == "Exhibit"):
            insert_form = Create("Exhibit", "EXHIBIT", ["id","material","description","value","excavationPlace","excavationDate","categoryId","positionId"])
            insert_form.run()
        if (selected_item == "Employee"):
            insert_form = Create("Employee","EMPLOYEE", ["id", "specialty"])
            insert_form.run()
        if (selected_item == "Visits"):
            insert_form = Create("Visits","VISITS", ["id", "date", "category"])
            insert_form.run()
        if (selected_item == "Event ticket"):
            insert_form = Create("Event ticket","EVENT_TICKET", ["id", "category", "eventId"])
            insert_form.run()
        if (selected_item == "Visit ticket"):
            insert_form = Create("Visit ticket","VISIT_TICKET", ["id", "category", "visitId"])
            insert_form.run()
        if (selected_item == "Event Room"):
            insert_form = Create("Event Room","EVENT_ROOM", ["id", "name", "description", "capacity"])
            insert_form.run()
        if (selected_item == "Exchange Request"):
            insert_form = Create("Exchange Request","EXGANGE_REQUEST", ["id", "country", "city", "postCode", "address", "addressNumber", "phone"])
            insert_form.run()
        if (selected_item == "Research Request"):
            insert_form = Create("Research Request","RESEARCH_REQUEST", ["id", "type", "description"])
            insert_form.run()
        if (selected_item == "Event Request"):
            insert_form = Create("EVENT_REQUEST", ["id", "type", "eventId"])
            insert_form.run()
        if (selected_item == "Room Request"):
            insert_form = Create("Room Request","ROOM_REQUEST", ["id", "pieceCapacity", "description"])
            insert_form.run()
        if (selected_item == "Position"):
            insert_form = Create("Position","POSITION", ["id", "column", "row"])
            insert_form.run()
        if (selected_item == "Category"):
            insert_form = Create("CATEGORY", ["id", "start_date", "end_date", "name"])
            insert_form.run()
        if (selected_item == "Dimensions"):
            insert_form = Create("Dimensions","DIMENSIONS", ["id", "height", "width", "length", "exhibitId"])
            insert_form.run()
        if (selected_item == "Plans"):
            insert_form = Create("Plans","PLANS", ["emploeeyId", "eventId"])
            insert_form.run()
        if (selected_item == 'Refers to research'):
            insert_form = Create('Refers to research',"REFERS_TO_RESEARCH", ["researchId", "exhibitId"])
            insert_form.run()
        if (selected_item == "Refers to exchange"):
            insert_form = Create("Refers to exchange","REFERS_TO_EXCHANGE", ["exchangeId", "exhibitId"])
            insert_form.run()
        if (selected_item == "Approve"):
            insert_form = Create("Approve","APPROVE", ["id", "approveDate", "requestId", "employeeId"])
            insert_form.run()
        if (selected_item == "Request refers to room"):
            insert_form = Create("Request refers to room", "REQUEST_REFERS_ROOM",["roomId", "requestId", "startDate", "endDate"])
            insert_form.run()
    
    #Handle button clicks for reading data
    def read_button_click(self):
        selected_item = self.combo_box.get()
        self.root.destroy()
        print(selected_item)
        read_form = Read(selected_item)
        read_form.run()

    #Handle button clicks for updating data
    def update_button_click(self):
        selected_item = self.combo_box.get()
        self.root.destroy()
        if (selected_item == "Person"):
            update_form = Update("PERSON", ["id", "firstName", "lastName", "phone", "email"])
            update_form.run()
        if (selected_item == "Request"):
            update_form = Update("REQUEST", ["id", "description", "submitionDate", "startDate", "endDate", "personId"])
            update_form.run()
        if (selected_item == "Event"):
            update_form = Update("EVENT", ["id", "category", "description", "startDate", "endDate", "eventRoomId"])
            update_form.run()
        if (selected_item == "Exhibit"):
            update_form = Update("EXHIBIT", ["id", "material", "description", "value", "excavationPlace", "excavationDate", "categoryId", "positionId"])
            update_form.run()
        if (selected_item == "Employee"):
            update_form = Update("EMPLOYEE", ["id", "specialty"])
            update_form.run()
        if (selected_item == "Visits"):
            update_form = Update("VISITS", ["id", "date", "category"])
            update_form.run()
        if (selected_item == "Event ticket"):
            update_form = Update("EVENT_TICKET", ["id", "category", "eventId"])
            update_form.run()
        if (selected_item == "Visit ticket"):
            update_form = Update("VISIT_TICKET", ["id", "category", "visitId"])
            update_form.run()
        if (selected_item == "Event Room"):
            update_form = Update("EVENT_ROOM", ["id", "name", "description", "capacity"])
            update_form.run()
        if (selected_item == "Exchange Request"):
            update_form = Update("EXGANGE_REQUEST", ["id", "country", "city", "postCode", "address", "addressNumber", "phone"])
            update_form.run()
        if (selected_item == "Research Request"):
            update_form = Update("RESEARCH_REQUEST", ["id", "type", "description"])
            update_form.run()
        if (selected_item == "Event Request"):
            update_form = Update("EVENT_REQUEST", ["id", "type", "eventId"])
            update_form.run()
        if (selected_item == "Room Request"):
            update_form = Update("ROOM_REQUEST", ["id", "pieceCapacity", "description"])
            update_form.run()
        if (selected_item == "Position"):
            update_form = Update("POSITION", ["id", "column", "row"])
            update_form.run()
        if (selected_item == "Category"):
            update_form = Update("CATEGORY", ["id", "start_date", "end_date", "name"])
            update_form.run()
        if (selected_item == "Dimensions"):
            update_form = Update("DIMENSIONS", ["id", "height", "width", "length", "exhibitId"])
            update_form.run()
        if (selected_item == "Plans"):
            update_form = Update("PLANS", ["emploeeyId", "eventId"])
            update_form.run()
        if (selected_item == 'Refers to research'):
            update_form = Update('REFERS_TO_RESEARCH', ["researchId", "exhibitId"])
            update_form.run()
        if (selected_item == "Refers to exchange"):
            update_form = Update("REFERS_TO_EXCHANGE", ["exchangeId", "exhibitId"])
            update_form.run()
        if (selected_item == "Approve"):
            update_form = Update("APPROVE", ["id", "approveDate", "requestId", "employeeId"])
            update_form.run()
        if (selected_item == "REQUEST_REFERS_ROOM"):
            update_form = Update("REQUEST_REFERS_ROOM", ["roomId", "requestId", "startDate", "endDate"])
            update_form.run()

    #Handle button clicks for deleting data
    def delete_button_click(self):
        selected_item = self.combo_box.get()
        self.root.destroy()
        delete_form = Delete(selected_item, ["id"])
        delete_form.run()
        
    #Handle button clicks for custom queries
    def exhibit_position_button_click(self):
        selected_item = self.combo_box.get()
        self.root.destroy()
        position_form = ExhibitPosition(selected_item)
        position_form.run()
        
    def event_categories_button_click(self):
        self.root.destroy()
        answer_form = EventCategories()
        answer_form.run()
        
    def exhibit_categories_button_click(self):
        self.root.destroy()
        answer_form = ExhibitCategories()
        answer_form.run()
        
    def exhibitbycategory_button_click(self):
        self.root.destroy()
        answer_form = ExhibitByCategoryName()
        answer_form.run()

    #Start the main loop
    def run(self):
        self.root.mainloop()

#Class for handling data insertion  
class Create:
    def __init__(self, name:str, entity_name:str, attributes:list):
        self.entryBoxList = []
        
        self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
        self.entity_name = entity_name
        self.attributes = attributes
        self.tablename=name
        
        self.root = tk.Tk()
        self.root.title(f"Read {self.tablename} Data")
        self.root.geometry("700x550")
        
        self.create_widgets()
    
    #Create widgets for data insertion  
    def create_widgets(self):
        insert_label = tk.Label(self.root, text=f'Insert information in the {self.tablename} table', font=("Arial", 18))
        insert_label.pack()
        
        for attribute in self.attributes:
            label = tk.Label(self.root, text=attribute, font=("Arial", 16))
            label.pack()
            entry = tk.Entry(self.root, font=("Courier", 16))
            self.entryBoxList.append(entry)
            entry.pack()
            
        insert_button = customtkinter.CTkButton(master=self.root, text='Insert',corner_radius=12, font=("Courier", 16), command=self.insert_button_click)
        insert_button.place(relx=0.1, rely=0.9, anchor=tk.W)

        clear_button = customtkinter.CTkButton(master=self.root, text='Clear',corner_radius=12,font=("Courier", 16), command=self.clear_input_fields)
        clear_button.place(relx=0.4, rely=0.9, anchor=tk.W)

        exit_button = customtkinter.CTkButton(master=self.root, text='Exit',corner_radius=12, font=("Courier", 16), command=self.destroy)
        exit_button.place(relx=0.7, rely=0.9, anchor=tk.W)
    
    #Destroy this interface and recreate the main one
    def destroy(self):
        self.root.destroy()
        a = CTk()
        b = MainLayout(a)
        b.run()
    
    #Handle button click for data insertion    
    def insert_button_click(self):
        values = {child.winfo_name(): child.get() for child in self.root.winfo_children() if isinstance(child, tk.Entry)}
        print(values)
        self.museum_db.create(tableName=self.entity_name, attributes = {k: v for k, v in zip(self.attributes,[i[1] for i in values.items()])})
        self.museum_db.conn.close()
        
    #Clear input fields
    def clear_input_fields(self):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Entry):
                child.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
        self.museum_db.conn.close()

#Class for reading data
class Read:
    def __init__(self, table_name):
        self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
        self.tablename = table_name

        self.root = tk.Tk()
        self.root.title(f"Read {self.tablename} Data")
        self.root.geometry("900x500")

        #Creates a Treeview widget in order to present data as a table
        self.tree = ttk.Treeview(self.root) #
        self.tree['columns'] = ('',)  # Assuming the first column is ID
        self.tree.heading('#0', text='ID')

        #Fetch column names from the database
        cursor = self.museum_db.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.tablename} LIMIT 1")
        columns = [description[0] for description in cursor.description]

        for column in columns:
            self.tree['columns'] += (column,)
            self.tree.heading(column, text=column)
            self.tree.column(column, anchor='center', width=100) 
        self.tree.pack()

        #Create widgets
        read_button = customtkinter.CTkButton(master=self.root, text='Read', font=("Courier", 16), command=self.read_button_click)
        read_button.place(relx=0.1, rely=0.9, anchor=tk.W)
        
        clear_button = customtkinter.CTkButton(master=self.root, text='Clear', font=("Courier", 16), command=self.clear_input_fields)
        clear_button.place(relx=0.4, rely=0.9, anchor=tk.W)

        exit_button = customtkinter.CTkButton(master=self.root, text='Exit', font=("Courier", 16), command=self.destroy)
        exit_button.place(relx=0.7, rely=0.9, anchor=tk.W)

    #Destroy this interface and recreate the main one
    def destroy(self):
        self.root.destroy()
        a = CTk()
        b = MainLayout(a)
        b.run()
        
    def read_button_click(self):
        # Clear existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch data from the database
        data = self.museum_db.readAll(tableName=self.tablename)

        # Display data in the Treeview
        for record in data:
            self.tree.insert("", 'end', values=tuple(record))
    
    #Clear input fields
    def clear_input_fields(self):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Entry):
                child.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
        self.museum_db.conn.close()

#Class for updating data       
class Update:
    def __init__(self, tablename, toUpdate:list):
        self.entryBoxList = []
        
        self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
        self.tablename = tablename
        self.toUpdate = toUpdate
        
        self.root = tk.Tk()
        self.root.title(f"Update {self.tablename} Data")
        self.root.geometry("900x600")
        
        self.create_widgets()
    
    #Create widgets for updating data  
    def create_widgets(self):
        update_label = tk.Label(self.root, text=f'Update information in the {self.tablename} table', font=("Courier", 18))
        update_label.pack()
        
        for toupdate in self.toUpdate:
            label = tk.Label(self.root, text=toupdate, font=("Arial", 16))
            label.pack()
            entry = tk.Entry(self.root, font=("Courier", 16))
            self.entryBoxList.append(entry)
            entry.pack()

        update_button = customtkinter.CTkButton(master=self.root, text='Update', font=("Courier", 16), command=self.update_button_click)
        update_button.place(relx=0.1, rely=0.9, anchor=tk.W)
        
        clear_button = customtkinter.CTkButton(master=self.root, text='Clear', font=("Courier", 16), command=self.clear_input_fields)
        clear_button.place(relx=0.4, rely=0.9, anchor=tk.W)
        
        exit_button =customtkinter.CTkButton(master=self.root, text='Exit', font=("Courier", 16), command=self.destroy)
        exit_button.place(relx=0.7, rely=0.9, anchor=tk.W)
        
    #Destroy this interface and recreate the main one   
    def destroy(self):
        self.root.destroy()
        a = CTk()
        b = MainLayout(a)
        b.run()

    #Handle button click for updating data
    def update_button_click(self):
        values = {child.winfo_name(): child.get() for child in self.root.winfo_children() if isinstance(child, tk.Entry)}

        self.museum_db.updateBy(tableName=self.tablename.upper(), toUpdate = {k: v.get() for k, v in zip(self.toUpdate[1:], self.entryBoxList[1:])}, 
                                        conditions={"id":int(self.entryBoxList[0].get())})
        
        print(self.museum_db.readBy(self.tablename, {"id":int(self.entryBoxList[0].get())}))
        self.museum_db.conn.close()

    #Clear input fields
    def clear_input_fields(self):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Entry):
                child.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
        self.museum_db.conn.close()

# Class for deleting data by id
class Delete:
    def __init__(self, name:str, attributes):
        
        self.entryBoxList = []
        
        self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
        self.tablename = name
        self.attributes = attributes
        
        self.root = tk.Tk()
        self.root.title(f"Delete {self.tablename} Data")
        self.root.geometry("500x300")
        
        self.create_widgets()
    
    #Create widgets for deleting data  
    def create_widgets(self):
        delete_label = tk.Label(self.root, text=f'Delete information from the {self.tablename} table', font=("Courier", 18))
        delete_label.pack()
        
        label = tk.Label(self.root, text=self.attributes, font=("Arial", 16))
        label.pack()
        entry = tk.Entry(self.root, font=("Courier", 16))
        self.entryBoxList.append(entry)
        entry.pack()

        delete_button = customtkinter.CTkButton(master=self.root, text='Delete', font=("Courier", 16), command=self.delete_button_click)
        delete_button.place(relx=0.08, rely=0.7, anchor=tk.W)

        clear_button = customtkinter.CTkButton(master=self.root, text='Clear', font=("Courier", 16), command=self.clear_input_fields)
        clear_button.place(relx=0.38, rely=0.7, anchor=tk.W)

        exit_button = customtkinter.CTkButton(master=self.root, text='Exit', font=("Courier", 16), command=self.destroy)
        exit_button.place(relx=0.68, rely=0.7, anchor=tk.W)     
    
    #Destroy this interface and recreate the main one    
    def destroy(self):
        self.root.destroy()
        a = CTk()
        b = MainLayout(a)
        b.run()
    
    #Handle button click for deleting data
    def delete_button_click(self):
        values = {child.winfo_name(): child.get() for child in self.root.winfo_children() if isinstance(child, tk.Entry)}

        self.museum_db.deleteBy(tableName=self.tablename.upper(), attributes={"id":int(self.entryBoxList[0].get())})
        
        self.museum_db.conn.close()  
    
    #Clear input fields   
    def clear_input_fields(self):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Entry):
                child.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
        self.museum_db.conn.close()

# Class to find exhibits that belong to a certain category    
class ExhibitByCategoryName:
    def __init__(self):
        
        self.entryBoxList = []
        
        self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
    
    
        self.result = ""
        
        self.root = tk.Tk()
        self.root.title(f"Exhibit")
        self.root.geometry("600x300")
        
        self.result_label = ""
        
        self.create_widgets()
    
    #Create widgets for deleting data  
    def create_widgets(self):
        
        delete_label = tk.Label(self.root, text=f'Find the exhibit by the category that it belongs', font=("Courier", 18))
        delete_label.pack()
        
        label = tk.Label(self.root, text="Category", font=("Arial", 16))
        label.pack()
        entry = tk.Entry(self.root, font=("Courier", 16))
        self.entryBoxList.append(entry)
        entry.pack()
        self.result_label = tk.Label(self.root, text=f"Result: {self.result}", font=("Arial", 16), name="result_label")
        self.result_label.pack()

        find_button = customtkinter.CTkButton(master=self.root, text='Find', font=("Courier", 16), command=self.find_button_click)
        find_button.place(relx=0.08, rely=0.7, anchor=tk.W)

        clear_button = customtkinter.CTkButton(master=self.root, text='Clear', font=("Courier", 16), command=self.clear_input_fields)
        clear_button.place(relx=0.38, rely=0.7, anchor=tk.W)

        exit_button = customtkinter.CTkButton(master=self.root, text='Exit', font=("Courier", 16), command=self.destroy)
        exit_button.place(relx=0.68, rely=0.7, anchor=tk.W)     
    
    #Destroy this interface and recreate the main one    
    def destroy(self):
        self.root.destroy()
        a = CTk()
        b = MainLayout(a)
        b.run()
    
    #Handle button click for deleting data
    def find_button_click(self):
        values = {child.winfo_name(): child.get() for child in self.root.winfo_children() if isinstance(child, tk.Entry)}
        
        self.result= self.museum_db.getExhibitByCategoryName(categoryName=(self.entryBoxList[0].get()))
        print(self.result)
        self.museum_db.conn.close()
        self.result_label.config(text=f"Result: {self.result}")
        return self.result
        
    
    #Clear input fields   
    def clear_input_fields(self):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Entry):
                child.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
        self.museum_db.conn.close()

# Class to find the position of an exhibit
class ExhibitPosition:
    def __init__(self, attributes):
        
        self.entryBoxList = []
        
        self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
    
        self.attributes = attributes
        self.result = ""
        
        self.root = tk.Tk()
        self.root.title(f"Exhibit Position")
        self.root.geometry("500x300")
        
        self.result_label = ""
        
        self.create_widgets()
    
    #Create widgets for deleting data  
    def create_widgets(self):
        delete_label = tk.Label(self.root, text=f'Find the position of an exhibit', font=("Courier", 18))
        delete_label.pack()
        
        label = tk.Label(self.root, text="Id", font=("Arial", 16))
        label.pack()
        entry = tk.Entry(self.root, font=("Courier", 16))
        self.entryBoxList.append(entry)
        entry.pack()
        self.result_label = tk.Label(self.root, text=f"Result: {self.result}", font=("Arial", 16), name="result_label")
        self.result_label.pack()

        find_button = customtkinter.CTkButton(master=self.root, text='Find', font=("Courier", 16), command=self.find_button_click)
        find_button.place(relx=0.08, rely=0.7, anchor=tk.W)

        clear_button = customtkinter.CTkButton(master=self.root, text='Clear', font=("Courier", 16), command=self.clear_input_fields)
        clear_button.place(relx=0.38, rely=0.7, anchor=tk.W)

        exit_button = customtkinter.CTkButton(master=self.root, text='Exit', font=("Courier", 16), command=self.destroy)
        exit_button.place(relx=0.68, rely=0.7, anchor=tk.W)     
    
    #Destroy this interface and recreate the main one    
    def destroy(self):
        self.root.destroy()
        a = CTk()
        b = MainLayout(a)
        b.run()
    
    #Handle button click for deleting data
    def find_button_click(self):
        values = {child.winfo_name(): child.get() for child in self.root.winfo_children() if isinstance(child, tk.Entry)}
        
        self.result= self.museum_db.getExhibitPosition(exhibitId=(self.entryBoxList[0].get()))
        print(self.result)
        self.museum_db.conn.close()
        self.result_label.config(text=f"Result: {self.result}")
        return self.result
        
    
    #Clear input fields   
    def clear_input_fields(self):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Entry):
                child.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
        self.museum_db.conn.close()

# Class to find the event categories 
class EventCategories:
        def __init__(self):
            self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
           
            self.root = tk.Tk()
            self.root.title(f"Event Categories")
            self.root.geometry("400x200")


            # Fetch data
            data = ", ".join([item[0] for item in self.museum_db.getEventCategories()])

            # Display data
            label = tk.Label(self.root, text=f"Result: {data}", font=("Arial", 16))
            label.pack()


            clear_button = customtkinter.CTkButton(master=self.root, text='Clear', font=("Courier", 16), command=self.clear_input_fields)
            clear_button.place(relx=0.1, rely=0.7, anchor=tk.W)

            exit_button = customtkinter.CTkButton(master=self.root, text='Exit', font=("Courier", 16), command=self.destroy)
            exit_button.place(relx=0.6, rely=0.7, anchor=tk.W)

    #Destroy this interface and recreate the main one
        def destroy(self):
            self.root.destroy()
            a = CTk()
            b = MainLayout(a)
            b.run()
                
        #Clear input fields
        def clear_input_fields(self):
            for child in self.root.winfo_children():
                if isinstance(child, tk.Entry):
                    child.delete(0, tk.END)

        def run(self):
            self.root.mainloop()
            self.museum_db.conn.close()
 
 # Class for deleting data by id           

# Class to find the categories of the exhibits
class ExhibitCategories:
        def __init__(self):
            self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
           
            self.root = tk.Tk()
            self.root.title(f"Event Categories")
            self.root.geometry("400x200")


            # Fetch data
            data = ", ".join([item[0] for item in self.museum_db.getExhibitCategories()])

            # Display data
            label = tk.Label(self.root, text=f"Result: {data}", font=("Arial", 16))
            label.pack()


            clear_button = customtkinter.CTkButton(master=self.root, text='Clear', font=("Courier", 16), command=self.clear_input_fields)
            clear_button.place(relx=0.1, rely=0.7, anchor=tk.W)

            exit_button = customtkinter.CTkButton(master=self.root, text='Exit', font=("Courier", 16), command=self.destroy)
            exit_button.place(relx=0.6, rely=0.7, anchor=tk.W)

    #Destroy this interface and recreate the main one
        def destroy(self):
            self.root.destroy()
            a = CTk()
            b = MainLayout(a)
            b.run()
                
        #Clear input fields
        def clear_input_fields(self):
            for child in self.root.winfo_children():
                if isinstance(child, tk.Entry):
                    child.delete(0, tk.END)

        def run(self):
            self.root.mainloop()
            self.museum_db.conn.close()
        
#Start the program
if __name__ == "__main__":
    
    root = CTk()
    a =MainLayout(root)
    a.run()
