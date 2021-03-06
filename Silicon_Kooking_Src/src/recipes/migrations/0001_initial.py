# Generated by Django 2.0 on 2018-02-16 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=45, null=True)),
            ],
            options={
                'db_table': 'ingredient',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ingredientrecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(db_column='ingredient', on_delete=django.db.models.deletion.PROTECT, to='recipes.Ingredient')),
            ],
            options={
                'db_table': 'ingredientrecipe',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=200, null=True)),
                ('image', models.CharField(db_column='image', max_length=200, null=True)),
                ('ingredients', models.TextField(db_column='ingredients', null=True)),
                ('directions', models.TextField(db_column='directions', null=True)),
                ('author', models.CharField(db_column='author', max_length=45, null=True)),
                ('time', models.DateTimeField(db_column='time', null=True)),
                ('tags', models.TextField(db_column='tags', null=True)),
                ('publisher', models.ForeignKey(db_column='user', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'recipe',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RecipesRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=30)),
                ('updated', models.DateTimeField(db_column='updated')),
                ('timestamp', models.DateTimeField(db_column='timestamp')),
            ],
            options={
                'db_table': 'recipes_recipe',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='ingredientrecipe',
            name='recipe',
            field=models.ForeignKey(db_column='recipe', on_delete=django.db.models.deletion.PROTECT, to='recipes.Recipe'),
        ),
        migrations.AlterUniqueTogether(
            name='ingredientrecipe',
            unique_together={('recipe', 'ingredient')},
        ),
    ]
