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

    ## Now we will define the string first
    response =  """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>
    <u>Main Menu</u>
    </center>
    </body>
    </html>
    """.format(COLOR,my_uuid,)

    ## And then we return it. This gives us more flexibility
    ## than building it just-in-time for the "return" function

    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
