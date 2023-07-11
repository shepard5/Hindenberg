#Run this script before initiating Hindenburg Program

from bs4 import BeautifulSoup
import requests

def initial_benchmark():
    response = requests.get('http://hindenburgresearch.com/')  
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find('body').find_all('a')
    eighth_link = None
    if len(links) >= 8:
        eighth_link = links[7]['href']

    response = requests.get(eighth_link)
    soup = BeautifulSoup(response.content, "html.parser")
    body_text_benchmark = soup.body.get_text()
    return body_text_benchmark

    

