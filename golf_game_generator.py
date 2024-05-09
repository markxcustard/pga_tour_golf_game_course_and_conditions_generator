import random

class GolfGame:
    def __init__(self, courses):
        self.courses = courses

    def generate_course_info(self):
        course = random.choice(self.courses)
        crowd = self.generate_crowd()
        tee = self.generate_tee_location(course)
        pin = self.generate_pin_location()
        wind = self.generate_wind()
        green_firmness = self.generate_green_firmness()
        green_speed = self.generate_green_speed()
        fringe_firmness = self.generate_fringe_firmness()
        fringe_firmness_speed = self.generate_fringe_speed()
        fairway_firmness = self.generate_fairway_firmness()
        fairway_speed = self.generate_fairway_speed()
        first_cut_firmness = self.generate_first_cut_firmness()
        first_cut_length = self.generate_first_cut_length()
        second_cut_firmness = self.generate_second_cut_firmness()
        second_cut_length = self.generate_second_cut_length()
        
        return course, crowd, tee, pin, wind, green_firmness, green_speed, fringe_firmness, fringe_firmness_speed, fairway_firmness, fairway_speed, first_cut_firmness, first_cut_length, second_cut_firmness, second_cut_length
    
    def generate_crowd(self):
        return random.choice(['On', 'Off']
        )

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
    
    def generate_green_firmness(self):
        return random.choice(["Soft", "Average", "Firm", "Tournament"])
    
    def generate_green_speed(self):
        return random.choice(["Slow", "Average", "Fast", "Tournament"])

    def generate_fringe_firmness(self):
        return random.choice(["Soft", "Average", "Firm", "Tournament"])
    
    def generate_fringe_speed(self):
        return random.choice(["Slow", "Average", "Fast", "Tournament"])
    
    def generate_fairway_firmness(self):
        return random.choice(["Soft", "Average", "Firm", "Tournament"])
    
    def generate_fairway_speed(self):
        return random.choice(["Slow", "Average", "Fast", "Tournament"])
    
    def generate_first_cut_firmness(self):
        return random.choice(["Soft", "Firm", "Tournament"])
    
    def generate_first_cut_length(self):
        return random.choice(["Short", "Medium", "Long"])
    
    def generate_second_cut_firmness(self):
        return random.choice(["Soft", "Firm", "Tournament"])
    
    def generate_second_cut_length(self):
        return random.choice(["Short", "Medium", "Long"])
    
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

    print("Generated Golf Game Information:")
    print("Course:", course_info[0])
    print("Crowd:", course_info[1])
    print("Tee:", course_info[2])
    print("Pin:", course_info[3])
    print("Wind Direction:", course_info[4][0])
    print("Wind Speed:", course_info[4][1])
    print("Green Firmness:", course_info[5])
    print("Green Speed:", course_info[6])
    print("Fringe Firmness:", course_info[7])
    print("Fringe Speed:", course_info[8])
    print("Fairway Firmness:", course_info[9])
    print("Fairway Speed:", course_info[10])
    print("First Cut Firmness:", course_info[11])
    print("First Cut Length:", course_info[12])
    print("Second Cut Firmness:", course_info[13])
    print("Second Cut Length:", course_info[14])

if __name__ == "__main__":
    main()