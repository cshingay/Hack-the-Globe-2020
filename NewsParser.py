from GoogleNews import GoogleNews
googlenews = GoogleNews()

googlenews = GoogleNews('en','d')
headlines = []

def main():
    # will get the top stories
    googlenews.search("Top News")
    googlenews.getpage(1)
    googlenews.getpage(2)
    googlenews.result()

    texts = googlenews.result()
    result(texts)

def result(texts):
    f = open("newsresults.txt", "w+")
    for i in texts:
        temp_list = []
        temp_list.append(i["title"])
        temp_list.append(i["desc"])
        f.write(str(temp_list))
        f.write("\n")
    f.close()

    

if __name__=="__main__":
    main()

