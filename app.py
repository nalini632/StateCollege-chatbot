from flask import Flask, request, render_template
from google.cloud import dialogflow_v2 as dialogflow
import os

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\\Users\\NALINI.K\\Desktop\\flaskkkk\\json.json"

DIALOG_FLOW_PROJECTID = 'collegebot-hrhb'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def getbot_response():
    user_message = request.args.get('msg')
    sessionid = "abcd"
    response = detect_intent_text(DIALOG_FLOW_PROJECTID, sessionid, user_message, 'en')
    return response

def detect_intent_text(projectid, sessionid, text, language_code):
    sessionclient = dialogflow.SessionsClient()
    session = sessionclient.session_path(projectid, sessionid)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = sessionclient.detect_intent(request={"session": session, "query_input": query_input})
    return response.query_result.fulfillment_text

if __name__ == '__main__':
    app.run(debug=True)
