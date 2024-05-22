import pytest
from golf_game import GolfGame
from datetime import datetime
import pytz

@pytest.fixture
def game():
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
    return GolfGame(courses)

def test_generate_crowd(game):
    crowd = game.generate_crowd()
    assert crowd in ['On', 'Off']

def test_generate_tee_location(game):
    course = 'Augusta'
    tee = game.generate_tee_location(course)
    assert tee in ['Masters']

    course = 'Bandon Dunes'
    tee = game.generate_tee_location(course)
    assert tee in ['Black']

def test_generate_pin_location(game):
    pin = game.generate_pin_location() 
    assert pin in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def test_generate_wind_speed(game):
    wind_direction, wind_speed = game.generate_wind()
    
    assert wind_speed in [
        "1 to 2", "2 to 4", "3 to 5", "4 to 7",
        "6 to 9", "8 to 12", "10 to 15", "14 to 20", "18 to 25"
    ]

def test_generate_wind_direction(game):
    wind_direction, wind_speed = game.generate_wind()
    
    assert wind_direction in ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def test_generate_course_info(game):
    info = game.generate_course_info()
    
    # Ensure timestamp format is correct
    pacific = pytz.timezone('America/Los_Angeles')
    try:
        datetime.strptime(info['timestamp'], "%a, %d %b %Y %H:%M:%S %Z")
    except ValueError as e:
        pytest.fail(f"Timestamp format is incorrect: {e}")
    
    assert info['course'] in game.courses
    assert info['crowd'] in ['On', 'Off']
    assert info['time_of_day'] in ["Morning", "Afternoon", "Evening"]
    assert info['tee'] in ['Masters', 'Black']
    assert info['pin'] in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    assert info['wind_direction'] in ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    assert info['wind_speed'] in ["1 to 2", "2 to 4", "3 to 5", "4 to 7", "6 to 9", "8 to 12", "10 to 15", "14 to 20", "18 to 25"]
    assert info['green_firmness'] in ["Soft", "Average", "Firm", "Tournament"]
    assert info['green_speed'] in ["Slow", "Average", "Fast", "Tournament"]
    assert info['fringe_firmness'] in ["Soft", "Average", "Firm", "Tournament"]
    assert info['fringe_speed'] in ["Slow", "Average", "Fast", "Tournament"]
    assert info['fairway_firmness'] in ["Soft", "Average", "Firm", "Tournament"]
    assert info['fairway_speed'] in ["Slow", "Average", "Fast", "Tournament"]
    assert info['first_cut_firmness'] in ["Soft", "Firm", "Tournament"]
    assert info['first_cut_length'] in ["Short", "Medium", "Long"]
    assert info['second_cut_firmness'] in ["Soft", "Firm", "Tournament"]
    assert info['second_cut_length'] in ["Short", "Medium", "Long"]


def test_generate_green_firmness(game):
    firmness, speed = game.generate_condition()
    assert firmness in ["Soft", "Average", "Firm", "Tournament"]

def test_generate_green_speed(game):
    firmness, speed = game.generate_condition()
    assert speed in ["Slow", "Average", "Fast", "Tournament"]

def test_generate_fringe_firmness(game):
    firmness, speed = game.generate_condition()
    assert firmness in ["Soft", "Average", "Firm", "Tournament"]

def test_generate_fringe_speed(game):
    firmness, speed = game.generate_condition()
    assert speed in ["Slow", "Average", "Fast", "Tournament"]

def test_generate_fairway_firmness(game):
    firmness, speed = game.generate_condition()
    assert firmness in ["Soft", "Average", "Firm", "Tournament"]

def test_generate_fairway_speed(game):
    firmness, speed = game.generate_condition()
    assert speed in ["Slow", "Average", "Fast", "Tournament"]

def test_generate_first_cut_firmness(game):
    firmness, length = game.generate_condition(True)
    assert firmness in ["Soft", "Firm", "Tournament"]

def test_generate_first_cut_length(game):
    firmness, length = game.generate_condition(True)
    assert length in ["Short", "Medium", "Long"]

def test_generate_second_cut_firmness(game):
    firmness, length = game.generate_condition(True)
    assert firmness in ["Soft", "Firm", "Tournament"]

def test_generate_second_cut_length(game):
    firmness, length = game.generate_condition(True)
    assert length in ["Short", "Medium", "Long"]
