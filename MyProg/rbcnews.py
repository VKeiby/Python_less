from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.rbc.ru/')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('span', class_='main__feed__title')

results = []
# print(news)

for item in news:
    print(item.text)
    # title = item.find('span', class_='data-vr-headline').get_text(strip=True)
    # desc = item.find('span', class_='name-dop').get_text(strip=True)
    # href = item.a.get('href')
    results.append({
        'title': item
        # 'desc': desc,
        # 'href': href,
    })
# print(results)
# f = open('news.txt', 'w', encoding='utf-8')
# i = 1
# for item in results:
#     f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n')
#     i += 1
# f.close()
