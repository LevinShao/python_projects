import requests

print("No, I will never get off Reddit!")

name = "Levin"
print(f"Hello, {name}!")

def fetch_joke():
    response = requests.get('https://icanhazdadjoke.com/', headers = {'Accept': 'application/json'})
    joke = response.json()['joke']
    return joke

def main():
    joke = fetch_joke()
    print(f"Here's a random joke for you:")
    print(joke)

if __name__ == '__main__':
    main()