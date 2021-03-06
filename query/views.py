from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from query.forms import QueryBasicForm
from query.models import Post


class AboutView(TemplateView):
    template_name = 'query/about.html'

    def get(self, request):
        args = {'nbar': 'about'}
        return render(request, self.template_name, args)


class IndexView(TemplateView):
    template_name = 'query/index.html'

    def get(self, request):
        args = {'nbar': 'index'}
        return render(request, self.template_name, args)


class QueryView(TemplateView):
    template_name = 'query/query.html'

    def get(self, request):
        form = QueryBasicForm()
        posts = Post.objects.all().order_by('-created_date')
        args = {'form': form, 'posts': posts, 'nbar': 'query'}
        return render(request, self.template_name, args)

    def post(self, request):
        form = QueryBasicForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('query:query')
        else:
            form = QueryBasicForm()
            args = {'form': form, 'nbar': 'query'}
            return render(request, self.template_name, args)




