from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import MenuBarModel, AboutUsModel
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin  
class MenuBarPlugin(CMSPluginBase):
    model = MenuBarModel  
    module = _("MenuBar")
    name = _("MenuBar Plugin") 
    render_template = "menu_bar_plugin/menu_bar_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context



@plugin_pool.register_plugin  
class AboutUsPlugin(CMSPluginBase):
    model = AboutUsModel  
    module = _("AboutUs")
    name = _("AboutUs Plugin") 
    render_template = "menu_bar_plugin/about_us_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context