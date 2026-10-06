from django.db import migrations


def split(apps, schema_editor):
    Exchange = apps.get_model('faculty', 'ExchangeProgram')
    for p in Exchange.objects.all():
        value = p.university.strip()
        if value.endswith(')') and '(' in value:      
            name, country = value[:-1].rsplit('(', 1)
        elif ' - ' in value:
            name, country = value.rsplit(' - ', 1)
        elif ',' in value:
            name, country = value.rsplit(',', 1)
        else:
            name, country = value, ''
        p.university = name.strip()
        p.country = country.strip()
        p.save()


def join(apps, schema_editor):

    Exchange = apps.get_model('faculty', 'ExchangeProgram')
    for p in Exchange.objects.all():
        p.university = f'{p.university}, {p.country}' if p.country else p.university
        p.country = ''
        p.save()


class Migration(migrations.Migration):
    dependencies = [('faculty', '0004_add_country')]
    operations = [migrations.RunPython(split, join)]