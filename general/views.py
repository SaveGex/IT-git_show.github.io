from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from django.forms import BaseModelForm

from django.shortcuts import render, get_object_or_404

from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from typing import Any

from django.views import generic

from . import models
from . import forms

from ._func import get_direct_image_link, get_github_profile_image
class GeneralView(generic.TemplateView):
    template_name = "general/general.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        paginator = Paginator(models.Posts.objects.order_by("-published_date"), per_page=200)
        page_number = kwargs.get("page_number")
        page = paginator.get_page(page_number)

        context.update({
            'page': page,
            'page_number': page_number,
            # Добавьте дополнительные данные, если необходимо
        })

        return context



class CreateView(generic.CreateView):
    form_class = forms.Create
    template_name = "general/create.html"
    success_url = reverse_lazy("General:general", kwargs={"page_number": 1})


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mark_color = 'text-warning'
        context.update({
            'head_instruction': _("<span class='blockquote'>How it works? </span>"),
            'body_instruction': _(f"<span class='text-success blockquote'<br>In field <span class='{mark_color}'>'Name of task'</span> you have to write name of task. <br/>In field <span class='{mark_color}'>'Comment'</span> you can write description of task. <br/>In field <span class='{mark_color}'>'Sentence'</span> you have to write sentence, and words which you want will make fields for answer mark that <span class='{mark_color}'><span class='text-danger'>_</span>your word<span class='text-danger'>_</span></span> and in form it will showed as field for input. </span>"),
        })
        return context
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        Post_obj = form.save()  # Сохраняем объект

        github = get_github_profile_image(Post_obj.link)
        print(github)
        Post_obj.link_image = github
        Post_obj.save()
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print("Invalid form data:", form.data)
        print("Errors:", form.errors)  # Выводим ошибки формы

        context = self.get_context_data(form=form)
        form_data = form.data
        context.update({
            "form_data": form_data,
            "link_error": "link cannot be empty" if not form_data.get("link") else "",
            "name_error": "name cannot be empty" if not form_data.get("name") else "",
        })
        return super().form_invalid(form)


class DeleteView(generic.DeleteView):
    model = models.Posts
    success_url = reverse_lazy('General:general', kwargs = {"page_number": 1})
    template_name = 'general/general.html'

    
    def get_success_url(self) -> str:
        return self.success_url