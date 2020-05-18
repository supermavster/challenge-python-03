# Resolve the problem!!
import re

def run():
    # Start coding here
    with open('encoded.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    response = re.sub(r'[^\x00-\x7F]+','', text)
    print(response)


if __name__ == '__main__':
    run()
