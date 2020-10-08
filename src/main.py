import feedparser

def update_readme_medium_posts(medium_feed, readme_base, join_on):
    d = feedparser.parse(medium_feed)
    title = f"### {d['feed']['title']}"
    posts = []
    for item in d.entries:
        if item.get('tags'):
            posts.append(f" - [{item['title']}]({item['link']})")
    posts_joined = '\n'.join(posts)
    return readme_base[:readme_base.find(rss_title)] + f"{title}\n{posts_joined}"

rss_title = "### Stories by Dylan Roy on Medium"
updated_readme = update_readme_medium_posts("https://medium.com/feed/@dylanroy", readme_base, rss_title)