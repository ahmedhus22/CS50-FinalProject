# CS50-FinalProject
#### [CS50x Final Project](https://cs50.harvard.edu/x/2023/project/)

# Phishing Detection
This Flask web app aims to detect suspicious links by comparing the link provided with the link found on google and maintains a sqlite3 database which stores the suspicious links and safe links so that future references wont require web searches.

# Installation

```
git clone https://github.com/ahmedhus22/CS50-FinalProject.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Usage
move into the installed directory and execute

```
flask run
```

Enter any valid url to check if it could potentially be dangerous.

If valid url is not provided it prompts the user again to enter a url.

If the url is valid and the program has falsely identified a url as fake you can remove it from the database.

Removed urls are added to a different table and will be considered safe in the future.

You can also search for the correct/safe url by providing the name of the site.

# Detailed Description
## **app.py**
app.py is the main flask file that contains all routes and renders respective html 

based on which route the user visits. 
### Routes

- Most important route is the /check route which 
checks if the url entered is potentially dangerous or not. 

- /index route displays the homepage.

- /database route displays the potentially dangerous links stored as a table.

- /delete route deletes the selected row from the table only the most recently added can be deleted.

- /search route searches for the url provided in the safe database and returns all matches.

## **scrape.py**
scrape.py contains functions defined to scrape information from google.

verify functions takes a url as input and searches google with that url, google's 

first search result most likely will contain the correct url and thus if the input 

url is different from the first link, then its most likely a fake url and may lead to 

a phishing page.

### Regex
a linkRegex is defined which matches to only a part of the url of the form 
www.example.com/

This Regex is used to format and keep all the urls in the same form for comparison.

The Regex is also useful to get the 2nd level domain of the url i.e example in 
www.example.com/ as group(2) method for the match object contains the domain name.

## **database.py**
database.py contains functions defined for all database queries.

It uses sqlite3 and connects to url.db to store all urls.

### urls.db
urls.db is a sqlite3 database which contains 2 tables having schema:
```
CREATE TABLE urls(id INTEGER NOT NULL PRIMARY KEY, url TEXT NOT NULL, name TEXT);
CREATE TABLE safe(id INTEGER NOT NULL PRIMARY KEY, url TEXT NOT NULL, name TEXT);
```

## **html**
### templates/
The templates directory contains all templates for diplaying the pages.

layout.html is the template used by other pages to extend it.

jinja2 syntax is used.

### static/
It contains a css style sheet. Although not much css has been applied to the page, most of the styles are from bootstrap.

# Improvements that can be made
Scraping information from google is not efficient. It would be better to use an api, serpai could instead be used but it was too slow. Additionally this project would be better off as an extension or something else instead of a website.

The more data that can be acquired more accurate it would be able to detect with enough data the scraping part could be removed and instead machine learning would be useful.