import re

links_file = open('links.txt')
dynamic_links_file = open('new_links.txt', 'a')

for link in links_file.readlines():
    matchObj = re.search('(.*) src="(.*)"', link)
    if matchObj:
        new_link = matchObj.group(2)
        dynamic_links_file.write(f'<script src="{{{{ url_for(\'static\', filename=\'{new_link}\') }}}}"></script>\n')
