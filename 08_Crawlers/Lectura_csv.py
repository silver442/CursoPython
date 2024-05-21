import csv

with open('posts.csv', 'r', newline='', encoding='utf-8') as csvfile:
    postreader = csv.reader(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for fila in postreader:
        print(', '.join(fila))
        print()