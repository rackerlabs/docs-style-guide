# Markdown (MD) conventions


MD is a straightforward markup language that uses simple and implicit
syntax to introduce a variety of content elements. All the source
content formatted using MD is stored in files with the ``.md`` extension.

To keep the documentation format consistent, follow the guidelines
included in this chapter for all the MD source content.

For more information on MD conventions, see the following
resources:

* [Markdown Cheatsheet](ttps://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lists)

## Lines length

Wrap source lines so that lines length does not exceed 79 characters.
This requirement matches PEP8 standards (from Python) and helps with
side-by-side diffs on reviews.

## Headings

Each MD source file has the tree structure. Define up to three heading
levels within one file using the following non-alphanumeric characters:

For the first-level headings in an article, use the H3 level
(designated by ###).

* **H1** - single pound/hash;

* **H2** - double pound/hash;

* **H3** - triple pound/hash;

* **H4** - quadruple pound/hash.

**Input**

```
   # H1
   ## H2
   ### H3
 ```

Avoid using more than three levels of heading in an article (H3, H4, and
H5). If you need more than three levels, you should consider breaking
your article into two or more articles.

If a title contains a special character, such as a colon, enclose the title with
single quotation marks.

When code includes placeholders, show them in camelCase and enclose them in angle brackets.
For example, ``<hostName>``.

## Code and Syntax Highlighting

Code blocks are part of the Markdown spec, but syntax highlighting isn't. 
However, many renderers -- like Github -- support syntax
highlighting. Which languages are supported and how those language names 
should be written will vary from renderer to renderer. 

`Inline `code` has `back-ticks around` it.`

Inline `code` has `back-ticks` around it.

Blocks of code are either fenced by lines with three back-ticks ```, or
are indented with four spaces. We recommend only using the fenced
code blocks.

For example:

```

 javascript
 var s = "JavaScript syntax highlighting";
 alert(s);

```
 
## Linking to other articles

To link to another article on the support.rackspace.com site, use the
following format:
[<articleName>](/how-to/<articleName>). For example,
[Rackspace Email and Hosted Exchange settings](/how-to/rackspace-email-and-hosted-exchange-settings).
Note the use of the leading slash.

For external links to articles that are not on the Rackspace How-To site,
use the same format, but add the complete external URL. For example,
[OpenStack Contributor Guide](https://docs.openstack.org/contributor-guide/).
