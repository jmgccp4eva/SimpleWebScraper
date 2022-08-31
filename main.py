from bs4 import BeautifulSoup
import requests

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

def main():
    movieList = readInDict('movies.tsv')
    print(len(movieList))


if __name__=='__main__':
    main()