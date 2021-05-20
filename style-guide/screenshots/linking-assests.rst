.. _linking-assets:

=======================================================
Linking screenshots, images, diagrams, and other assets
=======================================================

Depending on the type of document, you can find visual assests in different
places:

-  **How-To**: Within the folder named for the article title.
-  **Expert Insights Blog**: Within the folder named for the post title.
-  **Developer Guides**: Many images are in the **\_images** directory, through
   they might be in other directories, too.
-  **Other documents**: Look for directories named **images** or **assets**.
   You can also find a section of the document that already links to an assest
   to find the appropriate location.

The following sections provide insturctions on linking to visual assests in
various documents:

-  `Linking to a visual assest in the How-To <#inking-to-a-visual-assest-in-the-how-to>`__
-  `Linking to a visual assest in the Expert Insights Blog <#inking-to-a-visual-assest-in-the-expert-insights-blog>`__
-  `Linking to a visual assest in a Developer Guide <#linking-to-a-visual-assest-in-a-developer-guide>`__


Linking to a visual assest the How-To
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a How-To article, add the image to the same directory as the article's
**index.md** file, and add a reference similar to the following example:

 `{{<image src="search-process-flow.jpg" alt="Shows the search process" title="">}}`

Linking to a visual assest in the Expert Insights Blog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For an Expert Insights Blog post, add the image to the same directory as the
post's **index.md** file, and add a reference similar to the following example:

`{{<img src="stacker-variable-able.png" alt="The table outlines Stacker environment variable files" title="">}}`

Linking to a visual assest in a Developer Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Cloud Networks Developer Guide stores the images in the **\_images**
directory.  To link to an image, insert code similar to the following example
at column one, near the text referencing it, and with a blank line before and
after the image reference:

`.. image:: /_images/cloud-networks-infographic-revised4.png
    :alt: Example of Cloud Networks interactions`
