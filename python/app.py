from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Replace with your actual IPinfo and Google Maps API keys
IPINFO_TOKEN = 'YOUR_IPINFO_TOKEN'
GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

@app.route('/')
def index():
    return render_template('index.html', google_maps_api_key=GOOGLE_MAPS_API_KEY)

@app.route('/location')
def location():
    # Get location based on IP address
    try:
        response = requests.get(f'https://ipinfo.io/json?token={IPINFO_TOKEN}')
        data = response.json()
        loc = data['loc'].split(',')
        latitude = loc[0]
        longitude = loc[1]
        return jsonify({'latitude': latitude, 'longitude': longitude})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


