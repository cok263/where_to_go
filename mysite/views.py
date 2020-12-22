from django.http import HttpResponse
from django.template import loader


def show_where_to_go(request):
    template = loader.get_template('product_page.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
