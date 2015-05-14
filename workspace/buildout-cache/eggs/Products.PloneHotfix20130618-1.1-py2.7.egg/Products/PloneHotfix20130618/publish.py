from ZPublisher import Publish
from ZPublisher.Publish import *

from marmoset_patch import marmoset_patch


def _original_publish(request, module_name, after_list, debug=0,
            # Optimize:
            call_object=call_object,
            missing_name=missing_name,
            dont_publish_class=dont_publish_class,
            mapply=mapply,
            ):
    pass


marmoset_patch(_original_publish, Publish.publish,
               extra_globals=Publish.publish.func_globals)


def _patched_processInputs(self):
    from urlparse import urlparse

    marker = object()
    self.__old__processInputs()
    ca = self.get('CANCEL_ACTION', marker)
    if ca is not marker:
        # Relative URLs aren't part of the spec, but are accepted by some
        # browsers.
        for part, base in zip(urlparse(ca)[:3], urlparse(self['BASE1'])[:3]):
            if not part:
                continue
            if not part.startswith(base):
                self['CANCEL_ACTION'] = ''
                break


def _patched_publish(request, *args, **kwargs):
    import types

    request.__old__processInputs = request.processInputs
    request.processInputs = types.MethodType(_patched_processInputs, request)

    return _original_publish(request, *args, **kwargs)


marmoset_patch(Publish.publish, _patched_publish,
               extra_globals={
                    '_patched_processInputs': _patched_processInputs,
                    '_original_publish': _original_publish,
                })
