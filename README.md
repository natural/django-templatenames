## django-templatenames

This package solves the problem of having to manually link django templates
with corresponding CSS and JS files.


Given a base template like this (filename `project/base.html`):

```
<html>
  <head>
    {% block css %}{% endblock %}
    {% block js %}{% endblock %}
  </head>
  <body>
    {% block content %}
    {% endblock %}
  </body>
</html>
```

And a template that inheirits from it (filename `project/trucks/detail.html`):

```
{% extends "base.html" %}

{% block css %}
  <link rel="stylesheet" type="text/css" href="trucks/detail.css">
{% endblock %}

{% block js %}
  <script src="trucks/detail.js">
{% endblock %}


{% block content %}
  Look, I'm a truck!
{% endblock %}

```

Using the template tags provided by `templatenames`, we can move these links to
the base template.  The modified `project/base.html`:

```
{% load templatenames %}
<html>
  <head>
    {% block css %}
      <link rel="stylesheet" type="text/css" href="{% css_name %}">
    {% endblock %}
    {% block js %}
      <script src="{% js_name %}">
    {% endblock %}
  </head>
  <body>
    {% block content %}
    {% endblock %}
  </body>
</html>
```

Updated `project/trucks/detail.html`:

```
{% extends "base.html" %}
{% block content %}
  Look, I'm a truck!
{% endblock %}

```
