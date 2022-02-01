import unittest
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os
#import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import requests
from urllib.error import URLError



def sleep_visual(seconds=10, razon=""):
    print("esperamos: "+razon+"\n")
    for i in range(seconds,0,-1):
        sys.stdout.write(str(i)+'.')
        sys.stdout.flush()
        sleep(1)
    print("\r\n")

def encuentra_elemento(URL,):
    try:
        return driver.find_element_by_xpath(URL)
        
    except NoSuchElementException as nse:
        print(nse)
        print("-----")
        print(str(nse))
        print("-----")
        print(nse.args)
        print("=====")

def link_existe(LINK):
    try:
        response = requests.get(LINK)
        return True
    except URLError as url_error:
        print("Server Not Found")
        return False
    else :
        print("There is no Error")
        return True


#user_string=os.getenv('12536554-k')
user_string='12536554-k'
#pass_string=os.getenv('rebeca')
pass_string='rebeca'


LINK = 'http://homer.sii.cl/'
while link_existe(LINK)==False:
    time.sleep(60)


cwd = os.getcwd()#direccion  del momento
print(cwd)
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : cwd}#se establece la carpeta actual como el default para la descarga
chrome_options.add_experimental_option('prefs', prefs)#empaquetamos las preferencias
#driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome('C:\\Users\\RVK-02\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)#partimos driver con opciones
#pantalla completa
#driver.maximize_window()
driver.get(LINK)

login_URL = "//ul[@id='main-menu']//a[contains(text(),'Mi Sii')]"
#login_element=WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(login_URL))
#login_element.click()
encuentra_elemento(login_URL).click()




#sleep(10)
sleep_visual(10,"ingresamos")

user_URL = "//input[@id='rutcntr']"
#try:
#    driver.find_element_by_xpath(user_URL).send_keys(user_string)
#except NoSuchElementException as nse:
#    print(nse)
#    print("-----")
#    print(str(nse))
#    print("-----")
#    print(nse.args)
#    print("=====")
encuentra_elemento(user_URL).send_keys(user_string)

#
#try:
#    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='rutcntr']"))).send_keys(user_string)
#except TimeoutException as toe:
#    print(toe)
#    print("-----")
#    print(str(toe))
#    print("-----")
#    print(toe.args)

pass_URL="//input[@id='clave']"
#try:
#    driver.find_element_by_xpath(pass_URL).send_keys(pass_string)
#except NoSuchElementException as nse:
#    print(nse)
#    print("-----")
#    print(str(nse))
#    print("-----")
#    print(nse.args)
#    print("=====")
encuentra_elemento(pass_URL).send_keys(pass_string)

boton_login ="//button[@id='bt_ingresar']"

try:
    driver.find_element_by_xpath(boton_login).click()
    #boton_element=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,boton_login)))
    #boton_element.click()
except NoSuchElementException as nse:
    print(nse)
    print("-----")
    print(str(nse))
    print("-----")
    print(nse.args)
    print("=====")

#sleep(5)
sleep_visual(5,"nos logeamos")

boton_confirm="//a[contains(text(),'Continuar')]"

try:
    driver.find_element_by_xpath(boton_confirm).click()
    
except NoSuchElementException as nse:
    print(nse)
    print("-----")
    print(str(nse))
    print("-----")
    print(nse.args)
    print("=====")

vuelta=True

while vuelta==True:
    sleep_visual(5,"vamonos a rcv")
    #ir a agina rcv
    driver.get('https://www4.sii.cl/consdcvinternetui/#/index')
    sleep(5)
    #seleccionar rut de empresa. acontinuacion direccion de selector
    #//body/div[@id='my-wrapper']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/form[1]/div[1]/select[1]
    select_empresa="//body/div[@id='my-wrapper']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/form[1]/div[1]/select[1]"

    try:
        select=Select(driver.find_element_by_xpath(select_empresa))
    #    select.click()
        select.select_by_visible_text('76404822-9')
        #break#continue
        #select.select_by_value('76000378-6')
    
    except NoSuchElementException as nse:
        print(nse)
        print("-----")
        print(str(nse))
        print("-----")
        print(nse.args)
        print("=====")
        break


    #//select[@id='periodoMes']
    select_empresa_mes="//select[@id='periodoMes']"
    try:
        select=Select(driver.find_element_by_xpath(select_empresa_mes))
        select.select_by_visible_text('Octubre')
        #break#continue
    
    except NoSuchElementException as nse:
        print(nse)
        print("-----")
        print(str(nse))
        print("-----")
        print(nse.args)
        print("=====")
        break

    boton_empresa_consulta = driver.find_element_by_xpath("//button[contains(text(),'Consultar')]")
    driver.execute_script("arguments[0].click();", boton_empresa_consulta)
    #con driver.exwcute_script se puede hacer un alerta?
    #que tal jquery?
    print("boton presionado")

    #boton_empresa_consulta="//button[contains(text(),'Consultar')]"
    #try:
    #    driver.find_element_by_xpath(boton_empresa_consulta).click()
    
    #except NoSuchElementException as nse:
    #    print(nse)
    #    print("-----")
    #    print(str(nse))
    #    print("-----")
    #    print(nse.args)
    #    print("=====")


    sleep_visual(5,"esperamos a que cargue la tabla")

    #existe la tabla con registros?
    #/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div[3]/div[3]/div[2]/div/div/div/table
    try:
        #tabla_registros = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/table[1]")
        
        try:
            #element = WebDriverWait(driver, 30,2).until((
            #    EC.presence_of_element_located(By.CSS_SELECTOR , "table.table.table-sm.ng-scope"))
            #)
            myTable = driver.find_element_by_tag_name("table")
            #print(myTable.text)
            myRows = myTable.find_elements(By.TAG_NAME, "tr")
            idx=0
            for row in myRows:
                
                if idx>0:
                    #col = row.find_elements_by_tag_name("td")[1]
                    myrow=row.text
                    print(myrow + "\n")
                    nombre_doc=myrow.split("(")[0]
                    #print(nombre_doc)
                    myrow=myrow.split("(")[1]
                    tip_doc=myrow.split(")")[0]
                    #print(tip_doc)
                    myrow=myrow.split(")")[1]
                    Tot_Docs= myrow.split()[0]
                    Exento= myrow.split()[1]
                    Neto= myrow.split()[2]
                    IVAR= myrow.split()[3]
                    IVAUC= myrow.split()[4]
                    IVANR= myrow.split()[5]
                    Total = myrow.split()[6]
                    #print(Tot_Docs)
                    #print(Exento)
                    #print(Neto)
                    #print(IVAR)
                    #print(IVAUC)
                    #print(IVANR)
                    #print(Total)
                idx=idx+1


        finally:
        #    print("no lo encontró")
            print("fin try table")
        #    #driver.quit()
        #    break
        
        #tabla_registros = driver.find_element_by_class_name("table table-sm ng-scope")
    except NoSuchElementException as nse:
        print(nse)
        print("-----")
        print(str(nse))
        print("-----")
        print(nse.args)
        print("=====")
        break
    #rows=driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody/tr')
    #print("rows:%d" , len(rows) )


    #btn btn-primary btn-block pull-right ng-scope
    boton_empresa_detalle = driver.find_element_by_class_name("btn.btn-primary.btn-block.pull-right.ng-scope")
    driver.execute_script("arguments[0].click();", boton_empresa_detalle)#descargamos a la carpeta establecida default
    

    vuelta=False


#sleep(5)
sleep_visual(5)
input("Press Enter to continue...")
driver.quit()

