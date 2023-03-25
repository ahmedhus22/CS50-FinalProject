from bs4 import BeautifulSoup
import requests,re

def formaturl(url):
    # Returns a formatted url, Returns None if input is not a url
    linkRegex = re.compile(r'''(
            (?:[A-Za-z0-9\-_]{0,63}     # matches the sub domain
            \.
            )
            ([A-Za-z0-9\-_]{1,63})      # matches the 2nd level domain and will be stored in match object group 2 if found
            \.
            (?:[A-Za-z]{1,63})
            /?
        )''',re.VERBOSE)
    return linkRegex.search(url).group()

def verify(link):
    """Returns True if the url is safe else False
        refer:https://www.reddit.com/r/learnpython/comments/supub9/how_to_get_url_of_the_first_google_search_result/"""

    url = 'https://www.google.com/search'

    headers = {
        'Accept' : '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': link}

    # Requests the html from google
    content = requests.get(url, headers = headers, params = parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    # Searches for the first link from the search result
    search = soup.find(id = 'search')
    first_link = search.find('a')
    link = first_link['href']

    # Format the url
    urlfound = formaturl(link)

    # if first result is same as given url, then link maybe safe return false
    if urlfound == link:
        return True
    else:
        return False