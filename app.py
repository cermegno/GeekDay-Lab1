import os
import uuid
from flask import Flask

app = Flask(__name__)
my_uuid = str(uuid.uuid1())

@app.route('/')
def mainmenu():

    response = """
    <html>
    <body>
     <h1><u>Event Agenda</u></h1>
     <h3>
     <ul>
       <li>09:00 - The wornderful world of Cloud Native
       <li>10:00 - DevOps demystified
       <li>11:00 - Agile for Dummies
     </ul>
     </h3>
     <br>
     Hi, I'm GUID: {}<br>
    </body>
    </html>
    """.format(my_uuid)

    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
