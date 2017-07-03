#!/usr/bin/env python3
import os
import uuid
from flask import Flask

app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#777799"
GREEN = "#99CC99"

COLOR = GREEN

@app.route('/')
def mainmenu():

    ## Let' open the sessions.txt file and dump contents to the console
    ## Note that it is not a good practice to open it here because we will
    ## have to open/close every time we access this page
    ## In the next exercise we will run it at the beginning of the program
    ## optionally you can load the contents into a structure like a Dictionary

    f = open('sessions.txt')
    session_list = f.readlines()
    ## Now session_list contains a list of strings, where each of the strings
    ## contains all the details about one session
    ## Close the file immediately
    f.close()

    session_info = []
    for each_session in session_list:
        ##print (each_session)
        session_info = each_session.split(',')
        print ("Session id  :",session_info[0])
        print ("Title       :",session_info[1])
        print ("Starts at   :",session_info[2])
        print ("Presenter   :",session_info[3])
        print ("Description :",session_info[4])

        ## You could also use this format to do the split
        ## This allows you to give meaningful name to each list item
        ## But if there are too many items it will break
##        (sid, title, stime, presenter, description) = each_session.split(',')
##        print ("sid is   : " + sid)
##        print ("title is : " + title)
    
    begin_html = """
    <html>
    <head>
    <! the link to your CSS would go here>
    </head>"""

    end_html = "</body></html>"

    mid_html =  """
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>
    <u>Main Menu</u>
    </center>
    """.format(COLOR,my_uuid,)

    response = begin_html + mid_html + end_html

    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
