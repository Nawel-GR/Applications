import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import os

import time

def main():
    # Driver
    driver = webdriver.Firefox()

    # Path
    current_path = os.getcwd()
    file_ = 'test.txt'

    # Saving the files
    l_music = [] 

    with open(f"current_path/{file_}", 'r') as file:
        for line in file:
            music = str(line.strip())
            l_music.append(music)

    # Download the links
    for i in l_music:
            driver.get('https://fdownload.app/es/facebook-to-mp3')

            link = driver.find_element('id', 's_input')

            link.send_keys(i)

            driver.find_element(By.CSS_SELECTOR, 'button[class = "btn-red"]').click()

            flag = 0

            while not flag:
            
                time.sleep(5)

                try:
                    driver.find_element(By.CSS_SELECTOR, 'a[data-fquality="320"]').click()
                    flag = 1
                except:
                    pass        

            time.sleep(5)

            driver.find_element(By.CSS_SELECTOR, 'button[id="closeModalBtn"]').click()

            flag = 0

            while not flag:
            
                time.sleep(5)

                try:
                    driver.find_element(By.CSS_SELECTOR, 'a[id="btn_convert_dl"]').click()
                    flag = 1
                except:
                    pass

            print(i)

if __name__== '__main__':
    main()