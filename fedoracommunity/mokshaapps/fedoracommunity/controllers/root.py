from moksha.lib.base import BaseController
from moksha.api.widgets.containers import TabbedContainer
from tg import expose, tmpl_context
from fedoracommunity.widgets.widgets import GlobalResourceInjectionWidget
from tw.jquery.ui_tabs import JQueryUITabs
from tw.core import CSSLink
from moksha.layout import LayoutWidget
from pylons import config

# Root for the whole fedora-community tree
class MainNav(TabbedContainer):
    template = 'mako:fedoracommunity.mokshaapps.fedoracommunity.templates.mainnav'
    config_key = 'fedoracommunity.mainnav.apps'
    
class RootController(BaseController):

    def __init__(self):
        self.mainnav_tab_widget = MainNav('main_nav_tabs', action="create");

    @expose('mako:fedoracommunity.mokshaapps.fedoracommunity.templates.index')
    def index(self):
        w = GlobalResourceInjectionWidget()
        w.register_resources()
        
        # FIXME: we won't always display the main nav
        tmpl_context.widget = self.mainnav_tab_widget
        
        return {'title': 'Fedora Community'}
    
    def default(self, *args, **kwds):
        # TODO: translate the rest of the URL into # and redirect to index
        # this should be done in moksha if a flag is set correctly
        pass