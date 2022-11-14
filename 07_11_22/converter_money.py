import requests
from bs4 import BeautifulSoup as BS

def get_exchange_rate(url, headers):
    r = requests.get(url, headers=headers)
    soup = BS(r.content, 'html.parser')
    data = soup.find('span', class_='DFlfde SwHCTb')
    rate = float(data['data-value'])
    return rate

def main():
    while True:
        user_choice = input('1.EUR to GBP\n2.GBP to EUR\n0.Exit')
        if user_choice == '1':
            amount = float(input('Please enter amount: '))
            print(get_exchange_rate(eur_gbp, headers) * amount)
        elif user_choice == '2':
            amount = float(input('Please enter amount: '))
            print(amount / get_exchange_rate(eur_gbp, headers))
        elif user_choice == '0':
            break
        else:
            print('Choice is out of range!')

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
eur_gbp = 'https://www.google.ru/search?q=eur+gbp&newwindow=1&source=hp&ei=rxlyY7GqG86Fxc8P6f28qA8&iflsig=AJiK0e8AAAAAY3Inv8Z_omCRKz1ZmbvfzdhYyyLTepcF&ved=0ahUKEwjxvbXDvK37AhXOQvEDHek-D_UQ4dUDCAg&uact=5&oq=eur+gbp&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoOCC4QgAQQsQMQxwEQ0QM6CAgAELEDEIMBOggIABCABBCxAzoUCC4QgAQQsQMQgwEQxwEQ0QMQ1AI6CwguEIAEEMcBEK8BOhEILhCABBCxAxCDARDHARCvAToHCAAQgAQQClAAWOsVYIQYaABwAHgAgAHqAYgBmgWSAQU2LjAuMZgBAKABAQ&sclient=gws-wiz'
main()

