import requests
from bs4 import BeautifulSoup

def getlistoflinks(comand):
    url = f"https://www.google.com/search?q={comand}&ie=UTF-8"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    resoults = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.startswith("/url?q="):
            href = href[7:] # Remove the /url?q= prefix
            end_pos = href.find("&")
            if end_pos != -1:
                href = href[:end_pos] # Remove the extra parameters
            if response.status_code >= 200 and response.status_code < 300:
                if "youtube" in href or "google" in href:
                    pass
                resoults.append(href)
    print(resoults)
    return resoults

def searchineachwebsite(listofwebs, strtosearch):
    for web in listofwebs:
        search_term = strtosearch
        site_url = web
        google_url = f"https://www.google.com/search?q={search_term}+site%3A{site_url}&ie=UTF-8"
        response = requests.get(google_url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = []
        for link in soup.find_all("a"):
            href = link.get("href")
            if href.startswith("/url?q="):
                href = href[7:] # Remove the /url?q= prefix
                end_pos = href.find("&")
                if end_pos != -1:
                    href = href[:end_pos] # Remove the extra parameters
                links.append(href)
    return links


def extractrelevantcontet(urls, target_keywords):
    for url in urls:
        print ("buscando en : " , url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        relevant_text = []
        for paragraph in soup.find_all("p"):
            text = paragraph.get_text()
            if any(keyword in text for keyword in target_keywords):
                relevant_text.append(text)
        return(relevant_text)
