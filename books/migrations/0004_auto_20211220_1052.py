# Generated by Django 3.0 on 2021-12-20 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('read_all_books_status', 'Can read all books')]},
        ),
    ]