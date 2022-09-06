"""
A very simple and basic web scraping script. Feel free to
use this as a source of inspiration, but, make sure to attribute
it if you do so.

This is by no means production code.
"""
# built-in imports
import re
from collections import defaultdict
from json import dump
from pprint import pprint
from urllib.request import urlopen
from xml.dom.minidom import Attr


import requests

# user packages
from bs4 import BeautifulSoup

# constants
BASE_URL = "https://www.domain.com.au"
N_PAGES = range(1, 3)  # update this to your liking
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# begin code
url_links = []
property_metadata = defaultdict(dict)

# generate list of urls to visit
for page in N_PAGES:
    print(page)
    url = BASE_URL + f"/rent/melbourne-region-vic/?sort=price-desc&page={page}"
    bs_object = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")

    # find the unordered list (ul) elements which are the results, then
    # find all href (a) tags that are from the base_url website.
    index_links = bs_object.find("ul", {"data-testid": "results"}).findAll(
        "a", href=re.compile(f"{BASE_URL}/*")  # the `*` denotes wildcard any
    )

    for link in index_links:
        # if its a property address, add it to the list
        if "address" in link["class"]:
            url_links.append(link["href"])


# for each url, scrape some basic metadata
for property_url in url_links[1:]:
    bs_object = BeautifulSoup(
        requests.get(property_url, headers=headers).text, "html.parser"
    )

    # looks for the header class to get property name
    property_metadata[property_url]["name"] = bs_object.find(
        "h1", {"class": "css-164r41r"}
    ).text

    # looks for the div containing a summary title for cost
    property_metadata[property_url]["cost_text"] = bs_object.find(
        "div", {"data-testid": "listing-details__summary-title"}
    ).text

    
    # extract coordinates from the hyperlink provided
    # i'll let you figure out what this does :P
    property_metadata[property_url]["coordinates"] = [
        float(coord)
        for coord in re.findall(
            r"destination=([-\s,\d\.]+)",  # use regex101.com here if you need to
            bs_object.find(
                "a", {"target": "_blank", "rel": "noopener noreferer"}
            ).attrs["href"],
        )[0].split(",")
    ]
    

    attr_dict = [feature.text for feature in bs_object \
            .find("div", {"data-testid": "property-features"}) \
            .findAll("span", {"data-testid": "property-features-text-container"})]
    
    if attr_dict == []:
        property_metadata[property_url]['rooms'] = 'null'
        property_metadata[property_url]['baths'] = 'null'
        property_metadata[property_url]['parking'] = 'null'
        property_metadata[property_url]['area'] = 'null'
    else:
        property_metadata[property_url]['rooms'] = re.findall(r'\d\s[A-Za-z]+', attr_dict[0])
        property_metadata[property_url]['baths'] = re.findall(r'\d\s[A-Za-z]+', attr_dict[1])
        property_metadata[property_url]['parking'] = re.findall(r'\d\s[A-Za-z]+', attr_dict[2])
        if len(attr_dict) == 4:
            property_metadata[property_url]['area'] = attr_dict[3]


    property_metadata[property_url]["desc"] = re.sub(
        r"<br\/>", "\n", str(bs_object.find("p"))
    ).strip("</p>")




# output to example json in data/raw/
with open("../data/raw/example.json", "w") as f:
    dump(property_metadata, f)
