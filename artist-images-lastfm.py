import bs4 as bs
import urllib.request
import sys
import multiprocessing.dummy as mp 
import os


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()



try:
    input_url = sys.argv[1]
except:
    input_url = input('url? ')

source = urllib.request.urlopen(input_url).read()
soup = bs.BeautifulSoup(source, 'lxml')

artist = soup.find("h1", {"class": "header-new-title"}).text
print("Artist: " + artist)

links_to_process = []
try:
    number_of_pages = soup.find("ul", {"class": "pagination-list"}).findAll("li")
    number_of_pages = int(number_of_pages[-2].text)
    for i in range(number_of_pages):
        links_to_process.append(input_url + '?page=' + str(i+1))
except:
    links_to_process.append(input_url)



img_urls = []
def get_img_urls(link):
    global img_urls
    source = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    image_list = soup.findAll('a', { 'class': 'image-list-item'})
    for a in image_list:
        img_urls.append('https://www.last.fm' + a['href'])

p=mp.Pool(20)
p.map(get_img_urls, links_to_process)
p.close()
p.join()



try:
    # resume from specific number in argv pos 2
    resume_number = int(sys.argv[2])
    img_urls = img_urls[resume_number:]
except:
    pass

l = len(img_urls)
print(f'Found {str(l)} images to download')
processed = 0
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

download_folder = os.path.join(os.getcwd(), artist)

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

def updateProgress():
    global processed 
    processed += 1
    printProgressBar(processed, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


def download_img(url):
    url = urllib.request.urlopen(url)
    soup2 = bs.BeautifulSoup(url, 'lxml')
    img_url = soup2.findAll('img', { 'class': 'js-gallery-image' })[0]['src']
    img_url = img_url.replace('/770x0','')
    img_url = img_url.split('#', 1)[0]

    # this is to get the real extension. Last.fm will get you a .jpg
    # link but it will redirect you to the correct url afterwards
    # could be a .gif. We want to preserve that
    try:
        img_url = urllib.request.urlopen(img_url).geturl()
    except:
        # print(f'error with {img_url}')
        updateProgress()
        
    # replacing jpg with webp files
    img_url = img_url.replace('jpg', 'webp')
    
    # https://lastfm.freetls.fastly.net/i/u/2bd061bfb76176d1d8c3f52cbb73350e.webp
    filename = img_url.split('i/u/', 1)[1]
    # 2bd061bfb76176d1d8c3f52cbb73350e.webp"
    filename, extension = filename.split('.', 1)
    # 2bd061bfb76176d1d8c3f52cbb73350e, webp

    artist_ = artist.replace(' ', '_')
    filename = artist_.lower() + '_'+ filename[0:10] + '.' + extension

    fullfilename = os.path.join(download_folder, filename)
    try:
        urllib.request.urlretrieve(img_url, fullfilename)
    except:
        # print(f'error with {img_url}')
        pass
    
    updateProgress()



p=mp.Pool(100) # wicked fast
# p=mp.Pool(12) # cpu/network easy
p.map(download_img, img_urls)
p.close()
p.join()



