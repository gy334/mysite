#usr/bin/python
#-*-coding:utf-8-*-
from .forms import LoginForm

def login_modal_form(request):
    return {'login_modal_form':LoginForm()}