from bs4 import BeautifulSoup
import time
import requests
i = 0

def Hindenburg_Refresh():

    response = requests.get('http://hindenburgresearch.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find('body').find_all('a')
    eighth_link = None
    
    if len(links) >= 8:
        eighth_link = links[7]['href']


    response = requests.get(eighth_link)
    soup = BeautifulSoup(response.content, "html.parser")
    body_text = soup.body.get_text()

    if body_text_benchmark != body_text:
        return body_text

    else:
        
        global recursion_count
        recursion_count = recursion_count + 1
        print("Function executed " + str(recursion_count) + " times")
        time.sleep(1)
        return

        Hindenburg_Refresh('http://hindenburgresearch.com/')
