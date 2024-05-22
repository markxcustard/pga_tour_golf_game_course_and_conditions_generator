from datetime import datetime
import random
import pytz

class GolfGame:
    def __init__(self, courses):
        self.courses = courses

    def generate_course_info(self):
        course = random.choice(self.courses)
        crowd = self.generate_crowd()
        time_of_day = self.generate_time_of_day()
        tee = self.generate_tee_location(course)
        pin = self.generate_pin_location()
        wind = self.generate_wind()
        green_firmness, green_speed = self.generate_condition()
        fringe_firmness, fringe_speed = self.generate_condition()
        fairway_firmness, fairway_speed = self.generate_condition()
        first_cut_firmness, first_cut_length = self.generate_condition(True)
        second_cut_firmness, second_cut_length = self.generate_condition(True)
        
        # Set the timezone to PST/PDT
        pacific = pytz.timezone('America/Los_Angeles')
        timestamp = datetime.now(pacific).strftime("%a, %d %b %Y %H:%M:%S %Z")

        return {
            "course": course,
            "crowd": crowd,
            "time_of_day": time_of_day,
            "tee": tee,
            "pin": pin,
            "wind_direction": wind[0],
            "wind_speed": wind[1],
            "green_firmness": green_firmness,
            "green_speed": green_speed,
            "fringe_firmness": fringe_firmness,
            "fringe_speed": fringe_speed,
            "fairway_firmness": fairway_firmness,
            "fairway_speed": fairway_speed,
            "first_cut_firmness": first_cut_firmness,
            "first_cut_length": first_cut_length,
            "second_cut_firmness": second_cut_firmness,
            "second_cut_length": second_cut_length,
            "timestamp": timestamp  # Ensure this is a formatted datetime string in PST/PDT
        }

    def generate_crowd(self):
        return random.choice(['On', 'Off'])
    
    def generate_time_of_day(self):
        return random.choice(["Morning", "Afternoon", "Evening"])

    def generate_tee_location(self, course):
        if course == 'Augusta':
            return random.choice(['Masters'])
        else:
            return random.choice(['Black'])

    def generate_pin_location(self):
        return random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    def generate_wind(self):
        speed_ranges = [
        "1 to 2", "2 to 4", "3 to 5", "4 to 7",
        "6 to 9", "8 to 12", "10 to 15", "14 to 20", "18 to 25"
        ]

        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        return random.choice(directions), random.choice(speed_ranges)
    
    def generate_condition(self, is_cut=False):
        if is_cut:
            firmness_levels = ["Soft", "Firm", "Tournament"]
        else:
            firmness_levels = ["Soft", "Average", "Firm", "Tournament"]
        speed_levels = ["Slow", "Average", "Fast", "Tournament"]
        
        firmness = random.choice(firmness_levels)
        
        if is_cut:
            length_levels = ["Short", "Medium", "Long"]
            length = random.choice(length_levels)
            return firmness, length
        else:
            speed = random.choice(speed_levels)
            return firmness, speed
