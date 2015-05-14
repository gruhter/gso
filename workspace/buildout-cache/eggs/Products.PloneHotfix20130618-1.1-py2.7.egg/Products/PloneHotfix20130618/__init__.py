import logging


logger = logging.getLogger('Products.PloneHotfix20130618')


hotfixes = [
    'catalog',
    'cb_decode',
    'dataitems',
    'get',
    'imports',
    'in_portal',
    'linkintegrity',
    'mail_password',
    'member_portrait',
    'objectmanager',
    'principiaredirect',
    'pts',
    'publish',
    'request',
    'sendto',
    'spamProtect',
    'traverser',
    'traverseName',
    'typeswidget',
    'wysiwyg',
    'zip',
    ]

PLONE_ONLY = ('imports', 'mail_password', 'member_portrait', 'sendto', 'spamProtect')

try:
    import plone.app.linkintegrity.utils
except ImportError:
    hotfixes.remove('linkintegrity')
try:
    import Products.Archetypes
except ImportError:
    hotfixes.remove('typeswidget')
try:
    import Products.ATContentTypes.browser.archive
except ImportError:
    hotfixes.remove('zip')
try:
    from Products import kupu
except ImportError:
    hotfixes.remove('wysiwyg')
try:
    import Products.CMFPlone
except ImportError:
    # No Plone. Remove all but the Zope patches.
    for f in PLONE_ONLY:
        if f in hotfixes:
            hotfixes.remove(f)


# Apply the fixes
for hotfix in hotfixes:
    try:
        __import__('Products.PloneHotfix20130618.%s' % hotfix)
        logger.info('Applied %s patch' % hotfix)
    except:
        logger.warn('Could not apply %s' % hotfix)
logger.info('Hotfix installed')
