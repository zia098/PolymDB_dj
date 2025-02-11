from django.db import models

class WildTypePolymerase(models.Model):
    id = models.AutoField(primary_key=True)  # Sync with MySQL
    name = models.TextField(db_column="Polymerase_Name")
    source_strain = models.TextField(db_column="Source strain", null=True)
    family = models.TextField(db_column="Family", null=True)
    exo_activity = models.TextField(db_column="exo_activity_5_3", null=True)
    doi = models.TextField(db_column="DOI", null=True) # this line is to add the DOI field to the model
  

    class Meta:
        db_table = "Wild_type_Polymerases"

class ModifiedPolymerase(models.Model):
    id = models.AutoField(primary_key=True)  # Sync with MySQL
    name = models.TextField(db_column="Polymerase_Name")
    base_polymerase = models.TextField(db_column="Base_Polymerase", null=True)
    modification_type = models.TextField(db_column="Modification_Type", null=True)
    modifications = models.TextField(db_column="Modifications", null=True)
    optimal_temp = models.IntegerField(db_column="Optimal_Temperature_c", null=True)
    melting_temp = models.IntegerField(db_column="Melting_Temperature_c", null=True)
    processivity = models.IntegerField(db_column="Processivity_bp", null=True)
    binding_affinity = models.IntegerField(db_column="Binding_Affinity_kd", null=True)
    ph_stability = models.TextField(db_column="pH_Stability_Range", null=True)
    optimal_ph = models.IntegerField(db_column="Optimal_pH", null=True)
    salt_tolerance_nacl = models.IntegerField(db_column="Salt_Tolerance_mM_NaCl", null=True)
    salt_tolerance_kcl = models.IntegerField(db_column="Salt_Tolerance_mM_KCI", null=True)
    activity = models.IntegerField(db_column="Activity", null=True)
    exo_activity_5_3 = models.TextField(db_column="exo_activity_5_3", null=True)
    enhanced_properties = models.TextField(db_column="Enhanced_Properties", null=True)
    doi = models.TextField(db_column="DOI", null=True)

    class Meta:
        db_table = "Modified_Polymerases"

class FusionDomain(models.Model):
    id = models.AutoField(primary_key=True)  # Sync with MySQL
    name = models.TextField(db_column="Domain Name")
    functional_type = models.TextField(db_column="Functional Type", null=True)
    source_protein = models.TextField(db_column="Source Protein", null=True)
    strain = models.TextField(db_column="Strain", null=True) 
    length = models.IntegerField(db_column="Length", null=True)
    sequence = models.TextField(db_column="Sequence (Amino Acid)", null=True) # 
    Applications = models.TextField(db_column="Applications", null=True)
    doi = models.TextField(db_column="DOI", null=True)

    class Meta:
        db_table = "Fusion_Domains"
