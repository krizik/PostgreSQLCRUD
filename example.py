import psycopg2
import sys
import ConfigParser

from pprint import pprint

class DatabaseConnection:

    def __init__(self):
        
        """
            Connection to DB

        """
        try:
            self.connection = psycopg2.connect(
                "dbname='test' user='postgres' host='localhost' password='1' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connect to database")

    def create_table(self):
        try:
            create_table_command = "CREATE TABLE second_table(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
            self.cursor.execute(create_table_command)
        except Exception as e: 
            print(e)

    def insert_new_item(self):
        try:
            new_item = ("some text", "56")
            insert_command = "INSERT INTO second_table(name, age) VALUES('" + new_item[0] + "','" + new_item[1] + "')"
            pprint(insert_command)
            self.cursor.execute(insert_command)
        except Exception as e: 
            print(e)

    def query_all(self):
        try:
            self.cursor.execute("SELECT * FROM second_table")
            items = self.cursor.fetchall()
            for item in items:
                pprint("each item : {0}".format(item))
        except Exception as e: 
            print(e)

    def update_item(self):
        try:
            update_command = "UPDATE second_table SET age=10 WHERE id=1"
            self.cursor.execute(update_command)
        except Exception as e: 
            print(e)

    def del_item(self):
        try:
            del_item = "DELETE from second_table WHERE id=1"
            self.cursor.execute(del_item)
        except Exception as e: 
            print(e)
            

    def drop_table(self):
        try:
            drop_table_command = "DROP TABLE second_table"
            self.cursor.execute(drop_table_command)
        except Exception as e: 
            print(e)

if __name__== '__main__':
    database_connection = DatabaseConnection()

    """ Init of DB class creation 
    
    Use 'database_connection.create_table()' for creating new table 

    Use 'database_connection.insert_new_item()' for insert new record info existing table
    
    Use 'database_connection.query_all()' for checking all existing items in table
    
    Use 'database_connection.update_item()' for update existing item by it's id
   
    Use 'database_connection.del_item()' for delete exitsting item by it's id

    Use 'database_connection.drop_table()' to drop existing table
    
    """

    #database_connection.create_table()
    #database_connection.insert_new_item()
    #database_connection.query_all()
    #database_connection.update_item()
    #database_connection.del_item()
    database_connection.drop_table()







