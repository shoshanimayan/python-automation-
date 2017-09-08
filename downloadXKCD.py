# webscraper that downloads every XKCD webcomic

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # download the page
    print('downloading page %s...'% url)
    res = requests.get(url)
    res.raise_for_status()
    soup= bs4.BeautifulSoup(res.text)

    # find the url of the webcomic image
    comicElem = soup.select('#comic img')
    if comicElem==[]:
        print('image not found')
    else:
        comicUrl= 'http:'+comicElem[0].get('src')
        res = requests.get(comicUrl)
        res.raise_for_status()

    # save the image
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for i in res.iter_content(100000):
        imageFile.write(i)
    imageFile.close()
    #get next page
    prevLink = soup.select('a[re;="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('done')
