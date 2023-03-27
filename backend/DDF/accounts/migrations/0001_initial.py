# Generated by Django 4.1.7 on 2023-03-27 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('PublicRequest', 'Public Request'), ('PrivateRequest', 'Private Request')], max_length=20)),
                ('request_title', models.CharField(max_length=300)),
                ('request_description', models.CharField(max_length=3000)),
                ('request_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], default='Debit', max_length=20)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('committee_approval_status', models.CharField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Pending', 'Pending')], default='Pending', max_length=20)),
                ('hod_approval_status', models.CharField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Pending', 'Pending')], default='Pending', max_length=20)),
                ('committee_review', models.CharField(blank=True, max_length=3000, null=True)),
                ('committee_review_date', models.DateTimeField(blank=True, null=True)),
                ('hod_review', models.CharField(blank=True, max_length=3000, null=True)),
                ('hod_review_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('committee_id', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='FacultyUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('faculty_id', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='HodUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('hod_id', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('remaining_budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.fundrequest')),
            ],
        ),
    ]
