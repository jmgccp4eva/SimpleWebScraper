from bs4 import BeautifulSoup
import requests

# Reads file and returns dictionary with all the data from that tsv file
def readInDict(file):
    myList = {}
    print('Reading in '+file)
    f = open(file,'r',encoding='utf-8')
    while True:
        line = f.readline().strip()
        if not line: break
        spl = line.split('\t')
        myList[spl[0]]=line
    f.close()
    return myList

# Iterates through dictionary, creates imdb url, reads cast and characters from url
# Writes a file for each movie with all actor codes and their character name
# 'Unknown Character Name' if the character's name isn't known or is blank
# Also, if there is an error, will automatically retry connecting to same url
# Appends each resulting movie-actors-characters to titleCastChar.tsv
def scrapeMovieCasts(moviesList,completeCount):
    blank_url = 'https://www.imdb.com/title/'
    currentCount=0
    total = len(moviesList)
    for movie in moviesList.keys():
        print(str(currentCount+1)+' of '+str(total)+'\t'+movie)
        cast = {}
        if currentCount<completeCount:
            pass
        else:
            try:
                url = blank_url + movie + '/fullcredits'
                r =  requests.get(url)
                soup = BeautifulSoup(r.content,'html.parser').select('table.cast_list tr td a')
                iterator = 0
                for iterator in range(0,len(soup)):
                    if len(soup[iterator].text)>0 and soup[iterator]['href'][:6]=='/name/':
                        try:
                            char = soup[iterator+1].text.strip()
                        except:
                            char = ''
                        if len(char)==0:
                            char = 'Unknown Character Name'
                        cast[soup[iterator]['href'][6:-1]]=char
                f = open('titleCastChar.tsv','a',encoding='utf-8')
                f.write(movie+'\t')
                first = True
                for actor,char in cast.items():
                    if not first:
                        f.write('~~~')
                    f.write(actor+":"+char)
                    first=False
                f.write('\n')
                f.close()
                completeCount+=1
            except:
                scrapeMovieCasts(moviesList,completeCount)
        currentCount+=1

def main():
    movieList = readInDict('movies.tsv')
    scrapeMovieCasts(movieList,0)


if __name__=='__main__':
    main()