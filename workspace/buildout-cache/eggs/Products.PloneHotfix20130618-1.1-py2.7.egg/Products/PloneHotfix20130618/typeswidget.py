from Products.Archetypes.Widget import TypesWidget


for fn in (TypesWidget.getCondition,
           TypesWidget.setCondition,
           TypesWidget.testCondition):

    if hasattr(fn.im_func, '__doc__'):
        del fn.im_func.__doc__
