from bs4 import BeautifulSoup
import scraperwiki, time
html = scraperwiki.scrape("http://slon.ru")
soup = BeautifulSoup(html, 'lxml')

number = soup.find("span", attrs={"class": "join-us-button__number"})
users=int(number.text.replace(" ", ""))

date=time.strftime("%D")
scraperwiki.sqlite.save(unique_keys=['date'], data={"date": date, "users": users})
print("Today total number of paying users: " + str(users))
