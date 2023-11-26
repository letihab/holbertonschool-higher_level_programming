#!/usr/bin/python3
"""list all states with a name starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],  # Change 'connexion' to 'db'
        port=3306
    )
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"  # Filter for names starting with 'N'
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()



    


