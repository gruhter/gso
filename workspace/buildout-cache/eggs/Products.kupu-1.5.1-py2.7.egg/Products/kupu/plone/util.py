# Utility functions used by Kupu tool
import os
from App.Common import package_home
from Products.CMFCore.DirectoryView import createDirectoryView
from Products.kupu import kupu_globals
try:
    from App.class_init import InitializeClass
except ImportError:
    from Globals import InitializeClass

kupu_package_dir = package_home(kupu_globals)

from plone.outputfilters.setuphandlers import unregister_mimetype
from plone.outputfilters.setuphandlers import unregister_transform
from plone.outputfilters.setuphandlers import unregister_transform_policy
from plone.outputfilters.setuphandlers import register_transform_policy

# trying to get rid of some deprecation warnings in a
# backwards compatible way
from Products.CMFCore.utils import getToolByName

# Imported from Products.CMFCore as it is removed in 2.3
import Products
from os.path import abspath
ProductsPath = [ abspath(ppath) for ppath in Products.__path__ ]
def minimalpath(p):
    """ Convert (expanded) filepath to minimal filepath.

    The minimal filepath is the cross-platform / cross-setup path stored in
    persistent objects and used as key in the directory registry.

    Returns a slash-separated path relative to the Products path. If it can't
    be found, a normalized path is returned.
    """
    p = abspath(p)
    for ppath in ProductsPath:
        if p.startswith(ppath):
            p = p[len(ppath)+1:]
            break
    return p.replace('\\','/')

def register_layer(self, relpath, name, out, add=True):
    """Register a file system directory as skin layer
    """
    print >>out, "register skin layers"
    skinstool = getToolByName(self, 'portal_skins')
    if name not in skinstool.objectIds():
        kupu_plone_skin_dir = minimalpath(os.path.join(kupu_package_dir, relpath))
        createDirectoryView(skinstool, kupu_plone_skin_dir, name)
        print >>out, "The layer '%s' was added to the skins tool" % name

    if not add:
        return

    # put this layer into all known skins
    for skinName in skinstool.getSkinSelections():
        path = skinstool.getSkinPath(skinName) 
        path = [i.strip() for i in path.split(',')]
        try:
            if name not in path:
                path.insert(path.index('custom')+1, name)
        except ValueError:
            if name not in path:
                path.append(name)

        path = ','.join(path)
        skinstool.addSkinSelection(skinName, path)

def unregister_layers(self, names, out):
    """Remove a directory from the skins"""
    skinstool = getToolByName(self, 'portal_skins')

    # remove this layer from all known skins
    for skinName in skinstool.getSkinSelections():
        path = skinstool.getSkinPath(skinName) 
        path = [i.strip() for i in path.split(',')]

        opath = list(path)
        for name in names:
            if name in path:
                path.remove(name)

        if opath != path:
            path = ','.join(path)
            skinstool.addSkinSelection(skinName, path)

            print >>out, "removed layers '%s' from '%s'" % (', '.join(names), skinName)
    self.changeSkin(None)


def layer_installed(self, name):
    skinstool = getToolByName(self, 'portal_skins')

    # remove this layer from all known skins
    for skinName in skinstool.getSkinSelections():
        path = skinstool.getSkinPath(skinName) 
        path = [i.strip() for i in path.split(',')]

        if name not in path:
            return False
    return True

UID_TRANSFORM = 'html-to-captioned'
INVERSE_TRANSFORM = 'captioned-to-html'
MT_SAFE = 'text/x-html-safe'
MT_CAPTIONED = 'text/x-html-captioned'

def install_transform(self):
    """ Deprecated -- we now use the transforms from plone.outputfilters instead. """
    # XXX deprecation warning

def remove_transform(self):
    """Remove outdated transforms."""
    unregister_transform(self, UID_TRANSFORM)
    unregister_transform(self, INVERSE_TRANSFORM)
    unregister_mimetype(self, MT_CAPTIONED)
    unregister_transform_policy(self, MT_SAFE)
    register_transform_policy(self, "text/x-html-safe", "html_to_plone_outputfilters_html")


try:
    from zope.i18nmessageid import Message
    from zope.i18n import translate as i18n_translate
    def translate(label, context):
        if isinstance(label, Message):
            return i18n_translate(label, context=context)
        return label
except ImportError:
    def Message(msg, *args, **kw):
        return msg
    def translate(label, context):
        return label

