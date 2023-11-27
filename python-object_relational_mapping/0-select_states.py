#!/usr/bin/python3
"""list all states with a name starting with
N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states():
    connexion = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    curs = connexion.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    connexion.close()

if __name__ == "__main__":
    list_states()
