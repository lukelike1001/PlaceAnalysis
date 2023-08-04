# run on python 3.11.2
from bs4 import BeautifulSoup
from csv import writer

# scrapes a reddit url to find the top 500 comments
def find_comments(input_path: str, output_path: str):

    # import the html file to be read using BeautifulSoup
    html_file = open(input_path, encoding="utf8")
    soup = BeautifulSoup(html_file, "html.parser")

    # open a new csv file in a new folder to write data into
    with open(output_path, "w", newline="", encoding="utf8") as f:

        # the header labels each column for readability
        csv_writer = writer(f)
        header = ["Comments"]
        csv_writer.writerow(header)

        # top level comments are written with the class <div class="md">
        comments = soup.find_all("div", {"class": "md"})

        for comment in comments:
            if comment.p == None:
                continue
            row = [comment.p.text.strip()]
            csv_writer.writerow(row)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "websites/place23.html"
    output_path = "place23.csv"
    find_comments(input_path, output_path)