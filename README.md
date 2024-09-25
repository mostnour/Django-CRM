# django CMS

.. image:: https://img.shields.io/pypi/v/django-cms.svg
    :target: https://pypi.python.org/pypi/django-cms/
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/django-cms/
.. image:: https://img.shields.io/pypi/l/django-cms.svg
    :target: https://pypi.python.org/pypi/django-cms/
.. image:: https://codeclimate.com/github/divio/django-cms/badges/gpa.svg
   :target: https://codeclimate.com/github/divio/django-cms
   :alt: Code Climate

Open source enterprise content management system based on the Django framework and backed by the non-profit django CMS Association (`Sponsor us! <https://www.django-cms.org/en/memberships/>`_).

## django CMS Admin Style


|pypi| |python| |django| |djangocms| |djangocms4| |coverage|

Adds pretty CSS styles for the django CMS admin interface. Supports optional
``django-admin-shortcuts`` package.


.. note::

    This project is considered 3rd party (no supervision by the `django CMS Association <https://www.django-cms.org/en/about-us/>`_). Join us on `Slack                 <https://www.django-cms.org/slack/>`_ for more information.

+---------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/divio/djangocms-admin-style/master/preview/dashboard.png   | .. image:: https://raw.githubusercontent.com/divio/djangocms-admin-style/master/preview/listview.png   |
+---------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/divio/djangocms-admin-style/master/preview/datepicker.png  | .. image:: https://raw.githubusercontent.com/divio/djangocms-admin-style/master/preview/shortcuts.png  |
+---------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

The shortcuts you see on top of the dashboard are from `django-admin-shortcuts <https://github.com/alesdotio/django-admin-shortcuts/>`_
>>>>>>> d0166a9297f74f40de0151a04a20aa22059187b8

*******************************************
Contribute to this project and win rewards
*******************************************

<<<<<<< HEAD
Because django CMS is a community-driven project, we welcome everyone to `get involved in the project <https://www.django-cms.org/en/contribute/>`_. Become part of a fantastic community and help us make django CMS the best open source CMS in the world.


.. ATTENTION::

    Please use the ``develop-4`` branch as the target for pull requests for on-going development.

    Security fixes will be backported to older branches by the core team as appropriate.


## Features

* hierarchical pages
* extensive built-in support for multilingual websites
* multi-site support
* draft/publish workflows
* version control
* a sophisticated publishing architecture, that's also usable in your own applications
* frontend content editing
* a hierarchical content structure for nested plugins
* an extensible navigation system that your own applications can hook into
* SEO-friendly URLs
* designed to integrate thoroughly into other applications

Developing applications that integrate with and take advantage of django CMS features is easy and well-documented.

More information on `our website <https://www.django-cms.org>`_.

## Requirements

See the `Python/Django requirements for the current release version
<http://docs.django-cms.org/en/latest/#software-version-requirements-and-release-notes>`_ in our documentation.

See the `installation how-to guide for an overview of some other requirements and dependencies of the current release
<https://docs.django-cms.org/en/latest/introduction/01-install.html>`_.


## Getting started

These `tutorials <http://docs.django-cms.org/en/latest/introduction/index.html>`_ take you step-by-step through some key aspects of django CMS.

## Documentation

Our documentation working group maintains documentation for several versions of the project. Key versions are:

* `stable <http://docs.django-cms.org>`_ (default), for the **current release** version
* `latest <http://docs.django-cms.org/en/latest/>`_, representing the latest build of the **develop-4 branch**

For more information about our branch policy, see `Branches
<http://docs.django-cms.org/en/latest/contributing/development-policies.html>`_.

Our documentation is hosted courtesy of `Read the Docs <https://readthedocs.org>`_.

The dependencies for the docs are compiled by `pip-tools <https://github.com/jazzband/pip-tools>`_.


## Test django CMS in our demo

The demo platform is kindly provided by Divio, platinum member of the django CMS Association.

.. image:: https://raw.githubusercontent.com/django-cms/django-cms/develop/docs/images/try-with-divio.png
   :target: https://www.django-cms.org/en/django-cms-demo/
   :alt: Try demo with Divio Cloud

## Getting Help

Please head over to our `Discord Server <https://discord-support-channel.django-cms.org>`_ or Stackoverflow for support.

## Professional support

Choose from a list of `trusted tech partner <https://www.django-cms.org/en/tech-partners/>`_ of the django CMS Association to get your website project delivered successfully.

Choose a `trusted web host <https://www.django-cms.org/en/hosting-services/>`_ for your django CMS project and get your website online today.


## The django CMS Association

The django CMS Association is a non-profit organization that was founded in 2020 with the goal to drive the success of django CMS, by increasing customer happiness, market share and open-source contributions. We provide infrastructure and guidance for the django CMS project.

The non-profit django CMS Association is dependent on donations to fulfill its purpose. The best way to donate is to become a member of the association and pay membership fees. The funding will be funneled back into core development and community projects.

`Join the django CMS Association <https://www.django-cms.org/en/contribute/>`_.


## Credits

* Includes icons and adapted icons from `Bootstrap <https://icons.getbootstrap.com>`_.
* Includes icons from `FamFamFam <http://www.famfamfam.com>`_.
* Python tree engine powered by
  `django-treebeard <https://tabo.pe/projects/django-treebeard/>`_.
* JavaScript tree in admin uses `jsTree <https://www.jstree.com>`_.
* Many thanks to
  `all the contributors <https://github.com/django-cms/django-cms/graphs/contributors>`_
  to django CMS!
=======
Because this is a an open-source project, we welcome everyone to
`get involved in the project <https://www.django-cms.org/en/contribute/>`_ and
`receive a reward <https://www.django-cms.org/en/bounty-program/>`_ for their contribution.
Become part of a fantastic community and help us make django CMS the best CMS in the world.

We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

We're grateful to all contributors who have helped create and maintain this package.
Contributors are listed at the `contributors <https://github.com/django-cms/djangocms-admin-style/graphs/contributors>`_
section.


## Documentation

See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/djangocms-admin-style/blob/master/setup.py>`_
file for additional dependencies:



## Installation

For a manual install:

* run ``pip install djangocms-admin-style``
* add ``djangocms_admin_style`` to your ``INSTALLED_APPS`` just before ``'django.contrib.admin'``
* run ``python manage.py migrate djangocms_admin_style``


## Configuration

The django CMS Admin Style overrides django admin's ``base_site.html``,
but you can still partially customize this page. Look at the source of
``templates/admin/base_site.html`` and override the templates that are included
in various blocks. For example, you can add your own CSS in
``templates/admin/inc/extrastyle.html``.

The following additional settings can be set:

* ``CMS_ENABLE_UPDATE_CHECK = True``
  Set to ``False`` to disable the update notification.
* ``CMS_UPDATE_CHECK_TYPE = ('minor')``
  Set to ``('patch')`` to get only patch notifications.
  (minor = 3.x.x, patch = 3.4.x)

The update checker does not gather or record any data.

To **compile CSS** run the following commands using **node 16**:

* ``nvm use``
* ``npm install``
* ``npx gulp icons sass bundle``


For further options have a look at the ``gulpfile.js``.

## Dark mode support

Django supports a dark mode admin since version 3.1. djangocms-admin-style
introduces css variables that contain color codes and change with the selected
mode:

+-------------------------------+-----------+---------------------------+-----------+
| **CMS variable name**         | **Color** | **Django admin fallback** | **Color** |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-white``               | #ffffff   | ``--body-bg``             | #ffffff   |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-black``               | #000000   | ``--body-fg``             | #303030   |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-gray``                | #666      | ``--body-quiet-color``    | #666      |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-gray-lightest``       | #f2f2f2   | ``--darkened-bg``         | #f8f8f8   |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-gray-lighter``        | #ddd      | ``--border-color``        | #ccc      |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-gray-light``          | #999      | ``--close-button-bg``     | #888      |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-gray-darker``         | #454545   |                           |           |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-gray-darkest``        | #333      |                           |           |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-gray-super-lightest`` | #f7f7f7   |                           |           |
+-------------------------------+-----------+---------------------------+-----------+
| ``--dca-primary``             | #00bbff   | ``--primary``             | #79aec8   |
+-------------------------------+-----------+---------------------------+-----------+


## Extending styles in your own app

If your project or app requires specific styles if djangocms-admin-style is
installed (e.g., to better adjust to the django CMS style) you can add selective
styling by adding the ``.djangocms-admin-style`` selector::

    // Show widget in CMS colors if djangocms-admin-style is installed
    .djangocms-admin-style #my-widget {
        color:  var(--dca-primary, black);
    }

We recommend to following rules for your app's admin css:

- Try avoid using ``color``, ``background`` etc. styles where possible and meaningful
- If necessary use as few as possible standard django CMS colors (preferably
  from see above list with fallback colors)
- Usage: ``var(--dca-color-var, var(--fallback-color-var, #xxxxxx))`` where
  ``#xxxxxx`` represents the light version of the color.

## Running Tests

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements/base.txt
    python setup.py test

In order to run **integration tests** you need to have Docker installed,
then run the following command::

    make test

To test other Django versions simply append `VERSION=4.1``. You can also
run the test server through::

    make run

The integration tests are written using Casperjs, phantomcss and
djangocms-casper-helpers.


.. |pypi| image:: https://badge.fury.io/py/djangocms-admin-style.svg
    :target: http://badge.fury.io/py/djangocms-admin-style
.. |build| image:: https://travis-ci.org/django-cms/djangocms-admin-style.svg?branch=master
    :target: https://travis-ci.org/django-cms/djangocms-admin-style
.. |coverage| image:: https://codecov.io/gh/django-cms/djangocms-admin-style/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/django-cms/djangocms-admin-style

.. |python| image:: https://img.shields.io/badge/python-3.5+-blue.svg
    :target: https://pypi.org/project/djangocms-admin-style/
.. |django| image:: https://img.shields.io/badge/django-2.2%2B-blue.svg
    :target: https://www.djangoproject.com/
.. |djangocms| image:: https://img.shields.io/badge/django%20CMS-3.6%2B-blue.svg
    :target: https://www.django-cms.org/
.. |djangocms4| image:: https://img.shields.io/badge/django%20CMS-4-blue.svg
    :target: https://www.django-cms.org/