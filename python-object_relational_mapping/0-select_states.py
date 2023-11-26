#!/usr/bin/python3
"""list all states with a name starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1], 
                                 passwd=sys.argv[2], connexion=sys.argv[3], port=3306)
    cursor = connection.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()

    


