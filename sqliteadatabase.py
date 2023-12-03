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
# create a new note for a specific user
# arguments : userid, subject, date, text
# returns : noteid or -1 if note creation fails
def createnote(userid, subject, date, text, url="") -> int:
    con = connect()
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO notes (userid, subject, date, text, url) VALUES (?, ?, ?, ?, ?)", [userid, subject, date, text, url])
        noteid = cur.lastrowid
        con.commit()
    except:
        noteid = int(-1)
    con.close()
    return(noteid)
