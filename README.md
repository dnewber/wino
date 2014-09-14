wino
====

A simple Python wrapper for the [Wine.com API](https://api.wine.com/). Response formats include JSON and XML.


Installation
------------

```python

pip install wino
```

Usage
-----

```python

>>> import wino as w

# Require necessary api key
>>> c = w.Catalog("insert-your-api-key-here", "json")

# Search catalog
>>> c.search("mondavi")

# Parameters can be passed as well
>>> c.search("mondavi", size = 1, state = 'CA')

```

To Do
-----

- Add appropriate tests (via unittest, perhaps?)
- Build out Category API portion
- Update documentation to include use cases, etc.
