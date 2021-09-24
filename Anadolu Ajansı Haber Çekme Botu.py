import feedparser
url = "https://www.aa.com.tr/tr/rss/default?cat=guncel"
news = feedparser.parse(url)
NewsCounter = 0
for new in news.entries:
    NewsCounter += 1
    print(NewsCounter,". Haber Aşağıdadır")
    print("Haber linki:  " +new.link)
    print("Haber Başlığı: " +new.title)
    print("Haber Açıklaması:  "+new.description)
    print("-"*50, "\n")
