import requests
import bs4

## Returns zero-padded string version of the verseNum number that can be used to identify the verseNum in the DOM
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

    ## verseContent is assigned the span tag whose id ends in the value of verseNum
    verseContent = soup.select('[id$="' + str(verseNum) + '"]')[0]

    ## To clean up the verse formatting from extraenous asterisks and footnote signs, we iterate and delete direct descendants of verseContent
    
    print(verseContent)
    ## Return the verseNum's text without any HTML tags
    return verseContent.text.strip()

print(getVerse('Proverbs', 3, 5))


## Todo:
#  - copy over all RegExs
#  - format strings