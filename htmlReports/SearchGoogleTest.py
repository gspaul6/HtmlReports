from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import os
from selenium.webdriver.common.action_chains import ActionChains

class SearchGoogle(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        options=Options()
        options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        #implicit wait
        self.driver.implicitly_wait(20)
        #Maximise the Window
        self.driver.maximize_window()
   
   
    
    def test_search_by_anyname(self):
        self.driver.get("https://www.geeksforgeeks.org/")
        search_box= self.driver.find_element(By.XPATH, '//*[@id="RA-root"]/div/div[1]/div[1]/div[2]/span/span/span[2]/button/span')
        

    def test_click(self):
        self.driver.get("https://www.geeksforgeeks.org/")
        search_box= self.driver.find_element(By.XPATH, '//*[@id="userProfileId"]/a')
        search_box.click()    
           
       
    @classmethod 
    def tearDown(self) -> None:
        #self.driver.close()
        #self.driver.quit()
        print("Test completed")
        


if __name__=='__main__':
    if os.path.exists('reports'):
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
    else:
        print("The path doesnt exits")




