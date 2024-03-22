import json
import requests
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def acessar_pagina_dinamica(link):
    navegador = webdriver.Chrome (service=ChromeService(ChromeDriverManager().install()))
    navegador.get(link)
    #clicar em download pdf
    #find_element e find_element
    dowload_pdf=navegator.find_element(By.CSS_SELECTOR, #pdf). find_eleme
    #clicar na caixa da página embaixo

def main():
    link = "https://www.batatais.sp.gov.br/diario-oficial"
    acessar_pagina_dinamica(link)
    
    
    
if __name__ == "__main__":
    main()