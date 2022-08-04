from bs4 import BeautifulSoup
import requests
url=("https://www.amazon.in/s?k=iphone+13&sprefix=ip%2Caps%2C224&ref=nb_sb_ss_ts-doa-p_1_2")
data = requests.get(url).text
data2 = BeautifulSoup(data,"lxml") #parcer
# print(data)

# print(data2.prettify)
# for div_tag in data2.find_all("div",{"class":"s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16"}):
for div_tag in data2.find_all("span",{"class":"a-size-medium a-color-base a-text-normal"}):
        print(div_tag)
        for div_2 in data2.find_all("span",{"class":"a-price-whole"}):
            print(div_2.text)
# print(x)