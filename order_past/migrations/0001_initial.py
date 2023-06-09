# Generated by Django 4.1.7 on 2023-03-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('don_ordre', models.CharField(max_length=100, null=True)),
                ('clientLivre', models.CharField(max_length=100, null=True)),
                ('n_CdeClient', models.CharField(max_length=100, null=True)),
                ('PosClt', models.CharField(max_length=100, null=True)),
                ('Ech_Clt', models.CharField(max_length=100, null=True)),
                ('DateCdeClient', models.DateField()),
                ('Dev', models.CharField(max_length=100, null=True)),
                ('n_CdePrev', models.CharField(max_length=100, null=True)),
                ('PosPrev', models.CharField(max_length=100, null=True)),
                ('ArticleInterne', models.CharField(max_length=100, null=True)),
                ('ArticleClient', models.CharField(max_length=100, null=True)),
                ('Designation1', models.CharField(max_length=100, null=True)),
                ('Qte', models.FloatField(null=True)),
                ('OTP', models.CharField(max_length=100, null=True)),
                ('MSN', models.CharField(max_length=100, null=True)),
                ('n_SerieDebut', models.CharField(max_length=100, null=True)),
                ('n_SerieFin', models.CharField(max_length=100, null=True)),
                ('Prix_net', models.FloatField(null=True)),
                ('DtLv_Souh', models.DateField()),
                ('NonFact', models.CharField(max_length=100, null=True)),
                ('Rf', models.CharField(max_length=100, null=True)),
                ('BF', models.CharField(max_length=100, null=True)),
                ('BL', models.CharField(max_length=100, null=True)),
                ('Designation2', models.CharField(max_length=100, null=True)),
                ('Designation3', models.CharField(max_length=100, null=True)),
                ('Designation4', models.CharField(max_length=100, null=True)),
                ('Designation5', models.CharField(max_length=100, null=True)),
                ('Destinataire', models.CharField(max_length=100, null=True)),
                ('Pri', models.CharField(max_length=100, null=True)),
                ('Inctm', models.CharField(max_length=100, null=True)),
                ('Incoterms2', models.CharField(max_length=100, null=True)),
                ('CPmt', models.CharField(max_length=100, null=True)),
                ('GrI', models.CharField(max_length=100, null=True)),
                ('TaxD', models.IntegerField(null=True)),
                ('NoteEntete', models.CharField(max_length=100, null=True)),
                ('n_Contrat', models.CharField(max_length=100, null=True)),
                ('Div', models.CharField(max_length=100, null=True)),
                ('Itin', models.CharField(max_length=100, null=True)),
                ('n_CdeSAP', models.CharField(max_length=100, null=True)),
                ('PosteSAP', models.CharField(max_length=100, null=True)),
                ('TyPo', models.CharField(max_length=100, null=True)),
                ('n_CdeSILOG', models.CharField(max_length=100, null=True)),
                ('PosSILOG', models.CharField(max_length=100, null=True)),
                ('SG', models.CharField(max_length=100, null=True)),
                ('SL', models.CharField(max_length=100, null=True)),
                ('Dtlivr_Ech', models.DateField(null=True)),
                ('QtecdeeEch', models.FloatField(null=True)),
                ('QteConf_Ech', models.FloatField(null=True)),
                ('CtrPr', models.CharField(max_length=100, null=True)),
                ('Sort_March', models.CharField(max_length=100, null=True)),
                ('OrgCm', models.CharField(max_length=100, null=True)),
                ('design_centre_profit', models.CharField(max_length=100, null=True)),
                ('Designation_CP', models.CharField(max_length=100, null=True)),
                ('Program_responsible', models.CharField(max_length=100, null=True)),
                ('rate', models.FloatField(null=True)),
                ('price_euro', models.FloatField(null=True)),
                ('monday', models.DateField()),
                ('diff_date', models.FloatField(null=True)),
                ('past_status', models.CharField(max_length=100, null=True)),
                ('Error_Bill_vs_Price', models.CharField(max_length=100, null=True)),
                ('Error_Routes', models.CharField(max_length=100, null=True)),
                ('Error_type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_past_per_cp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('week', models.IntegerField()),
                ('cp', models.CharField(max_length=30)),
                ('count', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_past_per_divsion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('week', models.IntegerField()),
                ('division', models.CharField(max_length=30)),
                ('count', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_past_per_errors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('week', models.IntegerField()),
                ('error', models.CharField(max_length=30)),
                ('count', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_past_per_organisme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('week', models.IntegerField()),
                ('organisme', models.CharField(max_length=30)),
                ('count', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
    ]
