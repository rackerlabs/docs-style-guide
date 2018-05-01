#!/bin/python3
# coding: utf-8
"""Test prebuild."""

from os import listdir, path, remove
from shutil import copyfile

from pypandoc import get_pandoc_version
from pytest import mark

import postbuild
import prebuild

docdir = "tools/"
mdsuffix = '.md'
tempsuffix = '.temp'
ignore = 'README.md'
extensions = (mdsuffix, tempsuffix)
mdexample = "tools/example.mkdwn"
copydoc = "tools/readpass.md.temp"
readpass = "tools/readpass.md"
readfail = "tools/readfail.md"
writepass = "tools/writepass.md"
writefail = "tools/writefail.md"

samplemd = """# Heading 1
This is some text

## Heading 2
This is some more text.
This is an *emphasized* word.

<!--table-->
| Tables        | Are           | Cool  |
| ------------- |-------------- | ----- |
| col 3 is      | nifty         | $1600 |
| col 2 is      | awesome       |   $12 |
| zebra stripes | are neat      |    $1 |
<!--endtable-->

More paragraphs."""

sampleoutput = """# Heading 1
This is some text

## Heading 2
This is some more text.
This is an *emphasized* word.

```eval_rst
+-----------------+------------+---------+
| Tables          | Are        | Cool    |
+=================+============+=========+
| col 3 is        | nifty      | $1600   |
+-----------------+------------+---------+
| col 2 is        | awesome    | $12     |
+-----------------+------------+---------+
| zebra stripes   | are neat   | $1      |
+-----------------+------------+---------+

```

More paragraphs."""

ltable = """# Heading 1
This is some text

## Heading 2
This is some more text.
This is an *emphasized* word.

```eval_rst
.. list-table::
   :widths: 33 33 33
   :header-rows: 1

   * - Tables
     - Are
     - Cool
   * - col 3 is
     - nifty
     - $1600
   * - col 2 is
     - awesome
     - $12
   * - zebra stripes
     - are neat
     - $1

```

More paragraphs.
"""


def test_setup():
    """Set up for tests."""
    copyfile(mdexample, readpass)
    assert path.exists(readpass) is True


def test_adjustrow():
    """Test adjustrow."""
    pass


def test_buildtable():
    """Test buildtable."""
    pass


def test_copydocs():
    """Test copydocs."""
    assert prebuild.copydocs(prebuild.listfiles(docdir, mdsuffix, ignore),
                             tempsuffix) == 0
    alteredlist = [readpass, copydoc]
    dirpass = []
    for file in listdir(docdir):
        if any(file.endswith(ext) for ext in extensions):
            dirpass.append('tools/' + file)
    assert set(dirpass) == set(alteredlist)
    assert prebuild.copydocs('failext', tempsuffix) == 1


def test_listfiles():
    """Test listfiles."""
    correctlist = [path.realpath('tools/readpass.md')]
    assert prebuild.listfiles(docdir, mdsuffix, ignore) == correctlist


def test_listtable():
    """Test listtable."""
    assert prebuild.listtable(sampleoutput) == ltable


@mark.skipif(get_pandoc_version() < '1.13',
             reason='requires pandoc >= 1.13')
def test_parsedoc():
    """Test parsedoc."""
    assert prebuild.parsedoc(samplemd) == sampleoutput


def test_preparse():
    """Test preparse."""
    instring = 'A string of <br />markdown.'
    outstring = 'A string of @br@markdown.'
    assert prebuild.preparse(instring) == outstring


def test_processdocs():
    """Test processdocs."""
    passresult = prebuild.processdocs(prebuild.listfiles(docdir, mdsuffix,
                                                         ignore))
    failresult = prebuild.processdocs('failstring')
    assert passresult == 0
    assert failresult == 1


def test_postparse():
    """Test postparse."""
    instring = 'A string of @br@markdown.'
    outstring = 'A string of \n      markdown.'
    assert prebuild.postparse(instring) == outstring


def test_readfile():
    """Test readfile."""
    passresult = prebuild.readfile(readpass)
    failresult = prebuild.readfile(readfail)
    assert type(passresult) == str
    assert failresult == 1


def test_writefile():
    """Test writefile."""
    passresult = prebuild.writefile(writepass, "Hello world")
    failresult = prebuild.writefile(writefail, ['asdf'])
    assert passresult == 0
    assert failresult == 1


def test_readpass():
    """Test readpass file."""
    assert path.isfile(readpass) is True


def test_cleanup():
    """Test cleanup amd remove test files."""
    files = prebuild.listfiles(docdir, tempsuffix, ignore)
    assert postbuild.cleanup(files, tempsuffix) == 0
    assert postbuild.cleanup(123, tempsuffix) == 1
    for file in listdir(docdir):
        if file.endswith(mdsuffix):
            remove('tools/' + file)


if __name__ == '__main__':
    pass
