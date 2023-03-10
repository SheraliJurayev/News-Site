from django.shortcuts import render , get_object_or_404 , HttpResponse
from .models import News , Category 
from .forms import ContactForm
from django.views.generic import TemplateView , ListView , UpdateView , DeleteView , CreateView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from news_project.custom_permissions import OnlyLoggedSuperUser
from django.contrib.auth.admin import User
 
# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)   
    context = {
        'news_list': news_list
    }

    return render(request , "news/news_list.html" ,context)



def news_detail(request,news):

    news_detail = get_object_or_404(News, slug = news , status=News.Status.Published)

    context = {
        'news': news_detail
    }

    return render(request, 'news/news_detail.html', context = context)


# def  homePageView(request):
#     news_list =  News.objects.all().order_by('-publish_time') [:10]
#     categories = Category.objects.all()
#     local_one = News.objects.filter(category__name = "Mahalliy").order_by('-publish_time')[:1]
#     local_news = News.objects.all().filter(category__name="Mahalliy").order_by('-publish_time')[:5]

#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         "local_one" : local_one,
#         "local_news": local_news
#     }    

#     return render(request, 'news/index.html',  context)

class HomePageView(ListView):   
    model = News
    template_name = "news/index.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data( **kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.all().order_by('-publish_time') [:5]
        context['mahalliy_xabarlar'] =News.objects.filter(category__name = "Mahalliy").order_by('-publish_time')[:5]
        context['xorij_xabarlari'] =News.objects.filter(category__name = "Xorij").order_by('-publish_time')[:5]
        context['sport_xabarlari'] =News.objects.filter(category__name = "Sport").order_by('-publish_time')[:5]
        context['texnologiya_xabarlari'] =News.objects.filter(category__name = "Texnologiya").order_by('-publish_time')[:5]

        return context



def viewPage404(request):   

    context = {
        'error_message': 'Page not found' 
        }

    return render(request, 'news/404.html' , context)

# def contactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None) 

#     if request.method == 'POST'and form.is_valid():
#         form.save()
#         return HttpResponse ("<h2> Tez orada siz bilan bog'lanamiz ! </h2>")

#     context = {
#         "form" : form
#      }

#     return render(request, 'news/contact.html' , context)  

class ContactPageView(TemplateView):

    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):

        form = ContactForm()

        context = {
            "form" : form 
        }

        return render(request, "news/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if request.method == "POST" and form.is_valid():
            form.save()

            return HttpResponse ("<h2> Tez orada siz bilan bog'lanamiz! </h2>")    

        context = {
            'form': form 
        }    

        return render (request, "news/contact.html", context)      

class LocalNewsView(ListView):
        model = News
        template_name = "news/mahalliy.html"
        context_object_name = "mahalliy_yangiliklar"

        def get_queryset(self):
            news=self.model.objects.all().filter(category__name = "Mahalliy")
            return news

class ForeignNewsView(ListView):
        model = News
        template_name = "news/xorij.html"
        context_object_name = "xorij_yangiliklari"

        def get_queryset(self):
            news=self.model.objects.all().filter(category__name = "Xorij")
            return news

class TechnologyNewsView(ListView):
        model = News
        template_name = "news/texnologiya.html"
        context_object_name = "texnologiya_yangiliklari"
        
        def get_queryset(self):
            news=self.model.objects.all().filter(category__name = "Texnologiya")
            return news

class SportNewsView(ListView):
        model = News
        template_name = "news/sport.html"
        context_object_name = "sport_yangiliklari"
        
        def get_queryset(self):
            news=self.model.objects.all().filter(category__name = "Sport")
            return news
        
class NewsUpdateView(OnlyLoggedSuperUser , UpdateView):
     model  = News 
     fields = ('title', 'body' , 'image', 'category' , 'status')
     template_name = 'crud/news_update.html'

class NewsDeleteView(OnlyLoggedSuperUser , DeleteView):
     model = News
     template_name = 'crud/news_delete.html'
     success_url = reverse_lazy('home_page')



class NewsCreateView(OnlyLoggedSuperUser , CreateView):
     model = News
     template_name = 'crud/news_create.html'
     fields = ('title','slug', 'body','image', 'category', 'status')  


def  admin_page_view(request):
     admin_users = User.objects.filter(is_superuser=True)

     context = {
          'admin_users': admin_users
          }
     return render(request, 'pages/admin_page.html', context)

