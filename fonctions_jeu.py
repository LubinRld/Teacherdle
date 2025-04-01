import sqlite3

def  test_successful(guess,co,cu):
    print(cu)
    print(guess)
    result = cu.execute("SELECT * from Teachers WHERE nom ={}".format(guess))
    return result