from flask import *
from weather import get_current_weather, get_autocomplete_weather
from sendemail import sendEmail
from wfuncions import *

app = Flask(__name__)
text_input = ""

# Ruta de la pagina principal
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        place_request = request.form["place_autocomplete"]
    else:
        place_request = "auto:ip"
    data = get_current_weather(place_request)
    aiq_data = air_quality(data["current"]["air_quality"])
    forecast_data = forecast(data["forecast"]["forecastday"], data["location"]["localtime"])
    return render_template('index.html', data=data, aiq_data=aiq_data, forecast_data=forecast_data)

@app.route('/r', methods=["POST"])
def change():
    global text_input
    new_data = request.form.get('text')
    text_input = get_autocomplete_weather(new_data)
    return jsonify({'text':text_input})

# Ruta de la pagina principal
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["contact-info-elements-name"]
        email = request.form["contact-info-elements-email"]
        subject = request.form["contact-info-elements-subject"]
        message = request.form["contact-info-elements-message"]
        sendEmail(name=name, email=email, message=message, subject=subject)
        return redirect(url_for('home'))
    else:
        return render_template('contact.html')


# Iniciar el servidor web
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)