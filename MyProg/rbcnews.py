from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.rbc.ru/')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('span', class_='main__feed__title')
newsPlus = soup.find_all('a', class_='news-feed__item')

results = []
# print(newsPlus)

for item in newsPlus:
    # print(item)
    # currency = item.find('span', class_='news-feed__item__title').get_text(strip=True)
    title = item.find('span', class_='news-feed__item__title').get_text(strip=True)
    # desc = item.find('span', class_='news-feed__item__date-text').get_text(strip=True)
    # href = item.a.get('href')
    # print(title)
    results.append({
        'title': title,
        # 'desc': desc,
        # 'href': href,
    })
print(results)
f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'News № {i}\n {item["title"]}\n')
    # print(f'News № {i}\n {item["title"]}\nDescription: {item["desc"]}\nHREF: {item["href"]}\n')
    print(f'News № {i}\n {item["title"]}\n')
    i += 1
f.close()
