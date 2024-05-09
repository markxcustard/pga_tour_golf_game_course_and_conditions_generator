import pytest
from golf_game_generator import GolfGame

@pytest.fixture
def game():
    courses = [
        'Augusta', 'Bandon Dunes', 'Banff Springs', 'Bay Hill', 'Chambers Bay',
        'East Lake', 'Evian Resort', 'Harbour Town', 'Liberty National', 'Marco Simone',
        'Oak Hill', 'Olympia Fields', 'Pebble Beach', 'PGA West', 'Pinehurst No.2',
        'Quail Hallow', 'Royal Liverpool', 'Royal Troon', 'Southern Hiils', 'St. Andrews',
        'Tara Iti', 'Teeth of the Dog', 'The Country Club', 'The LA Country Club',
        'The Ocean Course', 'The Riviera Country Club', 'Torrey Pines', 'TPC Boston',
        'TPC Sawgrass', 'TPC Scottsdale', 'TPC Southwind', 'Valhalla', 'Whistling Straights',
        'Wilmington Country Club', 'Wolf Creek'
    ]
    return GolfGame(courses)

def test_generate_crowd(game):
    crowd = game.generate_crowd()
    assert crowd in ['On', 'Off']

def test_generate_time_of_day(game):
    time_of_day = game.generate_time_of_day()
    assert time_of_day in ["Morning", "Afternoon", "Evening"]

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

def test_generate_wind(game):
    wind_direction, wind_speed = game.generate_wind()
    assert wind_speed in [
        "1 to 2", "2 to 4", "3 to 5", "4 to 7",
        "6 to 9", "8 to 12", "10 to 15", "14 to 20", "18 to 25"
    ]
    assert wind_direction in ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def test_generate_condition(game):
    # Testing regular condition generation
    firmness, speed = game.generate_condition()
    assert firmness in ["Soft", "Average", "Firm", "Tournament"]
    assert speed in ["Slow", "Average", "Fast", "Tournament"]

    # Testing cut condition generation
    firmness, length = game.generate_condition(is_cut=True)
    assert firmness in ["Soft", "Firm", "Tournament"]
    assert length in ["Short", "Medium", "Long"]

def test_generate_course_info(game):
    course_info = game.generate_course_info()
    assert len(course_info) == 16
    assert isinstance(course_info[0], str)  # Course
    assert course_info[1] in ['On', 'Off']  # Crowd
    assert course_info[2] in ['Masters', 'Black']  # Tee
    assert course_info[3] in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']  # Pin
    assert isinstance(course_info[4], tuple)  # Wind
    assert course_info[5] in ["Soft", "Average", "Firm", "Tournament"]  # Green Firmness
    assert course_info[6] in ["Slow", "Average", "Fast", "Tournament"]  # Green Speed
    assert course_info[7] in ["Soft", "Average", "Firm", "Tournament"]  # Fringe Firmness
    assert course_info[8] in ["Slow", "Average", "Fast", "Tournament"]  # Fringe Speed
    assert course_info[9] in ["Soft", "Average", "Firm", "Tournament"]  # Fairway Firmness
    assert course_info[10] in ["Slow", "Average", "Fast", "Tournament"]  # Fairway Speed
    assert course_info[11] in ["Soft", "Firm", "Tournament"]  # First Cut Firmness
    assert course_info[12] in ["Short", "Medium", "Long"]  # First Cut Length
    assert course_info[13] in ["Soft", "Firm", "Tournament"]  # Second Cut Firmness
    assert course_info[14] in ["Short", "Medium", "Long"]  # Second Cut Length
    assert course_info[15] in ["Morning", "Afternoon", "Evening"]  # Time of Day
