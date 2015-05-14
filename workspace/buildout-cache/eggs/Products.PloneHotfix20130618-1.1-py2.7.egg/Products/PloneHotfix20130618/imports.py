from AccessControl import ModuleSecurityInfo
try:
    from Products import Archetypes
except ImportError:
    pass
from Products import CMFPlone
try:
    from Products import MimetypesRegistry
except ImportError:
    pass
try:
    from Products import PlacelessTranslationService
except ImportError:
    pass


BAD_IMPORTS = {
    'Products.Archetypes.utils': [
        'HAS_KERNEL_UUID',
        'KERNEL_UUID',
        'kernel_make_uuid',
        'md5',
        'random',
        'socket',
        'time',
        'transaction',
        'ClassSecurityInfo',
        'InitializeClass',
        'mapply',
        'OrderedDict',
        'call_original',
        'wrap_method',
        'unwrap_method',
        'mergeSecurity',
        'setSecurity',
        'createZope2Bridge',
        'createZope3Bridge',
        'deprecated',
        'getGTS',
        'getPkgInfo',
        'makeBridgeMaker',
        'makeZ2Bridges',
        'makeZ3Bridges',
        ],
    'Products.CMFPlone.browser.navtree': [
        'INavigationRoot',
        'buildFolderTree',
        'plone',
        'ploneview',
        'sys',
        'utils',
        ],
    'Products.CMFPlone.utils': [
        'deprecated',
        'abspath',
        're',
        'OFS',
        'aq_get',
        'package_home',
        'ImageFile',
        'CMFCoreToolInit',
        'PACKAGE_HOME',
        'WWW_DIR',
        'transaction',
        'ToolInit',
        'sys',
        'ClassSecurityInfo',
        'zope',
        'BaseView',
        'BrowserView',
        'Globals',
        'IFileNameNormalizer',
        'IMAGE_SCALE_PARAMS',
        'ITranslatable',
        'IUserPreferredFileNameNormalizer',
        'Image',
        'MEMBER_IMAGE_SCALE',
        'PIL_QUALITY',
        'PIL_SCALING_ALGO',
        'context',
        'fromZ2Interface',
        'getGlobalTranslationService',
        'lookupTranslationId',
        'scale_image',
        'ulocalized_time',
        'warnings',
        'ComponentLookupError',
        'createTopLevelTabs',
        'Zope2',
        'dirname',
        ],
    'Products.MimetypesRegistry.common': [
        'logging',
        'os',
        'time',
        'skins_dir',
        ],
    'Products.PlacelessTranslationService': [
         'os',
        'logging',
        'isdir',
        'deprecate',
        'Globals',
        'ImageFile',
        'pts_globals',
        'CACHE_PATH',
        'get_registered_packages',
        'ModuleSecurityInfo',
        'PTSWrapper',
        'get_products',
        'patches',
        'warnings',
        'misc_',
        'make_translation_service',
        'initialize2',
        'os',
        ],
}


def patch_security():

    ModuleSecurityInfo('OFS.ObjectManager').setDefaultAccess(0)
    ModuleSecurityInfo('OFS.ObjectManager').declareObjectPrivate()
    ModuleSecurityInfo('OFS.ObjectManager').declarePublic('BeforeDeleteException')

    for m in BAD_IMPORTS:
        modsec = ModuleSecurityInfo(m)
        for a in BAD_IMPORTS[m]:
            modsec.declarePrivate(a)


_original_initialize = CMFPlone.initialize
def _initialize_wrapper(context):
    result = _original_initialize(context)
    patch_security()
    return result


CMFPlone.initialize = _initialize_wrapper


patch_security()
