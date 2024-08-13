from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, "lxml")
    links = soup.find_all('section')
    for link in links:
        link_h2 = link.h2.text
        link_p = link.p.text

        print(link_h2)
        print(link_p)