import requests
import html2text
import os


class BlogPoster:
    def __init__(self):
        """
        Initialize the DevToPoster with the API key.
        """
        self.api_key = os.getenv("BLOG_API_KEY")
        if not self.api_key:
            raise ValueError("Blog API key is missing! Ensure it is set in the environment variables.")
        self.headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key
        }
        self.api_url = "https://dev.to/api/articles"

    @staticmethod
    def html_to_markdown(html_content):
        """
        Convert HTML content to Markdown.
        """
        converter = html2text.HTML2Text()
        converter.ignore_links = False
        return converter.handle(html_content)

    def post_article(self, title, html_content, published=True, canonical_url=None):
        """
        Post an article to Dev.to.
        """
        # Convert HTML to Markdown
        markdown_content = self.html_to_markdown(html_content)

        # Prepare the article data
        article_data = {
            "article": {
                "title": title,
                "published": published,
                "body_markdown": markdown_content,
                "tags": []
            }
        }

        # Add canonical URL if provided
        if canonical_url:
            article_data["article"]["canonical_url"] = canonical_url

        # Send the POST request
        response = requests.post(self.api_url, headers=self.headers, json=article_data)

        # Handle the response
        if response.status_code != 201:
            print("❌ Failed to post article")
            print("Error:", response.json())
            return None