from httplib2 import Http
from json import dumps

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    url = '<URL-PROVIDED-BY-GOOGLE-CHAT>'
    bot_message = {
        'text' : 'Free book, from Packtpub: https://www.packtpub.com/packt/offers/free-learning'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
