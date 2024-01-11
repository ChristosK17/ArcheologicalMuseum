import sqlite3
from timer import timeIt

class MuseumDatabase:
    def __init__(self, db_name, tableSchemaPath):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        with open(tableSchemaPath, "r") as table:
            for command in table.read().split(");")[:-1]:
                self.cursor.execute(command.replace("\n", "")+");")
        self.conn.commit()

    @timeIt
    def create(self, tableName, attributes):
        columns = ', '.join(attributes.keys())
        values = ', '.join(map(lambda x: f'"{x}"', attributes.values()))
        query = f"""INSERT INTO {tableName} ({columns}) VALUES ({values})"""
        self.cursor.execute(query)
        self.conn.commit()

    @timeIt
    def readAll(self, tableName):
        query = f"""SELECT * FROM {tableName}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    @timeIt
    def readBy(self, tableName, attributes):
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in attributes.items()])
        query = f"""SELECT * FROM {tableName} WHERE {conditions}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    @timeIt
    def updateBy(self, tableName, toUpdate, conditions):
        toUpdate = ' , '.join([f'{key} = "{value}"' for key, value in toUpdate.items()])
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in conditions.items()])
        query = f"""UPDATE {tableName} SET {toUpdate} WHERE {conditions}"""
        print("UPDATE QUERY: "+query)
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    @timeIt
    def deleteAll(self, tableName):
        query = f"""DELETE FROM {tableName}"""
        self.cursor.execute(query)
        self.conn.commit()

    @timeIt
    def deleteBy(self, tableName, attributes):
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in attributes.items()])
        query = f"""DELETE FROM {tableName} WHERE {conditions}"""
        self.cursor.execute(query)
        self.conn.commit()
    
    @timeIt
    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def generateToTestRelations(self):
        query_list = """
                insert into VISITS (id, date, category) values (16, '11/23/2023', 'Adult');
                insert into VISITS (id, date, category) values (86, '6/27/2023', 'Elderly');
                insert into VISITS (id, date, category) values (36, '8/28/2023', 'Disabled');
                insert into VISITS (id, date, category) values (77, '2/23/2023', 'Adult');
                insert into VISITS (id, date, category) values (46, '12/18/2023', 'Adult');
                insert into VISIT_TICKET (id, category, visitId) values (27, 'Adult', 16);
                insert into VISIT_TICKET (id, category, visitId) values (35, 'Disabled', 16);
                insert into VISIT_TICKET (id, category, visitId) values (64, 'Adult', 16);
                insert into VISIT_TICKET (id, category, visitId) values (74, 'Elderly', 86);
                insert into VISIT_TICKET (id, category, visitId) values (21, 'Disabled', 36);
                insert into VISIT_TICKET (id, category, visitId) values (68, 'Adult', 77);
                insert into VISIT_TICKET (id, category, visitId) values (34, 'Adult', 46);
                """.split(";")
        for query in query_list:
            self.cursor.execute(query+";")
            self.conn.commit()
    
    @timeIt
    def generateToTestPerformance(self, amount):
        from faker import Faker
        import random
        fake = Faker("el_GR")
        for i in range(amount):
            query = f"INSERT INTO PERSON (id, firstName, lastName, phone, email) VALUES ({i}, '{str(fake.first_name())}', '{str(fake.last_name())}', '{str(''.join((random.choice('0123456789') for i in range(10))))}', '{str(''.join((random.choice('abcdxyzpqr') for i in range(15))))}')"
            self.cursor.execute(query)
            self.conn.commit()


if __name__ == "__main__":
    museum_db = MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
    
    #museum_db.create(tableName="EMPLOEEY", attributes={"id":2314,"specialty":"test3" })
    
    museum_db.deleteAll("VISITS")
    museum_db.deleteAll("VISIT_TICKET")

    museum_db.generateToTestRelations()
    
    result = museum_db.query("SELECT * FROM VISIT_TICKET WHERE visitId=16")
    print(result)
    
    result = museum_db.readAll("VISITS")
    print(result)

    result = museum_db.readAll("VISIT_TICKET")
    print(result)

    result = museum_db.readBy("VISIT_TICKET", attributes={"id":27})
    print(result)

    museum_db.updateBy("VISIT_TICKET", toUpdate={"category":"TEST"}, conditions={"id":27})

    result = museum_db.readBy("VISIT_TICKET", attributes={"id":27})
    print(result)

    museum_db.deleteBy("VISIT_TICKET", attributes={"id":27})

    result = museum_db.readBy("VISIT_TICKET", attributes={"id":27})
    print(result)

    for i in [1, 10, 100, 1000, 10000]:
        print(f"\n\n FOR {i} INSERTIONS\n")

        museum_db.deleteAll("PERSON")

        museum_db.generateToTestPerformance(i)

        result = museum_db.readAll("PERSON")
        #print(result)


    museum_db.conn.close()
