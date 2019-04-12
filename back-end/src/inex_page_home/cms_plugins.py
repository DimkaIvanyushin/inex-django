from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin  
class MenuBarPlugin(CMSPluginBase):
    model = MenuBarModel  
    module = _("Inex Plugin")
    name = _("MenuBar Plugin") 
    render_template = "template_plugin/menu_bar_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin  
class AboutUsPlugin(CMSPluginBase):
    model = AboutUsModel  
    module = _("Inex Plugin")
    name = _("AboutUs Plugin") 
    render_template = "template_plugin/about_us_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin  
class SliderPlugin(CMSPluginBase):
    model = SliderModel  
    module = _("Inex Plugin")
    name = _("Slider Plugin") 
    render_template = "template_plugin/slider_template.html"
    allow_children = True

    def render(self, context, instance, placeholder):

        slides_count = SliderItem.objects.all().count()

        context.update({
            'instance': instance,
            'slides_count': range(slides_count)
            })
           
        return context


@plugin_pool.register_plugin  
class SliderItemPlugin(CMSPluginBase):
    model = SliderItem
    module = _("Inex Plugin")
    name = _('Slide')
    render_template = 'template_plugin/slide_template.html'
    parent_classes = ['SliderPlugin']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class SmallFeaturesPlugin(CMSPluginBase):
    model = SmallFeaturesModel
    module = _("Inex Plugin")
    name = _('SmallFeatures')
    render_template = 'template_plugin/smallFeatures_template.html'
 
    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class AlertCtaPlugin(CMSPluginBase):
    model = AlertCtaModel
    module = _("Inex Plugin")
    name = _('Alert Cta Plugin')
    render_template = 'template_plugin/alert_cta_template.html'
 
    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context