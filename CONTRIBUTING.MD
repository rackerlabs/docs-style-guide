# Contributor guidelines

These guidelines provide the general process for maintaining source files that
build the Rackspace Cloud Files developer documentation.

- [Project description](#project-description)
- [Updating and adding content](#updating-and-adding-content)
- [General style guidelines](#general-style-guidelines)
- [Submitting your content](#submitting-changes)
- [Previewing changes](#previewing-changes)

##Project description
<!-- Provide as little or as much information about architecture as needed to help
contributors figure out which file to update.-->

This project is developed and built by using the
[Python Sphinx documentation generator](http://sphinx-doc.org/). Content is
written in [reStructuredText](http://sphinx-doc.org/rest.html), which is the markup syntax and
parser component of [Python Docutils](http://docutils.sourceforge.net/index.html).





## Updating and adding content

Contributions are submitted, reviewed, and accepted by using GitHub pull requests, following the [GitHub workflow](GITHUBING.md) for this repository.

To update existing source files or add new ones, follow the [GitHub workflow](GITHUBING.md) for this repository.

* Update source files by using the GitHub editor or any plain text editor.
* Format source files with
  [reStructuredText syntax](http://www.sphinx-doc.org/en/stable/rest.html).
* For quick syntax checking, try the
[Online reStructuredText editor](http://rst.ninjs.org/).

## General style guidelines

When you add or update content, use the following general style guidelines, which are
described in detail in [Style guidelines for technical content](https://developer.rackspace.com/docs/style-guide/):

- Use sentence-style capitalization.
- Use consistent text formatting.
- Write clear and consistent code examples.
- Use active voice.
- Use present tense.
- Write to the user by using second person and imperative mood.
- Write clear and consistent step text.
- Clarify pronouns such as *it*, *this*, *there*, and *that*.
- Clarify gerunds and participles.
- Use consistent terminology.

<!-- Adding build from source guidelines until we can provide a link to automated gh-pages
output, or to the staging URL that Ash is working on.
-->

# Submitting changes

When you've completed your changes, submit a pull request. Someone on the Information Development team will review your PR.
- Minor updates and corrections get a quick review to ensure that content is error-free and doesn't introduce other issues.
- More complex changes or additions require both technical and editorial review.

Depending on the review feedback, you might be asked to make additional changes.

After content has been reviewed and approved, the updates can be merged to the master branch. The merge triggers the build and
deploy process. Typically, new content is available on developer.rackspace.com within a minute or two after it is merged. Larger
updates might take a bit longer.

## Previewing changes

When you submit a pull request, the Strider build process creates a preview of your changes in a staging environment.
After the build process completes, the following message displays in the pull request comments with a link to the content: ``Your content preview is now ready.``

You can also build the project locally by using the `tox` command.
