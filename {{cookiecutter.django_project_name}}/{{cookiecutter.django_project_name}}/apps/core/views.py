import json

from django.views.generic import TemplateView


class VuejsView(TemplateView):
    template_name = "{{cookiecutter.vuejs_project_name}}.html"

    def get_context_data(self, **kwargs):
        context = super(VuejsView, self).get_context_data()
        context["base_url"] = self.request.build_absolute_uri("/api/v1/")
        context["example"] = json.dumps({"example": 123456})

        return context
