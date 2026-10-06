import re
from django.db import migrations


def only_digits(apps, schema_editor):
    Exchange = apps.get_model('faculty', 'ExchangeProgram')
    for p in Exchange.objects.all():
        match = re.search(r'\d+', p.seats)
        p.seats = match.group() if match else '0'
        p.save()


class Migration(migrations.Migration):
    dependencies = [('faculty', '0005_split_university_country')]

    operations = [migrations.RunPython(only_digits, migrations.RunPython.noop)]