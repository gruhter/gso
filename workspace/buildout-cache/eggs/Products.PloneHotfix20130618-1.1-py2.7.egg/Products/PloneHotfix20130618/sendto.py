from Products.CMFPlone.PloneTool import PloneTool


if hasattr(PloneTool.sendto.im_func, '__doc__'):
    del PloneTool.sendto.im_func.__doc__
