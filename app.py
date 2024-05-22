from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import sqlite3
from golf_game import GolfGame
import traceback

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    return conn

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/generate_course', methods=['GET'])
def generate_course():
    try:
        courses = [
            'Augusta', 'Bandon Dunes', 'Banff Springs', 'Bay Hill', 'Chambers Bay',
            'East Lake', 'Evian Resort', 'Harbour Town', 'Liberty National', 'Marco Simone',
            'Oak Hill', 'Olympia Fields', 'Pebble Beach', 'PGA West', 'Pinehurst No.2',
            'Quail Hallow', 'Royal Liverpool', 'Royal Troon', 'Southern Hills', 'St. Andrews',
            'Tara Iti', 'Teeth of the Dog', 'The Country Club', 'The LA Country Club',
            'The Ocean Course', 'The Riviera Country Club', 'Torrey Pines', 'TPC Boston',
            'TPC Sawgrass', 'TPC Scottsdale', 'TPC Southwind', 'Valhalla', 'Whistling Straights',
            'Wilmington Country Club', 'Wolf Creek'
        ]
        game = GolfGame(courses)
        course_info = game.generate_course_info()
        
        # Save the generated course info to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            course TEXT, crowd TEXT, time_of_day TEXT, tee TEXT, pin TEXT,
                            wind_direction TEXT, wind_speed TEXT, green_firmness TEXT,
                            green_speed TEXT, fringe_firmness TEXT, fringe_speed TEXT,
                            fairway_firmness TEXT, fairway_speed TEXT, first_cut_firmness TEXT,
                            first_cut_length TEXT, second_cut_firmness TEXT, second_cut_length TEXT,
                            timestamp TEXT)''')
        cursor.execute('''INSERT INTO results (course, crowd, time_of_day, tee, pin, wind_direction, wind_speed, green_firmness, green_speed, fringe_firmness, fringe_speed, fairway_firmness, fairway_speed, first_cut_firmness, first_cut_length, second_cut_firmness, second_cut_length, timestamp)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (course_info["course"], course_info["crowd"], course_info["time_of_day"],
                        course_info["tee"], course_info["pin"], course_info["wind_direction"],
                        course_info["wind_speed"], course_info["green_firmness"], course_info["green_speed"],
                        course_info["fringe_firmness"], course_info["fringe_speed"], course_info["fairway_firmness"],
                        course_info["fairway_speed"], course_info["first_cut_firmness"], course_info["first_cut_length"],
                        course_info["second_cut_firmness"], course_info["second_cut_length"], course_info["timestamp"]))
        conn.commit()
        conn.close()
        
        return jsonify(course_info)
    except Exception as e:
        print("Error generating course:", e)
        print(traceback.format_exc())
        return jsonify({"error": "An error occurred while generating the course."}), 500

@app.route('/results', methods=['GET'])
def get_results():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT course, crowd, time_of_day, tee, pin, wind_direction, wind_speed, green_firmness, green_speed, fringe_firmness, fringe_speed, fairway_firmness, fairway_speed, first_cut_firmness, first_cut_length, second_cut_firmness, second_cut_length, timestamp FROM results ORDER BY timestamp DESC LIMIT 25')
        results = cursor.fetchall()
        conn.close()
        
        keys = ['course', 'crowd', 'time_of_day', 'tee', 'pin', 'wind_direction', 'wind_speed', 'green_firmness', 
                'green_speed', 'fringe_firmness', 'fringe_speed', 'fairway_firmness', 'fairway_speed', 
                'first_cut_firmness', 'first_cut_length', 'second_cut_firmness', 'second_cut_length', 'timestamp']
        results_dicts = [dict(zip(keys, result)) for result in results]
        
        return jsonify(results_dicts)
    except Exception as e:
        print("Error fetching results:", e)
        print(traceback.format_exc())
        return jsonify({"error": "An error occurred while fetching the results."}), 500

if __name__ == '__main__':
    app.config['DATABASE'] = 'golf_course_results.db'
    app.run(debug=True)
