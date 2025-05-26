from textwrap import dedent
import urllib.parse

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
linkedin_share = "https://www.linkedin.com/sharing/share-offsite/"

def on_page_markdown(markdown, **kwargs):
    page = kwargs.get("page")
    config = kwargs["config"]
    if page.meta.get("template") != "post.html":
        return markdown
    
    page_url = config.site_url + page.url
    page_title = urllib.parse.quote(page.title+"\n")

    return markdown + dedent(f"""
    <div style="text-align: center; markdown = "1">
    <h2 style="font-weight:bold; text-decoration:underline;">Share this post</h2>
    [Share on :simple-x]({x_intent}?text={page_title}{page_url}) |
    [Share on :simple-facebook]({fb_sharer}?u={page_url}) |
    [Share on :simple-linkedin]({linkedin_share}?url={page_url})
    </div>
    """)