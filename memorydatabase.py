import datetime

# ---- HARDCODED DATA STARTS HERE ----
# notes is a list of note dictionary
notes = []

# First test note for first user
note = {
    "userid" : 0,
    "subject" : "sub1",
    "date" : datetime.datetime.now(),
    "text" : "text1",
    "url" : ""
}

# Add note to the notes list
notes.append(note)

# Second test note for second user
note = {
    "userid" : 1,
    "subject" : "sub2",
    "date" : datetime.datetime.now(),
    "text" : "text2",
    "url" : ""
}

# Add note to the notes list
notes.append(note)

# Third test note for first user
note = {
    "userid" : 0,
    "subject" : "sub3",
    "date" : datetime.datetime.now(),
    "text" : "text3",
    "url" : ""
}

# Add note to the notes list
notes.append(note)

# ---- HARDCODED DATA ENDS HERE ----

# create a new note for a specific user
# arguments : userid, subject, date, text
# returns : noteid or -1 if note creation fails
def createnote(userid, subject, date, text, url="") -> int:
    # TODO: Error handling will be added later. 
    # Create a note item
    note = {
        "userid" : userid,
        "subject" : subject,
        "date" : date,
        "text" : text,
        "url" : url
    }

    # Add note item to notes list
    notes.append(note)

    return(len(notes) - 1)

# list database ids of notes of a user
# arguments : userid
# returns : list of user's notes
def listusernotes(userid) -> []:
    # Create a new empty list that will contain ids and subject of a user notes
    usernotes = []
    # Database id of a single note
    dbid = 0
    # Go through all the notes and populate the new list that contains ids of one user
    for n in notes:
        if n["userid"] == userid:
            usernotes.append(dbid)
        # Next dbid to check
        dbid += 1
    
    # Return the populated list of notes of one user
    return usernotes

# list note details
# arguments : noteid
# returns : a note item as a dictionary
def notedetails(noteid) -> {}:
    # TODO: When database is used this function is used to fetch details from there
    # Now we simply return the information from notes list
    return notes[noteid]

# delete a note
# arguments : noteid
# returns : True is success or False in case of failure
def deletenote(noteid) -> bool:
    # Delete a list item
    notes.pop(noteid)
    # Return True for now
    return True