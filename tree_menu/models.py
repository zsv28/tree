from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    """
    Model representing a menu.
    """
    name = models.CharField(
        max_length=100, unique=True, verbose_name=_("Menu Name"))

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Model representing an item within a menu.
    """
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items',
        verbose_name=_("Menu"))
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True,
        related_name='children', verbose_name=_("Parent Item"))
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    url = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("URL"))
    named_url = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Named URL"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Order"))

    class Meta:
        verbose_name = _("Menu Item")
        verbose_name_plural = _("Menu Items")
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_url(self):
        """
        Returns the URL for this menu item. If a named URL is provided,
        it resolves
        it to the actual URL. Otherwise, it returns the explicit URL.
        """
        if self.named_url:
            return reverse(self.named_url)
        return self.url
