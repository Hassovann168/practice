import sqlite3

DATABASE = 'database.db'

def create_products_table():
	con = sqlite3.connect(DATABASE)
	con.execute("CREATE TABLE IF NOT EXISTS products (numb, cost)")
	con.close()