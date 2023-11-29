import sqlite3

class MuseumDatabase:
    def __init__(self, db_name, tableSchemaPath):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        with open(tableSchemaPath, "r") as table:
            for command in table.read().split(");")[:-1]:
                self.cursor.execute(command.replace("\n", "")+");")
        self.conn.commit()

    def create(self, tableName, **kwargs):
        columns = ', '.join(kwargs.keys())
        values = ', '.join(map(lambda x: f'"{x}"', kwargs.values()))
        query = f"""INSERT INTO {tableName} ({columns}) VALUES ({values})"""
        self.cursor.execute(query)
        self.conn.commit()

    def readAll(self, tableName):
        query = f"""SELECT * FROM {tableName}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def readBy(self, tableName, **kwargs):
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in kwargs.items()])
        query = f"""SELECT * FROM {tableName} WHERE {conditions}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def updateBy(self, tableName, toUpdate, conditions):
        toUpdate = ' AND '.join([f'{key} = "{value}"' for key, value in toUpdate.items()])
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in conditions.items()])
        query = f"""SELECT * FROM {tableName} SET {toUpdate} WHERE {conditions}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
        
    def deleteAll(self, tableName):
        query = f"""DELETE FROM {tableName}"""
        self.cursor.execute(query)
        self.conn.commit()

    def deleteBy(self, tableName, **kwargs):
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in kwargs.items()])
        query = f"""DELETE FROM {tableName} WHERE {conditions}"""
        self.cursor.execute(query)
        self.conn.commit()


if __name__ == "__main__":
    museum_db = MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
    
    museum_db.create("EMPLOEEY", specialty="Archeologist")
    
    result = museum_db.readAll("EMPLOEEY")
    
    print(result)

    museum_db.conn.close()