from Shared.DC.Scripts.Bindings import Bindings
from zExceptions import NotFound


_original_bindAndExec = Bindings._bindAndExec


def escape(string):
    if isinstance(string, basestring):
        return string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    return string


def _patched_bindAndExec(self, args, kw, caller_namespace):
    '''
    Prepares the bound information and calls _exec(),
    possibly with a namespace.
    '''
    if hasattr(self, 'getId'):
        id = self.getId()
        if id == 'spamProtect':
            if self.REQUEST.get('PUBLISHED') is self:
                raise NotFound('Script may not be published.')
            else:
                new_args = []
                for a in args:
                    new_args.append(escape(a))
                new_kw = {}
                for k, v in kw.items():
                    new_kw[k] = escape(v)

                args = new_args
                kw = new_kw

    return _original_bindAndExec(self, args, kw, caller_namespace)


Bindings._bindAndExec = _patched_bindAndExec
