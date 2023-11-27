
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
DRIVER = webdriver.Chrome(service=chrome_service)

def input_data_to_web(element,data,driver = DRIVER):
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, element))
    )
    input_element.clear()
    input_element.send_keys(data)

def read_element(element_out,element_in, driver = DRIVER):
    result_row = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, element_out))
    )

    price_element = result_row.find_element(By.CLASS_NAME, element_in)

    return (price_element.get_attribute('innerHTML'))

def processing1(input_data,url, driver = DRIVER):
    city_from_codes = {
    "Санкт-Петербург":'3',
    "Москва":'4',
    "Новосибирск":'1',
    "Екатеринбург":'5',
    "Тында":'6',
    "Благовещенск":'7',
    "Хабаровск":'8',
    "Владивосток":'9',
    "Комсомольск-на-Амуре":'13',
}
    driver.get(url)
    select_element = Select(driver.find_element(By.NAME,"idcity_from"))
    select_element.select_by_value(city_from_codes[input_data["city_from"]])  
    
    input_data_to_web("idcity_to",input_data['city_to'])
    input_data_to_web("weight",input_data['weight'])
    input_data_to_web("volume",input_data['volume'])
    input_data_to_web("l1",input_data['l1'])
    input_data_to_web("l2",input_data['l2'])
    input_data_to_web("l3",input_data['l3'])


    calculate_button = driver.find_element(By.NAME, "submit")
    calculate_button.click()

    return_data = read_element("all_cost","price")

    driver.quit()

    return (return_data)

input_data1 = {
"city_from":"Санкт-Петербург",
"city_to": "Новосибирск",
"weight":"10",
"volume":"10",
"l1":"1",
"l2":"5",
"l3":"2",
}

def processing2(input_data,url, driver = DRIVER):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    
    input_data_to_web("form_pole12",input_data["weight"])
    input_data_to_web("form_pole13",input_data["volume"])

    dropdown_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-button')))


    print(len(dropdown_elements))
    first_dropdown_toggle = dropdown_elements[1]
    first_dropdown_toggle.click()
    
    option_item_text = input_data['city_to']
    option_item = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@class="ui-menu-item-wrapper" and text()="{option_item_text}"]')))
    option_item.click()
    

    second_dropdown_toggle = dropdown_elements[0]
    second_dropdown_toggle.click()

 
    option_item_text = input_data["city_from"]
    option_item = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@class="ui-menu-item-wrapper" and text()="{option_item_text}"]')))
    option_item.click()
 
    first_dropdown_toggle.click()

    total_sum_element = wait.until(EC.presence_of_element_located((By.ID, 'TotalSum')))


    total_sum_td = WebDriverWait(total_sum_element, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'td2'))
    )


    return_data = total_sum_td.text.strip()

    input()

    driver.quit()

    return (return_data)

input_data2 = {
"city_from":"Пенза",
"city_to": "Ижевск",
"weight":"10",
"volume":"10",
"l1":"1",
"l2":"5",
"l3":"2",
}

def processing3(input_data,url, driver = DRIVER):
    driver.get(url)
    wait = WebDriverWait(driver, 10) 
    def input_params(param,data):
        data_input = driver.find_element(By.ID, param)
        data_input.clear()
        data_input.send_keys(data)


    input_params('ves',input_data['weight'])
    input_params('obem',input_data['volume'])
    input_params('dlina',input_data['l2'])
    input_params('shirina',input_data['l1'])
    input_params('visota',input_data['l3'])

    city_input = driver.find_element(By.CLASS_NAME, 'form-control.from-city')
    city_input.clear()
    city_input.send_keys(input_data["city_from"])
    wait = WebDriverWait(driver, 10)
    time.sleep(1)
    suggestions = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'autocomplete-suggestion')))

    
    for suggestion in suggestions:
        if input_data["city_from"] in suggestion.text:
            suggestion.click()
            break



    

    city_input = driver.find_element(By.CLASS_NAME, 'form-control.to-city')
    city_input.clear()
    city_input.send_keys(input_data["city_to"])
    wait = WebDriverWait(driver, 10)
    time.sleep(1)
    suggestions = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'autocomplete-suggestion')))

   
    for suggestion in suggestions:
        if input_data["city_to"] in suggestion.text:
            suggestion.click()
            break
    
    price_element = wait.until(EC.presence_of_element_located((By.ID, 'priceAllText')))

    time.sleep(2)

  
    price_text = price_element.text.strip()



   

    driver.quit()

    return (price_text)

input_data3 = {
"city_from":"Краснодар",
"city_to": "Санкт-Петербург",
"weight":"10",
"volume":"10",
"l1":"1",
"l2":"5",
"l3":"2",
}

def processing4(input_data,url, driver = DRIVER):
    driver.get(url)
    wait = WebDriverWait(driver, 10)  

    def choose_option(driver, container_class, desired_option_text):
        
        container_element = driver.find_element(By.CLASS_NAME, container_class)
        select_styled_element = container_element.find_element(By.CLASS_NAME, 'select-styled')
        select_styled_element.click()

        select_options = WebDriverWait(container_element, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'select-options'))
        )

        options = select_options.find_elements(By.TAG_NAME, 'li')

        for option in options:
            if option.text == desired_option_text:
                option.click()
                break
    

    choose_option(driver, 'city-col.city-where.whereFrom', input_data['city_from'])
    choose_option(driver, 'city-col.where', input_data['city_to'])

    
    driver.find_element(By.NAME,'length').send_keys(input_data['l2'])  
    driver.find_element(By.NAME,'weight').send_keys(input_data['weight']) 
    driver.find_element(By.NAME,'height').send_keys(input_data['l1']) 
    driver.find_element(By.NAME,'width').send_keys(input_data['l3']) 

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-red.btn-calc'))
    )
    button.click()

    result_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'result-value'))
    )


    price_text = result_element.text


    driver.quit()

    return (price_text)

input_data4 = {
"city_from":"Краснодар",
"city_to": "Санкт-Петербург",
"weight":"10",
"volume":"10",
"l1":"1",
"l2":"5",
"l3":"2",
}

def processing5(input_data,url, driver = DRIVER):
    driver.get(url)
    wait = WebDriverWait(driver, 10)  

    from_city_input = driver.find_element(By.ID, 'calc__from_city')
    from_city_input.send_keys(input_data5["city_from"])

    wait = WebDriverWait(driver, 10)
    autocomplete_item_from = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ajax_suggest_autocomplete__item')))
    autocomplete_item_from.click()


    to_city_input = driver.find_element(By.ID, 'calc__to_city')
    to_city_input.send_keys(input_data5["city_to"])

    time.sleep(1)


    autocomplete_item_to = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ajax_suggest_autocomplete__item')))
    autocomplete_item_to.click()

    def data_input(path,data):

       
        data_input = driver.find_element(By.ID, path)

        
        data_input.clear()

        data_input.send_keys(data)

    data_input('calc__weight',input_data5["weight"])
    data_input('calc__length',input_data5["l2"])
    data_input('calc__width',input_data5["l3"])
    data_input('calc__height',input_data5["l1"])


    calculate_button = driver.find_element(By.ID, 'calc__count_btn')

  
    calculate_button.click()



    input()
  
    price_text = 0


    driver.quit()

    return (price_text)

input_data5 = {
"city_from":"Москва",
"city_to": "Ижевск",
"weight":"10",
"volume":"10",
"l1":"1",
"l2":"1",
"l3":"1",
}

def processing6(input_data,url, driver = DRIVER):
    driver.get(url)
    wait = WebDriverWait(driver, 10)  


    def city_input(path,data):
        data_input = driver.find_element(By.ID, path)
        data_input.clear()
        data_input.send_keys(data)

    def num_input_by_class(class_name, value):
        input_element = driver.find_element(By.CLASS_NAME, class_name)
        input_element.clear()
        input_element.send_keys(value)





    city_input('fromCity',input_data['city_from'])
    city_input('toCity',input_data['city_to'])
    num_input_by_class("form-control.weightCalc",input_data["weight"])
    num_input_by_class('form-control.heightCalc',input_data["l2"])
    num_input_by_class('form-control.widthCalc',input_data["l3"])
    num_input_by_class('form-control.longCalc',input_data["l1"])

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary'))
    )
    button.click()

    time.sleep(1)

    result_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'tk-calc-result__final'))
)
    

    price_text = result_element.text

    driver.quit()

    return (price_text)

input_data6 = {
"city_from":"Москва",
"city_to": "Ижевск",
"weight":"10",
"volume":"1",
"l1":"1",
"l2":"1",
"l3":"1",
}



if __name__ == '__main__':
    #print (processing1(input_data,'http://xn--80aodq4af.xn--p1ai/calculator/'))
    #print (processing2(input_data2,'https://tranzit-auto.ru/raschet-i-oformlenie-perevozki/'))
    #print (processing3(input_data3,'https://nevatk.ru/calc-mini/'))
    #print (processing4(input_data4,'https://calculator.glavtrassa.ru/'))
    #print (processing5(input_data5,'http://ltl.nawinia.com/#calculation'))
    print (processing6(input_data6,'https://tk-skorost.ru/servisy/kalkulyator-sbornykh-gruzov/'))
    pass


