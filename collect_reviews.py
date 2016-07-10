import requests
from bs4 import BeautifulSoup

def scrape_review_urls(base_url):
    summary_reviews = []
    page = 1
    url_review_pages = [12*x for x in range(0,100)]

    for review_page in url_review_pages:
        if page ==1:
            url_review = requests.get(base_url)
            soup2 = BeautifulSoup(url_review.content,'html.parser')
            page+=1
            summary_reviews.append(soup2.findAll('div', class_="genericReview_container"))

        else:
            url_review = requests.get('{}/{}'.format(base_url,review_page))
            soup2 = BeautifulSoup(url_review.content,'html.parser')
            summary_reviews.append(soup2.findAll('div', class_="genericReview_container"))
            page+=1

    return summary_reviews

def collect_read_more_url(summary_reviews):

    review_urls = set()
    for page in summary_reviews:
        for review in page:
            for link in review.findAll('a'):
                if 'review' in link['href']:
                    review_urls.add(link['href'])
                else:
                    pass
    return review_urls

def collect_review_text(read_more_url, write_to_file):

    out_file  = open(write_to_file, "wt")

    for item in read_more_url:
        temp_url = requests.get(item)
        temp_soup = BeautifulSoup(temp_url.content, 'html.parser')
        temp = temp_soup.find('div', class_='beerReview_comments')

        for review_content in temp.strings:
            try:
                out_file.write(review_content)
            except:
                pass
def main():
    sum_rev = scrape_review_urls('http://www.twobeerdudes.com/beer/review/pgn/')
    ind_rev_return = collect_read_more_url(sum_rev)
    collect_review_text(ind_rev_return, 'data/beer_reviews.txt')

if __name__ == '__main__':
    main()
