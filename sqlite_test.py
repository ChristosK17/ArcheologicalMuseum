import sqlite3

class MuseumDatabase:
    def __init__(self, db_name, tableSchemaPath):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        with open(tableSchemaPath, "r") as table:
            self.cursor.execute(table.read())
        # (f'''
        #     CREATE TABLE IF NOT EXISTS {table_name} (
        #         {columns}
        #     )
        # ''')
        self.conn.commit()

    def create(self, tableName, **kwargs):
        #self.cursor.execute(
        columns = ', '.join(kwargs.keys())
        values = ', '.join(map(lambda x: f'"{x}"', kwargs.values()))
        print(f"""INSERT INTO {tableName} ({columns}) VALUES ({values})""") # ", ".join(kwargs.values())
        self.conn.commit()

    def readAll(self, tableName):
        #self.cursor.execute(
        print(f"""SELECT * FROM {tableName}""")
        self.conn.commit()

    def readBy(self, tableName, **kwargs):
        #self.cursor.execute(
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in kwargs.items()])
        print(f"""SELECT * FROM {tableName} WHERE {conditions}""")
        self.conn.commit()

    def deleteAll(self, tableName):
        #self.cursor.execute(
        print(f"""DELETE FROM {tableName}""")
        self.conn.commit()

    def deleteBy(self, tableName, **kwargs):
        #self.cursor.execute(
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in kwargs.items()])
        print(f"""DELETE FROM {tableName} WHERE {conditions}""")
        self.conn.commit()


if __name__ == "__main__":
    museum_db = MuseumDatabase('ArcheologicalMuseum.db', "file/path/tableSchema.txt")
    
    museum_db.create("agalma", peos="megalo", orthio="mono gia esena", koiliakoi="vevaios", arxaioellhnikos_popos="kai to rotas?")
    
    print()

    museum_db.readBy("agalma", peos="megalo", orthio="mono gia esena", koiliakoi="vevaios", arxaioellhnikos_popos="kai to rotas?")

    museum_db.conn.close()