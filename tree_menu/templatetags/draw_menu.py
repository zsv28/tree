from django import template
from django.db.models import Prefetch
from django.urls import resolve

from tree_menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag(
    'tree_menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Renders a menu by its name.
    """
    request = context['request']
    current_url = resolve(request.path_info).url_name

    # Optimized database query to fetch all menu items
    menu = Menu.objects.prefetch_related(
        Prefetch(
            'items',
            queryset=MenuItem.objects.order_by('order')
        )
    ).get(name=menu_name)

    menu_items = {item.id: item for item in menu.items.all()}

    # Build the menu tree structure
    root_items = []
    for item in menu.items.all():
        if item.parent_id is None:
            root_items.append(item)
        else:
            parent_item = menu_items[item.parent_id]
            if not hasattr(parent_item, 'children_items'):
                parent_item.children_items = []
            parent_item.children_items.append(item)

    def mark_active_items(items):
        """
        Recursively marks the active menu item based on the current URL.
        """
        active = False
        for item in items:
            item.active = (item.get_url() == request.path)
            if item.active or mark_active_items(
                    getattr(item, 'children_items', [])):
                item.active = True
                active = True
        return active

    mark_active_items(root_items)

    return {'menu': root_items, 'request': request}
