import sqlite3

def isurlFake(url):
    """Returns True if url exists in fake urls Table"""
    con = sqlite3.connect("database.db")

    cur = con.cursor()
    cur.execute("SELECT url FROM urls WHERE url=:url", {'url': url})
    fakeurl = cur.fetchone()
    #con.commit() commit is not required for SELECTS

    con.close()
    # fakeurl is None if there are no urls 
    if fakeurl == None:
        return False
    else:
        return True
