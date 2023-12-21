
import sqlite3
import PySimpleGUI as sg
import db_handler as handler
from timer import timeIt

class MainLayout:
    def __init__(self):
        self.names = ['Person','Request', 'Event', 'Exhibit']
        sg.theme('Purple')
        lst = sg.Combo(self.names, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-COMBO-')
        self.layout = [[lst, sg.Button('Read'), sg.Button('Update'), sg.Button('Delete'),sg.Button('Exit')],
                [sg.Text("", key='-MSG-', font=('Arial Bold', 14),justification='center')] ]
        self.window = sg.Window('DB Menu', self.layout, size=(500, 150))
    
    def run(self):
        while True:
            event, values = self.window.read()
            print(event, values)
            if event in (sg.WIN_CLOSED, 'Exit'): break
            if event == 'Create': 
                self.names.append(values['-COMBO-'])
                print(self.names)
                self.window['-COMBO-'].update(values=self.names, value=values['-COMBO-'])
            if event == '-COMBO-':
                selected_item = values['-COMBO-']
                if selected_item == 'Person': 
                    form1 = Create("Person", "PERSON", ["id", "firstname", "lastname" ,"phone", "email"])
                    form1.run()
                if selected_item == 'Request': 
                    form2 = Create("Request", "REQUEST", ["ID", "Description", "Submition Date" ,"Start Date", "End Date","Person Id", "Row"])
                    form2.run()
                if selected_item == 'Event': 
                    form3 = Create("Event", "EVENT", ["ID", "Category", "Description" ,"Start Date", "End Date","Event Room"])
                    form3.run()
                if selected_item == 'Exhibit': 
                    form4 = Create("Exhibit", "EXHIBIT", ["ID", "Name", "Material" ,"Rythm", "Description","Value","Excavation Place", "Excavation Date", "Category ID", "Position ID"])
                    form4.run()    
            if event == 'Delete': 
                # call = Delete("Exhibit","id","12")
                # call.run()
                delete_form = Delete(values['-COMBO-'], 'Person', ["ID","First Name"])
                delete_form.run()
        self.window.close()

class Create:
    def __init__(self, name:str, entity_name:str, attributes:list):
        self.museum_db = handler.MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
        
        sg.theme('BlueMono')
        self.layout = []
        self.layout.append([sg.Text(f'Enter the following information in order to insert an {name} in your database', font=("Courier", 18))])
        self.layout.append([sg.VPush()])
        
        self.entity_name = entity_name
        self.attributes = attributes
        self.entity_name = entity_name        
        
        for attribute in self.attributes:
                self.layout.append([sg.Text(attribute, size=(1+len(attribute), 1), font=("Arial", 16)), sg.InputText(font=("Courier", 16), pad=(0, 10))])
                self.layout.append([sg.VPush()])
        
        self.layout.append([sg.Button('Insert', font=("Courier", 16)), sg.Button('Exit', font=("Courier", 16))])
        self.window = sg.Window("Data Entry Form", self.layout, size=(900, 600))

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if event == 'Insert':
                self.museum_db.create(tableName=self.entity_name, attributes = {k: v for k, v in zip(self.attributes,[i[1] for i in values.items()])})
                self.museum_db.conn.close()

        self.window.close()
        
    def clear_input_fields(self,values):
        for key in values: self.window[key].update(' ')
        
class Delete:
    def __init__(self, name:str, column:str, attributes:list):
        self.conn = sqlite3.connect("ArcheologicalMuseum.db")
        self.table_name = name
        self.table_col = column
        self.attributes = attributes
        
        sg.theme('DarkBlue')
        self.layout = []
        self.layout.append([sg.Text(f'Enter the following information in order to delete a value frow your base', font=("Courier", 18))])
        self.layout.append([sg.VPush()])
        
        for attribute in attributes:
                self.layout.append([sg.Text(attribute, size=(1+len(attribute), 1), font=("Arial", 16)), sg.InputText(font=("Courier", 16), pad=(0, 10))])
                self.layout.append([sg.VPush()])
        self.layout.append([sg.Button('Delete', font=("Courier", 16)), sg.Button('Exit', font=("Courier", 16))])

        self.window = sg.Window("Data Deletion Form", self.layout, size=(900, 600))
        
    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if event == 'Delete':
                query = f"DELETE FROM {self.table_name} WHERE {self.condition_column} = ?"
                params = [values[f'{attribute}'] for attribute in self.attributes]
                self.conn.execute(query, params)
                self.conn.commit()
                
                sg.popup('Requested Data Deleted Successfully!')
                self.clear_input_fields(values)
                
        self.conn.close()
        self.window.close()
        
    def clear_input_fields(self,values):
        for key in values: self.window[key].update(' ')
        
# class Read:
    
# class Update:
        

if __name__ == "__main__":
    # form1 = Create("Research Request", ["ID", "type", "description"])
    # form1.run()
    
    # form2 = Create("Event", ["ID", "category", "description" ,"startDate", "endDate","eventRoom"])
    # form2.run()
    a =MainLayout()
    a.run()
