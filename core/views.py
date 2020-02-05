from django.views.generic import ListView

from .models import Produto


class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    #Paginando com cinco elemento
    paginate_by = 5
    #essa paginação vai ser ordenada por id
    ordering = 'id'

