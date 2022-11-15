
def speak_print(user):
    from win32com.client import Dispatch
    speaker = Dispatch('SAPI.spvoice')
    print(user)
    speaker.Speak(user)

def requesting(country):
    import requests
    import json

    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=6241fb2102eb48d49cb3e1c9406a6155'
    News = requests.get(url=url)
    print(News.text)                # Over here its in javascript format
    parse = json.loads(News.text)
    title_desc = [i for i in enumerate(parse['articles'])]

    for count,i in enumerate(title_desc, start=1):

        news = list(i)[1]       # Makes a list / converting from tuple for ease of access
        speak_print(f'\nNews{count}')
        for key in news:
            if key == 'title':
                speak_print(news['title'])          # These searches for the title in the dictionary else it
            elif key == 'url':           # Searches for the url
                print(news['url'])
        if count >= 10:
            break


if __name__ == '__main__':
    requesting('au')

