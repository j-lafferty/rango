# When importing Django models, make sure you have imported your
# project's settings by importing 'django' and setting the 
# environment variable 'DJANGO_SETTINGS_MODULE' to be your
# project's settings file.
# You can then call 'django.setup()' to import your
# Django project's settings.

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django

django.setup()

from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then, we will create a dictionary of dictionaries for our categories.
    # This allows us to iterate  through each data structure,
    # and add the data to our models.

    python_pages = [
        {'title': 'Offical Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'How To Think Like A Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/'},
    ]

    django_pages = [
        {'title': 'Offical Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial101/'},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/'},
        {'title': 'How To Tango With Django',
         'url': 'http://www.tangowithdjango.com/'},
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottleepy.org/docs/dev/'},
        {'title': 'Flask',
         'url': 'htt[://flask.pocoo.org'},
    ]

    cats = {
        'Python': {'pages': python_pages},
        'Django': {'pages': django_pages},
        'Other Frameworks': {'pages': other_pages}
    }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    # Print out the categories we have added.

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start the execution here!

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
