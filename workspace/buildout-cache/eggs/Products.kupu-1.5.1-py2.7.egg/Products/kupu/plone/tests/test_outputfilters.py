from Products.kupu.plone.tests.kuputestcase import KupuTestCase

class OutputFiltersIntegrationTestCase(KupuTestCase):

    def testFilters(self):
        self.setup_content()
        
        # Let's transform some text/html to text/x-html-safe, which should
        # trigger the filters.
        text = """<html>
<head></head>
 <body>
  <img src="resolveuid/%s/image_thumb" class="image-left captioned" width="200" alt="My alt text" />
  <p><img src="/folder/gamma" class="image-right captioned" width="200" style="border-width:1px" /></p>
  <pre>This is line 1
       This is line 2</pre>
 </body>
</html>""" % self.portal.folder.gamma.UID()
        transformed_text = self.portal.portal_transforms.convertTo(
            'text/x-html-safe', text, mimetype='text/html', context=self.portal)
        self.assertEqual("""<dl style="width:200px;" class="image-left captioned">
<dt><a rel="lightbox" href="/plone/folder/gamma"><img src="http://nohost/plone/folder/gamma/image_thumb" alt="My alt text" title="Image" height="84" width="200" /></a></dt>
 <dd class="image-caption" style="width:200px;">My caption</dd>
</dl>
  <p><dl style="width:200px;" class="image-right captioned">
<dt><img src="http://nohost/plone/folder/gamma/image" alt="Image" title="Image" height="331" width="200" style="border-width:1px" /></dt>
 <dd class="image-caption" style="width:200px;">My caption</dd>
</dl></p>
  <pre>This is line 1
       This is line 2</pre>""", str(transformed_text).strip())

        # now turn off the settings and make sure the filters are not applied
        self.kupu.configure_kupu(captioning=True, linkbyuid=True)
        transformed_text_2 = self.portal.portal_transforms.convertTo(
            'text/x-html-safe', text, mimetype='text/html', context=self.portal)
        self.assertNotEqual(transformed_text_2, transformed_text)


from unittest import TestSuite, makeSuite
def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(OutputFiltersIntegrationTestCase))
    return suite
