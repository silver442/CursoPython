import re

codigo1="sjdjdjdsk255sjkdjksjljdksjskl"

codigo2="dksjksjslkjslddjh133jhjhkshjkshkj"

codigo3="ghsdjkks255kjskjdkjslsd"


if re.search("255",codigo1):

    print("he encontrado el codigo")

else:
    print("No he encontrado el codigo")