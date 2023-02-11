import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class SampleTeseCase(unittest.TestCase):

    def setUp(self):
        # open Firefox browser
        self.driver = webdriver.Chrome()
        # maximize the window size
        self.driver.maximize_window()
        # delete the cookies
        self.driver.delete_all_cookies()
        # navigate to the url
        self.driver.get('http://localhost:3000/')

    def test(self):
        ### test case 1: compress jpg image
        # find the input file
        inputElement = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')
        # send the file path
        inputElement.send_keys(os.getcwd() + '/image01.jpg')
        # wait for 5 seconds to upload the image
        time.sleep(5)
        # find the compress button
        compressButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/button')
        # click the button
        compressButton.click()
        # wait for 5 seconds to compress the image
        time.sleep(5)
        # find the download button
        downloadButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div/a')
        # click the button
        downloadButton.click()
        # wait for 5 seconds to download the image
        time.sleep(5)
        # assert the file is downloaded in browser download folder
        self.assertTrue(os.path.exists(os.path.expanduser('~/Downloads/image01.jpg')))
        # print success message
        print(bcolors.OKGREEN + 'test case 1: compress jpg image - success\n\n' + bcolors.ENDC)
        # wait for 5 seconds to see the result
        time.sleep(5)

        ### test case 2: change uploaded image
        # find the input file
        inputElement = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')
        # send the file path
        inputElement.send_keys(os.getcwd() + '/image02.jpg')
        # wait for 5 seconds to upload the image
        time.sleep(5)
        # find the compress button
        compressButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/button')
        # click the button
        compressButton.click()
        # wait for 5 seconds to compress the image
        time.sleep(5)
        # find the download button
        downloadButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div/a')
        # click the button
        downloadButton.click()
        # wait for 5 seconds to download the image
        time.sleep(5)
        # assert the file is downloaded in browser download folder
        self.assertTrue(os.path.exists(os.path.expanduser('~/Downloads/image02.jpg')))
        # print success message
        print(bcolors.OKGREEN + 'test case 2: change uploaded image - success\n\n' + bcolors.ENDC)
        # wait for 5 seconds to see the result
        time.sleep(5)

        # test case 3: compress png image
        # find the input file
        inputElement = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')
        # send the file path
        inputElement.send_keys(os.getcwd() + '/image03.png')
        # wait for 5 seconds to upload the image
        time.sleep(5)
        # find the compress button
        compressButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/button')
        # click the button
        compressButton.click()
        # wait for 5 seconds to compress the image
        time.sleep(5)
        # find the download button
        downloadButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div/a')
        # click the button
        downloadButton.click()
        # wait for 5 seconds to download the image
        time.sleep(5)
        # assert the file is downloaded in browser download folder
        self.assertTrue(os.path.exists(os.path.expanduser('~/Downloads/image03.png')))
        # print success message
        print(bcolors.OKGREEN + 'test case 3: compress png image - success\n\n' + bcolors.ENDC)
        # wait for 5 seconds to see the result
        time.sleep(5)

        # test case 4: compress webp image
        # find the input file
        inputElement = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')
        # send the file path
        inputElement.send_keys(os.getcwd() + '/image04.webp')
        # wait for 5 seconds to upload the image
        time.sleep(5)
        # find the compress button
        compressButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/button')
        # click the button
        compressButton.click()
        # wait for 5 seconds to compress the image
        time.sleep(5)
        # find the download button
        downloadButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div/a')
        # click the button
        downloadButton.click()
        # wait for 5 seconds to download the image
        time.sleep(5)
        # assert the file is downloaded in browser download folder
        self.assertTrue(os.path.exists(os.path.expanduser('~/Downloads/image04.webp')))
        # print success message
        print(bcolors.OKGREEN + 'test case 4: compress webp image - success\n\n' + bcolors.ENDC)
        # wait for 5 seconds to see the result
        time.sleep(5)

        # test case 5: compress bmp image
        # find the input file
        inputElement = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')
        # send the file path
        inputElement.send_keys(os.getcwd() + '/image05.bmp')
        # wait for 5 seconds to upload the image
        time.sleep(5)
        # find the compress button
        compressButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/button')
        # click the button
        compressButton.click()
        # wait for 5 seconds to compress the image
        time.sleep(5)
        # find the download button
        downloadButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div/a')
        # click the button
        downloadButton.click()
        # wait for 5 seconds to download the image
        time.sleep(5)
        # assert the file is downloaded in browser download folder
        self.assertTrue(os.path.exists(os.path.expanduser('~/Downloads/image05.bmp')))
        # print success message
        print(bcolors.OKGREEN + 'test case 5: compress bmp image - success\n\n' + bcolors.ENDC)
        # wait for 5 seconds to see the result
        time.sleep(5)

        # test case 6: compress gif image
        # find the input file
        inputElement = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')
        # send the file path
        inputElement.send_keys(os.getcwd() + '/image06.gif')
        # wait for 5 seconds to upload the image
        time.sleep(5)
        # find the compress button
        compressButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/button')
        # click the button
        compressButton.click()
        # wait for 5 seconds to compress the image
        time.sleep(5)
        # find the download button
        downloadButton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div/a')
        # click the button
        downloadButton.click()
        # wait for 5 seconds to download the image
        time.sleep(5)
        # assert the file is downloaded in browser download folder
        self.assertTrue(os.path.exists(os.path.expanduser('~/Downloads/image06.gif')))
        # print success message
        print(bcolors.OKGREEN + 'test case 6: compress gif image - success\n\n' + bcolors.ENDC)
        # wait for 5 seconds to see the result
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
