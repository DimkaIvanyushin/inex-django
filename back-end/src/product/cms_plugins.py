from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *
from inex_page_home.models import AboutUsModel
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin  
class AboutUsRevercePlugin(CMSPluginBase):
    model = AboutUsModel  
    module = _("Inex Plugin")
    name = _("AboutUsReverce Plugin") 
    render_template = "template_plugin/about_us_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
