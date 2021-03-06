'''  Retrieve and print words from a URL

Usage:
     Python3 words.py <URL>
'''
import sys
from urllib.request import urlopen

def fetch_words(url):
    ''' Fetch a string of words from a URL.
        
        Args:
            url: The URL of a UTF-8 text document.

        Returns:
            A list of strings containing the words from the document.
    '''
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_items(items):
    ''' Prints items one per line.

    Args:
        An iterable or mutable series of printable items.
    '''
    for item in items:
        print (item)
    if isinstance(items, str):
        print (items.split())

def main(url):
    ''' Prints each word from a text document

    Args:
        url: The URL of a UTF-8 text document
    '''
    words = fetch_words(url)
    print_items(words)

if __name__ == "__main__":
    main(sys.argv[1]) 