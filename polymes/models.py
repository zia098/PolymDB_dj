from django.db import models

class WildTypePolymerase(models.Model):
    id = models.AutoField(primary_key=True)  # Sync with MySQL
    name = models.TextField(db_column="Polymerase_Name")
    source_strain = models.TextField(db_column="Source strain", null=True, blank=True)
    family = models.TextField(db_column="Family", null=True, blank=True)
    exo_activity = models.TextField(db_column="exo_activity_5_3", null=True, blank=True)
    sequence = models.TextField(db_column="sequence", null=True, blank=True)
    doi = models.TextField(db_column="DOI", null=True, blank=True)
    genbank = models.TextField(db_column="GenBank", null=True)
    uniprot = models.TextField(db_column="UniProt", null=True)
    PDB = models.TextField(db_column="PDB", null=True)
  

    class Meta:
        db_table = "Wild_type_Polymerases"
'''
class ModifiedPolymerase(models.Model):
    id = models.AutoField(primary_key=True)  # Sync with MySQL
    name = models.TextField(db_column="Polymerase_Name", blank=True)
    base_polymerase = models.TextField(db_column="Base_Polymerase", null=True,blank=True)
    modification_type = models.TextField(db_column="Modification_Type", null=True,blank=True)
    modifications = models.TextField(db_column="Modifications", null=True,blank=True)
    optimal_temp = models.FloatField(db_column="Optimal_Temperature_c", null=True,blank=True)
    melting_temp = models.FloatField(db_column="Melting_Temperature_c", null=True,blank=True)
    processivity = models.FloatField(db_column="Processivity_bp", null=True,blank=True)
    binding_affinity = models.FloatField(db_column="Binding_Affinity_kd", null=True,blank=True)
    ph_stability = models.TextField(db_column="pH_Stability_Range", null=True,blank=True)
    optimal_ph = models.FloatField(db_column="Optimal_pH", null=True, blank=True)
    salt_tolerance_nacl = models.FloatField(db_column="Salt_Tolerance_mM_NaCl", null=True, blank=True)
    salt_tolerance_kcl = models.FloatField(db_column="Salt_Tolerance_mM_KCI", null=True, blank=True)
    activity = models.FloatField(db_column="Activity", null=True, blank=True)
    sequence = models.TextField(db_column="Sequences", null=True, blank=True)
    exo_activity_5_3 = models.TextField(db_column="exo_activity_5_3", null=True, blank=True)
    enhanced_properties = models.TextField(db_column="Enhanced_Properties", null=True, blank=True)
    applications = models.TextField(db_column="Applications", null=True, blank=True)
    genbank = models.TextField(db_column="GenBank", null=True, blank=True)
    uniprot = models.TextField(db_column="UniProt", null=True, blank=True)
    PDB = models.TextField(db_column="PDB", null=True, blank=True)
    doi = models.TextField(db_column="DOI", null=True, blank=True)

    class Meta:
        db_table = "Modified_Polymerases"'
'''

class ModifiedPolymerase(models.Model):
    id = models.AutoField(primary_key=True)  # Sync with MySQL
    name = models.TextField(db_column="Polymerase_Name", blank=True)
    base_polymerase = models.TextField(db_column="Base_Polymerase", null=True,blank=True)
    modification_type = models.TextField(db_column="Modification_Type", null=True,blank=True)
    modifications = models.TextField(db_column="Modifications", null=True,blank=True)
    optimal_temp = models.TextField(db_column="Optimal_Temperature_c", null=True,blank=True)
    melting_temp = models.TextField(db_column="Melting_Temperature_c", null=True,blank=True)
    processivity = models.TextField(db_column="Processivity_bp", null=True,blank=True)
    binding_affinity = models.TextField(db_column="Binding_Affinity_kd", null=True,blank=True)
    ph_stability = models.TextField(db_column="pH_Stability_Range", null=True,blank=True)
    optimal_ph = models.TextField(db_column="Optimal_pH", null=True, blank=True)
    salt_tolerance_nacl = models.TextField(db_column="Salt_Tolerance_mM_NaCl", null=True, blank=True)
    salt_tolerance_kcl = models.TextField(db_column="Salt_Tolerance_mM_KCI", null=True, blank=True)
    activity = models.TextField(db_column="Activity", null=True, blank=True)
    exo_activity_5_3 = models.TextField(db_column="exo_activity_5_3", null=True, blank=True)
    exo_activity_3_5 = models.TextField(db_column="exo_activity_3_5", null=True, blank=True)
    enhanced_properties = models.TextField(db_column="Enhanced_Properties", null=True, blank=True)
    #general_error = models.TextField(db_column="General_Error", null=True, blank=True)
    applications = models.TextField(db_column="Applications", null=True)
    genbank = models.TextField(db_column="GenBank", null=True, blank=True)
    uniprot = models.TextField(db_column="UniProt", null=True, blank=True)
    PDB = models.TextField(db_column="PDB", null=True, blank=True)
    title = models.TextField(db_column="TITLE", null=True, blank=True)
    doi = models.TextField(db_column="DOI", null=True, blank=True)

    class Meta:
        db_table = "all_modified_polymerases"
        #db_table = "all_polymerases_1"
        #db_table = "Batch_1"




class FusionDomain(models.Model):
    id = models.AutoField(primary_key=True)  # Sync with MySQL
    name = models.TextField(db_column="Domain Name")
    functional_type = models.TextField(db_column="Functional Type", null=True, blank=True)
    source_protein = models.TextField(db_column="Source Protein", null=True, blank=True)
    strain = models.TextField(db_column="Strain", null=True, blank=True) 
    length = models.IntegerField(db_column="Length", null=True, blank=True)
    sequence = models.TextField(db_column="Sequence (Amino Acid)", null=True, blank=True) # 
    Applications = models.TextField(db_column="Applications", null=True, blank=True)
    doi = models.TextField(db_column="DOI", null=True, blank=True)

    class Meta:
        db_table = "Fusion_Domains"
