# Generated by Django 4.2.7 on 2023-11-27 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('budget_spend', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('total_points', models.PositiveIntegerField(default=0)),
                ('task_count', models.PositiveIntegerField(default=0)),
                ('points_done', models.PositiveIntegerField(default=0)),
                ('progress', models.PositiveIntegerField(default=0)),
                ('weight', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)),
                ('priority', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High'), (4, 'Urgent')], default=1)),
                ('state', models.IntegerField(choices=[(1, 'To do'), (2, 'In process'), (3, 'Ready for inspection'), (4, 'Done')], default=1)),
            ],
            options={
                'verbose_name': 'section',
                'verbose_name_plural': 'sections',
                'ordering': ['priority', '-title'],
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Tagulous_Task_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('weight', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)),
                ('priority', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High'), (4, 'Urgent')], default=1)),
                ('points', models.PositiveIntegerField(default=0)),
                ('state', models.IntegerField(choices=[(1, 'To do'), (2, 'In process'), (3, 'Ready for inspection'), (4, 'Done')], default=1)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
                ('assignor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested_tasks', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.project')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='section.section')),
                ('tags', tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, help_text='Enter a comma-separated tag string', to='section.tagulous_task_tags')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
                'ordering': ['priority', '-title'],
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tagulous_Section_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='SectionMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('B', 'Busy'), ('A', 'Available')], default='A', max_length=10)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.section')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='section_members', through='section.SectionMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='section',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddField(
            model_name='section',
            name='section_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projectmember'),
        ),
        migrations.AddField(
            model_name='section',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, help_text='Enter a comma-separated tag string', to='section.tagulous_section_tags'),
        ),
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('weight', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)),
                ('priority', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High'), (4, 'Urgent')], default=1)),
                ('points', models.PositiveIntegerField(default=0)),
                ('state', models.IntegerField(choices=[(1, 'To do'), (2, 'In process'), (3, 'Ready for inspection'), (4, 'Done')], default=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('assignee', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('assignor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.project')),
                ('section', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='section.section')),
            ],
            options={
                'verbose_name': 'historical task',
                'verbose_name_plural': 'historical tasks',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSection',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('budget_spend', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('total_points', models.PositiveIntegerField(default=0)),
                ('task_count', models.PositiveIntegerField(default=0)),
                ('points_done', models.PositiveIntegerField(default=0)),
                ('progress', models.PositiveIntegerField(default=0)),
                ('weight', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)),
                ('priority', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High'), (4, 'Urgent')], default=1)),
                ('state', models.IntegerField(choices=[(1, 'To do'), (2, 'In process'), (3, 'Ready for inspection'), (4, 'Done')], default=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.project')),
                ('section_leader', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.projectmember')),
            ],
            options={
                'verbose_name': 'historical section',
                'verbose_name_plural': 'historical sections',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['title', 'priority'], name='section_tas_title_1c2963_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['title'], name='section_tas_title_aca783_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='sectionmember',
            unique_together={('user', 'section')},
        ),
        migrations.AddIndex(
            model_name='section',
            index=models.Index(fields=['title', 'priority'], name='section_sec_title_fa5be1_idx'),
        ),
        migrations.AddIndex(
            model_name='section',
            index=models.Index(fields=['title'], name='section_sec_title_b78b18_idx'),
        ),
    ]
