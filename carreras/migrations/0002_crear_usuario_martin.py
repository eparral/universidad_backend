from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations


def crear_usuario_martin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    usuario, _ = User.objects.get_or_create(username='martin')
    usuario.password = make_password('123456')
    usuario.is_active = True
    usuario.save(update_fields=['password', 'is_active'])


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carreras', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_usuario_martin, migrations.RunPython.noop),
    ]
