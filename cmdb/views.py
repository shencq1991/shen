from django.shortcuts import render
from django.http import HttpResponse
from cmdb.models import Post
from cmdb.models import Echarts
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
import json

# Create your views here.

def index(request):
    return render(request,"index.html",)

def base(request):
    return render(request,"base.html",)


def content(request,pk):
    content = get_object_or_404(Post, pk=pk)
    # 展示的是第PK条数据（一条记录）
    # content.body = markdown.markdown(content.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    # data = get_object_or_404(Echarts,pk=pk)

    return render(request,"content.html",{'content':content
                                          })


def ie(request):
    return render(request,"ie.html",)




def web_1(request):

    return render(request,"web_1.html",)




def web_blog(request):
    limit = 8
    post = Post.objects.all().order_by('code')
    p = Paginator(post,limit)
    page = request.GET.get('page')
    try:
        contents = p.page(page)
    except PageNotAnInteger:
        contents = p.page(1)
    except EmptyPage:
        contents = p.page(paginator.num_pages)

    return render(request,"web_blog.html",{'contents':contents})


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'web1.html',{'error_msg': error_msg})
    try:
        content = get_object_or_404(Post, code=q)
    except:
        content = get_object_or_404(Post, name=q)
    return render(request, 'content.html', {'error_msg': error_msg,
                                               'content': content})


