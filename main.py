import requests
import bs4

## Returns formatted string version of the verse number that can be used to identify the verse in the DOM
def formatVerse(verse):
    verse = str(verse)
    if len(verse) == 1:
        return '00' + verse
    elif len(verse) == 2:
        return '0' + verse
    else:   
        return verse

def getVerse(book, chapter, verse):
    verse = formatVerse(verse)
    ## Format web address with book and chapter variables
    web_address = 'https://www.jw.org/en/library/bible/nwt/books/' + book + '/' + str(chapter)

    ## Request web address and throw an error if the status code is not successful
    try: 
        res = requests.get(web_address)
        res.raise_for_status()
    except:
        return {'Error': 'Verse not found'}

    ## Assign the HTML to a BeautifulSoup object stored within the soup variable
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    ## Assign the span tag ending in the verse variable's value to verseContent
    verseContent = soup.select('[id$="' + str(verse) + '"]')[0]

    ## Take out the verse number contained in the sup.verseNum tag from the start of the verse
    verseContent.select('.verseNum')[0].decompose()

    ## Return the verse's text without any HTML tags
    return verseContent.text.strip()

print(getVerse('Genesis', 50, 23))


## Todo:
#  - take out all footnotes and spans
#  - copy over all RegExs