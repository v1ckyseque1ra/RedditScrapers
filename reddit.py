import praw

# Replace these with your actual credentials
reddit_client_id = 'pXtqtGWntXaqdOra0-mFeg'
reddit_client_secret = 'DVNG7SKt8LjPZTqMPEvuej_tpZBoGw'
reddit_user_agent = 'DataScrapingEurope'  # This can be any descriptive name

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=reddit_user_agent
)

def scrape_reddit(subreddit_name, num_posts=10):
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.top(limit=num_posts)

    for post in top_posts:
        print(f'Title: {post.title}')
        print(f'Author: {post.author}')
        print(f'URL: {post.url}')
        print(f'Score: {post.score}')
        print(f'Number of comments: {post.num_comments}')
        print('-' * 50)

# Example usage
your_reddit=input("insert your reddit ")
scrape_reddit(your_reddit, num_posts=5)  # Replace 'your_reddit' with the desired subreddit name
