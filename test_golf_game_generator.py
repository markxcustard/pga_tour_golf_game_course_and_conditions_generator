import pytest
from golf_game_generator import GolfGame

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

def test_generate_green_firmness(game):
    green_firmness = game.generate_green_firmness()
    assert green_firmness in ["Soft", "Average", "Firm", "Tournament"]

def test_generate_green_speed(game):
    green_speed = game.generate_green_speed()
    assert green_speed in ["Slow", "Average", "Fast", "Tournament"]

def test_generate_fringe_firmness(game):
    fringe_firmness = game.generate_fringe_firmness()
    assert fringe_firmness in ["Soft", "Average", "Firm", "Tournament"]

def test_generate_fringe_speed(game):
    fringe_speed = game.generate_fringe_speed()
    assert fringe_speed in ["Slow", "Average", "Fast", "Tournament"]

def test_generate_fairway_firmness(game):
    fairway_firmness = game.generate_fairway_firmness()
    assert fairway_firmness in ["Soft", "Average", "Firm", "Tournament"]

def test_generate_fairway_speed(game):
    fairway_speed = game.generate_fairway_speed()
    assert fairway_speed in ["Slow", "Average", "Fast", "Tournament"]

def test_generate_first_cut_firmness(game):
    first_cut_firmess = game.generate_first_cut_firmness()
    assert first_cut_firmess in ["Soft", "Firm", "Tournament"]

def test_generate_first_cut_length(game):
    first_cut_length = game.generate_first_cut_length()
    assert first_cut_length in ["Short", "Medium", "Long"]

def test_generate_second_cut_firmness(game):
    second_cut_firmess = game.generate_second_cut_firmness()
    assert second_cut_firmess in ["Soft", "Firm", "Tournament"]

def test_generate_second_cut_length(game):
    second_cut_length = game.generate_second_cut_length()
    assert second_cut_length in ["Short", "Medium", "Long"]
