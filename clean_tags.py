import os

files = os.listdir('/home/scuttlest/Devel/hexamedia/content/reviews/steam/')
for filename in files:
    with open('/home/scuttlest/Devel/hexamedia/content/reviews/steam/' + filename, 'r') as in_file:
        text = in_file.read()
    new_page = ''
    for line in text.split('\n'):
        if 'Tags: ' in line:
            print(filename, line)
            if 'negative review' in line:
                new_page += 'Tags: negative review\n'
            elif 'neutral review' in line:
                new_page += 'Tags: neutral review\n'
            elif 'positive review' in line:
                new_page += 'Tags: positive review\n'
        else:
            new_page += line + '\n'
    print(new_page)
    with open('/home/scuttlest/Devel/hexamedia/content/reviews/steam/' + filename, 'w') as out_file:
        out_file.write(new_page)
