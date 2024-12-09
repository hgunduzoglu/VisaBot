from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains

# Function to initialize the Chrome browser in normal mode
def initialize_browser():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    # ChromeDriver servis yolu (kendine uygun path ile değiştir)
    driver_path = r"C:/webdriver/chromedriver.exe"
    service = Service(driver_path)

    # Tarayıcı oturumunu mevcut oturuma bağla
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Tarayıcı ile işlemlere devam edebilirsin
    print("Tarayıcı oturumuna başarıyla bağlandı!")
    # Function to allow manual login due to SMS authentication
    if driver is None:
        print("Driver NoneType, tarayıcı oturumu başlatılamadı.")
    else:
        print("Driver başarıyla oluşturuldu ve tarayıcı oturumu başlatıldı.")
    return driver
def manual_login(driver):
    print("Please login manually and complete the SMS authentication within 2 minutes.")
    time.sleep(120)  # Give 2 minutes for manual login

# Function to select checkboxes and buttons after login
def select_initial_options(driver):
    try:
        # Select the initial checkboxes and click the "Yeni Rezervasyon Başlat" button
        driver.find_element(By.ID, "mat-checkbox-1").click()
        driver.find_element(By.ID, "mat-checkbox-2").click()
        
        driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-dashboard/section[1]/div/div[2]/div/button").click()
       

        # Select the second checkbox and click "Devam Et"
        driver.find_element(By.ID, "mat-checkbox-3").click()
       
        driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-dashboard/section/div/button").click()
       

    except Exception as e:
        print(f"Error occurred during initial selections: {e}")

# Function to fill the form automatically
def fill_form(driver):
    try:
        print("Filling the form with applicant details...")

        # Fill the form with the provided details
        time.sleep(2)
        driver.find_element(By.ID, "mat-input-6").send_keys("NAME")
        driver.find_element(By.ID, "mat-input-7").send_keys("SURNAME")
        driver.find_element(By.ID, "mat-input-8").send_keys("PASSPORT NO")
        driver.find_element(By.ID, "mat-input-9").send_keys("International tel number prefix (ie. TR =90")
        driver.find_element(By.ID, "mat-input-10").send_keys("PHONE NUMBER")
        driver.find_element(By.ID, "mat-input-11").send_keys("MAIL")
        select_mat_option(driver, "//mat-select[@id='mat-select-0']", "SEX")
        select_mat_option(driver, "//mat-select[@id='mat-select-2']", "Country")
        
        
        print("Form filled successfully.")
       

    except Exception as e:
        print(f"Error occurred while filling the form: {e}")
    kaydet_button = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-applicant-details/section/mat-card[2]/app-dynamic-form/div/div/app-dynamic-control/div/div/div[1]/button')
    kaydet_button.click()
    time.sleep(1)

# Function to select appointment details
def select_appointment_details(driver):
    try:
        # Select appointment category and location
        
        select_mat_option(driver, "//mat-select[@id='mat-select-4']", "1 - Uzun Donem") # visa type
        select_mat_option(driver, "//mat-select[@id='mat-select-6']", "2 - AB/PL vatandasinin aile üyeleri") # category
        select_mat_option(driver, "//mat-select[@id='mat-select-8']", "Ankara - ankara Başkonsolosluğu Yetki Bölgesi") # location
        driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-application-details/section/form/mat-card[2]/button").click()
        time.sleep(1)
        
        

       

    except Exception as e:
        print(f"Error occurred while selecting appointment details: {e}")
    
    try:
        musait_tarih = driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-book-appointment-split-slot/section/mat-card[1]/div[2]/div/div/full-calendar/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[2]/td[1]")
        musait_tarih.click()
        driver.find_element(By.ID, "STRadio1").click()
    except:
        pass
    
    

# Function to confirm final terms and choose SMS notification
def confirm_terms_and_sms(driver):
    try:
        # Select checkboxes for terms and notifications
        driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
        driver.find_element(By.XPATH, "//input[@value='SMS']").click()
        driver.find_element(By.XPATH, "//button[text()='Devam Et']").click()
        time.sleep(3)

    except Exception as e:
        print(f"Error occurred while confirming terms and SMS: {e}")

# Function to select the payment method as "bankada ödeme"
def select_payment_method(driver):
    try:
        # Select "bankada ödeme" as the payment method
        payment_method_select = Select(driver.find_element(By.ID, "payment_method"))
        payment_method_select.select_by_visible_text("bankada ödeme")
        driver.find_element(By.XPATH, "//button[text()='Devam Et']").click()
        time.sleep(3)

    except Exception as e:
        print(f"Error occurred while selecting payment method: {e}")

# Main function to run the bot
def select_mat_option(driver, mat_select_xpath, option_text):
    try:
        # 1. Mat-select öğesini bul ve tıkla
        mat_select = driver.find_element(By.XPATH, mat_select_xpath)
        mat_select.click()

        # 2. Açılan menüden doğru seçeneği bul ve tıkla
        option_xpath = f"//mat-option//span[contains(text(), '{option_text}')]"
        option = driver.find_element(By.XPATH, option_xpath)
        option.click()

    except Exception as e:
        print(f"Seçenek seçilirken hata oluştu: {e}")

def run_bot():
    driver = initialize_browser()
    #driver.get("https://visa.vfsglobal.com/tur/tr/pol/login")  # Replace with the actual login page URL
    

    # Step 1: Manual login process
    #manual_login(driver)

    # Step 2: Select initial checkboxes and continue
    select_initial_options(driver)

    # Step 3: Fill the form with applicant details
    fill_form(driver)

    # Step 4: Select appointment date and time
    select_appointment_details(driver)

    # Step 5: Bypass additional services
    #bypass_additional_services(driver)

    # Step 6: Confirm terms and select SMS notification
    #confirm_terms_and_sms(driver)

    # Step 7: Select payment method as "bankada ödeme"
    #select_payment_method(driver)

    # Close the browser after completion
    driver.quit()

# Start the bot when the script is run
if __name__ == "__main__":
    run_bot()
