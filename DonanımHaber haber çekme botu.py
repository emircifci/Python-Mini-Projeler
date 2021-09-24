import feedparser
url = "https://www.aa.com.tr/tr/rss/default?cat=guncel"
news = feedparser.parse(url)
NewsCounter = 0
for new in news.entries:
    NewsCounter += 1
    print(NewsCounter,". Haber Aşağıdadır")
    print("Haber linki:  " +new.link)
    print("Haber Başlığı: " +new.title)
    if new.description == False or 1==1:
        print("Haber Açıklaması:  "+new.description)
    else:
        print("Açıklama yok")    
    print("-"*50, "\n")
