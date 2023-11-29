from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import undetected_chromedriver
from browsermobproxy import Server
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# server = Server(r"C:\Users\Dmitrii\Desktop\browsermob-proxy-2.1.4\bin\browsermob-proxy",options={'port': 8090})
# server.start()
# print("server.start()")
# proxy = server.create_proxy()

try:

    ua = UserAgent()
    options = webdriver.ChromeOptions()

    options.add_argument(r'--user-data-dir=C:\Users\Dmitrii\AppData\Local\Google\Chrome\User Data\Profile 2')
    # Замените параметр для отключения WebGPU и другие параметры командной строки
    options.add_argument('--origin-trial-disabled-features=WebGPU')
    options.add_argument('----flag-switches-begin')
    options.add_argument('--flag-switches-end')

    #options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument(f'--proxy-server={proxy.proxy}')


    #proxy.new_har("example", options={'captureHeaders': True, 'captureContent': True})
    

    
    #driver = webdriver.Chrome(options=options)
    driver = undetected_chromedriver.Chrome(options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
    'source':'''
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;

'''
})

    #driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    time.sleep(1)
    driver.get('https://eservice.rclgroup.com/CargoTracking/view/cargoTrackingNew')

    actions = ActionChains(driver)

    time.sleep(3)

    #driver.execute_script("window.open('https://eservice.rclgroup.com/CargoTracking/view/cargoTrackingNew')")

    driver.execute_script('''window.open("https://eservice.rclgroup.com/CargoTracking/view/cargoTrackingNew", "_blank");''')

    # Открытие новой вкладки
    #body = driver.find_element(By.TAG_NAME,"body")
    #body.send_keys(Keys.CONTROL + 't')

    time.sleep(3)
    # Переключение на новую вкладку



    driver.switch_to.window(driver.window_handles[1])

    # Открытие новой веб-страницы на новой вкладке
    #driver.get("https://eservice.rclgroup.com/CargoTracking/view/cargoTrackingNew")

    time.sleep(3)
    element = driver.find_element(By.ID, "statusBkgNo")

    

    element.send_keys("BSIU2857197")

    time.sleep(3)

    button_element = driver.find_element(By.ID,"submitBlNo")

    button_element.click()

    time.sleep(3)

    arrow_icon = driver.find_element(By.CSS_SELECTOR,".fa.fa-angle-down")

    arrow_icon.click()


    time.sleep(3)

    row_element = driver.find_element(By.CSS_SELECTOR,"tr.odd.shown")

    # Получаем текст из всех ячеек внутри элемента <tr>
    cells_text = [cell.text for cell in row_element.find_elements(By.TAG_NAME,"td")]

    info = ["No","BL Number","Booking Number","Container Number","Status"]
    
    headers_information = dict(zip(info, cells_text[:-1]))

    

    columns_els = driver.find_elements(By.CLASS_NAME,"col-sm-2.col-md-2.col-lg-2.fontFamily")
    
    # Разделяем массив на две части
    information = columns_els[:len(columns_els) // 2]
    time_status = columns_els[len(columns_els) // 2:]

    status_info = dict()

    for i in range(5):
        status_info[information[i].text] = time_status[i].text
    

    print(headers_information)
    print (status_info)

finally:
    driver.quit()
    #server.stop()