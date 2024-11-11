# Django Hello World App

A simple Django app that displays "Hello, World!" when accessed.

## Installation

1. Add 'django.contrib.hello' to your INSTALLED_APPS setting:
```python
INSTALLED_APPS = [
    ...
    'django.contrib.hello',
]
```

2. Include the hello URLconf in your project urls.py:
```python
path('hello/', include('django.contrib.hello.urls')),
```

## Usage

After installation, visit `/hello/` to see the "Hello, World!" message.
