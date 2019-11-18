# binary

[![Travis CI] https://travis-ci.org/erskaggs/python-binary.svg?branch=master

CLI tool for artifactory interaction.

## Global Configuration File ##

To specify all connection-related settings in a central file, ```~/.artifactory.cfg```

Example:

```ini
[artifactory]
username = <your username>
password = <your password>
url = <artifcatory_url>
```

You can copy the config template to ~/.artifactory.cfg then update that cfg file to your settings

# Installation

Simply run:

    $ cd python-binary
    $ pip install .

# Usage

To use it:

    $ binary --help

