from django.db import migrations

def admin_and_employee_creation(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).bulk_create([
        Group(name='admin'),
        Group(name='employee'),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.RunPython(admin_and_employee_creation),
    ]
