import sqlite3

def isurlFake(url):
    """Returns True if url exists in fake urls Table"""
    con = sqlite3.connect("urls.db")

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

def inserturl(url, name):
    con = sqlite3.connect("urls.db")
    cur = con.cursor()

    with con:
        cur.execute("INSERT INTO urls(url, name) VALUES(:url, :name)", {'url': url, 'name': name})
    con.close()

def geturls():
    """Returns a list of tuples where each element contains a row from the table"""
    con = sqlite3.connect("urls.db")
    cur = con.cursor()

    cur.execute("SELECT url, name FROM urls")

    # urls contain a list of tuples
    urls = cur.fetchall()
    con.close()
    
    return urls

def delurl(url, name):
    """Deletes a row from the Table for given name and adds it to safe table"""
    con = sqlite3.connect("urls.db")
    cur = con.cursor()

    with con:
        cur.execute("DELETE FROM urls WHERE name=:name", {'name': name})
        cur.execute("INSERT INTO safe(url, name) VALUES(:url, :name)", {'url': url, 'name': name})
    con.close()

def isurlSafe(url):
    """Returns True if the url is in the safe table"""
    con = sqlite3.connect("urls.db")
    cur = con.cursor()

    cur.execute("SELECT url FROM safe WHERE url=:url", {'url': url})
    safeurl = cur.fetchone()

    con.close()

    # safe url is None if there is no url in the table
    if safeurl is None:
        return False
    else:
        return True

def insertsafe(url, name):
    con = sqlite3.connect("urls.db")
    cur = con.cursor()

    with con:
        cur.execute("INSERT INTO safe(url, name) VALUES(:url, :name)", {'url': url, 'name': name})
    con.close()

def getsafe(name):
    """Returns a list of tuples where each element contains a row from safe table matching given name"""
    con = sqlite3.connect("urls.db")
    cur = con.cursor()

    cur.execute("SELECT url, name FROM safe WHERE name LIKE :name", {'name': name})

    # safe contain a list of tuples
    safe = cur.fetchall()
    if len(safe) == 0:
        cur.execute("SELECT url, name FROM safe WHERE name LIKE :name", {'name': "%" + name + "%"})
        safe = cur.fetchall()
    con.close()
    
    return safe