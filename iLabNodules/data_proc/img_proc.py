# -*- coding: utf-8 -*-

from django.http import JsonResponse
from . import load
from ..settings import BASE_DIR
import os


def load_img(request):
    res = {}
    file_name = request.GET['src']
    mhd_file = os.path.join(BASE_DIR, "data/" + str(file_name))
    if os.path.isfile(mhd_file):
        save_path = os.path.join(BASE_DIR, "index/static/image")
        cnt = load.load_img(mhd_file, save_path)
        res['max_cnt'] = cnt
        print(request.GET['src'])

    return JsonResponse(res)


def load_nodules(request):
    file_name = request.GET['src']
    mhd_file = os.path.join(BASE_DIR, "data/" + str(file_name))
    res = {}
    if file_name == "1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860.mhd":
        res = {'nodules': [
            {'x': 211, 'y': 44, 'z': 77},
            {'x': 154, 'y': 405, 'z': 117},
        ]}
    else:
        if file_name == "1.3.6.1.4.1.14519.5.2.1.6279.6001.100621383016233746780170740405.mhd":
            res = {'nodules': [
                {'x': 335, 'y': 376, 'z': 141},
                {'x': 292, 'y': 220, 'z': 251},
                {'x': 250, 'y': 379, 'z': 230},
            ]}
    return JsonResponse(res)
