# run on python 3.11.2
from bs4 import BeautifulSoup
from csv import writer

# scrapes a reddit url to find the top 500 comments
def find_comments(input_paths: str, output_path: str):

    # open a new csv file in a new folder to write data into
    with open(output_path, "w", newline="", encoding="utf8") as f:

        # the header labels each column for readability
        csv_writer = writer(f)
        header = ["Comments"]
        csv_writer.writerow(header)

        # import the html file to be read using BeautifulSoup
        for html_path in input_paths:
            html_file = open(html_path, encoding="utf8")
            soup = BeautifulSoup(html_file, "html.parser")

            # top level comments are written with the class <div class="md">
            comments = soup.find_all("div", {"class": "md"})

            for comment in comments:
                if comment.p == None:
                    continue
                row = [comment.p.text.strip()]
                csv_writer.writerow(row)

# main method that calls the web scraper function
if __name__ == "__main__":

    # define the input path storing the html files and
    # the output path where we would like to store the comments
    input_path = "websites/"
    output_path = "data/place_comments.csv"
    
    # list all the html files we would like to scrape
    html_files = ["place_is_back.html", "timelapse_day_1.html", "leaderboard_day_1.html",
                  "timelapse_day_2.html", "leaderboard_day_2.html", "timelapse_day_3.html",
                  "bots_and_scripts.html", "leaderboard_day_3.html", "timelapse_day_4.html",
                  "leaderboard_day_5.html", "last_expansion.html", "leaderboard_day_6.html",
                  "ends_today.html", "ends_soon.html", "thank_you.html",
                  "place23.html", "final_leaderboard.html", "official_timelapse.html"]
    
    # update the input directory for each of the files
    html_paths = [input_path + html_file for html_file in html_files]

    # run the comment scraping tool
    find_comments(html_paths, output_path)