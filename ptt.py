import requests
from lxml import etree

f= open("result.txt","w+",encoding='utf-8')
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
username = input("Input a user name:")
print("Wait for a sec...")
for p in range (0, 10):
    res = requests.get("https://www.pttweb.cc/user/" + username + "?t=message&page=" + str(p))
    content = res.content.decode()
    html = etree.HTML(content)

    for i in range(4,14):
        name = html.xpath('//*[@id="app"]/div/main/div/div/div/div/div/div[3]/div[' +str(i) + ']/a/span/text()')[0]
        board = html.xpath('//*[@id="app"]/div/main/div/div/div/div/div/div[3]/div[' +str(i) + ']/div[1]/a/span/text()')[0]
        floor = html.xpath('//*[@id="app"]/div/main/div/div/div/div/div/div[3]/div[' +str(i) + ']/div[2]/div/span[1]/text()')[0]
        responde = html.xpath('//*[@id="app"]/div/main/div/div/div/div/div/div[3]/div[' +str(i) + ']/div[2]/div/span[2]/span/text()')[0]
        commento = html.xpath('//*[@id="app"]/div/main/div/div/div/div/div/div[3]/div[' +str(i) + ']/div[2]/div/span[3]/span[2]/text()')[0]
        time = html.xpath('//*[@id="app"]/div/main/div/div/div/div/div/div[3]/div[' +str(i) + ']/div[2]/div/span[5]/text()')[0]
        f.write(name+'\n')
        f.write(board+'\n')
        f.write(floor+'樓 '+ responde + ' ' +commento+'\n')
        f.write(time+'\n')
        f.write("============================\n")

f.close()
print("Open result.txt and find the surprise!")

