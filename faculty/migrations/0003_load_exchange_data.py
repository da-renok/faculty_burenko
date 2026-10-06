from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('faculty', '0002_exchangeprogram')]

    operations = [
        migrations.RunSQL(
            sql="""
            INSERT INTO faculty_exchangeprogram (university, languages, seats, deadline, description) VALUES
            ('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15',
             'Найбільший університет Польщі, багато програм англійською.'),
            ('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01',
             'Один з найстарших університетів Європи.'),
            ('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20',
             'Найстаріший і найбільший університет Литви.'),
            ('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15',
             'Краківський університет, заснований у 1364 році.'),
            ('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10',
             'Провідний дослідницький університет Естонії.'),
            ('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30',
             'Один із найбільших університетів Чехії, місто Брно.');
            """,
            reverse_sql="DELETE FROM faculty_exchangeprogram;",
        ),
    ]