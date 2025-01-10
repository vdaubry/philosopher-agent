from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from automating_content_creation_for_enhanced_efficiency.blog_poster import BlogPoster

class BlogPostToolInput(BaseModel):
    title: str = Field(..., description="Title of the blog post.")
    html_content: str = Field(..., description="HTML content of the blog post.")

class BlogTool(BaseTool):
    name: str = "blog_poster_tool"
    description: str = ("A tool to post a blog article with a title and HTML content.")
    args_schema: Type[BaseModel] = BlogPostToolInput

    def _run(self, title: str, html_content: str) -> str:
        blog_poster = BlogPoster()
        blog_poster.post_article(title, html_content)

        return f"\nBlog Article successfully posted"

