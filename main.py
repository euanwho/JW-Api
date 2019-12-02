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

    ## verseContent is assigned an array of the spans inside the span tag whose id ends in the value of verseNum
    verseContent = soup.select('[id$="' + str(verseNum) + '"] span')

    ## Iterates through contents of spans, if the child is not a tag, then it is concatenated to verseText
    verseText = ''
    for span in verseContent:
        for child in span.contents:
            if not isinstance(child, bs4.Tag):
                verseText += child.strip()
                
    return verseText

print(getVerse('Proverbs', 3, 15))


## Todo:
# - redo variable names
