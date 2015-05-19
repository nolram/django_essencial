__author__ = 'marlon'

import os

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join


def get_page_or_404(name):
    """Retorna o conteúdo da página como um template Django ou gera um erro 404. """
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page not found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page not found')

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page


def page(request, slug='index'):
    """
    Renderiza a página solicitada, se ela for encontrada.
    :param request:
    :param slug:
    :return:
    """
    file_name = '{}.html'.format(slug)
    page2 = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page2
    }
    return render(request, 'page.html', context)