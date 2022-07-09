import pytest
import time
from selenium import webdriver
def test_01():
        driver=webdriver.Chrome()  #打开浏览器
        driver.implicitly_wait(10) #driver.implicitly_wait(10)
        driver.maximize_window()  #以全屏打开浏览器
        driver.get("https://opensea.io/assets/matic/0xecc82095b2e23605cd95552d90216faa87606c40/3305") #打开opensea的链接
        time.sleep(2) #等待2秒
        driver.find_elements_by_xpath('//button[@class="sc-1xf18x6-0 sc-glfma3-0 hiIVBZ gyCmAw sc-1skvztv-0 fPnOUC"]')[0].click() #以xpath的方法来定位这个元素
        time.sleep(3) #等待3秒
        text=driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]').text  #以xpath的方法来定位这个元素
        print(text) #输出这个元素的文案
        assert "We queued the item for an update" in text  #判断这个文案是否在这个元素的文案里面
# We've queued this item for an update! Check back in a minute...
if __name__=="__main__":
    pytest.main(['-v','-s'])  #运行脚本