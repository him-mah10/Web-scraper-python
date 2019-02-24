from requests import get
from bs4 import BeautifulSoup
import csv
import os

generic1 = \
    'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_'
generic2 = '?_encoding=UTF8&pg='
j = 1
s=os.path.dirname(__file__)
r='output/com_book.csv'
file = open(os.path.join(s,r), 'w')
file.write('Name,URL,Author,Price,Number of Ratings,Average Rating\n')
for i in range(1, 6, 1):
    url = generic1 + str(i) + generic2 + str(i)
    html = get(url)
    pre = html
    html_soup = BeautifulSoup(html.text, 'html.parser')
    books_div_list = html_soup.find_all('div', class_='zg_itemImmersion'
            )
    for book in books_div_list:
        temp = book.a
        if temp == None:
            file.write('NOT AVAILABLE,')
        else:
            file.write(temp.text.strip().replace(',', ' ') + ',')

        temp = book.a['href']
        if temp == None:
            file.write('NOT AVAILABLE,')
        else:
            file.write('https://www.amazon.com' + temp + ',')

        temp = book.find('a', {'class': 'a-size-small a-link-child'})
        if temp == None:
            file.write('NOT AVAILABLE,')
        else:
            file.write(temp.text.strip().replace(',', ' ') + ',')

        temp = book.find('span', {'class': 'p13n-sc-price'})
        if temp == None:
            file.write('NOT AVAILABLE,')
        else:
            file.write(temp.text.strip().replace(',', ' ') + ',')

        temp = book.find('a', {'class': 'a-size-small a-link-normal'})
        if temp == None:
            file.write('NOT AVAILABLE,')
        else:
            file.write(temp.text.strip().replace(',', '') + ',')

        temp = book.i
        if temp == None or temp.text.strip() == 'Prime':
            file.write('NOT AVAILABLE\n')
        else:
            file.write(temp.text.strip().replace(',', ' ') + '\n')
