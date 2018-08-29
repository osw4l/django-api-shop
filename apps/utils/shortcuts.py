import datetime
from django.shortcuts import _get_queryset


def get_object_or_none(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except:
        return None


def get_list_or_none(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    obj_list = list(queryset.filter(*args, **kwargs))
    if not obj_list:
        return None
    return obj_list


def generate_code(klass):
    out = 0
    items = klass.objects.all().count() + 1
    if items < 10:
        out = '000{0}'.format(items)
    elif 10 >= items < 100:
        out = '00{0}'.format(items)
    elif 100 >= items < 1000:
        out = '0{0}'.format(items)
    elif items >= 1000:
        out = '{0}'.format(items)
    data = out
    object_ = get_object_or_none(klass, codigo=data)
    if object_ is None:
        return data
    else:
        generate_code(klass)
