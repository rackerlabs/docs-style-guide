.. _how-to-article-guidelines:

=========================
How-To article guidelines
=========================

This section includes guidelines specifically for How-To articles that are
published at https://support.rackspace.com/. The section duplicates the
information in the `Style guidelines for contributing content <https://github.com/rackerlabs/rackspace-how-to/blob/master/style-guidelines.md>`_ in
the ``rackspace-how-to`` repository on GitHub. Use these guidelines, in
addition to the others in this style guide, when you write or review any
How-To articles for this site.

Follow these guidelines when writing content:

- :ref:`Use sentence-style capitalization for titles and headings
  <sentence-style-capitalization-guidelines>`
- :ref:`Use active voice<active-voice>`
- :ref:`Use present tense<present-tense>`
- :ref:`Write to the user by using second person and imperative mood
  <write-to-user>`
- :ref:`Write clear and consistent step text<step-text>`
- :ref:`Use consistent text formatting<consistent-text-format>`
- :ref:`Clarify pronouns such as it, this, there, and that
  <clarify-pronouns>`
- :ref:`Clarify gerunds and participles<gerunds-and-participles>`
- :ref:`Write clear and consistent code examples<code-examples-guidelines>`
- :ref:`Use consistent terminology<consistent-terminology>`
- :ref:`When and when not to suggest contacting Support<support-mentions>`

For comprehensive writing and style guidelines, see other sections in this
style guide.


.. _sentence-style-capitalization-guidelines:

Use sentence-style capitalization for titles and headings
---------------------------------------------------------

Use sentence-style capitalization for all titles and headings. In sentence-
style capitalization, you capitalize only the first word of the title or
heading, plus any proper nouns, proper adjectives, and terms that are always
capitalized, such as some acronyms and abbreviations. If the title includes a
colon, capitalize the first word that follows the colon, regardless of its
part of speech.

Following are some examples:

- Install or upgrade PHP 5.3 for CentOS 5.x
- Ubuntu 8.04 LTS (Hardy Heron): Using mod_python to serve your application
- PHP configuration limits for Cloud Sites
- Troubleshoot a Vyatta site-to-site VPN connection
- Differences between IMAP and POP

For more information about titles and headings, see the `Titles and headings <https://developer.rackspace.com/docs/style-guide/style/titles-and-headings/>`__ topic in this style guide.

.. _active-voice:

Use active voice
----------------

In general, write in *active* voice rather than *passive* voice.

- Active voice identifies the agent of action as the subject of the
  verb—usually the user.
- Passive voice identifies the recipient (not the source) of the action as the
  subject of the verb.

Active-voice sentences clarify the performer of an action and are easier to
understand than passive-voice sentences. Passive voice is usually less
engaging and more complicated than active voice. When you use passive voice,
the actions and responses of the software can be difficult to distinguish from
those of the user. In addition, passive voice usually requires more words than
active voice.

Following are examples of active voice:

- After you install the software, start the computer.
- Click **OK** to save the configuration.
- Create a server.
- Rackspace products and services solve your business problems.

For more information about voice, see the `Use active voice <https://developer.rackspace.com/docs/style-guide/writing/use-active-voice>`__ section in this style guide.

.. _present-tense:

Use present tense
-----------------

Users read documentation to perform tasks or gather information. For users,
these activities take place in their present, so the present tense is
appropriate in most cases. Additionally, present tense is easier to read than
past or future tense.

Use future tense only when you need to emphasize that something will occur
later (from the users' perspective). To easily find and remove instances of
future tense, search for *will*.

Following are examples of present tense:

- After you log in, your account begins the verification process.
- Any user with a Cloud account can provision multiple ServiceNet database
  instances.
- The product prompts you to verify the deletion.
- To back up Cloud Sites to Cloud Files by using this example, you create two
  cron jobs. One job backs up the cloud site and database, and the second job
  uploads the backup to Cloud Files.

For more information about present tense, see the `Use present tense <https://developer.rackspace.com/docs/style-guide/writing/use-present-tense/#use-present-tense>`__ section in the complete style guide.

.. _write-to-user:

Write to the user by using second person and imperative mood
------------------------------------------------------------

Users are more engaged with documentation when you use second person (that is,
you address the user as *you*). Second person promotes a friendly tone by
addressing users directly. Using second person with the imperative mood (in
which the subject *you* is understood) and active voice helps to eliminate
wordiness and confusion about who or what initiates an action, especially in
procedural steps.

Using second person also avoids the use of gender-specific, third-person
pronouns such as *he*, *she*, *his*, and *hers*. If you must use third person,
use the pronouns *they* and *their*, but ensure that the pronoun matches the
referenced noun in number.

Use first person plural pronouns (*we*, *our*) judiciously. These pronouns
emphasize the writer or Rackspace rather than the user, so before you use
them, consider whether second person or imperative mood is more "user
friendly." However, use *we recommend* rather than *it is recommended* or
*Rackspace recommends*. Also, you can use *we* in the place of *Rackspace* if
necessary.

The first-person singular pronoun *I* is acceptable in the question part of
FAQs.

Avoid switching person (point of view) in the same document.

.. note::

   This guidelines document is written in second person, and the headings and
   task examples use imperative mood.

For more information about this topic, see the `Write to the user by using second person and imperative mood <https://developer.rackspace.com/docs/style-guide/writing/write-to-the-user/#write-to-the-user>`__ section in this style guide.

.. _step-text:

Write clear and consistent step text
------------------------------------

When you are providing instructions to users, you should generally number the
steps (unless you have just one step). For the steps, use the following
guidelines. The guidelines are followed by an example. For more extensive
examples, see the `Steps <https://developer.rackspace.com/docs/style-guide/style/tasks/#steps>`__ section of this style guide.

- Write each step as a complete imperative sentence (that is, a sentence that
  starts with an imperative verb) and use ending punctuation. In steps, the
  focus is on the user, and the voice is active.

- Usually, include only a single action in each step. If two actions are
  closely related, such as opening a menu and selecting a command from the
  menu, you can include both actions in one step.

- If a step specifies where to perform an action, state where to perform the
  action before describing the action.

- If a step specifies a situation or a condition, state the situation or
  condition before describing the action.

- Do *not* include explanatory or reference information in the action part of
  a step. If needed, follow the step with one or more paragraphs that provide
  such information.

- Do *not* document system actions, responses, or results as steps. Put
  necessary statements in paragraphs following the steps to which they apply.

- Use screenshots sparingly. Screenshots can help to orient the user, but a
  screenshot of every field or dialog box is usually not necessary.

- To indicate that a step is optional, include *(Optional)*, in italics, as a
  qualifier at the beginning of the step.

- If more than one method exists for completing an action, document only one
  method, usually the most efficient or preferred method.

.. _consistent-text-format:

Use consistent text formatting
------------------------------

Certain text should be formatted differently from the surrounding text to
designate a special meaning or to make the text stand out to the user. Usually
this formatting is accomplished by applying a different font treatment (such
as bold, italics, or monospace).

The following table covers the most common items that should be formatted. For
more detailed formatting information, see the `Text formatting <https://developer.rackspace.com/docs/style-guide/style/text-formatting/>`__ section of
the  style guide.

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Text item
     - Treatment
     - Example
   * - Text you want to emphasize
     - Italics
     - The offset *must* be a multiple of the limit (or zero).
   * - Error messages
     - Monospace
     - ``The user does not have permission to perform this action.``
   * - Code examples
     - Monospace
     - ``$ grep "ftp" /etc/xinetd.d/*``
   * - File, directory, and folder names
     - Bold
     - However, if these items are shown as part of code, use monospace.
       For example:
       Copy the **index.php** file from your computer to the **content**
       folder.
       The following example shows a basic configuration for the FTP service,
       in a file in the ``/etc/xinetd.d`` directory.
   * - Keyboard key names and combinations
     - Bold
     - Press **Enter**.
   * - UI fields
     - Bold
     - Select **Start > Control Panel**, and then click the **Mail** icon.
   * - Placeholder text
     - Show in camelCase.
     - If the authoring tool allows it, apply italics to placeholders; if not,
       enclose them in angle brackets.
       For example: *hostName* or ``<hostName>``

.. _clarify-pronouns:

Clarify pronouns such as it, this, there, and that
--------------------------------------------------

Pronouns are useful, but you must ensure that their antecedents (the words
that they are used in place of) are clear, and that they (the pronouns) don’t
contribute to vagueness and ambiguity.

- **It**: Ensure that the antecedent of *it* is clear. If multiple singular
  nouns precede *it*, any of them could be the antecedent. Also, avoid using
  *it is* to begin a sentence. Such a construction hides the real subject of
  the sentence.

- **This**: Avoid beginning a sentence with the pronoun *this*, unless you
  follow this with a noun to clarify its meaning.

- **There**: Avoid using *there is* and *there are* as the subject of a
  sentence or clause. Using *there* shifts the focus away from the real
  subject and often uses unnecessary words.

- **That**: Avoid using *that* as a demonstrative pronoun (which stands in
  for or points to a noun). Instead, use it as an adjective and follow it with
  a noun.

For more examples, see the `Use pronouns carefully <https://developer.rackspace.com/docs/style-guide/writing/use-pronouns-carefully/>`__
section of this style guide.

.. _gerunds-and-participles:

Clarify gerunds and participles
-------------------------------

Participles are verbs that end in *-ed* or *-ing* and act as modifiers.
Gerunds are verbs that end in *-ing* and act as nouns. Both types of words are
useful and acceptable, but confusion can arise if they are not placed
precisely in a sentence. For example, the word *meeting* can be a gerund or a
modifier (or even a noun) depending on its placement in a sentence. Clarify
gerunds and participles as necessary.

For more information and examples, see the `Clarify gerunds and participles <https://developer.rackspace.com/docs/style-guide/writing/clarify-gerunds-participles>`__ section of this style guide.

.. _code-examples-guidelines:

Write clear and consistent code examples
----------------------------------------

Observe the following guidelines when creating blocks of code as input or
output examples:

- Do not use screenshots to show code examples. Format them as blocks of code,
  in monospace, by using the appropriate markup in your authoring tool.

- When showing input, include a command prompt (such as $).

- As often as necessary, show input and output in separate blocks and provide
  explanations for each. For example, if the input contains arguments or
  parameters, explain those. If the user should expect something specific in
  the output, or you want to show only part of lengthy output, provide an
  explanation. Provide your users the information that they need, and separate
  the input and output when it makes sense.

- When the command is simple, and there is nothing specific to say about the
  output, you can show the input and output in the same code block, as the
  user would actually see the code in their own terminal. The inclusion of the
  command prompt will differentiate the input from the output.

- Ensure that any placeholder text in code is obvious. If the authoring tool
  allows it, apply italics to placeholders; if not, enclose them in angle
  brackets. Show all placeholder text in camelCase.

- Follow the conventions of the programming language used and preserve the
  capitalization that the author of the code used.

- For readability, you can break up long lines of input into blocks by ending
  each line with a backslash.

- If the input includes a list of arguments or parameters, show the important
  or relevant ones first, and group related ones. If no other order makes
  sense, use alphabetical order. If you explain the arguments or parameters in
  text, show them in the same order that they appear in the code block.

The following example illustrates many of these guidelines. For more examples,
see the `Code examples <https://developer.rackspace.com/docs/style-guide/style/code-examples/>`__ section of this style guide.

**Example: Create a VM running a Docker host**

1. Show all of the available virtual machines (VMs) that are running Docker
   by running the following command:

   ``$ docker-machine ls``

   If you have not created any VMs yet, your output should look as follows:

   ``NAME   ACTIVE   DRIVER   STATE   URL``

2. Create a VM that is running Docker by running the following command:

   ``$ docker-machine create --driver virtualbox test``

   The ``--driver`` flag indicates what type of driver the machine will run
   on. In this case, ``virtualbox`` indicates that the driver is Oracle
   VirtualBox. The final argument in the command gives the VM a name, in this
   case, ``test``.

   The output should look as follows:

   .. code::

      Creating VirtualBox VM...
      Creating SSH key...
      Starting VirtualBox VM...
      Starting VM...
      To see how to connect Docker to this machine, run: docker-machine env test

3. Run ``docker-machine ls`` again to see the VM that you created by running
   the following command:

   ``$ docker-machine ls``

   The output should look as follows:

   .. code::

      NAME             ACTIVE   DRIVER       STATE     URL                         SWARM
      test                      virtualbox   Running   tcp://192.168.99.101:237

.. _consistent-terminology:


Use consistent terminology
--------------------------

Use words as they are defined in a general dictionary, in an accepted industry
dictionary or style guide, or for your particular project. Each word or phrase
should have only one meaning, and should be used consistently throughout the
documentation.

- Don't use the same word to describe two or more different concepts. For
  example, don't use *agent* to refer to both a person and a process.

- If a word has both a technical meaning and a general meaning, don't use it
  to express both meanings. Instead, use a synonym for the general meaning.
  For example, use *interface* as a noun that means user interface. Instead of
  also using *interface* as a verb, use *interact*.

- Don't use different words to mean the same thing. Standardize on the use of
  one word for a particular object. Technical writing is not creative writing,
  and you should not be concerned that you will bore customers with colorless
  prose. Clarity is the goal, so using a precise set of terms consistently is
  required. Following is a common example of multiple terms that refer to the
  same thing:

  - menu command *(the preferred term)*
  - menu item
  - menu option

- Use a word as only one part of speech. Many words can be correctly used as a
  verb and as a noun or an adjective, such as *display*. However, using the
  same word as more than one part of speech in the same document can be
  confusing to customers and translators, so avoid it when possible.

- Avoid fabricated words. Examples of fabricated words are *marketecture* or
  *edutainment*. Most such words are specific to a single business culture and
  are not understood in other cultures.

- Standardize words and spelling across a documentation set.

- Don't use terms with different meanings interchangeably. Some terms have
  similar but distinct meanings and should not be used interchangeably. For
  example:

  - environment, platform
  - version, release
  - panel, screen
  - window, dialog box

Additionally, replace the following nonpreferred terms with the preferred
terms.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Avoid
     - Preferred
   * - allow
     - enable or you can (unless referring to permissions)
   * - as
     - because (describing a reason for)
   * - below
     - following (when referring to the placement of information "on the page")
   * - box
     - computer (or an more specific term, such as server)
   * - checkbox
     - check box
   * - click on
     - click
   * - config
     - configuration
   * - deselect
     - clear
   * - desire
     - want
   * - desired
     - wanted, correct, appropriate
   * - double click
     - double-click
   * - e.g.
     - for example
   * - enter in
     - enter
   * - etc.
     - and so on (or revise to omit)
   * - i.e.
     - that is
   * - info
     - information
   * - information on
     - information about
   * - internet
     - internet
   * - log into
     - log in to
   * - may
     - might (could happen) or can (is able to)
   * - machine
     - computer (except when discussing a virtual machine, or VM)
   * - once
     - after (to mean occurring subsequently in time or order)
   * - make
     - sure	ensure
   * - please
     - Omit. It is not necessary.
   * - refer to
     - see
   * - right click
     - right-click
   * - since
     - because (describing a reason for)
   * - using
     - by using

For more guidelines about terminology, see the following sections in the
style guide:

- `Terminology for a global audience <https://developer.rackspace.com/docs/style-guide/terminology/terms-for-global-audience/#terms-for-global-audience>`__
- `Terminology <https://developer.rackspace.com/docs/style-guide/terminology/>`__

.. _support-mentions:

When and when not to suggest contacting Support
-----------------------------------------------

A customer who has sought out documentation has inherently communicated that
documentation is their preferred channel of support at that moment. Suggesting
that they contact the Support team directly undermines the purpose of the
documentation and diminishes the user's confidence in the instructions.

- Don't suggest contacting Support directly.

- Don't include Support phone numbers.

- Don't recommend creating a ticket unless it is for gaining access to a
  Rackspace feature.

  You should not recommend contacting the Support team in an article unless
  doing so is a required step. A required step is a task that the customer
  cannot complete without contacting Support by phone or by opening a ticket.
