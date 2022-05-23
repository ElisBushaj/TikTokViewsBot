import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class zefoy_bot:
    def __init__(self, video_url, index):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome("chromedriver", options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.video_url = video_url
        self.index = index
        for _ in range(index):
            self.script()
    def script(self):
        try:
            self.driver.get("https://zefoy.com/")
            sleep(random.randint(4, 5))
            if len(self.driver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/form/div/div/img")) > 0:
                x = input("[-] Zefoy security code: ")
                self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div/div/div/input").send_keys(x)
                sleep(2)
                self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div/div/div/div/button").click()
                sleep(random.randint(3, 4))
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
            sleep(random.randint(1, 2))
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div/input").send_keys(self.video_url)
            sleep(random.randint(1, 2))
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div/div/button").click()
            sleep(random.randint(1, 2))
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/div/div[1]/div/form/button").click()
            print("[+] 1000 views")
            if self.index != 1:
                sleep(4 * 60)
        except:
            self.script()

if __name__ == '__main__':
    video_url = input("[-] Video Url: ").strip()
    index = int(input("[-] Views Zefoy 4min/K: "))
    print(f"[+] Script will finish after {index * 4} mins")
    zefoy_bot(video_url, index)
    print("[-] Finished!")