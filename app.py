from flask import Flask, jsonify, render_template
from sqlalchemy.orm import sessionmaker
from models import GolfCourseResult, engine
from golf_game_generator import GolfGame
from datetime import datetime
import pytz

app = Flask(__name__)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate_course():
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

    # Save the result to the database
    result = GolfCourseResult(
        course=course_info["course"],
        crowd=course_info["crowd"],
        time_of_day=course_info["time_of_day"],
        tee=course_info["tee"],
        pin=course_info["pin"],
        wind_direction=course_info["wind_direction"],
        wind_speed=course_info["wind_speed"],
        green_firmness=course_info["green_firmness"],
        green_speed=course_info["green_speed"],
        fringe_firmness=course_info["fringe_firmness"],
        fringe_speed=course_info["fringe_speed"],
        fairway_firmness=course_info["fairway_firmness"],
        fairway_speed=course_info["fairway_speed"],
        first_cut_firmness=course_info["first_cut_firmness"],
        first_cut_length=course_info["first_cut_length"],
        second_cut_firmness=course_info["second_cut_firmness"],
        second_cut_length=course_info["second_cut_length"],
        timestamp=course_info["timestamp"]  # Store the timestamp as a string
    )
    session.add(result)
    session.commit()

    # Keep only the last 25 results
    results_count = session.query(GolfCourseResult).count()
    if results_count > 25:
        oldest_result = session.query(GolfCourseResult).order_by(GolfCourseResult.id).first()
        session.delete(oldest_result)
        session.commit()

    return jsonify(course_info)

@app.route('/last_25', methods=['GET'])
def get_last_25_results():
    results = session.query(GolfCourseResult).order_by(GolfCourseResult.id.desc()).limit(25).all()
    results_data = [
        {
            "course": result.course,
            "crowd": result.crowd,
            "time_of_day": result.time_of_day,
            "tee": result.tee,
            "pin": result.pin,
            "wind_direction": result.wind_direction,
            "wind_speed": result.wind_speed,
            "green_firmness": result.green_firmness,
            "green_speed": result.green_speed,
            "fringe_firmness": result.fringe_firmness,
            "fringe_speed": result.fringe_speed,
            "fairway_firmness": result.fairway_firmness,
            "fairway_speed": result.fairway_speed,
            "first_cut_firmness": result.first_cut_firmness,
            "first_cut_length": result.first_cut_length,
            "second_cut_firmness": result.second_cut_firmness,
            "second_cut_length": result.second_cut_length,
            "timestamp": result.timestamp  # Directly use the stored timestamp string
        }
        for result in results
    ]
    return jsonify(results_data)

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)
