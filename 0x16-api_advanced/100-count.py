#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests

# Constants
REDDIT_API_BASE_URL = 'https://www.reddit.com'
API_HEADERS = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
}
DEFAULT_SORT = 'hot'
DEFAULT_LIMIT = 30

def sort_histogram(histogram):
    '''Sorts and prints the given histogram.
    '''
    # Filter out items with count 0
    histogram = [(word, count) for word, count in histogram if count > 0]
    
    # Create a dictionary to aggregate counts
    histogram_dict = {}
    for item in histogram:
        word, count = item
        if word in histogram_dict:
            histogram_dict[word] += count
        else:
            histogram_dict[word] = count
    
    # Sort the histogram first by count (in descending order) and then alphabetically by word
    sorted_histogram = sorted(histogram_dict.items(), key=lambda kv: (-kv[1], kv[0].lower()))
    
    # Print the sorted histogram
    for word, count in sorted_histogram:
        print(f"{word.lower()}: {count}")

def count_words(subreddit, word_list, histogram=None, n=0, after=None):
    '''Counts the number of times each word in a given wordlist
    occurs in a given subreddit.
    '''
    if histogram is None:
        # Initialize histogram with word_list
        word_list = [word.lower() for word in word_list]
        histogram = [(word, 0) for word in word_list]
    
    # Make an API request
    res = requests.get(
        f'{REDDIT_API_BASE_URL}/r/{subreddit}/.json',
        params={
            'sort': DEFAULT_SORT,
            'limit': DEFAULT_LIMIT,
            'count': n,
            'after': after or ''
        },
        headers=API_HEADERS,
        allow_redirects=False
    )
    
    if res.status_code == 200:
        data = res.json()['data']
        posts = data.get('children', [])
        titles = [post['data']['title'].lower() for post in posts]
        
        # Update the histogram with word counts
        for i, (word, count) in enumerate(histogram):
            word_count = sum(title.split().count(word) for title in titles)
            histogram[i] = (word, count + word_count)
        
        if len(posts) >= DEFAULT_LIMIT and data.get('after'):
            # Recursively fetch more posts
            count_words(subreddit, word_list, histogram, n + len(posts), data['after'])
        else:
            # Sort and print the histogram when done
            sort_histogram(histogram)
    else:
        # Handle API request error
        print(f"Error: {res.status_code}")

if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    word_list = input("Enter keywords (space-separated): ").split()
    count_words(subreddit, word_list)
	else: 
		return
#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests

# Constants
REDDIT_API_BASE_URL = 'https://www.reddit.com'
API_HEADERS = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
}
DEFAULT_SORT = 'hot'
DEFAULT_LIMIT = 30

def sort_histogram(histogram):
    '''Sorts and prints the given histogram.
    '''
    # Filter out items with count 0
    histogram = [(word, count) for word, count in histogram if count > 0]
    
    # Create a dictionary to aggregate counts
    histogram_dict = {}
    for item in histogram:
        word, count = item
        if word in histogram_dict:
            histogram_dict[word] += count
        else:
            histogram_dict[word] = count
    
    # Sort the histogram first by count (in descending order) and then alphabetically by word
    sorted_histogram = sorted(histogram_dict.items(), key=lambda kv: (-kv[1], kv[0].lower()))
    
    # Print the sorted histogram
    for word, count in sorted_histogram:
        print(f"{word.lower()}: {count}")

def count_words(subreddit, word_list, histogram=None, n=0, after=None):
    '''Counts the number of times each word in a given wordlist
    occurs in a given subreddit.
    '''
    if histogram is None:
        # Initialize histogram with word_list
        word_list = [word.lower() for word in word_list]
        histogram = [(word, 0) for word in word_list]
    
    # Make an API request
    res = requests.get(
        f'{REDDIT_API_BASE_URL}/r/{subreddit}/.json',
        params={
            'sort': DEFAULT_SORT,
            'limit': DEFAULT_LIMIT,
            'count': n,
            'after': after or ''
        },
        headers=API_HEADERS,
        allow_redirects=False
    )
    
    if res.status_code == 200:
        data = res.json()['data']
        posts = data.get('children', [])
        titles = [post['data']['title'].lower() for post in posts]
        
        # Update the histogram with word counts
        for i, (word, count) in enumerate(histogram):
            word_count = sum(title.split().count(word) for title in titles)
            histogram[i] = (word, count + word_count)
        
        if len(posts) >= DEFAULT_LIMIT and data.get('after'):
            # Recursively fetch more posts
            count_words(subreddit, word_list, histogram, n + len(posts), data['after'])
        else:
            # Sort and print the histogram when done
            sort_histogram(histogram)
    else:
        # Handle API request error
        print(f"Error: {res.status_code}")

if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    word_list = input("Enter keywords (space-separated): ").split()
    count_words(subreddit, word_list)
