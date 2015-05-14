from Products.ATContentTypes.browser.archive import ArchiveView


def view_forbidden(self, *args, **kwargs):
    return self.context.raiseUnauthorized()


ArchiveView.getZipFile = view_forbidden