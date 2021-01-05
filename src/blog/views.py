from django.shortcuts import render

posts = [
    {
        'title':'التدوينة الاولى',
        'content':' نص التدوينة الاولى',
        'post_date':'15-3-2019',
        'author':'Ahmed Abouissa'
    },
    {
        'title':'التدوينة الثانية',
        'content':' نص التدوينة الثانية',
        'post_date':'15-3-2019',
        'author':'Ahmed Abouissa'
    }, 
    {
        'title':'التدوينة الثالثة',
        'content':' نص التدوينة الثالثة',
        'post_date':'15-3-2019',
        'author':'Ahmed Abouissa'
    }, 
    {
        'title':'التدوينة الرابعة',
        'content':' نص التدوينة الرابعة',
        'post_date':'15-3-2019',
        'author':'Ahmed Abouissa'
    }, 
    {
        'title':'التدوينة الخامسة',
        'content':' نص التدوينة الخامسة',
        'post_date':'15-3-2019',
        'author':'Ahmed Abouissa'
    }
]

# Create your views here.
def home(request):
    context = {
        'title':'الرئيسية',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)
