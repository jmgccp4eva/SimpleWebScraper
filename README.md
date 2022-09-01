# SimpleWebScraper

Takes movies.tsv file from SimpleDataParserCleanser project
and web scrapes for cast fo movie and the characters they played.

1. Reads in moviesList from movies.tsv
2. Iterates through each movie:
   1. Builds url
   2. Uses BeautifulSoup to scrape data
   3. Iterates through this data to build dictionary of cast
   4. Appends movie-actors:character played to file

NOTE: If there is an error, should automatically call
itself where it left off, attempting again and again
until all ~137K movies have been read.

NOTE: This is a simple scraper.  
It will take over 24 hours (it took about 26 hours for me) 
to complete the entire scraping process.  I could have 
had this threaded and would take a significantly shorter
amount of time.  However, then it wouldn't be a "simple"
web scraper.