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
        
        Parameters
        ----------
        dbname : str
            name of the database
        tableSchemaPath : str
            path of table schema to 
        
        Returns
        -------
        none
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

        Parameters
        ----------
        tableName : str
            name of table
        attributes : dict
            dictionary with format {"id":5, "name":"Alex"}

        Returns
        -------
        none
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
        
        Parameters
        ----------
        tableName : str
            name of table
        Returns
        -------
        list
            A list of all fetched results
        """
        query = f"""SELECT * FROM {tableName}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    @timeIt
    def readBy(self, tableName, attributes):
        """
        Abstract implementation of read by operation
        
        Parameters
        ----------
        tableName : str
            name of table
        attributes : dict
            dictionary with format {"id":5, "name":"Alex"}
        Returns
        -------
        list
            A list of all fetched results filtered by attributes
        """
        conditions = ' AND '.join([f'{key} = "{value}"' for key, value in attributes.items()]) # Construct string to filter attributes
        query = f"""SELECT * FROM {tableName} WHERE {conditions}"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    @timeIt
    def updateBy(self, tableName, toUpdate, conditions):
        """
        Abstract implementation of read by operation

        Parameters
        ----------
        tableName : str
            name of table
        toUpdate : dict
            dictionary with format {"id":5, "name":"Alex"}
        conditions : dict
            dictionary with format {"id":5, "name":"Alex"}
        Returns
        -------
        none
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
        
        Parameters
        ----------
        tableName : str
            name of table
        Returns
        -------
        none
        """
        query = f"""DELETE FROM {tableName}"""
        self.cursor.execute(query)
        self.conn.commit()

    @timeIt
    def deleteBy(self, tableName, attributes):
        """
        Abstract implementation of create operation

        Parameters
        ----------
        tableName : str
            name of table
        attributes : dict
            dictionary with format {"id":5, "name":"Alex"}
        Returns
        -------
        none
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
                Parameters
        ----------
        query : str
            The query we want to execute
        Returns
        -------
        list
            A list of all fetched results
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def generateToTestRelations(self):
        """
        Function to generate data in order to test
        the database. It loads all the insert operations
        from a local file and executes them.
        """
        with open("dummyDataQueries.txt", "r", encoding="utf8") as f:
            query_list = f.read().split(";")
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
    
    def getAmountOfTicketForEvent(self):
        """
        Custom querie to get the amount of tickets for an event.
        """
        return self.query(f"SELECT eventId, COUNT(*) FROM EVENT_TICKET GROUP BY eventId")

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
    result = museum_db.getAmountOfTicketForEvent()
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
