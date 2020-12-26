import urllib
import re
import sys
from BeautifulSoup import BeautifulSoup

# define a scrape_posts method to separate each post within a given webpage
def scrape_posts(output):
    output = output.split('&raquo;')
    output = output[1].split('ReplyQuick')
    delimiters = 'QuoteSelect PostDeselect PostLink to PostMemberGive GiftBack to TopPost', 'GMT -5', 'QuoteSelect PostDeselect PostLink to PostBack to TopPost', 'via mobile'
    pattern = '|'.join(delimiters)
    output = re.split(pattern, output[0])

    p = (len(output)/3-1)

    post_output = []
    
    months = ['onjan', 'onfeb', 'onmar', 'onapr', 'onmay', 'onjun', 
          'onjul', 'onaug', 'onsept', 'onoct', 'onnov', 'ondec', 
          'onJan', 'onFeb', 'onMar', 'onApr', 'onMay', 'onJun', 
          'onJul', 'onAug', 'onSept', 'onOct', 'onNov', 'onDec']
    
    for item in output:
        title = False
        for m in months:
            if m in item:
                title = True
        if not (title or item == '' or item == '\n'):
            post_output.append(item)
    
    return post_output, p

# for each thread on the Colic Support website, scrape each post (and if there are 
# multiple pages dedicated to one thread, scrape each post from each of those pages)
# at each step in the loop, display the total number of posts and threads so far for
# debugging purposes (and if the current thread does not exist, display 'No thread')

posts = 0
threads = 0
docs = []
for i in xrange(500, 1221):
    url = 'http://colicsupport.proboards.com/thread/' + str(i+1)
    page = urllib.urlopen(url)

    # separate a thread by post
    soup = BeautifulSoup(page.read())
    soup.prettify()
    output = soup.getText()
    if 'Oops, there was an error!' in output:
        print "Page: " + str(i+1) + ', No Thread'
        continue

    threads += 1
    output, p = scrape_posts(output)
    posts += p
    for item in output:
        docs.append(item.encode('utf-8')+'\n')

    j = 2
    while True:
        soup2 = BeautifulSoup(urllib.urlopen(url+"?page=" + str(j)).read())
        soup2.prettify()
        output2, p = scrape_posts(soup2.getText())
        if output == output2:
            break
        else:
            for item in output2:
                docs.append(item.encode('utf-8') + '\n')
            posts += p
        output = output2
        j += 1

    print "Page: " + str(i+1) + ', Total Posts:', str(posts) + ', Total Threads: ' + str(threads)

print docs

# to see all scraped posts, see src/colic_scrape.txt and to see url's mentioned, see src/colic_urls.txt


