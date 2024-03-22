# Generated by Django 5.0.2 on 2024-03-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_product"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="user_id",
            new_name="User_id",
        ),
        migrations.AddField(
            model_name="product",
            name="pic",
            field=models.ImageField(null=True, upload_to="static/img/products/"),
        ),
    ]
