from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver
import time
from selenium.webdriver.common.action_chains import ActionChains


try:


    options = webdriver.ChromeOptions()

    options.add_argument(r'--user-data-dir=C:\Users\Dmitrii\AppData\Local\Google\Chrome\User Data\Profile 2')
    options.add_argument('--origin-trial-disabled-features=WebGPU')
    options.add_argument('----flag-switches-begin')
    options.add_argument('--flag-switches-end')

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


    driver.maximize_window()
    time.sleep(1)
    driver.get('https://eservice.rclgroup.com/CargoTracking/view/cargoTrackingNew')

    actions = ActionChains(driver)

    time.sleep(3)

    driver.execute_script('''window.open("https://eservice.rclgroup.com/CargoTracking/view/cargoTrackingNew", "_blank");''')

    time.sleep(3)
 
    driver.switch_to.window(driver.window_handles[1])

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


    cells_text = [cell.text for cell in row_element.find_elements(By.TAG_NAME,"td")]

    ##### Postprocessing #####

    info = ["No","BL Number","Booking Number","Container Number","Status"]
    
    headers_information = dict(zip(info, cells_text[:-1]))

    columns_els = driver.find_elements(By.CLASS_NAME,"col-sm-2.col-md-2.col-lg-2.fontFamily")
    

    information = columns_els[:len(columns_els) // 2]
    time_status = columns_els[len(columns_els) // 2:]

    status_info = dict()

    for i in range(5):
        status_info[information[i].text] = time_status[i].text
    

    print(headers_information)
    print (status_info)

finally:
    driver.quit()
