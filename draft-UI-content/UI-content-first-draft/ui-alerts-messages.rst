.. _ui-alert-message-guidelines:

===============================
UI alert and message guidelines
===============================

Alerts and messages inform users about progress that they make or problems
that they encounter in the UI. They must be clearly written, be free from
grammar and punctuation problems, and follow the style and terminology for
guidelines in this guide.

Users gain understanding from the content of the messages (text, icons, color)
as well as the context (where on the screen and when in the user flow the
messages appear). So users can recover quickly, alerts and messages should
provide essential information to help them understand and address issues.

General guidelines
------------------

When writing alerts and messages, use the following rules:

- Be courteous and do not blame the user.
- Use present tense to describe conditions that currently exist, or use past
  tense to describe a specific event that occurred in the past.
- Guide users with the imperative voice (``Enter a valid email.``) or the
  active voice (``The Control Panel is not responding.``) where possible.
- Keep sentences short but helpful.
- Alerts and messages must be accurate, complete, and helpful.
- Adhere to the guidelines in the :ref:`Style Guide<messages>` for writing
  alerts and messages.

Message types
-------------

The following types are messages are the most common:

- Error
- Warning
- Information
- Confirmation
- Success

Error
~~~~~

Use error messages to inform users that a problem in the system or application
occurred. Users or systems cannot continue their tasks until the problem is
resolved. An example of an error message is ``The file could not be found.``.

Warning
~~~~~~~

Use warning messages to alert users about a condition that might cause
problems in the future. User can generally continue with their tasks, but
those tasks might not be completed in a way that is expected. An example of a
warning message is ``The service could not open all documents. Some documents
were skipped.``.

Information
~~~~~~~~~~~

Use information messages to provide information about normal conditions and
operations. An example of an information message is ``Updates are being
processed.``.

Confirmation
~~~~~~~~~~~~

Use confirmation messages to ask users to verify an action that the users or
sometimes the system initiated. Also, use confirmation prompts to ask users
for additional information to complete a step or to ask whether to save
information for future use. And example of a confirmation prompt is ``Do you
want to close this document without saving your changes?``.

Success
~~~~~~~

Use success messages to tell users that an action successfully completed. An
example of a success prompt is ``Server successfully deleted.``.

Style
-----

For information about style for error messages, including icons and color, see
the `Helix design guide <http://helix.rax.io>`_ and the `Helix developer guide <https://rackerlabs.github.io/helix-ui/>`_.

Examples
--------

The following table shows examples of the different types of alerts.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Type
     - Example
   * - Error
     - * ``Unable to create the volume.``
       * ``Unable to retrieve the image.``
   * - Warning
     - * ``Policy check failed.``
       * ``Insufficient privilege level exists to view usr information.``
   * - Information
     - * ``Updating volume snapshot snapshot-name.``
       * ``Creating volume volume-name.``
   * - Confirmation
     - * ``Do you want to close this document without saving your changes?``
       * ``Do you want to reset your password?``
   * - Success
     - * ``Successfully created key pair key-pair-name.``
       * ``Image successfully updated.``
