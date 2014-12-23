from django import template
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.templatetags.staticfiles import StaticFilesNode

register = template.Library()

class FileRevNode(StaticFilesNode):
    """ Overrides normal static file handling by first checking for file revisions in
    settings.FILEREVS, before falling back to the actual requested filename. Otherwise
    indentical to normal static tag.
    """

    def url(self, context):
        path = self.path.resolve(context)
        revved_path = settings.FILEREVS.get(path)
        if revved_path is not None:
            return staticfiles_storage.url(revved_path)
        else:
            return super(FileRevNode, self).url(context)


@register.tag
def static(parser, token):
    return FileRevNode.handle_token(parser, token)
