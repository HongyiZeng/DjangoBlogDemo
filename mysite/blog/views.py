from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_title(request):  # 2
    blogs = BlogArticles.objects.all()  # 3
    return render(request, "blog/titles.html", {"blogs": blogs})  # 4


def blog_article(request, article_id):
    # article = BlogArticles.object.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})
