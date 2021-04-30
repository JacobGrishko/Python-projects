import requests


def comp_views(web):
    r = requests.get(web, stream=True)
    names_views = {0: "no result"}
    for line in r.iter_lines():
        line = str(line)
        if 'views' in line:
            parts = line.split(' views"}')
            for part in parts:
                vid_name = ""
                vid_views = 0
                new_part = part[part.rfind('"')+1:]
                new_part = new_part.replace(',', '')
                if len(new_part) > 15:
                    if "by" in new_part:
                        vid_name = new_part.split(" by ")[0]
                    vid_views = int(new_part[new_part.rfind(" ")+1:])
                    if vid_name and vid_views:
                        names_views[vid_views] = vid_name


    print('The vid with max views is "{0}"'.format(names_views[max(names_views.keys())]))
    print("Here is the link: ")
    link="https://www.youtube.com/results?search_query="+names_views[max(names_views.keys())]
    link = link.replace(' ', '+')
    link = link.replace('[', '%d')
    link = link.replace(']', '%d')

    r = requests.get(link, stream=True)
    for line in r.iter_lines():
        line = str(line)
        if 'views' in line:
            vid_link = line.split('"url":"/watch?')[1]
            vid_link = vid_link[:vid_link.find('"')]
            print("https://www.youtube.com/watch?"+vid_link)
