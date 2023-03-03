from django import template
from django.utils.datastructures import MultiValueDictKeyError

from menu.models import Item


register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu):
    """
    Формирует контекстный словарь для передачи в шаблон 'draw_menu.html'.

     - Если пользователь активирует какой-либо пункт меню, то в словарь
    включается вся ветка дочерних пунктов.
    """
    items = Item.objects.filter(menu__title=menu)
    item_values = items.values()
    super_parents = [item for item in item_values.filter(parent=None)]

    try:
        selected_item = items.get(id=context['request'].GET[menu])
        expanded_items_id_list = get_expanded_items_id_list(selected_item)
        for parent in super_parents:
            if parent['id'] in expanded_items_id_list:
                parent['child_items'] = get_child_items(
                    item_values, parent['id'], expanded_items_id_list
                )
        result_dict = {'items': super_parents}
    except MultiValueDictKeyError:
        result_dict = {'items': super_parents}

    result_dict['menu'] = menu
    return result_dict


def get_expanded_items_id_list(parent):
    """
    Формирует список всех развернутых пунктов меню.
    """
    expanded_items_id_list = []
    while parent:
        expanded_items_id_list.append(parent.id)
        parent = parent.parent
    return expanded_items_id_list


def get_child_items(item_values, current_parent_id, expanded_items_id_list):
    """
    Для переданного в аргументе текущего родителя рекурсивно
    формирует список дочерних элементов.
    """
    current_parent_child_list = [
        item for item in item_values.filter(parent_id=current_parent_id)
    ]
    for child in current_parent_child_list:
        if child['id'] in expanded_items_id_list:
            child['child_items'] = get_child_items(
                item_values, child['id'], expanded_items_id_list
            )
    return current_parent_child_list
