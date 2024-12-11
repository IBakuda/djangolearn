from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    news = Articles.objects.order_by('date')  #([:1] вывод одной записи)
    return render(request, 'news/news_home.html', {'news': news})

def create(request):

    # Обработка данных полученных из из формы
    error = ''
    if request.method == 'POST':                # метод передачи данных   (form method="post"  код из html)
        form = ArticlesForm(request.POST)       # данные полученные от пользователя, находящиеся в форме
        if form.is_valid():                     # проверка корректного заполнения данных
            form.save()                         # данные сохраняются и происходит переадресация на главную
            return redirect('news_home')
        else:
            error = 'Форма заполнена не верно'  # вывод ошибки в случае не правильного ввода данных

    #создание форма для обработки данных и занесение их в таблицу в бд
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)