wino
====

A simple Python wrapper for the [Wine.com API](https://api.wine.com/).


Installation
------------

Coming soon...


Usage
-----

```python

>>> import wino as w

# Require necessary api key
>>> c = w.Catalog("insert-your-api-key-here")

# Search catalog
>>> c.search("mondavi")

# Parameters can be passed as well
>>> c.search("mondavi", size = 1, state = 'CA')

```

More updates in documentation and code to come soon...