.. _diagram-guidelines:

==================
Diagram guidelines
==================

Diagrams can help users visualize complex processes in a simplified way.
However, diagrams can sometimes be too simplistic, confusing the user instead
of providing help. The decision about whether a diagram might be helpful
depends on the context of each document and the discretion of each writer.

-  `When to use diagrams <#when-to-use-diagrams>`__
-  `Before you create a diagram <#before-you-create-a-diagram>`__
-  `Request a diagram from Creative Services <#request-a-digram-from-creative-services>`_
-  `Diagram checklist <#diagram-checklist>`__

When to use diagrams
~~~~~~~~~~~~~~~~~~~~

Before using a diagram, consider tables or lists as possible alternatives.

Include diagrams in the following situations:

-  When there is evidence of a process, whether the process is automated
   or manual

-  When you need to clarify configurations and settings, such as the
   architecture for virtual servers

-  When you need to define a complex workflow within a Rackspace product

Do *not* include diagrams in the following situations:

-  When a workflow is simplistic, such as using the Control Panel to
   create a cloud server

-  When there is no interaction with a Rackspace product

Before you create a diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create diagrams, you need to access the recommended software and
download the required icons and stencils.

Software
--------

Use `draw.io <https://www.draw.io/>`__ to create your diagrams. Draw.io
enables you to create diagrams directly in your web browser of choice.

To get started with draw.io, see the instructions in the `Draw.io Online
User
Manual <https://support.draw.io/display/DO/Draw.io+Online+User+Manual>`__.

Icons, stencils, and shapes
---------------------------

Download Rackspace's library of product icons and stencils. These icons
and stencils are considered **objects**.

-  The product icons are blue and are located in `this zip
   file <https://github.com/rackerlabs/docs-style-guide/blob/master/style-guide/screenshots/images/zip/ProductIcons.zip>`__.

-  Stencils are used to represent certain functions and hardware such as
   the world wide web or a server. These stencils are black and are
   located in `this zip
   file <https://github.com/rackerlabs/docs-style-guide/blob/master/style-guide/screenshots/images/zip/RackspaceDiagramIcons.zip>`__.

After you download the icons and stencils, you can being making diagrams
in Draw.io.

Request a diagram from Creative Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you'd rather request a diagram from the Creative Services team than create it yourself,
consult the **Writer's Handbook** *Processes* section for instructions.

Diagram checklist
~~~~~~~~~~~~~~~~~

Use the following standards when creating diagrams:

Properties
----------

Each diagram property is located on the right side of the Draw.io
main screen under **Diagrams**.

-  **Paper size**: Set the paper size to **A4 (210 mm x 297 mm)**
   and **Landscape**.

-  **Background color**: Set the background color to **none**.

-  **File format**: Save all diagrams as editable SVG files, as follows:

   #. Click **File > Save As**.
   #. Type a descriptive name for the file, and replace ``.xml`` with
      ``.svg`` at the end of the file name. The file is saved to your local
      directory.

-  **File name**: Create unique and meaningful file names to
   differentiate diagrams.

Text formatting
---------------

-  **Font**: Set the font to **Helvetica**.

-  **Titles:** Title must be **bolded**, aligned **left**, and be at
   least **24px** in size. Use sentence-style capitalization.

Objects
-------

-  **Product icons**: An icon represents its corresponding product. Product
   icons are always blue. Following is the Cloud Images icon.

   .. figure:: images/img/images.png
      :alt: Cloud Images stencil

   .. note::

      If you find a Rackspace product icon that is not blue, send an email to
      how-to@rackspace.com and a member of our team will create a blue version
      of the icon.

-  **Stencils**: A stencil represents a concept or function.
   Stencils that are *not* Rackspace products should always appear in
   black.

-  **Labels**: Label all product icons, stencils, and shapes, according to
   their function within the diagram. Use sentence-style capitalization (that
   is, capitalize *only* terms that are proper or are normally capitalized).

Background
----------

If possible, use a transparent background and don’t add borders or shadow
effects to the diagram to avoid distracting interactions with the reader's
screen background.


\<alt\> property
----------------

Use the \<alt\> property to briefly describe the screenshot for
visually-impaired readers. The following list provides some guidance:

      -  For decorative images: leave alt-text blank.
      -  For images with text: use the text in the image.
      -  For charts and graphs: summarize the trend or take-away point.
      -  For other images: What does the image represent or add to the document?

Lines and arrows
----------------

-  **Line usage**: Use lines are used to connect and display a
   relationship between two or more objects.

-  **Line width**: Line width must be at least **2pt**. You can
   change the width of a line in the **Format Panel** under **Style**
   when you select the line.

-  **Line shape**: Keep lines straight unless a line needs to change
   direction.

-  **Rounded line corners**: If a line changes direction, the corner
   in which the change of direction occurs must be rounded. You can
   change to rounded corners by selecting the line, going to the
   **Format Panel** under **Style**, and selecting **Rounded** in the
   dropdown menu.

-  **Solid lines**: Use solid lines to show a direct relationship
   between objects, as shown in the following example.

   .. figure:: images/img/solid-lines.png
      :alt: Example of solid lines

-  **Dashed lines**: Use dashed lines to group objects that are
   connected through a network, as shown in the following example.

   .. figure:: images/img/dashed-lines.png
      :alt: Example of dashed lines

-  **Dotted lines**: Use dotted lines to show how data entered by
   the user travels, as shown in the following example.

   .. figure:: images/img/dotted-lines.png
      :alt: Example of dotted lines

-  **One-way and two-way arrows:** Use arrows to represent direct
   interactions between two or more stencils. If a stencil is attached
   to an arrow, it implies that the product represented by the stencil
   needs to interact with another piece of the diagram.

   In the following example, the CDN management service needs to interact
   with the CDN to perform its function. Similarly, the CDN needs to be
   managed by the CDN management service. The relationship is two-way, so
   the line has arrows on both ends pointed to both stencils.

   .. figure:: images/img/arrowsscreenshot.png
      :alt: Example of one-way and two-way arrows
