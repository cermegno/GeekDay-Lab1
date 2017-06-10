import os
import uuid
from flask import Flask
import time

app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#777799"
GREEN = "#99CC99"

COLOR = GREEN

f = open('sessions2.txt')
session_list = f.readlines()
## Now session_list contains a list of strings, where each of the strings
## contains all the details about one session
## Close the file immediately
f.close()

@app.route('/')
def mainmenu():

    ## Let's build HTML with the contents of sessions.txt file
    session_info = []
    mid_html =  ""
    for each_session in session_list:

        session_info = each_session.split(';')
        ## The time in the file is now formatted as 'epoch' time
        ## Find out how to convert this to a human readable format
        friendly_time = time.ctime(int(session_info[2]))
        
        mid_html += """
        <h2> {} </h2>
        Starts at : {}<br>
        Presenter : {}<br>
        {}<br>
        """.format(session_info[1], friendly_time, session_info[3], session_info[4])
    
    begin_html = """
    <html>
    <head>
    <! the link to your CSS would go here>
    </head>
    <body bgcolor="{}">
    <center><b><font color="white">Hi, I'm GUID:<br/>
    {}</b></br>
    <h1><u>AGENDA</u></h1>""".format(COLOR,my_uuid,)
    
    end_html = "</center></body></html>"

    response = begin_html + mid_html + end_html

    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
