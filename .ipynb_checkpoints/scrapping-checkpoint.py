from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


def scrapping():

    driver = webdriver.Chrome()
    
    # Keys to URL and Values to divs (xpath data-category)
    articles_divs = {
        'tarjetas-graficas': 'Tarjetas Gráficas',
        'procesadores': 'Procesadores',
        'placas-base': 'Placas Base', 
        'discos-duros': 'Discos Duros',
        'discos-duros-ssd': 'Discos Duros',
        'memorias-ram': 'Memorias RAM',
        'fuentes-alimentacion': 'Fuentes Alimentación',
        'multilectores': 'Multilectores',
        'tarjetas-sonido': 'Tarjetas Sonido',
        'torres': ['Torres ATX', 'Barebones','Phanteks','Accesorios Torres'],
        'ventiladores': ['Refrigeración Líquida','Pasta térmica','Ventiladores CPU', 'Ventiladores Suplementarios'],
        'grabadoras-dvd-blu-ray': 'Grabadoras DVD/Blu Ray',
        'capturadoras': 'Capturadoras',
        'monitores-pc': 'Monitores',
        'teclados': 'Teclados',
        'ratones': 'Ratones',
        'altavoces': 'Altavoces',
        'portatiles': 'Portátiles',
        'smartphone-moviles': 'Smartphone/Móviles',
        'televisores': 'Televisores',
        'tablets': 'Tablets',
        'videoconsolas-ps4': 'Videoconsolas PS4',
        'videoconsolas-nintendo-switch': 'Videoconsolas Nintendo Switch',
        'videoconsolas-xbox-one': 'Videoconsolas Xbox One',
        'videoconsolas-nintendo-ds-3ds': 'Videoconsolas Nintendo DS/3DS'
    }
    
    
    articles_list = []
    categories_list = []
    prices_list = []
    stock_list = []
    divs_torres = []
    divs_ventiladores = []   
    
    for k, v in articles_divs.items():
        while True:
            #While loop to iterate again if an article wasn't catched.
            try:
                print('Categoría: '+k)
                driver.get(url="https://www.pccomponentes.com/"+k)
                while True:
                    try:
                        #Pop-Up
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cn__close_modal']"))).click()
                        print("Pop-up closed")
                        break
                    except TimeoutException:
                        break
                
                while True:
                    try:
                        #Accept Cookies
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-block btn-primary  btn-lg m-t-1 accept-cookie']"))).click() 
                        print("Cookies accepted")
                        break
                    except TimeoutException:
                        break
                
                while True:
                    try:
                        #Show more
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary btn-block btn-lg btn-more']"))).click() 
                        print("Show more button clicked ...")
                        break
                    except TimeoutException:
                        break
                        
                last_height = driver.execute_script("return document.body.scrollHeight")
                
                #Randoms mouse movements
                action = ActionChains(driver)
                
                total_articles = driver.find_element_by_xpath("//strong[@id='totalArticles']").text
                total_articles = int(total_articles)
                print('Total '+ k +' '+str(total_articles))
                
                while True:
                    #Infinite scroll 

                    # Scroll down to bottom
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    # Wait to load page
                    time.sleep(2)
                    
                
                    action.move_by_offset(random.randint(0,10),random.randint(0,10));
                    action.perform();
                    time.sleep(0.5)
                    
                    #Scroll top
                    driver.execute_script("window.scrollTo(0, 0);")
                                          
                    # Wait to load page
                    time.sleep(2)
                
                    # Calculate new scroll height and compare with last scroll height
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        # If heights are the same it will exit the function
                        break
                    last_height = new_height
                    
                time.sleep(2)
                
                #torres articles has different data-category names 
                if k == 'torres':
                    div_torres = []
                    for e in v:
                        div_torres.append(driver.find_elements_by_xpath("//article[@data-category="+"'"+e+"'"+']'))
                        #flat list to append all the different data-category articles at the same one
                        flat_torres_list = [item for flat_list in div_torres for item in flat_list]
                        
                    print('Number of DIVS '+ k + ' ' +str(len(flat_torres_list)))
                    
                    if len(flat_torres_list) >= total_articles - (total_articles*0.05): #Check scrapped all the articles
                        print('All articles were scrapped!')
                        
                        #Appending different features 
                        for i in flat_torres_list:
                            articles_list.append(i.get_attribute('data-name'))
                            categories_list.append(i.get_attribute('data-category')) 
                            prices_list.append(i.get_attribute('data-price'))
                            stock_list.append(i.get_attribute('data-stock-web'))
                            
                        break
                    else: 
                        print("Scrapping failed! Didn't get all articles !!!!!!! ----> "+k)

                #ventiladores articles has different data-category names         
                elif k == 'ventiladores':
                    div_ventiladores = []
                    for e in v:
                        div_ventiladores.append(driver.find_elements_by_xpath("//article[@data-category="+"'"+e+"'"+']'))
                        #flat list to append all the different data-category articles at the same one
                        flat_ventiladores_list = [item for flat_list in div_ventiladores for item in flat_list]
                        
                    print('Number of DIVS '+ k + ' ' +str(len(flat_ventiladores_list)))
                    
                    if len(flat_ventiladores_list) >= total_articles - (total_articles*0.05): #Check scrapped all the articles
                        print('All articles were scrapped!')
                        
                        for i in flat_ventiladores_list:
                            articles_list.append(i.get_attribute('data-name'))
                            categories_list.append(i.get_attribute('data-category')) 
                            prices_list.append(i.get_attribute('data-price'))
                            stock_list.append(i.get_attribute('data-stock-web'))
                        break
                    else: 
                        print("Scrapping failed! Didn't get all articles!! ----> "+k)

                #rest of articles that only have one data-category for each one        
                else:            
                    div = driver.find_elements_by_xpath("//article[@data-category="+"'"+v+"'"+']')
                    
                        
                    print('Number of DIVS '+ k + ' ' +str(len(div))) 
                    
                    if len(div) >= total_articles - (total_articles*0.05): #Check scrapped all the articles
                        print('All articles were scrapped!')
                        
                        for i in div:
                            articles_list.append(i.get_attribute('data-name'))
                            categories_list.append(i.get_attribute('data-category'))
                            prices_list.append(i.get_attribute('data-price'))
                            stock_list.append(i.get_attribute('data-stock-web'))
                        break
                        
                    else:
                        print("Scrapping failed! Didn't get all articles!! ----> "+k)
                        
                            
                      

            except SystemExit: # Replace Exception... with something more specific....
                break
                
    print('TOTAL OF ARTICLES SCRAPPED: '+str(len(categories_list)))
            
    return articles_list, categories_list, prices_list, stock_list


