def MakeWordList(url_article):

    import urllib.request
    from bs4 import BeautifulSoup
    import time

    url_easy=["http://www.eigo-duke.com/tango/chu1.html","http://www.eigo-duke.com/tango/chu2.html","http://www.eigo-duke.com/tango/chu3.html"]
    url_easy2="https://ejje.weblio.jp/parts-of-speech/kenej/%E4%B8%AD%E5%AD%A6_1"

    easy_words=[]
    with open("easy-words.txt","r") as f:
        for i in f:
            easy_words.append(i.rstrip("\n"))
    f.close()

    prepositions=[]
    with open("prepositions.txt","r") as f:
        for i in f:
            prepositions.append(i.rstrip("\n"))
    f.close()

    seasons=[]
    with open("seasons.txt","r") as f:
        for i in f:
            seasons.append(i.rstrip("\n"))
    f.close()

    past=[]
    with open("past.txt","r") as f:
        for i in f:
            past.append(i.rstrip("\n"))
    f.close()

    be=[]
    with open("be.txt","r") as f:
        for i in f:
            be.append(i.rstrip("\n"))
    f.close()

    theOthers=[]
    with open("theOthers.txt","r") as f:
        for i in f:
            theOthers.append(i.rstrip("\n"))
    f.close()

    # 記事のスクレイピング

    html = urllib.request.urlopen(url_article)
    soup = BeautifulSoup(html,'html.parser')
    sentense = soup.findAll('p')

    AllSentense=[]
    for i in sentense:
        AllSentense.append(i.text)

    words =[]
    for i in AllSentense:
        words.append(i.split(" "))
    AllWords=[]
    for i in words:
        AllWords = AllWords + i

    # 単語を正しい形に
    correct_new =[]
    for i in AllWords:
        i = i.lower()
        if "’" in i:
            continue
        else:
            if "," in i:
                i=i.replace(",","")
            if "." in i:
                i=i.replace(".","")
            if "?" in i:
                i=i.replace("?","")
            if "$" in i:
                continue
            if "&" in i:
                continue
            if ":" in i:
                i=i.replace(":","")
            if ";" in i:
                i=i.replace(";","")
            if "ー" in i:
                continue
            if "-" in i:
                continue
            if "–" in i:
                continue
            if "/" in i:
                continue
            if '"'in i:
                i=i.replace('"','')
            if "%" in i:
                continue
            if '“'in i:
                i=i.replace('“','')
            if "”" in i:
                i=i.replace("”","")
            if "(" in i:
                i=i.replace("(","")
            if ")" in i:
                i=i.replace(")","")
            correct_new.append(i)

    unknown=[]
    for i in correct_new:
        i =i.lower()
        i=WordNetLemmatizer().lemmatize(i,'v')
        if i in easy_words:
            continue
        elif i in prepositions:
            continue
        elif i in theOthers:
            continue
        elif i in be:
            continue
        elif i in seasons:
            continue
            elif len(i) ==1:
            continue
        elif i.isdigit()==True:
            continue
        elif i[-1]=="s":
            i = i.rstrip("s")
            if i in easy_words:
                continue
        elif i in unknown:
            continue
        else:
            unknown.append(i)


    base_url ='https://ejje.weblio.jp/content/'
    search_url=[]
    for i in unknown:
        search_url.append(base_url + i)


    meanings=[]
    sample=[]

    n=0
    with open('meaning.txt' , 'w') as f:

        for i in search_url:
            sample.append(i)

        for i in sample:
            html = urllib.request.urlopen(i)
            soup = BeautifulSoup(html, 'lxml')
            meaning = soup.find('td',class_='content-explanation')
            if meaning is None:
                n+=1
                continue
            else:
                f.write(unknown[n]+"\n"+meaning.text+"\n")
                n+=1
            time.sleep(0.2)
