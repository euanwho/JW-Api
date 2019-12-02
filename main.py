import requests
import bs4

## Returns formatted string version of the verseNum number that can be used to identify the verseNum in the DOM
def formatVerse(verseNum):
    verseNum = str(verseNum)
    if len(verseNum) == 1:
        return '00' + verseNum
    elif len(verseNum) == 2:
        return '0' + verseNum
    else:   
        return verseNum

def getVerse(book, chapterNum, verseNum):
    verseNum = formatVerse(verseNum)
    ## Format web address with book and chapter variables
    web_address = 'https://www.jw.org/en/library/bible/nwt/books/' + book + '/' + str(chapterNum)

    ## Request web address and throw an error if the status code is not successful
    try: 
        res = requests.get(web_address)
        res.raise_for_status()
    except:
        return {'Error': 'Verse not found'}

    ## Assign the HTML to a BeautifulSoup object stored within the soup variable
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    ## verseContent is assigned the span tag inside the span tag whose id ends in the value of verseNum
    verseContent = soup.select('[id$="' + str(verseNum) + '"] span')[0]

    ## To clean up the verse formatting from extraenous asterisks and footnote signs, we iterate and delete direct descendants of verseContent
    for child in verseContent.children:
        child.decompose()

    ## Return the verseNum's text without any HTML tags
    return verseContent.text.strip()

print(getVerse('Genesis', 50, 23))


## Todo:
#  - copy over all RegExs