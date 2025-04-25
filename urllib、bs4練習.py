from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

# res = request.urlopen(url)

# print('res.read():', res.read())

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}
req = request.Request(url = url, headers = headers)

#取得回應(打開req)
res = request.urlopen(req)

# 使用decode將bytes轉為字串
# print(res.read().decode('utf8'))

# 用html.parser把res轉成BeautifulSoup的物件
soup = BeautifulSoup(res, 'html.parser')

# action_bar = soup.findAll('div', {'id' : 'action-bar-container'})
action_bar = soup.findAll('div', id='action-bar-container')
print(action_bar)
print()

tmp_div = action_bar[0].find('div')
print('Other <div> :')
print(tmp_div)
print()

tmp_a = action_bar[0].find('a')
print('Other <a> :')
print(tmp_a)
print()

# .text 會取出這個標籤裡的文字內容
tmp_text_in_a = tmp_a.text
print('Text in <a> tag :')
print(tmp_text_in_a)
print()

# .string 也會取出這個標籤裡的文字內容
tmp_text_in_a = tmp_a.string
print('Text in <a> tag :')
print(tmp_text_in_a)
print()

tmp_url = tmp_a['href']
print('URL :')
print(tmp_url)
print()
# 手動寫網址前面的部分並組合他們
print('https://www.ptt.cc'+tmp_url)


