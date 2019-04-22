from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Solutions, SolutionsPluginModel, BreadcrumbsSolution
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin  
class SolutionsGridPlugin(CMSPluginBase):
    model = SolutionsPluginModel  
    module = _("Inex Solution Plugin")
    name = _("Solutions Plugin") 
    render_template = "plugin/solution_template.html"

    def render(self, context, instance, placeholder):

        solutions = Solutions.objects.all()
        context.update({'instance': instance, 'solutions': solutions})
        return context

@plugin_pool.register_plugin  
class BreadcrumbsSolPlugin(CMSPluginBase):
    model = BreadcrumbsSolution  
    module = _("Inex Solution Plugin")
    name = _("Breadcrumbs Solutions Plugin") 
    render_template = "plugin/breadcrumbs_sol_template.html"

    def render(self, context, instance, placeholder):

        context.update({'instance': instance})
        return context


