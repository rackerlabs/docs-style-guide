.. _image-guidelines:

================
Image guidelines
================

Images, similar to screenshots and diagrams, can complement the text,
enabling readers to quickly grasp a concept. In the case of the Expert
Insights blog, pictures or artistic designs can also add visual interest and
capture the reader's attention. However, you should avoid using images to
replace text because transalation services and tools for the visually impaired
don't interpret or translate images. The \<alt\> tag helps, but don't rely on
that to convey your message.

-  `When to use diagrams <#when-to-use-diagrams>`__
-  `Image checklist <#image-checklist>`__

When to use images
~~~~~~~~~~~~~~~~~~

Include images in the following situations:

-  When you need to clarify configurations and settings, such as the
   architecture for virtual servers

-  When you need to define a complex workflow within a Rackspace product

Do *not* include images in the following situations:

-  When a workflow is simplistic, such as using the Control Panel to
   create a cloud server

-  When there is no interaction with a Rackspace product


Image checklist
~~~~~~~~~~~~~~~

Use the following standards for images:

-  **Size**: Make the images as small as you can without compromising their
   usefulness to reduce page-load time. Unless image clarity is critical,
   you can use 65-75 percent quality when saving your image. Following are
   the recommended maximum widths:

      -  Horizontal: maximum width 1200px
      -  Vertical: maximum width 900px

-  **Scope**: Limit the scope of an image to the relevant portion, eliminating
   distracting or unnecessary content and whitespace.
-  **Format**: The preferred formats are **PNG** or **SVG**, which are loseless
   formats. However, **JPG**, which is lossy and might look blurry, is smaller
   and might load faster.
-  **File name**: Create unique and meaningful file names to easily
   differentiate between images.
-  **Copyright**: Do not use copyrighted images without permission or
   appropriate credit.
-  **Titles:** Titles are not required. If you want to add a title to an
   image for clarity, follow the guidelines in :ref:`titles-and-headings`.
-  **Personal or private details**: Make sure to mask, modify, or remove
   any personal identifiers, passwords, logins, or other information that 
   could compromise security.
-  **\<alt\> property**: Use the \<alt\> property to briefly describe the
   screenshot for visually-impaired readers. The following list provides
   some guidance:

      -  For decorative images: leave alt-text blank.
      -  For images with text: use the text in the image.
      -  For charts and graphs: summarize the trend or take-away point.
      -  For other images: What does the image represent or add to the document?

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
