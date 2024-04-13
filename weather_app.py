# from flask import Flask, render_template, request, jsonify
# import requests
# from datetime import datetime
#
# app = Flask(__name__)
#
#
# def get_weather_color(weather_condition):
#     # Define a mapping of weather conditions to colors
#     weather_color_map = {
#         "Clear": "#FFFDDA",  # Light gray for clear weather
#         "Clouds":"#d3d3d3",  # Light gray for cloudy weather
#         "Rain": "#92BAD2",  # Cornflower blue for rainy weather
#         "Snow": "#ffffff",  # White for snowy weather
#         # Add more weather conditions and corresponding colors as needed
#     }
#     # Return the color based on the weather condition
#     return weather_color_map.get(weather_condition, "#f0f0f0")
# @app.context_processor
# def inject_functions():
#     return dict(get_weather_color=get_weather_color)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')
#
# # @app.route('/weather_map')
# # def weather_map():
# #     # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
# #     api_key = '09e1bd599470636b1cafa4556cab1d47'
# #     # Make a request to the OpenWeatherMap API to fetch weather map data
# #     url = f'http://api.openweathermap.org/data/2.5/weather?q=Canada&appid={api_key}'
# #     response = requests.get(url)
# #     data = response.json()
# #     # Extract weather map information from the response
# #     # You may need to adjust this based on the OpenWeatherMap API response format
# #     weather_map_data = {
# #         'temperature': data['main']['temp'],
# #         'humidity': data['main']['humidity'],
# #         # Add more weather map data as needed
# #     }
# #     return weather_map_data
#
# @app.template_filter('to_12_hour_format')
# def to_12_hour_format(value):
#     # Convert time string to datetime object
#     time_obj = datetime.strptime(value, '%H:%M:%S')
#     # Format datetime object in 12-hour format
#     return time_obj.strftime('%I:%M %p')
#
#
# @app.route('/forecast', methods=['GET'])
# def forecast():
#     city = request.args.get('city')
#
#     if not city:
#         return 'City name is required!', 400
#
#     api_key = '09e1bd599470636b1cafa4556cab1d47'
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
#
#     try:
#         response = requests.get(url)
#         data = response.json()
#         if data.get('cod') == '404':
#             return 'City not found!', 404
#     except Exception as e:
#         print(e)
#         return 'An error occurred while processing your request.', 500
#
#     return render_template('index.html', data=data)
#
#
# @app.route('/7dayforecast', methods=['GET'])
# def seven_day_forecast():
#     city = request.args.get('city')
#
#     if not city:
#         return 'City name is required!', 400
#
#     api_key = '09e1bd599470636b1cafa4556cab1d47'
#     url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
#
#     try:
#         response = requests.get(url)
#         data = response.json()
#         if data.get('cod') == '404':
#             return 'City not found!', 404
#     except Exception as e:
#         print(e)
#         return 'An error occurred while processing your request.', 500
#
#     return render_template('result.html', data=data)
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=8001)
