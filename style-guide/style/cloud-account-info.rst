.. _cloud-account-info:

=========================
Cloud account information
=========================

In examples of API authentication requests, and other examples where we
are teaching the use of the API and expect that users might copy the
code and use it, use variables or the following standard values for
account numbers, usernames, passwords, API keys, and so on. Format the
variables by using camelCase and italics, and also use bold within the
examples.

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Information
     - Use
     - Don't use
   * - Account or tenant ID
     - *yourAccountId*

       *yourTenantId*

       ``$account``

       ``$tenant``
     - 658405
   * - Username
     - *yourUsername*

       ``$username``
     - robb4554
   * - Password
     - *yourPassword*

       ``$password``
     - J$12345\*
   * - API key
     - *yourApiKey*

       ``$apikey``
     - of938go4915e114f7ff5448910fee68c
   * - Authentication token
     - *xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*

       ``$token``
     - 2e356864f39831523c184to646b1997b

In example API operation requests and responses, in which we want users
to see actual values from the system, use "real-looking" values that are
nevertheless obviously made up, such the following one for
``X-Auth-Token``:

.. code::

   abcdef123ghi4j5k67m8910n12op3qrs

.. warning::

   Don't include or show actual writer or user account
   credentials in code examples or screenshots.
