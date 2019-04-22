from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *
from inex_page_home.models import AboutUsModel, ProductSectionModel
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin  
class BreadcrumbsProductPlugin(CMSPluginBase):
    model = BreadcrumbsProductModel  
    module = _("Inex Product Plugin")
    name = _("Breadcrumbs Product Plugin") 
    render_template = "template_plugin/breadcrumbs_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class AllProductPlugin(CMSPluginBase):
    model = ProductSectionModel  
    module = _("Inex Product Plugin")
    name = _("All Product Plugin") 
    render_template = "template_plugin/all_product_template.html"

    def render(self, context, instance, placeholder):
        group_products = GroupProduct.objects.all()

        context.update({'instance': instance, 'group_products': group_products})
        return context

@plugin_pool.register_plugin  
class AboutUsRevercePlugin(CMSPluginBase):
    model = AboutUsModel  
    module = _("Inex Product Plugin")
    name = _("AboutUsReverce Plugin") 
    render_template = "template_plugin/about_usreverce_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class ProductFullPlugin(CMSPluginBase):
    model = ProductSectionModel  
    module = _("Inex Product Plugin")
    name = _("Product Full Plugin") 
    render_template = "template_plugin/product_full_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class AboutUsImgPlugin(CMSPluginBase):
    model = AboutUsImgModel  
    module = _("Inex Product Plugin")
    name = _("About Us Img Plugin") 
    render_template = "template_plugin/about_usimg_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class ThProductPlugin(CMSPluginBase):
    model = ThProductModel  
    module = _("Inex Product Plugin")
    name = _("Th Product Plugin") 
    render_template = "template_plugin/th_product_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  
class DescProductPlugin(CMSPluginBase):
    model = DescProductModel  
    module = _("Inex Product Plugin")
    name = _("Description Product Plugin") 
    render_template = "template_plugin/desc_product_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context