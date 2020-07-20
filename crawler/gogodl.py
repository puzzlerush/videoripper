from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ep_links_xpath = "//a[.//span[contains(text(), 'EP')]]"
mp4upload_link_xpath = "//li[@class='mp4']//a"
mp4upload_download_xpath = "//button[@data-plyr='download']"

class GogoanimeDownloader():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        
    def get_ep_links(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, ep_links_xpath)))
        ep_links_elements = self.driver.find_elements_by_xpath(ep_links_xpath)
        ep_links = []
        for elem in ep_links_elements:
            ep_links.append(elem.get_attribute("href"))
        ep_links.reverse()
        return ep_links

    def get_raw_video_link_mp4(self, ep_link):
        self.driver.get(ep_link)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, mp4upload_link_xpath)))
        mp4_btn = self.driver.find_element_by_xpath(mp4upload_link_xpath)
        video_link = mp4_btn.get_attribute("data-video")
        self.driver.get(video_link)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, mp4upload_download_xpath)))
        dl_btn = self.driver.find_element_by_xpath(mp4upload_download_xpath)
        return dl_btn.get_attribute("href")
        
    
    def dl_videos(self, ep_links):
        for ep_link in ep_links:
            self.driver.get(self.get_raw_video_link_mp4(ep_link))

    def stop(self):
        self.driver.quit()
