import httpx
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

def acessar_pagina(link):
    pagina = httpx.get(link)
    bs = BeautifulSoup(pagina.text,"html.parser")
    print(bs)
    return bs 

def extrair_infos(link):
    pagina = acessar_pagina(link) 
    diarios = pagina.find("div",attrs={"class":"content"}).find_all("div",attrs={"class":"card border-0"})
    print(diarios)



    

def main():
    link = "https://www.batatais.sp.gov.br/diario-oficial"
    extrair_infos(link)
    
    
    
if __name__ == "__main__":
    main()