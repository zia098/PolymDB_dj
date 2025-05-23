# Generated by Django 5.1.5 on 2025-02-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polymes', '0002_alter_wildtypepolymerase_doi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fusiondomain',
            name='applications',
        ),
        migrations.RemoveField(
            model_name='fusiondomain',
            name='functional_role',
        ),
        migrations.RemoveField(
            model_name='fusiondomain',
            name='sequence_aa',
        ),
        migrations.RemoveField(
            model_name='fusiondomain',
            name='sequence_nt',
        ),
        migrations.RemoveField(
            model_name='fusiondomain',
            name='uniprot',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='applications',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='binding_affinity',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='enhanced_properties',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='exo_activity',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='melting_temp',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='modifications',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='optimal_ph',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='ph_range',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='processivity',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='salt_tolerance_kcl',
        ),
        migrations.RemoveField(
            model_name='modifiedpolymerase',
            name='salt_tolerance_nacl',
        ),
        migrations.AlterField(
            model_name='fusiondomain',
            name='doi',
            field=models.TextField(db_column='DOI', null=True),
        ),
        migrations.AlterField(
            model_name='fusiondomain',
            name='functional_type',
            field=models.TextField(db_column='Functional Type', null=True),
        ),
        migrations.AlterField(
            model_name='fusiondomain',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fusiondomain',
            name='length',
            field=models.IntegerField(db_column='Length', null=True),
        ),
        migrations.AlterField(
            model_name='fusiondomain',
            name='name',
            field=models.TextField(db_column='Domain Name'),
        ),
        migrations.AlterField(
            model_name='fusiondomain',
            name='source_protein',
            field=models.TextField(db_column='Source Protein', null=True),
        ),
        migrations.AlterField(
            model_name='fusiondomain',
            name='strain',
            field=models.TextField(db_column='Strain', null=True),
        ),
        migrations.AlterField(
            model_name='modifiedpolymerase',
            name='activity',
            field=models.IntegerField(db_column='Activity', null=True),
        ),
        migrations.AlterField(
            model_name='modifiedpolymerase',
            name='base_polymerase',
            field=models.TextField(db_column='Base_Polymerase', null=True),
        ),
        migrations.AlterField(
            model_name='modifiedpolymerase',
            name='doi',
            field=models.TextField(db_column='DOI', null=True),
        ),
        migrations.AlterField(
            model_name='modifiedpolymerase',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='modifiedpolymerase',
            name='modification_type',
            field=models.TextField(db_column='Modification_Type', null=True),
        ),
        migrations.AlterField(
            model_name='modifiedpolymerase',
            name='name',
            field=models.TextField(db_column='Polymerase_Name'),
        ),
        migrations.AlterField(
            model_name='modifiedpolymerase',
            name='optimal_temp',
            field=models.IntegerField(db_column='Optimal_Temperature_c', null=True),
        ),
    ]
