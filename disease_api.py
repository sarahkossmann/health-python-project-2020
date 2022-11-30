import icd10
import string
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health.settings')
django.setup()

from account.models import Disease

code = []

for digit in range(00,100):

    for letter in string.ascii_uppercase:

        if len(str(digit)) == 1:
            digit = '0'+str(digit)

        codes = (letter+str(digit))
        code.append(codes)

# print(code)

# c = icd10.find("D05")
# print(c.description)
for c in code:
    if icd10.find(c):
        d = Disease(code=c, description=icd10.find(c).description)
        # d.save()

#
# chaque profil avoir une variable (medical history avec liste de codes)
# construire db avec idc10 (table et remplir avec les infos)