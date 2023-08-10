# run on python 3.11.2
from bs4 import BeautifulSoup
from csv import writer
import requests

# scrapes a wikipedia page to extract all its sentences
def find_sentences(input_urls: str, output_path: str):

    # open a new csv file in a new folder to write data into
    with open(output_path, "w", newline="", encoding="utf8") as f:

        # the header labels each column for readability
        csv_writer = writer(f)
        header = ["Sentences"]
        csv_writer.writerow(header)

        # import the html file to be read using BeautifulSoup
        for url in input_urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")

            # find all texts in the 
            comments = soup.find_all('p')

            for comment in comments:
                if comment == None:
                    continue
                block = comment.get_text()
                block = block.replace("\n", " ")
                sentences = block.split(". ")
                for sentence in sentences:
                    csv_writer.writerow([sentence])

# main method that calls the web scraper function
if __name__ == "__main__":

    # define the input path storing the html files and
    # the output path where we would like to store the comments
    input_path = "websites/"
    output_path = "sentences_EN.csv"
    
    # list all the urls to scrape from wikipedia
    urls = ["https://en.wikipedia.org/wiki/Apricot"]

    # run the comment scraping tool
    find_sentences(urls, output_path)