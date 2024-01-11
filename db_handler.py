import sqlite3
from timer import timeIt

class MuseumDatabase:
    """
    Database Handler
    """
    
    def __init__(self, db_name, tableSchemaPath):
        """
        Class initializer. Connects to database, 
        initialize cursos and generates tables from files
        """
        self.conn = sqlite3.connect(db_name) # Initialize connection
        self.cursor = self.conn.cursor() # Initialize cursor
        with open(tableSchemaPath, "r") as table: # Generate tables from file
            for command in table.read().split(");")[:-1]:
                self.cursor.execute(command.replace("\n", "")+");")
        self.conn.commit()

    # CRUD Implementation

    @timeIt # Decorator to time function
    def create(self, tableName, attributes):
        """
        Abstract implementation of create operation
        tableName : str
            name of table
        attributes : dict
            dictionary with format {"id":5, "name":"Alex"}
        """
        columns = ', '.join(attributes.keys()) # Construct attribute name sequence
        values = ', '.join(map(lambda x: f'"{x}"', attributes.values())) # Construct attribute value sequence
        query = f"""INSERT INTO {tableName} ({columns}) VALUES ({values})""" # Construct querie
        self.cursor.execute(query)
        self.conn.commit()

    @timeIt
    def readAll(self, tableName):
        """
        Abstract implementation of read all operation
        tableName : str
            name of table
        """
        query = f"""SELECT * FROM {tableName}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    @timeIt
    def readBy(self, tableName, attributes):
        """
        Abstract implementation of read by operation
        tableName : str
            name of table
        attributes : dict
            dictionary with format {"id":5, "name":"Alex"}
        """
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in attributes.items()]) # Construct string to filter attributes
        query = f"""SELECT * FROM {tableName} WHERE {conditions}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    @timeIt
    def updateBy(self, tableName, toUpdate, conditions):
        """
        Abstract implementation of read by operation
        tableName : str
            name of table
        toUpdate : dict
            dictionary with format {"id":5, "name":"Alex"}
        conditions : dict
            dictionary with format {"id":5, "name":"Alex"}
        """
        toUpdate = ' , '.join([f'{key} = "{value}"' for key, value in toUpdate.items()])
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in conditions.items()])
        query = f"""UPDATE {tableName} SET {toUpdate} WHERE {conditions}"""
        print("UPDATE QUERY: "+query)
        self.cursor.execute(query)
        self.conn.commit()
    
    @timeIt
    def deleteAll(self, tableName):
        """
        Abstract implementation of delete all operation
        tableName : str
            name of table
        """
        query = f"""DELETE FROM {tableName}"""
        self.cursor.execute(query)
        self.conn.commit()

    @timeIt
    def deleteBy(self, tableName, attributes):
        """
        Abstract implementation of create operation
        tableName : str
            name of table
        attributes : dict
            dictionary with format {"id":5, "name":"Alex"}
        """
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in attributes.items()])
        query = f"""DELETE FROM {tableName} WHERE {conditions}"""
        self.cursor.execute(query)
        self.conn.commit()
    
    # Functions to test performace

    @timeIt
    def query(self, query):
        """
        Simple function to execute querie
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def generateToTestRelations(self):
        """
        Function to generate data in order to test
        the database. It loads all the insert operations
        from a local file and executes them.
        """
        query_list = """
insert into VISITS (id, date, category) values (16, '5/11/2023', 'Adult');
insert into VISITS (id, date, category) values (86, '6/5/2023', 'Elderly');
insert into VISITS (id, date, category) values (36, '8/5/2023', 'Disabled');
insert into VISITS (id, date, category) values (77, '2/4/2023', 'Adult');
insert into VISITS (id, date, category) values (46, '12/4/2023', 'Adult');
insert into VISIT_TICKET (id, category, visitId) values (27, 'Adult', 16);
insert into VISIT_TICKET (id, category, visitId) values (35, 'Disabled', 16);
insert into VISIT_TICKET (id, category, visitId) values (64, 'Adult', 16);
insert into VISIT_TICKET (id, category, visitId) values (74, 'Elderly', 86);
insert into VISIT_TICKET (id, category, visitId) values (21, 'Disabled', 36);
insert into VISIT_TICKET (id, category, visitId) values (68, 'Adult', 77);
insert into VISIT_TICKET (id, category, visitId) values (34, 'Adult', 46);
insert into EXHIBIT (id, name, matterial, description, value, exavationPlace, exavationDate, categoryId, positionId) values ('M1', 'Severe', 'Marble', 'Ο Δίας ονομαζόταν στα Αρχαία Ελληνικά Ζευς, λέξη που στη γενική πτώση ήταν του Διός, (σπανιότερα του Ζηνός), απόπου προήλθε και η νεοελληνική ονομασία.', 32454353, 'Kristinehamn', '3/1/2023', 1, 'S1');
insert into EXHIBIT (id, name, matterial, description, value, exavationPlace, exavationDate, categoryId, positionId) values ('S1', 'CELEBREX', 'Steel', 'Ο Δίας ονομαζόταν στα Αρχαία Ελληνικά Ζευς, λέξη που στη γενική πτώση ήταν του Διός, (σπανιότερα του Ζηνός), απόπου προήλθε και η νεοελληνική ονομασία.', 41652416, 'Kristinehamn', '10/21/2023', 3, 'D1');
insert into EXHIBIT (id, name, matterial, description, value, exavationPlace, exavationDate, categoryId, positionId) values ('C1', 'White', 'Copper', 'Ο Δίας ονομαζόταν στα Αρχαία Ελληνικά Ζευς, λέξη που στη γενική πτώση ήταν του Διός, (σπανιότερα του Ζηνός), απόπου προήλθε και η νεοελληνική ονομασία.', 39407979, 'Tumba', '2/24/2023', 3, 'D2');
insert into EXHIBIT (id, name, matterial, description, value, exavationPlace, exavationDate, categoryId, positionId) values ('M2', 'Venlafaxine', 'Marble', 'Ο Δίας ονομαζόταν στα Αρχαία Ελληνικά Ζευς, λέξη που στη γενική πτώση ήταν του Διός, (σπανιότερα του Ζηνός), απόπου προήλθε και η νεοελληνική ονομασία.', 65396384, 'Nūrābād', '4/13/2023', 2, 'D3');
insert into EXHIBIT (id, name, matterial, description, value, exavationPlace, exavationDate, categoryId, positionId) values ('M3', 'Lactulose', 'Marble', 'Ο Δίας ονομαζόταν στα Αρχαία Ελληνικά Ζευς, λέξη που στη γενική πτώση ήταν του Διός, (σπανιότερα του Ζηνός), απόπου προήλθε και η νεοελληνική ονομασία.', 15054787, 'Santiago', '8/14/2023', 1, 'S2');
insert into EXHIBIT (id, name, matterial, description, value, exavationPlace, exavationDate, categoryId, positionId) values ('B1', 'TOMEGALOAGALMA', 'Brass', 'Ο Δίας ονομαζόταν στα Αρχαία Ελληνικά Ζευς, λέξη που στη γενική πτώση ήταν του Διός, (σπανιότερα του Ζηνός), απόπου προήλθε και η νεοελληνική ονομασία.', 36352814, 'Gunungangka', '7/25/2023', 3, 'D4');
insert into CATEGORY (id, start_date, end_date, name) values (1, '1/1/2023', '5/27/2023', 'Arxaio');
insert into CATEGORY (id, start_date, end_date, name) values (2, '7/8/2023', '10/8/2023', 'PolyArxaio');
insert into CATEGORY (id, start_date, end_date, name) values (3, '5/1/2023', '5/28/2023', 'ParaPolyArxaio');
insert into POSITION (id, column, row) values ('S1', 55, 10);
insert into POSITION (id, column, row) values ('D1', 85, 15);
insert into POSITION (id, column, row) values ('D2', 78, 90);
insert into POSITION (id, column, row) values ('D3', 36, 91);
insert into POSITION (id, column, row) values ('S2', 16, 62);
insert into POSITION (id, column, row) values ('D4', 37, 7);
insert into EVENT_TICKET (id, category, eventId) values (98, 'Student', 1);
insert into EVENT_TICKET (id, category, eventId) values (44, 'Abult', 1);
insert into EVENT_TICKET (id, category, eventId) values (84, 'Abult', 1);
insert into EVENT_TICKET (id, category, eventId) values (40, 'Student', 1);
insert into EVENT_TICKET (id, category, eventId) values (91, 'Abult', 1);
insert into EVENT_TICKET (id, category, eventId) values (38, 'Abult', 1);
insert into EVENT_TICKET (id, category, eventId) values (54, 'Elderly', 1);
insert into EVENT_TICKET (id, category, eventId) values (1, 'Abult', 2);
insert into EVENT_TICKET (id, category, eventId) values (97, 'Disabled', 1);
insert into EVENT_TICKET (id, category, eventId) values (59, 'Abult', 2);
insert into EVENT_TICKET (id, category, eventId) values (5, 'Kid', 1);
insert into EVENT_TICKET (id, category, eventId) values (47, 'Kid', 2);
insert into EVENT_TICKET (id, category, eventId) values (14, 'Abult', 1);
insert into EVENT_TICKET (id, category, eventId) values (20, 'Student', 2);
insert into EVENT_TICKET (id, category, eventId) values (6, 'Disabled', 2);
insert into EVENT (id, category, description, startDate, endDate, eventRoomId) values (1, 'A', 'Ο Δίας είναι ο θεός του ουρανού και του κεραυνού στην ελληνική μυθολογία. Είναι το νεότερο παιδί του Κρόνου και της Ρέας.', '3/5/2024', '5/5/2024', 1);
insert into EVENT (id, category, description, startDate, endDate, eventRoomId) values (2, 'B', 'Ο Δίας είναι ο θεός του ουρανού και του κεραυνού στην ελληνική μυθολογία. Είναι το νεότερο παιδί του Κρόνου και της Ρέας.', '1/2/2024', '3/2/2024', 2);
insert into EVENT_ROOM (id, name, description, capacity) values (1, 'Pollaplon', 'Ο Ησίοδος μας μεταφέρει τα περί της μυθικής Τιτανομαχίας, αναφέροντας ότι ο Δίας και τα αδέλφια του πολέμησαν εναντίον του Κρόνου και των Τιτάνων για την κυριαρχία επάνω στη Γη.', 111);
insert into EVENT_ROOM (id, name, description, capacity) values (2, 'Kentrikh', 'Ο Ησίοδος μας μεταφέρει τα περί της μυθικής Τιτανομαχίας, αναφέροντας ότι ο Δίας και τα αδέλφια του πολέμησαν εναντίον του Κρόνου και των Τιτάνων για την κυριαρχία επάνω στη Γη.', 259);
                """.split(";")
        for query in query_list:
            self.cursor.execute(query+";")
            self.conn.commit()
    
    @timeIt
    def generateToTestPerformance(self, amount):
        """
        Simple function to generate batches of
        data and time the performace of the database.

        amount : int
            amount of data to generate
        """
        from faker import Faker
        import random
        fake = Faker("el_GR")
        for i in range(amount):
            query = f"INSERT INTO PERSON (id, firstName, lastName, phone, email) VALUES ({i}, '{str(fake.first_name())}', '{str(fake.last_name())}', '{str(''.join((random.choice('0123456789') for i in range(10))))}', '{str(''.join((random.choice('abcdxyzpqr') for i in range(15))))}')"
            self.cursor.execute(query)
            self.conn.commit()
    
    # Custom Queries
    def getExhibitByCategoryName(self, categoryName):
        """
        Custom querie to get exhibits by category name.
        """
        return self.query(f"SELECT EXHIBIT.name FROM EXHIBIT WHERE EXHIBIT.categoryId IN (SELECT CATEGORY.id FROM CATEGORY WHERE CATEGORY.name='{categoryName}')")
    
    def getExhibitPosition(self, exhibitId):
        """
        Custom querie to get exhibit position.
        """
        return self.query(f"SELECT row, column FROM POSITION WHERE id IN ( SELECT positionId FROM EXHIBIT WHERE id='{exhibitId}' )")
    
    def getEventCategories(self):
        """
        Custom querie to get categories of the events that take place.
        """
        return self.query(f"SELECT category FROM EVENT ORDER BY category ASC")
    
    def getExhibitCategories(self):
        """
        Custom querie to get exhibit categories.
        """
        return self.query(f"SELECT name FROM CATEGORY ORDER BY name ASC")

if __name__ == "__main__":
    museum_db = MuseumDatabase('ArcheologicalMuseum.db', "schema.sql")
    
    #museum_db.create(tableName="EMPLOEEY", attributes={"id":2314,"specialty":"test3" })
    for table in ["VISITS", "VISIT_TICKET", "EXHIBIT", "CATEGORY", "POSITION", "EVENT", "EVENT_ROOM", "EVENT_TICKET"]:
        museum_db.deleteAll(table)

    museum_db.generateToTestRelations()
    
    result = museum_db.getExhibitByCategoryName("ParaPolyArxaio")
    print("Custom:", result)
    result = museum_db.getExhibitPosition('S1')
    print("Custom:", result)
    result = museum_db.getEventCategories()
    print("Custom:", result)
    
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
