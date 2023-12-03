import sqlite3

# connect to the database
def connect() -> sqlite3.Connection:
    con = sqlite3.connect("notes.sqlite")
    # Try to create a table everytime to ensure that database exists
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE notes(id INTEGER PRIMARY KEY AUTOINCREMENT, userid, subject, date, text, url)")
    except:
        pass
        # Table likely exists - ignore and continue
    return con

