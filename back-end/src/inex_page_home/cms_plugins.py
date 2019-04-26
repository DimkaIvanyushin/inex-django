from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *
from product.models import GroupProduct, Product
from solutions.models import Solutions
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site


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

        len_slider = len(instance.child_plugin_instances)
        slider_paginate = range(len_slider)
        
        instance.child_plugin_instances[0].active = "active"

        context.update({
            'instance': instance,
            'slider_paginate': slider_paginate
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
class SmallFeaturesSectionPlugin(CMSPluginBase):
    module = _("Inex Plugin")
    name = _('Small Features Section')
    render_template = 'template_plugin/small_features_section_template.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class SmallFeaturesPlugin(CMSPluginBase):
    model = SmallFeaturesModel
    module = _("Inex Plugin")
    name = _('Small Features Box')
    render_template = 'template_plugin/small_features_template.html'
    parent_classes = ['SmallFeaturesSectionPlugin']

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

@plugin_pool.register_plugin  
class ProductSectionPlugin(CMSPluginBase):
    model = ProductSectionModel
    module = _("Inex Plugin")
    name = _('Product Section Plugin')
    render_template = 'template_plugin/product_section_template.html'
 
    def render(self, context, instance, placeholder):

        groupProduct = GroupProduct.objects.all()
        context.update({'instance': instance, 'groupProduct': groupProduct})
        return context

@plugin_pool.register_plugin  
class SolutionSectionPlugin(CMSPluginBase):
    model = SolutionSectionModel
    module = _("Inex Plugin")
    name = _('Solution Section Plugin')
    render_template = 'template_plugin/solution_section_template.html'
 
    def render(self, context, instance, placeholder):

        solutions = Solutions.objects.all()
        context.update({'instance': instance, 'solutions': solutions})
        return context

@plugin_pool.register_plugin  
class PricePlugin(CMSPluginBase):
    model = PriceModel
    module = _("Inex Plugin")
    name = _('Price Plugin')
    allow_children = True
    render_template = 'template_plugin/price_template.html'
 
    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class PriceBoxPlugin(CMSPluginBase):
    model = PriceBoxModel
    module = _("Inex Plugin")
    name = _('PriceBox Plugin')
    render_template = 'template_plugin/price_box_template.html'
    parent_classes = ['PricePlugin']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class AlertMdlPlugin(CMSPluginBase):
    model = AlertMdlModel
    module = _("Inex Plugin")
    name = _('AlertMdl Plugin')
    render_template = 'template_plugin/alert_mdl_template.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class LastBlogPlugin(CMSPluginBase):
    model = LastBlogModel
    module = _("Inex Plugin")
    name = _('Last Blog Plugin')
    render_template = 'template_plugin/last_blog_template.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class ContactUsPlugin(CMSPluginBase):
    model = ContactUsModel
    module = _("Inex Plugin")
    name = _('Contact Us Plugin')
    render_template = 'template_plugin/contact_us_template.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class ContactPlugin(CMSPluginBase):
    module = _("Inex Plugin")
    name = _('Contact Plugin')
    render_template = 'template_plugin/contact_template.html'

    def render(self, context, instance, placeholder):

        item = MenuBarModel.objects.latest('cmsplugin_ptr_id')

        context.update({'instance': instance, 'item': item})
        return context

@plugin_pool.register_plugin  
class RecallPlugin(CMSPluginBase):
    model = RecallModel
    module = _("Inex Plugin")
    name = _('Recall Plugin')
    render_template = 'template_plugin/recall_template.html'
    allow_children = True

    def render(self, context, instance, placeholder):

        len_slider = len(instance.child_plugin_instances)
        slider_paginate = range(len_slider)
        instance.child_plugin_instances[0].active = "active"

        context.update({'instance': instance, 'slider_paginate': slider_paginate})
        return context

@plugin_pool.register_plugin  
class RecallPagePlugin(CMSPluginBase):
    module = _("Inex Plugin")
    name = _('Recall Page Plugin')
    render_template = 'template_plugin/recall_page_template.html'
    parent_classes = ['RecallPlugin']
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class RecallBoxPlugin(CMSPluginBase):
    model = RecallBoxModel
    module = _("Inex Plugin")
    name = _('Recall Box Plugin')
    render_template = 'template_plugin/recall_box_template.html'
    parent_classes = ['RecallPagePlugin']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin 
class FooterPlugin(CMSPluginBase):
    model = FooterModel
    module = _("Inex Plugin")
    name = _('Footer Plugin')
    render_template = 'template_plugin/footer_template.html'

    def render(self, context, instance, placeholder):
        contact = MenuBarModel.objects.latest('cmsplugin_ptr_id')
        
        context.update({'instance': instance, 'contact': contact})
        return context


@plugin_pool.register_plugin 
class NavBarPlugin(CMSPluginBase):
    module = _("Inex Plugin")
    name = _('Nav Bar Plugin')
    render_template = 'template_plugin/nav_bar_template.html'

    def render(self, context, instance, placeholder):

        groupProducts = GroupProduct.objects.all()

        # if context['request'].session.get('products', False):
        # count_product = len(context['request'].session['products'])
        # print(count_product)

        context.update({'instance': instance, 'groupProducts': groupProducts})
        return context