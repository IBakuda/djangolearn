from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

class NewsDetailsView(DetailView): #динамическая страница для просмотра новостей
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUptadeView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete_news.html'
    success_url = '/news/'


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