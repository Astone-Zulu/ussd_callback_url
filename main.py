from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "USSD App Running"

@app.route("/ussd", methods=['POST'])
def ussd_handler():

    session_id = request.values.get("sessionId", "")
    text = request.values.get("text", "")

    if text == "":
        response = "CON Zambia Crime Portal\n"
        response += "1. Report Theft\n"
        response += "2. Report GBV\n"
        response += "3. Report Fraud"

    elif text == "1":
        response = "CON Theft Type:\n1. Home Break-in\n2. Street Mugging"

    elif text == "2":
        response = "END ALERT: High Priority case logged."

    elif text in ["1*1", "1*2"]:
        response = f"END Case ZP{session_id[-4:]} logged successfully."

    else:
        response = "END Invalid option. Try again."

    return Response(response, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))