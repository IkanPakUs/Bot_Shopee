import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.page_load_strategy = 'eager'

login_qr = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F"                        
product_name = "cart"                                       
flash_sale = login_qr + product_name                                                                        

button_without_coin = '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[9]/button'
button_with_coin = '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[12]/button'


class ShopBot():
    def __init__(self): 
        self.driver = webdriver.Chrome(options = options)
        self.driver.maximize_window()
        self.driver.get("https://shopee.co.id/buyer/login/qr?next=https%253A%252F%252Fshopee.co.id%252Fcart")          

    def countdownTimer(self):                           
        target_m =60                          
        target_s =60                                                               
        current_m = time.strftime("%M")
        current_s = time.strftime("%S")
        minutes = target_m - int(current_m) - 1
        seconds = target_s - int(current_s)
        total_second = minutes * 60 + seconds - 1
        while total_second:
            mins, secs = divmod(total_second, 60)
            print(f'{mins:02d}:{secs:02d}', end='\r')
            time.sleep(0.99)
            total_second -= 1

    def addProduct(self):
        self.driver.refresh()
        self.driver.implicitly_wait(30)

        # add_to_cart = self.driver.find_element_by_xpath(
        #     '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'
        #     ).click()
        
        checklist = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[1]/div[3]/div/div[1]/div/div[1]/label/div'
            ).click()
        checkout = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button'
            ).click()
        
        # make_order = self.driver.find_element_by_xpath(button_with_coin).click()


if __name__ == "__main__":
    ShopBot = ShopBot()
    ShopBot.countdownTimer()
    ShopBot.addProduct()
    print('Finish')
    time.sleep(5)
