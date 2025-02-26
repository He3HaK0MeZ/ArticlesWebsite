# Generated by Django 4.1 on 2024-05-09 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_article_category_delete_worker_article_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.CharField(
                blank=True, max_length=255, unique=True, verbose_name="Альт.название"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                upload_to="images/thumbnails/%Y/%m/%d/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=("png", "jpg", "webp", "jpeg", "gif")
                    )
                ],
                verbose_name="Превью поста",
            ),
        ),
    ]
