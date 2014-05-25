import logging
from kotti_media.resources import Audio
from kotti_blog.resources import BlogEntry
from kotti.util import _
from fanstatic import Library
from fanstatic import Resource
from kotti.fanstatic import edit_needed
from kotti.fanstatic import view_needed

library = Library('shupcast', 'static')
css = Resource(library, 'css/shupcast.css', depends=view_needed.resources)

log = logging.getLogger(__name__)


def kotti_configure(settings):

    Audio.type_info.addable_to.append("Blog entry")
    BlogEntry.type_info.add_selectable_default_view(
        "media_folder_view", _("Media Folder")
    )
    view_needed.add(css)
    edit_needed.add(css)
