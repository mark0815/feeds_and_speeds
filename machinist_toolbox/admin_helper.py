from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
import typing as t


def changelist_link(model_class, link_title: str, filter_dict: t.Dict[str, str] = None):
    obj_content_type = ContentType.objects.get_for_model(model_class)
    obj_content_type.app_label

    url = reverse(
        f"admin:{obj_content_type.app_label}_{obj_content_type.model}_changelist"
    )
    if filter_dict:
        url = url + "?" + urlencode(filter_dict)
    return format_html('<a href="{}">{}</a>', url, link_title)
