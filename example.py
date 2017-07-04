import psycopg2
import sys
sys.dont_write_bytecode = True

from config import config
from pprint import pprint
 

class DatabaseConnection: 

	def connect(self):

		""" Connect to the PostgreSQL database server 
			Getting **params from database.ini file 
		"""
		conn = None

		try:
			# read connection parameters
			params = config()
	 
			# connect to the PostgreSQL server
			pprint('Connecting to the PostgreSQL database...')
			self.conn = psycopg2.connect(**params)
	 		self.conn.autocommit = True

			# create a cursor
			self.cur = self.conn.cursor()

		except (Exception, psycopg2.DatabaseError) as error:
			pprint(error)

		finally:
			if conn is not None:
				conn.close()
				pprint('Database connection closed.')
 
 
	def create_table(self):
		try:
			create_table_command = "CREATE TABLE first_table(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
			self.cur.execute(create_table_command)
			pprint('Table was created.')
		except Exception as e: 
			pprint(e)
	
	def insert_new_item(self):
		try:
			new_item = ("some text", "56")
			insert_command = "INSERT INTO first_table(name, age) VALUES('" + new_item[0] + "','" + new_item[1] + "')"
			pprint('Item was added.')
			self.cur.execute(insert_command)
		except Exception as e: 
			pprint(e)

	def query_all(self):
		try:
			query_all_command = ("SELECT * FROM first_table")
			self.cur.execute(query_all_command)
			items = self.cur.fetchall()
			for item in items:
				pprint("each item : {0}".format(item))
		except Exception as e: 
			pprint(e)

	def update_item(self):
		try:
			update_command = "UPDATE first_table SET age=10 WHERE id=1"
			self.cur.execute(update_command)
		except Exception as e: 
			pprint(e)


	def del_item(self):
		try:
			del_item = "DELETE from first_table WHERE id=1"
			self.cur.execute(del_item)
			pprint('Item was deleted.')
		except Exception as e: 
			pprint(e)
			

	def drop_table(self):
		try:
			drop_table_command = "DROP TABLE first_table"
			self.cur.execute(drop_table_command)
			pprint('Table was deleted.')
		except Exception as e:
			pprint(e)
		


if __name__ == '__main__':

	database_connection = DatabaseConnection()

	database_connection.connect()
	
	database_connection.create_table()

	database_connection.insert_new_item()
	"""Example of INSERT """
	
	database_connection.update_item()
	"""Example of UPDATE """
	
	database_connection.query_all()
	"""Example of SELECT """

	database_connection.del_item()
	"""Example of DELETE """
	
	database_connection.drop_table()

		
		
