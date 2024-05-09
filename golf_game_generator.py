import random

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
        
        return course, crowd, tee, pin, wind, green_firmness, green_speed, fringe_firmness, fringe_speed, fairway_firmness, fairway_speed, first_cut_firmness, first_cut_length, second_cut_firmness, second_cut_length, time_of_day
    
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

def print_course_info(course_info):
    print("Generated Golf Game Information:")
    print("Course:".ljust(20), course_info[0])
    print("Crowd:".ljust(20), course_info[1])
    print("Time of Day:".ljust(20), course_info[15])
    print("Tee:".ljust(20), course_info[2])
    print("Pin:".ljust(20), course_info[3])
    print("Wind Speed:".ljust(20), course_info[4][1])
    print("Wind Direction:".ljust(20), course_info[4][0])
    print("Green Firmness:".ljust(20), course_info[5])
    print("Green Speed:".ljust(20), course_info[6])
    print("Fringe Firmness:".ljust(20), course_info[7])
    print("Fringe Speed:".ljust(20), course_info[8])
    print("Fairway Firmness:".ljust(20), course_info[9])
    print("Fairway Speed:".ljust(20), course_info[10])
    print("First Cut Firmness:".ljust(20), course_info[11])
    print("First Cut Length:".ljust(20), course_info[12])
    print("Second Cut Firmness:".ljust(20), course_info[13])
    print("Second Cut Length:".ljust(20), course_info[14])


def main():
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

    game = GolfGame(courses)
    course_info = game.generate_course_info()

    print_course_info(course_info)


if __name__ == "__main__":
    main()
