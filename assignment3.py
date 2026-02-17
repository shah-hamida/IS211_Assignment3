import argparse
import urllib.request
import csv
import io
import re
# other imports go here

def downloadData(url):
    """Downloads the data"""
    """
       Reads data from a URL and returns the data as a string

       :param url:
       :return: the content of the URL
       """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response



def main(url):
    print(f"Running main with URL = {url}...")
    results = downloadData(url)

    csv_data = csv.reader(io.StringIO())
    for row in csv_data:
        path_file = row[0]
        datetime_access = row[1]
        browser = row[2]
        status_request = row[3]
        size_bytes = row[4]

    #processing the image hits
    image_file= 0
    total_file = 0

    image_hits = re.compile(r"\.(jpg|gif|png)$")

    with open("weblog.csv" , encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_file += 1
            path_file = row[0]
            if image_hits.search(path_file):
                image_file += 1
    percentage_wise = (image_file / total_file) * 100
    print(f"Image requests account for {percentage_wise}% of all requests")

    #processing the browser hits
    Firefox = 0
    Chrome = 0
    Internet_explorer = 0
    Safari = 0
    User_agent = row[2]


    if re.search(r"Firefox", User_agent):
        Firefox +=1
    elif re.search(r"Chrome", User_agent):
        Chrome +=1
    elif re.search(r"Internet Explorer", User_agent):
        Internet_explorer +=1
    elif re.search(r"Safari", User_agent):
        Safari +=1

    browser= {
        "Firefox": Firefox,
        "Chrome": Chrome,
        "Internet Explorer": Internet_explorer,
        "Safari": Safari,
    }

    popular_browser= max(browser, key=browser.get)
    print(f"The most popular browser is {popular_browser} ")



if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
