from django.shortcuts import render
from .models import Blog,Blog_Category
from django.core.paginator import Paginator
from comments.models import Weblog_Comments
from django.http import JsonResponse

# Create your views here.


#* WEBLOG VIEW

def Weblog(request):
    blogs = Blog.objects.all().order_by('-id')
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'blogs':page_obj,'page_obj': page_obj}

    return render(request,'weblog.html',context)

#* WEBLOG VIEW

#* WEBLOG CATEGORY VIEW

def Weblog_Category(request,cat):
    category = Blog_Category.objects.filter(en_name = cat).first()

    if category is None:
        raise IndexError('not find')
    
    blogs = Blog.objects.filter(category = category).order_by('-id')
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'blogs':page_obj,'page_obj': page_obj,'category':category}

    return render(request,'weblog_category.html',context)

#* WEBLOG CATEGORY VIEW

#* WEBLOG DETAIL VIEW

def Detail_Weblog(request,pk,slug):
    blogs = Blog.objects.all().order_by('-id')
    categorys = Blog_Category.objects.all()
    info = Blog.objects.filter(id = pk,slug = slug).first()
    comments = Weblog_Comments.objects.filter(weblog = info)
    if info is None:
        raise IndexError('not find')

    context = {'info':info,'categorys':categorys,'blogs':blogs,'comments':comments}
    
    #! NEW COMMENT

    if request.POST.get("comment"):
        if request.user.is_authenticated:
            comment = request.POST.get('comment')
            new_comment = Weblog_Comments.objects.create(
                user = request.user,
                weblog =  info,
                comment = comment
            )
            new_comment.save()
            data = {
                'success':'ok'
            }
            print('success')

            return JsonResponse(data)

        else:
            data = {
                'error':'error'
            }
            
            return JsonResponse(data)
        
    #! NEW COMMENT

    return render(request,'detail_weblog.html',context)


#* WEBLOG DETAIL VIEW