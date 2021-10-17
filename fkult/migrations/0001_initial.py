# Generated by Django 2.2.24 on 2021-10-17 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stregsystem', '0014_mobilepayment_nullable_customername_20210908_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(help_text='IMDB/TMDB id of movie (e.g. Pulp Fiction tt0110912)', max_length=16, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=128)),
                ('original_title', models.CharField(blank=True, max_length=128, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='')),
                ('avg_rating', models.FloatField(blank=True, help_text='average rating given by movie API', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('theme', models.CharField(max_length=128)),
                ('votes', models.IntegerField(blank=True, help_text='number of fkult votes received on season initiation', null=True)),
                ('accepted', models.BooleanField(blank=True, help_text='accepted at fkult season initiation', null=True)),
                ('movies', models.ManyToManyField(help_text='pair of movies for the event', to='fkult.Movie')),
                ('proposer', models.ForeignKey(blank=True, help_text='proposer of event, given as fklub member to derive name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='stregsystem.Member')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fkult.Season')),
            ],
        ),
    ]
