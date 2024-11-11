# Django Hello World App

A stylish Django app that displays random animated greetings with dynamic color schemes. Features include:

- Randomly selected friendly greetings with matching emojis
- Beautiful gradient backgrounds that change with each greeting
- Smooth animation effects
- Clean, modern typography
- Responsive design that works on all devices

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
