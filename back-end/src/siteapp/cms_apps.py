from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class MyApphook(CMSApp):
    app_name = "product"
    name = "Product Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["product.urls"]


@apphook_pool.register
class SolutionsApphook(CMSApp):
    app_name = "solutions"
    name = "Solutions Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["solutions.urls"]

@apphook_pool.register
class AboutApphook(CMSApp):
    app_name = "about"
    name = "About Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["about.urls"]

@apphook_pool.register
class ContactApphook(CMSApp):
    app_name = "contact"
    name = "Contact Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["contact.urls"]