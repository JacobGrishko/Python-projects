import downPics

print("hello, write something you would search in youtube. the app will give you the video with the most views.")
inp = input(">")
search = "https://www.youtube.com/results?search_query="+inp
downPics.comp_views(search)
