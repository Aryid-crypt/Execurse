import sqlite3 as sl

def get_password_hash(username):
	con = sl.connect("Execurse.db")
	cursor = con.cursor()
	query = """SELECT password FROM USER where username = ?"""
	cursor.execute(query, [username])
	result = cursor.fetchall()
	cursor.close()
	passwordHash = result[0][0]
	return passwordHash

get_password_hash("example")
