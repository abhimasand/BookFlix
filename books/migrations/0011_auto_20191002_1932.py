# Generated by Django 2.1.3 on 2019-10-02 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20191002_0429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_book_currently_reading',
            name='book',
        ),
        migrations.AddField(
            model_name='user_book_currently_reading',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Intermediate_Book'),
        ),
        migrations.RemoveField(
            model_name='user_book_reading',
            name='book',
        ),
        migrations.AddField(
            model_name='user_book_reading',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Intermediate_Book'),
        ),
        migrations.RemoveField(
            model_name='user_book_wishlisted',
            name='book',
        ),
        migrations.AddField(
            model_name='user_book_wishlisted',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Intermediate_Book'),
        ),
    ]