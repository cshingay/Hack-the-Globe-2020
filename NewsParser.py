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
    headlines = googlenews.gettext()
    output(headlines)

def output(headlines):
    # parse through headlines and insert them into a new file
    pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    f = open("topnews.txt", "w+")
    
    for i in range(len(headlines)):
        temp_string = ''
        for char in headlines[i]:
            if char not in pun:
                temp_string = temp_string + char
        
        headlines[i] = temp_string
        line = headlines[i].split()
        for word in line:
            f.write(word + "\t")
        f.write("\n")

    f.close()


if __name__=="__main__":
    main()

