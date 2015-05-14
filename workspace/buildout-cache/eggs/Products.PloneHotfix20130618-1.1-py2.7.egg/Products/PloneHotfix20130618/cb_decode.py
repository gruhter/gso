from marshal import loads
from urllib import unquote

from OFS import CopySupport

from marmoset_patch import marmoset_patch


def _cb_decode(s, maxsize=8192):
    import zlib

    dec = zlib.decompressobj()
    data = dec.decompress(unquote(s), maxsize)
    if dec.unconsumed_tail:
        raise ValueError
    del dec

    return loads(data)


marmoset_patch(CopySupport._cb_decode, _cb_decode)
