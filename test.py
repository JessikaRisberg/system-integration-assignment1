import requests
from requests.exceptions import HTTPError


def get_response_example():
    response = requests.get('https://api.github.com/helloworld')

    print(response.status_code)

    if response.status_code == 200:
        print("success!")
    if response.status_code == 404:
        print("Not found!")

    if response.status_code:
        print("Success!")
    else:
        print("Error!")


def bool_values():


    class MyClass:
        def __init__(self, value: int = 0):
            self.value = value

        def __bool__(self):
            return self.value != 0


    m = MyClass(5)
    print(m.value)

    if m.value:
        print("Value is set")
    else:
        print("Value is not set")


def request_exceptions():
    try:
        response = requests.get('https://api.github.com/')

        # om response var "successful", gör inget. Annars raise exception
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'Success! {response.status_code}')
        data = response.json() # avkoda dokumentet som JSON. sparas som python dict


def request_with_params_and_haeaders():
    response = requests.get('https://api.github.com/search/repositories',
                            params={'q': 'requests+language:python'},
                            header={'Accept': 'application/vnd.github.v3.match-text+json'})

    data = response.json()
    first_hit = data['items'][0]
    print(first_hit['name'])
    print(first_hit['description'])


def request_with_other_methods():
    response = requests.head('https://httpbin.org/get')
    print(response.headers['Content-Type'])
    print(response.text)

    response = requests.delete('https://httpbin.org/delete')
    print(response.status_code)
    print(response.text)

    response = requests.post('https://httpbin.org/post', data={'key': 'value'})
    # application/x-www-form-urlencoded
    print(response.status_code)

    # inspektera hur vår fråga såg ut
    print(response.request.url)


request = requests.get('http://httpbin.org/basic-auth/kyhtest/abcde', auth=('kyhtest', 'abcde'))
print('Response code', request.status_code)
print('Response content: \n', request.text)