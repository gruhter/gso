Plone hotfix, 2013-06-18
========================

This hotfix fixes multiple vulnerabilities in Plone,
including arbitrary code execution and privilege escalation.

This hotfix should be applied to the following versions of Plone:

* Plone <= 4.3.1
* Plone <= 4.2.6
* Any older version of Plone including 2.1, 2.5, 3.0, 3.1, 3.2, 3.3, 4.0, and 4.1


The hotfix is officially supported by the Plone security team on the
following versions of Plone in accordance with the Plone
`version support policy`_: 3.3.6, 4.1.6, 4.2.6, 4.3 and 4.3.1.
However it has also received some testing on older versions of Plone.
The fixes included here will be incorporated into subsequent releases of Plone,
so Plone 4.2.6, 4.3.1 and greater should not require this hotfix.


Installation
============

Installation instructions can be found at
http://plone.org/products/plone-hotfix/releases/20130618


Q&A
===

Q: How can I confirm that the hotfix is installed correctly and my site is protected?
  A: On startup, the hotfix will log a number of messages to the Zope event log
  that look like this::

    2013-06-18 21:15:26 INFO Products.PloneHotfix20130618 Applied typeswidget patch

  The exact list of patches attempted depends on the version of Plone.
  If a patch is attempted but fails, it will be logged as a warning that says
  "Could not apply". This may indicate that you have a non-standard Plone
  installation.

Q: How can I report problems installing the patch?
  A: Contact the Plone security team at security@plone.org, or visit the
  #plone channel on freenode IRC.

Q: How can I report other potential security vulnerabilities?
  A: Please email the security team at security@plone.org rather than discussing
  potential security issues publicly.

.. _`version support policy`: http://plone.org/support/version-support-policy
