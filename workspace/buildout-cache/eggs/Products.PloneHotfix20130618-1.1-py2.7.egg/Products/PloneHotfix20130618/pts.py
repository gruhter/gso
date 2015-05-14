from Products.PlacelessTranslationService import PlacelessTranslationService
try:
    from Products.PlacelessTranslationService import PTSWrapper
except ImportError:
    PTSWrapper = None
try:
    PlacelessTranslationService = PlacelessTranslationService.PlacelessTranslationService
    PTSWrapper = PlacelessTranslationService.PTSWrapper
except AttributeError:
    pass


TARGETS = [PlacelessTranslationService.translate]
if hasattr(PlacelessTranslationService, 'utranslate'):
    # utranslate may not be available
    TARGETS.append(PlacelessTranslationService.utranslate)

if PTSWrapper is not None:
    TARGETS.append(PTSWrapper.translate)

for fn in TARGETS:

    if hasattr(fn.im_func, '__doc__'):
        del fn.im_func.__doc__
