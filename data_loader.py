from urllib.request import urlopen

from openaiClient import create_embedding
from pineconeClient import save_embedding
from bs4 import BeautifulSoup


def split(text:str):
    return text.split("\n\n")

def split_max_size(text:str, size:int):
        split_text = text.split(" ")
        result = []
        chunk = ""
        for word in split_text:
            if (len(chunk) + len(word)) > size:
                result.append(chunk)
                chunk = ""
            chunk =chunk + word + " "

        result.append(chunk)
        return result

def save_chunks_embeddings(chunks):
    for chunk in chunks:
        emb = create_embedding(chunk)
        save_embedding(chunk,emb)

def load_data(text):
    chunks = split_max_size(text, size=300)
    save_chunks_embeddings(chunks)

def parse_webpage(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    text = '\n'.join(chunk for chunk in lines if chunk)
    print(text)
    return text

#load_data(CINEMA_FAQ_DATA)
#text = parse_webpage('https://multiplex.ua/about')
#load_data(text)
