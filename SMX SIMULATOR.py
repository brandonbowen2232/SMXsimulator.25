import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import random
import sys

# Platform-specific sound handling
if sys.platform == "win32":
    import winsound
    def play_sound(sound_type):
        if sound_type == "click": winsound.Beep(1000, 50)
        elif sound_type == "success":
            winsound.Beep(1200, 80)
            winsound.Beep(1500, 100)
        elif sound_type == "warning": winsound.Beep(400, 250)
        elif sound_type == "danger":
            winsound.Beep(300, 150)
            winsound.Beep(200, 200)
else:
    def play_sound(sound_type): print("\a", end="")

class MotocrossGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Motocross Simulation")
        self.root.geometry("720x860")  
        self.root.configure(bg="#1a1a1a")

        # Game Season & Calendar States
        self.current_year = 2025
        self.calendar_phase = "OFF-SEASON"  # "SX", "SX-BREAK", "MX", "MX-BREAK", "SMX", "OFF-SEASON"
        self.current_round = 3             # Starts on Off-Season Week 3
        
        # Points Allocation Rules
        self.points_system = [26, 23, 21, 19, 17, 15, 13, 11, 9, 7, 6, 5, 4, 3, 2, 1]

        # Game Economy & Progression Settings
        self.player_team = "HRC HONDA"
        self.team_balances = {
            "HRC HONDA": 1000000,
            "MONSTER ENERGY YAMAHA": 1000000,
            "MONSTER ENERGY KAWASAKI": 1000000,
            "TEAM TRIUMPH": 1000000,
            "FACTORY BETA": 1000000,
            "REDBULL KTM": 1000000,
            "ROCKSTAR HUSQVARNA": 1000000,
            "REDBULL DUCATI": 1000000
        }
        
        self.upgrade_costs = {1: 50000, 2: 150000, 3: 300000, 4: 500000, 5: 850000}

        self.team_garages = {
            "HRC HONDA": {"SPE": 4, "ACC": 4, "DUR": 4, "WGT": 4, "SUP": 4},
            "MONSTER ENERGY YAMAHA": {"SPE": 5, "ACC": 4, "DUR": 4, "WGT": 4, "SUP": 5},
            "MONSTER ENERGY KAWASAKI": {"SPE": 4, "ACC": 5, "DUR": 4, "WGT": 4, "SUP": 5},
            "TEAM TRIUMPH": {"SPE": 3, "ACC": 3, "DUR": 3, "WGT": 3, "SUP": 4},
            "FACTORY BETA": {"SPE": 2, "ACC": 2, "DUR": 3, "WGT": 2, "SUP": 3},
            "REDBULL KTM": {"SPE": 5, "ACC": 5, "DUR": 5, "WGT": 4, "SUP": 5},
            "ROCKSTAR HUSQVARNA": {"SPE": 4, "ACC": 4, "DUR": 4, "WGT": 5, "SUP": 4},
            "REDBULL DUCATI": {"SPE": 4, "ACC": 4, "DUR": 4, "WGT": 3, "SUP": 4}
        }

        self.first_names = ["Liam", "Noah", "Oliver", "James", "Elijah", "Mateo", "Henry", "Lucas", "William", "Benjamin", "Levi", "Jack", "Ezra", "Leo", "Owen", "Sam", "Ethan", "John", "Mason", "Luke"]
        self.last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Anderson", "Taylor", "Thomas", "White", "Harris", "Martin", "Clark", "Lewis", "Lee", "Walker", "Hall", "Allen"]

        # REAL-WORLD IMPORTED ROSTER DATABASE
        self.teams_database = {
            "HRC HONDA": {
                "RIDER_H1": {"name": "Jett Lawrence", "num": "18", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 21, "wins": 27, "championships": 3, "points": 0, "morale": 90, "ovr": 95, "trophies": 0},
                "RIDER_H2": {"name": "Hunter Lawrence", "num": "96", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 25, "wins": 8, "championships": 1, "points": 0, "morale": 88, "ovr": 91, "trophies": 0},
                "RIDER_H3": {"name": "Jo Shimoda", "num": "30", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 23, "wins": 5, "championships": 0, "points": 0, "morale": 85, "ovr": 88, "trophies": 0},
                "RIDER_H4": {"name": "Chance Hymas", "num": "10", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 20, "wins": 0, "championships": 0, "points": 0, "morale": 85, "ovr": 83, "trophies": 0},
                "RIDER_H5": {"name": "Carson Mumford", "num": "55", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 23, "wins": 0, "championships": 0, "points": 0, "morale": 80, "ovr": 78, "trophies": 0},
            },
            "MONSTER ENERGY YAMAHA": {
                "RIDER_Y1": {"name": "Haiden Deegan", "num": "38", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 20, "wins": 16, "championships": 3, "points": 0, "morale": 95, "ovr": 92, "trophies": 0},
                "RIDER_Y2": {"name": "Cooper Webb", "num": "02", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 30, "wins": 30, "championships": 3, "points": 0, "morale": 89, "ovr": 87, "trophies": 0},
                "RIDER_Y3": {"name": "Justin Cooper", "num": "32", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 27, "wins": 10, "championships": 1, "points": 0, "morale": 86, "ovr": 85, "trophies": 0},
                "RIDER_Y4": {"name": "Cole Davies", "num": "37", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 18, "wins": 4, "championships": 0, "points": 0, "morale": 87, "ovr": 86, "trophies": 0},
                "RIDER_Y5": {"name": "Max Anstie", "num": "61", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 32, "wins": 8, "championships": 0, "points": 0, "morale": 85, "ovr": 85, "trophies": 0},
                "RIDER_Y6": {"name": "Pierce Brown", "num": "163", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 24, "wins": 1, "championships": 0, "points": 0, "morale": 84, "ovr": 84, "trophies": 0},
                "RIDER_Y7": {"name": "Nate Thrasher", "num": "25", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 23, "wins": 5, "championships": 0, "points": 0, "morale": 83, "ovr": 83, "trophies": 0},
                "RIDER_Y8": {"name": "Michael Mosiman", "num": "23", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 26, "wins": 3, "championships": 0, "points": 0, "morale": 82, "ovr": 82, "trophies": 0},
                "RIDER_Y9": {"name": "Landen Gordon", "num": "180", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 19, "wins": 0, "championships": 0, "points": 0, "morale": 81, "ovr": 80, "trophies": 0},
                "RIDER_Y10": {"name": "Caden Dudney", "num": "82", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 18, "wins": 0, "championships": 0, "points": 0, "morale": 80, "ovr": 79, "trophies": 0},
            },
            "MONSTER ENERGY KAWASAKI": {
                "RIDER_K1": {"name": "Chase Sexton", "num": "04", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 26, "wins": 19, "championships": 2, "points": 0, "morale": 90, "ovr": 87, "trophies": 0},
                "RIDER_K2": {"name": "Garrett Marchbanks", "num": "36", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 24, "wins": 1, "championships": 0, "points": 0, "morale": 85, "ovr": 84, "trophies": 0},
                "RIDER_K3": {"name": "Levi Kitchen", "num": "47", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 24, "wins": 10, "championships": 0, "points": 0, "morale": 92, "ovr": 90, "trophies": 0},
                "RIDER_K4": {"name": "Seth Hammaker", "num": "10", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 25, "wins": 6, "championships": 1, "points": 0, "morale": 88, "ovr": 88, "trophies": 0},
                "RIDER_K5": {"name": "Cameron McAdoo", "num": "142", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 27, "wins": 4, "championships": 0, "points": 0, "morale": 85, "ovr": 85, "trophies": 0},
                "RIDER_K6": {"name": "Nicholas Romano", "num": "141", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 21, "wins": 0, "championships": 0, "points": 0, "morale": 84, "ovr": 84, "trophies": 0},
                "RIDER_K7": {"name": "Drew Adams", "num": "35", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 18, "wins": 0, "championships": 0, "points": 0, "morale": 82, "ovr": 80, "trophies": 0},
            },
            "REDBULL KTM": {
                "RIDER_KT1": {"name": "Jorge Prado", "num": "26", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 25, "wins": 0, "championships": 0, "points": 0, "morale": 94, "ovr": 92, "trophies": 0},
                "RIDER_KT2": {"name": "Eli Tomac", "num": "03", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 33, "wins": 52, "championships": 6, "points": 0, "morale": 91, "ovr": 90, "trophies": 0},
                "RIDER_KT3": {"name": "Aaron Plessinger", "num": "07", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 30, "wins": 4, "championships": 0, "points": 0, "morale": 89, "ovr": 86, "trophies": 0},
                "RIDER_KT4": {"name": "Julien Beaumer", "num": "13", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 19, "wins": 4, "championships": 0, "points": 0, "morale": 86, "ovr": 86, "trophies": 0},
            },
            "ROCKSTAR HUSQVARNA": {
                "RIDER_HQ1": {"name": "RJ Hampshire", "num": "24", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 29, "wins": 11, "championships": 1, "points": 0, "morale": 87, "ovr": 85, "trophies": 0},
                "RIDER_HQ2": {"name": "Malcolm Stewart", "num": "27", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 33, "wins": 2, "championships": 0, "points": 0, "morale": 85, "ovr": 84, "trophies": 0},
                "RIDER_HQ3": {"name": "Ryder DiFrancesco", "num": "34", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 20, "wins": 0, "championships": 0, "points": 0, "morale": 85, "ovr": 85, "trophies": 0},
                "RIDER_HQ4": {"name": "Daxton Bennick", "num": "58", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 19, "wins": 0, "championships": 0, "points": 0, "morale": 82, "ovr": 82, "trophies": 0},
                "RIDER_HQ5": {"name": "Casey Cochran", "num": "59", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 19, "wins": 0, "championships": 0, "points": 0, "morale": 80, "ovr": 79, "trophies": 0},
            },
            "TEAM TRIUMPH": {
                "RIDER_T1": {"name": "Jordon Smith", "num": "20", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 31, "wins": 13, "championships": 0, "points": 0, "morale": 84, "ovr": 83, "trophies": 0},
                "RIDER_T2": {"name": "Austin Forkner", "num": "33", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 27, "wins": 15, "championships": 0, "points": 0, "morale": 86, "ovr": 84, "trophies": 0},
                "RIDER_T3": {"name": "Jalek Swoll", "num": "21", "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": 25, "wins": 2, "championships": 0, "points": 0, "morale": 83, "ovr": 82, "trophies": 0},
            },
            "REDBULL DUCATI": {
                "RIDER_D1": {"name": "Justin Barcia", "num": "51", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 34, "wins": 17, "championships": 0, "points": 0, "morale": 86, "ovr": 85, "trophies": 0},
                "RIDER_D2": {"name": "Dylan Ferrandis", "num": "14", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 32, "wins": 8, "championships": 1, "points": 0, "morale": 85, "ovr": 84, "trophies": 0},
            },
            "FACTORY BETA": {
                "RIDER_B1": {"name": "Benny Bloss", "num": "60", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 28, "wins": 0, "championships": 0, "points": 0, "morale": 82, "ovr": 81, "trophies": 0},
                "RIDER_B2": {"name": "Mitchell Oldenburg", "num": "49", "class": "450", "status": "ACTIVE", "injury_weeks": 0, "age": 31, "wins": 0, "championships": 0, "points": 0, "morale": 80, "ovr": 78, "trophies": 0},
            }
        }

        self.current_viewing_team = None
        self.current_rider_key = None

        self.scouted_pool = []
        self.youth_academy = []
        self.free_agents_pool = []
        
        self.generate_weekly_scouts()
        self.generate_free_agents_market()

        self.create_main_menu()

    def calculate_machine_ovr(self, team_name):
        specs = self.team_garages[team_name]
        total = specs["SPE"] + specs["ACC"] + specs["DUR"] + specs["WGT"] + specs["SUP"]
        return round(total / 5.0, 1)

    def generate_weekly_scouts(self):
        self.scouted_pool = []
        for _ in range(10):
            name = f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
            age = random.randint(12, 16)
            true_dev = random.choices(range(1, 11), weights=[18, 16, 14, 12, 10, 9, 8, 6, 5, 2], k=1)[0]
            true_ovr = random.randint(35, 50) + (age - 12) * 2
            dev_low, dev_high = max(1, true_dev - 1), min(10, true_dev + 1)
            ovr_low, ovr_high = true_ovr - 3, true_ovr + 3
            self.scouted_pool.append({
                "name": name, "age": age, "true_dev": true_dev, "true_ovr": true_ovr,
                "dev_est": f"{dev_low}-{dev_high}", "ovr_est": f"{ovr_low}-{ovr_high}"
            })

    def generate_free_agents_market(self):
        self.free_agents_pool = []
        for _ in range(15):
            name = f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
            age = random.randint(16, 34)
            morale = random.randint(70, 99)
            ovr = random.randint(65, 92)
            rider_class = "450" if ovr > 78 or (ovr > 72 and random.choice([True, False])) else "250"
            
            base_value = int((ovr ** 2) * (140 - age) * 0.9)
            base_value = (base_value // 5000) * 5000  
            if base_value < 75000: base_value = 75000

            self.free_agents_pool.append({
                "name": name, "age": age, "morale": morale, "ovr": ovr,
                "class": rider_class, "value": base_value
            })

    # --- ADVANCED SIMULATION LOOP ENGINE ---

    def get_current_location_name(self):
        locations = {
            "SX": ["Anaheim 1", "San Diego", "Anaheim 2", "Glendale", "Oakland", "Seattle", "Arlington", "Daytona", "Indianapolis", "Detroit", "St. Louis", "Nashville", "Foxborough", "East Rutherford", "Pittsburgh", "Denver", "Las Vegas"],
            "MX": ["Fox Raceway", "Hangtown", "Thunder Valley", "High Point", "Southwick", "RedBud", "Spring Creek", "Washougal", "Unadilla", "Budds Creek", "Ironman"],
            "SMX": ["Charlotte Playoff 1", "Chicago Playoff 2", "Las Vegas World Finale"]
        }
        if self.calendar_phase in locations:
            return locations[self.calendar_phase][self.current_round - 1]
        return "N/A"

    def advance_simulation_week(self):
        play_sound("click")
        
        # 1. Update Injured Riders countdowns across all database entries
        for team_name, roster in self.teams_database.items():
            for r_key, r_data in roster.items():
                if r_data.get("injury_weeks", 0) > 0:
                    r_data["injury_weeks"] -= 1
                    if r_data["injury_weeks"] == 0:
                        r_data["status"] = "ACTIVE"

        # 2. Academy development rules
        for rider in self.youth_academy:
            if random.randint(1, 100) <= (rider["true_dev"] * 10):
                rider["true_ovr"] += random.randint(1, 3)
            if random.randint(1, 52) == 1: rider["age"] += 1

        self.generate_weekly_scouts()
        if random.randint(1, 2) == 1: self.generate_free_agents_market()

        # Handle Break Phase Logic / Transition Logic directly without running races
        if self.calendar_phase == "OFF-SEASON":
            if self.current_round == 3:
                self.calendar_phase = "SX"
                self.current_round = 1
                messagebox.showinfo("Season Started", f"Welcome to the {self.current_year} Supercross Season Championship!")
                self.create_rider_menu()
                return
            else:
                self.current_round += 1
                messagebox.showinfo("Off-Season Progress", f"Moved to Off-Season Week {self.current_round}.")
                self.create_rider_menu()
                return
        
        elif self.calendar_phase == "SX-BREAK":
            self.calendar_phase = "MX"
            self.current_round = 1
            messagebox.showinfo("Championship Transition", "Transitioning to Motocross Nationals Pro Season!")
            self.create_rider_menu()
            return
            
        elif self.calendar_phase == "MX-BREAK":
            self.calendar_phase = "SMX"
            self.current_round = 1
            messagebox.showinfo("Championship Transition", "Transitioning into SuperMotocross (SMX) Championship Playoffs!")
            self.create_rider_menu()
            return

        # Trigger simulated loading sequence animation for Race Weeks
        self.show_loading_simulation_screen()

    def show_loading_simulation_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="SIMULATING WEEKLY EVENTS", font=("Arial", 18, "bold"), fg="#ffffff", bg="#1a1a1a", pady=60).pack()
        
        lbl_action = tk.Label(self.root, text="Processing track setup configs...", font=("Courier", 11), fg="#ff9900", bg="#1a1a1a")
        lbl_action.pack(pady=10)

        progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        progress.pack(pady=20)

        def step_loading(val):
            if val <= 100:
                progress['value'] = val
                if val == 30: lbl_action.config(text="Calculating engine specs and tire adjustments...")
                if val == 65: lbl_action.config(text="Evaluating roster mechanics and tracking injury safety zones...")
                if val == 90: lbl_action.config(text="Finalizing checkered flag tallies...")
                self.root.after(15, lambda: step_loading(val + 5))
            else:
                play_sound("success")
                lbl_action.config(text="SIMULATION COMPLETE!", fg="#55ff55")
                tk.Button(self.root, text="VIEW RESULTS", font=("Arial", 12, "bold"), bg="#55ff55", fg="#000000", width=18, command=self.process_race_and_events).pack(pady=30)

        step_loading(0)

    def process_race_and_events(self):
        # 1. Run simulation calculations
        results_450, results_250 = self.simulate_class_race("450"), self.simulate_class_race("250")
        events_logged = self.simulate_injuries_and_bikes()

        # Update points allocation values based on placement finish ranks
        for idx, r_data in enumerate(results_450[:16]):
            r_data["points"] = r_data.get("points", 0) + self.points_system[idx]
        for idx, r_data in enumerate(results_250[:16]):
            r_data["points"] = r_data.get("points", 0) + self.points_system[idx]

        if results_450: results_450[0]["wins"] += 1
        if results_250: results_250[0]["wins"] += 1

        # 2. Advance the actual Calendar tracking values
        round_ended = False
        if self.calendar_phase == "SX" and self.current_round == 17:
            self.award_championship_trophy("SX")
            self.calendar_phase = "SX-BREAK"
            self.current_round = 1
            round_ended = True
        elif self.calendar_phase == "MX" and self.current_round == 11:
            self.award_championship_trophy("MX")
            self.calendar_phase = "MX-BREAK"
            self.current_round = 1
            round_ended = True
        elif self.calendar_phase == "SMX" and self.current_round == 3:
            self.award_championship_trophy("SMX")
            self.calendar_phase = "OFF-SEASON"
            self.current_round = 1
            self.current_year += 1
            round_ended = True
        else:
            self.current_round += 1

        # 3. Present Results Screen UI Dashboard
        self.display_race_results_dashboard(results_450, results_250, events_logged, round_ended)

    def simulate_class_race(self, rider_class):
        riders_pool = []
        for team_name, roster in self.teams_database.items():
            machine_bonus = self.calculate_machine_ovr(team_name) * 1.5
            for r_key, r_data in roster.items():
                if r_data["class"] == rider_class and r_data["status"] == "ACTIVE":
                    ovr = r_data.get("ovr", 75)
                    
                    # Target tier parameters derived directly from performance graph rules
                    if ovr >= 90: weight = 95
                    elif ovr >= 85: weight = 80
                    elif ovr >= 81: weight = 65
                    elif ovr >= 76: weight = 50
                    elif ovr >= 71: weight = 35
                    else: weight = 15

                    score = (ovr * 1.2) + weight + machine_bonus + random.uniform(10, 85)
                    riders_pool.append((score, r_data, team_name))
        
        riders_pool.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in riders_pool]

    def simulate_injuries_and_bikes(self):
        logs = []
        for team_name, roster in self.teams_database.items():
            dur_stat = self.team_garages[team_name]["DUR"]
            # Protection modifier scale rule reduction factor based on team's engineering tier levels
            dur_mod = 1.0 - ((dur_stat - 1) * 0.15) 

            # A. Rider Injury Events checks
            for r_key, r_data in roster.items():
                if r_data["status"] == "ACTIVE":
                    roll = random.uniform(0, 100)
                    if roll <= (0.5 * dur_mod): # Extreme
                        w = random.randint(10, 16)
                        r_data["status"] = f"INJURED ({w} Wks)"
                        r_data["injury_weeks"] = w
                        logs.append(f"🔴 EXTREME: {r_data['name']} ({team_name}) suffered a major crash. Out for {w} weeks!")
                    elif roll <= ((0.5 + 2.0) * dur_mod): # Major
                        w = random.randint(6, 10)
                        r_data["status"] = f"INJURED ({w} Wks)"
                        r_data["injury_weeks"] = w
                        logs.append(f"🟠 MAJOR: {r_data['name']} ({team_name}) broke a collarbone/arm. Out for {w} weeks!")
                    elif roll <= ((2.5 + 4.0) * dur_mod): # Medium
                        w = random.randint(3, 5)
                        r_data["status"] = f"INJURED ({w} Wks)"
                        r_data["injury_weeks"] = w
                        logs.append(f"🟡 MEDIUM: {r_data['name']} ({team_name}) suffered joint/hand issues. Out for {w} weeks!")
                    elif roll <= ((6.5 + 8.0) * dur_mod): # Minor
                        w = random.randint(1, 2)
                        r_data["status"] = f"INJURED ({w} Wks)"
                        r_data["injury_weeks"] = w
                        logs.append(f"⚪ MINOR: {r_data['name']} ({team_name}) sprained a wrist/ankle. Out for {w} weeks.")

            # B. Mechanical Breakdown Events checks
            roll_bike = random.uniform(0, 100)
            triggered_issue = None
            if roll_bike <= (1.0 * dur_mod): triggered_issue = "EXTREME ENGINE/CHASSIS BLOW"
            elif roll_bike <= ((1.0 + 3.0) * dur_mod): triggered_issue = "MAJOR TRANSMISSION SLIP"
            elif roll_bike <= ((4.0 + 6.0) * dur_mod): triggered_issue = "MEDIUM ENGINE MISFIRE"
            elif roll_bike <= ((10.0 + 10.0) * dur_mod): triggered_issue = "MINOR BRAKE FADE/CHAIN ISSUE"

            if triggered_issue:
                stat_target = random.choice(["SPE", "ACC", "DUR", "SUP"])
                if self.team_garages[team_name][stat_target] > 1:
                    self.team_garages[team_name][stat_target] -= 1
                    logs.append(f"🔧 MECHANICAL: {team_name} hit by a {triggered_issue}! -1 {stat_target} penalty applied.")
        return logs

    def award_championship_trophy(self, series_name):
        champ_450, champ_250 = None, None
        max_450, max_250 = -1, -1

        for team_name, roster in self.teams_database.items():
            for r_data in roster.values():
                if r_data["class"] == "450" and r_data.get("points", 0) > max_450:
                    max_450 = r_data["points"]
                    champ_450 = r_data
                if r_data["class"] == "250" and r_data.get("points", 0) > max_250:
                    max_250 = r_data["points"]
                    champ_250 = r_data

        if champ_450:
            champ_450["championships"] += 1
            champ_450["trophies"] = champ_450.get("trophies", 0) + 1
        if champ_250:
            champ_250["championships"] += 1
            champ_250["trophies"] = champ_250.get("trophies", 0) + 1

        messagebox.showinfo("CHAMPIONSHIP COMPLETED", 
                            f"🏆 {series_name} Season Champions Crowned!\n\n"
                            f"450cc Winner: {champ_450['name'] if champ_450 else 'N/A'} ({max_450} pts)\n"
                            f"250cc Winner: {champ_250['name'] if champ_250 else 'N/A'} ({max_250} pts)\n\n"
                            f"All championship points tracking registers have been reset for the next division round.")

        # Reset points after every championship phase sequence
        for roster in self.teams_database.values():
            for r_data in roster.values():
                r_data["points"] = 0

    def display_race_results_dashboard(self, r450, r250, logs, round_ended):
        self.clear_screen()
        
        title_str = f"RACE RESULTS – {self.get_current_location_name()}" if not round_ended else "FINALE ROUND WEEK COMPLETE"
        tk.Label(self.root, text=title_str, font=("Arial", 18, "bold"), fg="#ff9900", bg="#1a1a1a", pady=10).pack()

        # Class Standings Podiums Grid Splitting
        grid_frame = tk.Frame(self.root, bg="#1a1a1a")
        grid_frame.pack(fill="x", padx=20, pady=5)

        # 450 Podium Column Display UI 
        f450 = tk.Frame(grid_frame, bg="#222222", bd=1, relief="solid", padx=10, pady=10)
        f450.pack(side="left", fill="both", expand=True, padx=5)
        tk.Label(f450, text="450 RESULTS", font=("Arial", 12, "bold"), fg="#ffff55", bg="#222222").pack(anchor="w")
        for idx in range(min(5, len(r450))):
            col = "#ffcc00" if idx == 0 else "#ffffff"
            tk.Label(f450, text=f"{idx+1}. {r450[idx]['name']} (#{r450[idx]['num']})", font=("Courier", 10, "bold"), fg=col, bg="#222222").pack(anchor="w", pady=2)

        # 250 Podium Column Display UI
        f250 = tk.Frame(grid_frame, bg="#222222", bd=1, relief="solid", padx=10, pady=10)
        f250.pack(side="right", fill="both", expand=True, padx=5)
        tk.Label(f250, text="250 RESULTS", font=("Arial", 12, "bold"), fg="#ffff55", bg="#222222").pack(anchor="w")
        for idx in range(min(5, len(r250))):
            col = "#ffcc00" if idx == 0 else "#ffffff"
            tk.Label(f250, text=f"{idx+1}. {r250[idx]['name']} (#{r250[idx]['num']})", font=("Courier", 10, "bold"), fg=col, bg="#222222").pack(anchor="w", pady=2)

        # Player Owned Team Performance Highlights
        f_player = tk.Frame(self.root, bg="#2d2d2d", padx=15, pady=8, bd=1, relief="groove")
        f_player.pack(fill="x", padx=25, pady=10)
        tk.Label(f_player, text="YOUR TEAM STABLE SUMMARY", font=("Arial", 11, "bold"), fg="#55ff55", bg="#2d2d2d").pack(anchor="w")
        
        # Crosscheck finished fields
        for r_class, plist in [("450", r450), ("250", r250)]:
            for rank, r_data in enumerate(plist, 1):
                if any(r_data["name"] == d["name"] for d in self.teams_database[self.player_team].values()):
                    tk.Label(f_player, text=f"• ({r_class}cc) {r_data['name']} finished P{rank} -> Earned +{self.points_system[rank-1] if rank<=16 else 0} pts", 
                             font=("Courier", 10), fg="#ffffff", bg="#2d2d2d").pack(anchor="w")

        # System Tracking Log Window Panel
        tk.Label(self.root, text="TRACK INCIDENTS & BREAKDOWNS", font=("Arial", 12, "bold"), fg="#ff5555", bg="#1a1a1a").pack(pady=(10, 2))
        log_box = tk.Text(self.root, bg="#111111", fg="#cccccc", font=("Courier", 9), height=10, padx=10, pady=10, relief="flat")
        log_box.pack(fill="both", expand=True, padx=25, pady=5)
        
        if not logs:
            log_box.insert("end", "Clear race weekend. No critical rider injuries or major mechanical structural failures reported.")
        else:
            for entry in logs: log_box.insert("end", f"{entry}\n")
        log_box.config(state="disabled")

        tk.Button(self.root, text="CONTINUE TO MANAGEMENT", font=("Arial", 12, "bold"), bg="#ff9900", fg="#000000", width=25, command=self.create_rider_menu).pack(pady=20)

    # --- LEADERBOARDS GATEWAY LAYOUTS ---

    def check_forced_youth_promotions(self):
        for idx, rider in enumerate(list(self.youth_academy)):
            if rider["age"] >= 18:
                play_sound("warning")
                choice = messagebox.askyesno("Forced Graduation", f"{rider['name']} has reached 18!\nPromote to 250 squad?\n(No will release them).")
                if choice: self.execute_promotion_flow(idx, forced=True)
                else:
                    play_sound("danger")
                    self.youth_academy.pop(idx)
                self.check_forced_youth_promotions()
                break

    def clear_screen(self):
        for widget in self.root.winfo_children(): widget.destroy()

    def create_main_menu(self):
        self.clear_screen()
        title = tk.Label(self.root, text="MOTOCROSS SIMULATION", font=("Arial", 24, "bold"), fg="#ffffff", bg="#1a1a1a", pady=40)
        title.pack()
        
        tk.Button(self.root, text="NEW GAME", font=("Arial", 14, "bold"), width=20, height=2, bg="#333333", fg="#ffffff", command=self.create_team_select_menu).pack(pady=10)
        tk.Button(self.root, text="LOAD GAME", font=("Arial", 14, "bold"), width=20, height=2, bg="#333333", fg="#ffffff", command=lambda: [play_sound("click"), messagebox.showinfo("Load Game", "No local save profiles detected. Start a New Game!")]).pack(pady=10)
        tk.Button(self.root, text="QUIT", font=("Arial", 14, "bold"), width=20, height=2, bg="#aa2222", fg="#ffffff", command=self.root.quit).pack(pady=10)

    def create_team_select_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="SELECT YOUR TEAM", font=("Arial", 20, "bold"), fg="#ffffff", bg="#1a1a1a", pady=30).pack()
        for team_name in self.teams_database.keys():
            tk.Button(self.root, text=team_name, font=("Arial", 11, "bold"), width=30, bg="#2a2a2a", fg="#ffffff", command=lambda n=team_name: [play_sound("success"), self.select_player_team_action(n)]).pack(pady=5)

    def select_player_team_action(self, team_name):
        self.player_team = team_name
        self.create_rider_menu()

    def create_rider_menu(self):
        self.clear_screen()
        
        # Phase formatting titles setup 
        phase_map = {"SX": "Supercross", "SX-BREAK": "Mid-Season Break", "MX": "Motocross Nationals", "MX-BREAK": "SMX Playoff Prep Break", "SMX": "SuperMotocross Playoffs", "OFF-SEASON": "Off-Season Phase"}
        current_phase_title = phase_map[self.calendar_phase]

        tk.Label(self.root, text="MAIN MANAGEMENT HUB", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=15).pack()
        
        # Calendar Status Progress Bar Header Box
        cal_box = tk.Frame(self.root, bg="#ff9900", padx=15, pady=8, bd=1, relief="solid")
        cal_box.pack(fill="x", padx=40, pady=(0, 15))
        
        cal_str = f"YEAR: {self.current_year}  |  {current_phase_title.upper()}  |  WEEK/ROUND: {self.current_round}"
        tk.Label(cal_box, text=cal_str, font=("Courier", 11, "bold"), fg="#000000", bg="#ff9900").pack()

        btn_adv_text = "SIMULATE NEXT RACE" if self.calendar_phase in ["SX", "MX", "SMX"] else "ADVANCE SCHEDULE WEEK"
        tk.Button(self.root, text=btn_adv_text, font=("Arial", 16, "bold"), width=24, height=2, bg="#55ff55", fg="#000000", command=self.advance_simulation_week).pack(pady=(5, 15))
        
        tk.Button(self.root, text="TEAM ROSTER", font=("Arial", 14, "bold"), width=22, height=2, bg="#333333", fg="#ffffff", command=self.create_roster_options_menu).pack(pady=6)
        tk.Button(self.root, text="GARAGE", font=("Arial", 14, "bold"), width=22, height=2, bg="#333333", fg="#ffffff", command=self.create_garage_screen).pack(pady=6)
        tk.Button(self.root, text="FREE AGENCY", font=("Arial", 14, "bold"), width=22, height=2, bg="#333333", fg="#ffffff", command=self.create_free_agency_screen).pack(pady=6)
        tk.Button(self.root, text="LEADERBOARDS", font=("Arial", 14, "bold"), width=22, height=2, bg="#333333", fg="#ffffff", command=self.create_leaderboards_hub).pack(pady=6)
        tk.Button(self.root, text="SAVE AND EXIT", font=("Arial", 14, "bold"), width=22, height=2, bg="#aa2222", fg="#ffffff", command=self.create_main_menu).pack(pady=6)

        # Status Panel Widget
        info_frame = tk.Frame(self.root, bg="#222222", bd=2, relief="groove", padx=15, pady=12)
        info_frame.pack(fill="x", padx=40, pady=(15, 0))
        tk.Label(info_frame, text=f"TEAM NAME: {self.player_team}", font=("Arial", 11, "bold"), fg="#ff9900", bg="#222222").pack(anchor="w")
        tk.Label(info_frame, text=f"TEAM BALANCE: ${self.team_balances[self.player_team]:,}", font=("Arial", 11), fg="#ffffff", bg="#222222").pack(anchor="w", pady=(3, 3))
        
        line = tk.Frame(info_frame, bg="#222222")
        line.pack(fill="x")
        tk.Label(line, text=f"ENGINEERING OVR: {self.calculate_machine_ovr(self.player_team)}/5.0", font=("Arial", 11), fg="#888888", bg="#222222").pack(side="left")

    def create_leaderboards_hub(self):
        play_sound("click")
        self.clear_screen()
        
        tk.Label(self.root, text="LEADERBOARDS HUB", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=40).pack()
        
        tk.Button(self.root, text="TEAM RANKINGS", font=("Arial", 14, "bold"), width=24, height=2, bg="#333333", fg="#ffffff", command=self.create_team_rankings_screen).pack(pady=12)
        tk.Button(self.root, text="THE CHAMPIONSHIP", font=("Arial", 14, "bold"), width=24, height=2, bg="#333333", fg="#ffffff", command=self.create_championship_selection_screen).pack(pady=12)
        
        tk.Button(self.root, text="BACK TO MAIN MENU", font=("Arial", 11, "bold"), width=24, bg="#aa2222", fg="#ffffff", command=self.create_rider_menu).pack(pady=40)

    def create_team_rankings_screen(self):
        play_sound("click")
        self.clear_screen()
        
        tk.Label(self.root, text="TEAM RANKINGS", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=20).pack()
        tk.Label(self.root, text="Standings based on engineering and upgrade evaluations", font=("Arial", 11, "italic"), fg="#aaaaaa", bg="#1a1a1a").pack(pady=(0, 15))

        board_box = tk.Frame(self.root, bg="#222222", padx=20, pady=20, bd=2, relief="groove")
        board_box.pack(fill="both", expand=True, padx=40, pady=10)

        rankings = [(name, self.calculate_machine_ovr(name)) for name in self.teams_database.keys()]
        rankings.sort(key=lambda x: x[1], reverse=True)

        for rank, (team_name, ovr) in enumerate(rankings, 1):
            row = tk.Frame(board_box, bg="#2d2d2d" if team_name == self.player_team else "#222222", pady=6, padx=10)
            row.pack(fill="x", pady=2)

            color = "#ff9900" if team_name == self.player_team else "#ffffff"
            lbl_rank = tk.Label(row, text=f"#{rank} ".ljust(5), font=("Courier", 12, "bold"), fg="#ffcc00", bg=row.cget("bg"))
            lbl_rank.pack(side="left")

            lbl_name = tk.Label(row, text=f"{team_name.ljust(28)}", font=("Courier", 11, "bold"), fg=color, bg=row.cget("bg"))
            lbl_name.pack(side="left")

            lbl_ovr = tk.Label(row, text=f"MACHINE OVR: {ovr}/5.0", font=("Courier", 11), fg="#55ff55", bg=row.cget("bg"))
            lbl_ovr.pack(side="right")

        tk.Button(self.root, text="BACK", font=("Arial", 11, "bold"), width=15, bg="#555555", fg="#ffffff", command=self.create_leaderboards_hub).pack(pady=20)

    def create_championship_selection_screen(self):
        play_sound("click")
        self.clear_screen()
        
        tk.Label(self.root, text="THE CHAMPIONSHIP STANDINGS", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=40).pack()
        
        tk.Button(self.root, text="450 STANDINGS", font=("Arial", 14, "bold"), width=22, height=2, bg="#ff9900", fg="#000000", command=lambda: self.create_rider_standings_screen("450")).pack(pady=15)
        tk.Button(self.root, text="250 STANDINGS", font=("Arial", 14, "bold"), width=22, height=2, bg="#ff9900", fg="#000000", command=lambda: self.create_rider_standings_screen("250")).pack(pady=15)
        
        tk.Button(self.root, text="BACK", font=("Arial", 11, "bold"), width=15, bg="#555555", fg="#ffffff", command=self.create_leaderboards_hub).pack(pady=30)

    def create_rider_standings_screen(self, target_class):
        play_sound("click")
        self.clear_screen()
        
        tk.Label(self.root, text=f"{target_class}cc CURRENT STANDINGS", font=("Arial", 20, "bold"), fg="#ffffff", bg="#1a1a1a", pady=15).pack()

        container = tk.Frame(self.root, bg="#1a1a1a")
        container.pack(fill="both", expand=True, padx=25, pady=5)

        canvas = tk.Canvas(container, bg="#1a1a1a", highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#1a1a1a")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        rider_list = []
        for team_name, roster in self.teams_database.items():
            for r_key, r_data in roster.items():
                if r_data["class"] == target_class:
                    rider_list.append((r_data, team_name))
        
        rider_list.sort(key=lambda x: x[0].get("points", 0), reverse=True)

        for position, (rider, team_name) in enumerate(rider_list, 1):
            row = tk.Frame(scrollable_frame, bg="#2d2d2d" if team_name == self.player_team else "#222222", pady=6, padx=12, bd=1, relief="solid")
            row.pack(fill="x", width=640, pady=2)

            color = "#ff9900" if team_name == self.player_team else "#ffffff"
            
            pos_str = f"#{position} ".ljust(5)
            main_str = f"{rider['name'].ljust(22)} #{rider['num'].ljust(4)} TEAM: {team_name.ljust(25)} PTS {str(rider.get('points', 0)).zfill(3)} | CHIPS: {rider.get('championships', 0)}"

            tk.Label(row, text=pos_str, font=("Courier", 11, "bold"), fg="#ffcc00", bg=row.cget("bg")).pack(side="left")
            tk.Label(row, text=main_str, font=("Courier", 9, "bold"), fg=color, bg=row.cget("bg")).pack(side="left")

        tk.Button(self.root, text="BACK TO SELECTION", font=("Arial", 11, "bold"), width=20, bg="#aa2222", fg="#ffffff", command=self.create_championship_selection_screen).pack(pady=15)

    # --- FREE AGENCY SYSTEM ---

    def create_free_agency_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="PRO FREE AGENCY MARKET", font=("Arial", 20, "bold"), fg="#ffffff", bg="#1a1a1a", pady=10).pack()

        bal_bar = tk.Frame(self.root, bg="#222222", padx=15, pady=6, bd=1, relief="solid")
        bal_bar.pack(fill="x", padx=20, pady=5)
        tk.Label(bal_bar, text=f"Team Funds: ${self.team_balances[self.player_team]:,}", font=("Arial", 11, "bold"), fg="#55ff55", bg="#222222").pack(side="left")
        tk.Label(bal_bar, text="Market Size: 15 Available Contractors", font=("Arial", 11, "italic"), fg="#cccccc", bg="#222222").pack(side="right")

        container = tk.Frame(self.root, bg="#1a1a1a")
        container.pack(fill="both", expand=True, padx=15, pady=5)

        canvas = tk.Canvas(container, bg="#1a1a1a", highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#1a1a1a")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for idx, rider in enumerate(self.free_agents_pool):
            row = tk.Frame(scrollable_frame, bg="#222222", pady=6, padx=10, bd=1, relief="raised")
            row.pack(fill="x", width=660, pady=3)

            info_str = f"{rider['name'].ljust(22)} ({rider['class']}cc)  |  MOR {rider['morale']}%  |  AGE {rider['age']}  |  OVR {rider['ovr']}  |  ${rider['value']:,}"
            tk.Label(row, text=info_str, font=("Courier", 9, "bold"), fg="#ffffff", bg="#222222").pack(side="left")

            btn_negotiate = tk.Button(row, text="SIGN", font=("Arial", 8, "bold"), bg="#55ff55", fg="#000000", width=8,
                                      command=lambda i=idx: self.negotiate_contract_flow(i))
            btn_negotiate.pack(side="right")

        tk.Button(self.root, text="BACK TO MAIN MENU", font=("Arial", 11, "bold"), width=22, bg="#aa2222", fg="#ffffff", command=self.create_rider_menu).pack(pady=15)

    def negotiate_contract_flow(self, idx):
        play_sound("click")
        rider = self.free_agents_pool[idx]
        
        offer = simpledialog.askinteger(
            "Contract Negotiations",
            f"Rider: {rider['name']} (OVR {rider['ovr']})\n"
            f"Market Demands value: ${rider['value']:,}\n\n"
            f"Enter your financial offer ($):"
        )

        if offer is None: return  

        if offer > self.team_balances[self.player_team]:
            play_sound("warning")
            messagebox.showwarning("Insufficient Funds", "You cannot offer more money than your current team banking account hold!")
            return

        ratio = offer / float(rider["value"])
        
        if ratio < 0.75:
            play_sound("danger")
            messagebox.showerror("Offer Rejected", f"{rider['name']}: \"That offer is an insult to my career. No deal.\"")
            return
        elif ratio >= 1.20:
            success_rate = 95
        elif ratio >= 1.0:
            success_rate = 70 + int((ratio - 1.0) * 100)  
        else:
            success_rate = int((ratio - 0.75) * 4 * 70)  

        success_rate = max(5, min(success_rate, 95))

        if random.randint(1, 100) <= success_rate:
            play_sound("success")
            self.team_balances[self.player_team] -= offer
            self.free_agents_pool.pop(idx)  
            
            messagebox.showinfo("Deal Accepted!", f"Success! {rider['name']} accepted your contract offer for ${offer:,}!")
            self.assign_purchased_rider_number(rider)
        else:
            play_sound("warning")
            messagebox.showwarning("Offer Rejected", f"{rider['name']} turned down your contract configuration. They want closer to their estimated valuation.")
        
        self.create_free_agency_screen()

    def assign_purchased_rider_number(self, rider_data):
        while True:
            num = simpledialog.askstring("Assign Roster Number", f"Assign a 2-digit number for your new signing ({rider_data['name']}):")
            if not num: 
                num = str(random.randint(10, 99))
                messagebox.showinfo("Auto Number assigned", f"No number provided. Registered default #{num}.")

            num = num.strip().zfill(2)
            taken = any(d["num"] == num for d in self.teams_database[self.player_team].values())

            if taken:
                play_sound("warning")
                messagebox.showwarning("Number Taken", "That bike profile number is already claimed on your roster squad! Select another.")
            else:
                new_key = f"RIDER_FA_{random.randint(10000, 99999)}"
                self.teams_database[self.player_team][new_key] = {
                    "name": rider_data["name"], "num": num, "class": rider_data["class"],
                    "status": "ACTIVE", "injury_weeks": 0, "age": rider_data["age"], "wins": 0, "championships": 0, "points": 0,
                    "morale": rider_data["morale"], "ovr": rider_data["ovr"]
                }
                play_sound("success")
                messagebox.showinfo("Roster Updated", f"{rider_data['name']} has officially hit the tracks under your colors on bike #{num}!")
                break

    # --- GARAGE DECK ---

    def create_garage_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="TEAM FACTORY GARAGE", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=15).pack()

        header = tk.Frame(self.root, bg="#222222", padx=15, pady=8, bd=1, relief="solid")
        header.pack(fill="x", padx=30, pady=5)
        tk.Label(header, text=f"Available Funds: ${self.team_balances[self.player_team]:,}", font=("Arial", 12, "bold"), fg="#55ff55", bg="#222222").pack(side="left")
        tk.Label(header, text=f"MACHINE QUALITY OVR: {self.calculate_machine_ovr(self.player_team)}/5.0", font=("Arial", 12, "bold"), fg="#ff9900", bg="#222222").pack(side="right")

        specs_box = tk.Frame(self.root, bg="#1a1a1a", pady=10)
        specs_box.pack(fill="both", expand=True, padx=40)
        specs = self.team_garages[self.player_team]
        
        for sk, name in [("SPE", "SPEED (SPE)"), ("ACC", "ACCELERATION (ACC)"), ("DUR", "DURABILITY (DUR)"), ("WGT", "WEIGHT (WGT)"), ("SUP", "SUSPENSION (SUP)")]:
            row = tk.Frame(specs_box, bg="#262626", pady=8, padx=12, bd=1, relief="groove")
            row.pack(fill="x", pady=4)
            
            c_val = specs[sk]
            tk.Label(row, text=f"{name.ljust(22)} {c_val}/5", font=("Courier", 12, "bold"), fg="#ffffff", bg="#262626").pack(side="left")

            if c_val < 5:
                cost = self.upgrade_costs[c_val]
                b_text = f"UPGRADE (+${cost:,})"
                b_state, b_bg = "normal", "#ff9900"
            else:
                b_text, b_state, b_bg = "MAX LEVEL", "disabled", "#555555"

            tk.Button(row, text=b_text, font=("Arial", 9, "bold"), bg=b_bg, fg="#000000", state=b_state, width=22, command=lambda k=sk: self.purchase_stat_upgrade(k)).pack(side="right")

        exp = tk.Frame(self.root, bg="#222222", bd=2, relief="sunken", padx=15, pady=10)
        exp.pack(fill="x", padx=30, pady=10)
        tk.Label(exp, text="MANUAL MANUAL MECHANICS INFO", font=("Arial", 10, "bold"), fg="#ff9900", bg="#222222").pack(anchor="w")
        tk.Label(exp, text="• Speed: General power limits.\n• Acceleration: Rocket off the starting grid.\n• Durability: Critical prevention filter against mechanical breakdown hazards.\n• Weight: Flight and corner control.\n• Suspension: Track cushion adjustments.", font=("Arial", 9), fg="#cccccc", bg="#222222", justify="left").pack(anchor="w")

        tk.Button(self.root, text="BACK TO MAIN MENU", font=("Arial", 11, "bold"), width=22, bg="#aa2222", fg="#ffffff", command=self.create_rider_menu).pack(pady=15)

    def purchase_stat_upgrade(self, sk):
        c_val = self.team_garages[self.player_team][sk]
        if c_val >= 5: return
        cost = self.upgrade_costs[c_val]
        if self.team_balances[self.player_team] < cost:
            play_sound("warning")
            messagebox.showwarning("Insufficient Funds", "Not enough capital!")
            return
        self.team_balances[self.player_team] -= cost
        self.team_garages[self.player_team][sk] += 1
        play_sound("success")
        self.create_garage_screen()

    # --- ROSTER SUITE ---

    def create_roster_options_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="TEAM ROSTER OPTIONS", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=40).pack()
        tk.Button(self.root, text="YOUR TEAM", font=("Arial", 14, "bold"), width=22, height=2, bg="#333333", fg="#ffffff", command=self.create_your_team_roster).pack(pady=10)
        tk.Button(self.root, text="OTHER TEAMS", font=("Arial", 14, "bold"), width=22, height=2, bg="#333333", fg="#ffffff", command=self.create_other_teams_menu).pack(pady=10)
        tk.Button(self.root, text="YOUTH MANAGEMENT", font=("Arial", 14, "bold"), width=22, height=2, bg="#333333", fg="#ffffff", command=self.create_youth_management_hub).pack(pady=10)
        tk.Button(self.root, text="EXIT", font=("Arial", 14, "bold"), width=22, height=2, bg="#aa2222", fg="#ffffff", command=self.create_rider_menu).pack(pady=10)

    def create_youth_management_hub(self):
        self.clear_screen()
        tk.Label(self.root, text="YOUTH MANAGEMENT", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=40).pack()
        tk.Button(self.root, text="SCOUT YOUTH RIDERS", font=("Arial", 14, "bold"), width=24, height=2, bg="#333333", fg="#ffffff", command=self.create_scout_riders_screen).pack(pady=12)
        tk.Button(self.root, text="MANAGE YOUTH ROSTER", font=("Arial", 14, "bold"), width=24, height=2, bg="#333333", fg="#ffffff", command=self.create_manage_youth_roster_screen).pack(pady=12)
        tk.Button(self.root, text="EXIT", font=("Arial", 14, "bold"), width=24, height=2, bg="#aa2222", fg="#ffffff", command=self.create_roster_options_menu).pack(pady=12)

    def create_scout_riders_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="SCOUT YOUTH RIDERS", font=("Arial", 20, "bold"), fg="#ffffff", bg="#1a1a1a", pady=15).pack()
        spots = len(self.youth_academy)
        tk.Label(self.root, text=f"Academy Spots Filled: {spots}/5", font=("Arial", 12, "bold"), fg="#ff9900" if spots < 5 else "#ff5555", bg="#1a1a1a").pack(pady=(0, 10))

        frame = tk.Frame(self.root, bg="#1a1a1a")
        frame.pack(fill="both", expand=True, padx=15)
        for idx, r in enumerate(self.scouted_pool):
            row = tk.Frame(frame, bg="#222222", bd=1, relief="raised", padx=10, pady=5)
            row.pack(fill="x", pady=3)
            txt = f"{r['name'].ljust(25)} AGE: {r['age']}   DEV: {r['dev_est']}   OVR: {r['ovr_est']}"
            tk.Label(row, text=txt, font=("Courier", 10, "bold"), fg="#ffffff", bg="#222222").pack(side="left")
            tk.Button(row, text="SIGN", font=("Arial", 9, "bold"), bg="#55ff55", fg="#000000", width=8, command=lambda i=idx: self.sign_youth_prospect(i)).pack(side="right")

        tk.Button(self.root, text="BACK", font=("Arial", 10, "bold"), width=12, bg="#555555", fg="#ffffff", command=self.create_youth_management_hub).pack(pady=20)

    def sign_youth_prospect(self, index):
        if len(self.youth_academy) >= 5:
            play_sound("warning")
            messagebox.showwarning("Academy Full", "Your Youth Academy is full!")
            return
        play_sound("success")
        p = self.scouted_pool.pop(index)
        p["wins"], p["championships"], p["points"] = 0, 0, 0
        self.youth_academy.append(p)
        self.create_scout_riders_screen()

    def create_manage_youth_roster_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="YOUTH ACADEMY ROSTER", font=("Arial", 20, "bold"), fg="#ffffff", bg="#1a1a1a", pady=20).pack()
        if not self.youth_academy:
            tk.Label(self.root, text="[ Academy Vacant ]", font=("Arial", 13, "italic"), fg="#888888", bg="#1a1a1a").pack(pady=40)
        else:
            for idx, r in enumerate(self.youth_academy):
                row = tk.Frame(self.root, bg="#222222", bd=2, relief="groove", pady=8, padx=10)
                row.pack(fill="x", padx=15, pady=5)
                tk.Label(row, text=f"{r['name']} | AGE: {r['age']} | DEV: {r['true_dev']}/10 | OVR: {r['true_ovr']}", font=("Arial", 11, "bold"), fg="#ff9900", bg="#222222").pack(side="left")
                f = tk.Frame(row, bg="#222222")
                f.pack(side="right")
                tk.Button(f, text="PROMOTE", font=("Arial", 9, "bold"), bg="#55ff55", fg="#000000", width=9, command=lambda i=idx: self.execute_promotion_flow(i)).pack(side="left", padx=2)
                tk.Button(f, text="CUT", font=("Arial", 9, "bold"), bg="#aa2222", fg="#ffffff", width=6, command=lambda i=idx: self.cut_youth_rider(i)).pack(side="left", padx=2)

        tk.Button(self.root, text="BACK", font=("Arial", 10, "bold"), width=12, bg="#555555", fg="#ffffff", command=self.create_youth_management_hub).pack(pady=30)

    def execute_promotion_flow(self, index, forced=False):
        rider = self.youth_academy[index]
        if rider["age"] < 16 and not forced:
            play_sound("warning")
            messagebox.showwarning("Ineligible", "Rider must be at least 16.")
            return
        while True:
            num = simpledialog.askstring("Assign Bike Number", f"Enter an unused 2-digit number for {rider['name']}:")
            if num is None: return
            num = num.strip().zfill(2)
            if any(d["num"] == num for d in self.teams_database[self.player_team].values()):
                play_sound("warning")
                messagebox.showwarning("Taken", "Number taken.")
            else:
                play_sound("success")
                self.teams_database[self.player_team][f"RIDER_PROMOTE_{random.randint(1000,9999)}"] = {
                    "name": rider["name"], "num": num, "class": "250", "status": "ACTIVE", "injury_weeks": 0, "age": int(rider["age"]), "wins": 0, "championships": 0, "points": 0, "morale": 85, "ovr": rider["true_ovr"]
                }
                self.youth_academy.pop(index)
                self.create_manage_youth_roster_screen()
                break

    def cut_youth_rider(self, index):
        if messagebox.askyesno("Confirm", "Drop this prospect?"):
            self.youth_academy.pop(index)
            self.create_manage_youth_roster_screen()

    def create_your_team_roster(self):
        self.current_viewing_team = self.player_team
        self.display_roster_screen(is_player_owned=True)

    def create_other_teams_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="OTHER TEAMS", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=30).pack()
        for t in self.teams_database.keys():
            if t != self.player_team:
                tk.Button(self.root, text=t, font=("Arial", 11, "bold"), width=30, bg="#2a2a2a", fg="#ffffff", command=lambda name=t: self.open_rival_team_roster(name)).pack(pady=4)
        tk.Button(self.root, text="BACK", font=("Arial", 10, "bold"), width=10, bg="#555555", fg="#ffffff", command=self.create_roster_options_menu).pack(pady=25)

    def open_rival_team_roster(self, name):
        self.current_viewing_team = name
        self.display_roster_screen(is_player_owned=False)

    def display_roster_screen(self, is_player_owned):
        self.clear_screen()
        tk.Label(self.root, text=f"{self.current_viewing_team} ROSTER", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=20).pack()
        roster = self.teams_database[self.current_viewing_team]
        
        tk.Label(self.root, text="450 CLASS", font=("Arial", 16, "bold"), fg="#ff9900", bg="#1a1a1a").pack(pady=5)
        for k, d in list(roster.items()):
            if d["class"] == "450":
                tk.Button(self.root, text=f"{d['name']} #{d['num']} (OVR {d.get('ovr', 80)})", font=("Arial", 12), width=30, bg="#2a2a2a", fg="#ffffff", command=lambda key=k: self.create_rider_profile_screen(key, is_player_owned)).pack(pady=3)

        tk.Label(self.root, text="250 CLASS", font=("Arial", 16, "bold"), fg="#ff9900", bg="#1a1a1a").pack(pady=15)
        for k, d in list(roster.items()):
            if d["class"] == "250":
                tk.Button(self.root, text=f"{d['name']} #{d['num']} (OVR {d.get('ovr', 74)})", font=("Arial", 12), width=30, bg="#2a2a2a", fg="#ffffff", command=lambda key=k: self.create_rider_profile_screen(key, is_player_owned)).pack(pady=3)

        cmd = self.create_roster_options_menu if is_player_owned else self.create_other_teams_menu
        tk.Button(self.root, text="BACK", font=("Arial", 10, "bold"), width=10, bg="#555555", fg="#ffffff", command=cmd).pack(pady=30)

    # --- INFORMATION TAB RIDER PROFILE SCREEN ---
    def create_rider_profile_screen(self, r_key, is_player_owned):
        self.current_rider_key = r_key
        rider = self.teams_database[self.current_viewing_team][r_key]
        self.clear_screen()

        tk.Label(self.root, text="RIDER PROFILE INFORMATION", font=("Arial", 22, "bold"), fg="#ffffff", bg="#1a1a1a", pady=20).pack()
        f = tk.Frame(self.root, bg="#1a1a1a")
        f.pack(fill="both", expand=True, padx=20, pady=10)

        left = tk.Frame(f, bg="#222222", bd=2, relief="groove", padx=20, pady=20)
        left.pack(side="left" if is_player_owned else "top", fill="both", expand=True, padx=10)

        self.lbl_profile_title = tk.Label(left, text=f"{rider['name']} #{rider['num']}", font=("Arial", 16, "bold"), fg="#ff9900", bg="#222222")
        self.lbl_profile_title.pack(anchor="w", pady=(0, 10))

        # Dynamically display weeks left on recovery lines if currently out
        status_txt = f"STATUS: {rider['status']}"
        if rider.get("injury_weeks", 0) > 0:
            status_txt += f" (Returns in {rider['injury_weeks']} Wks)"

        self.lbl_status = tk.Label(left, text=status_txt, font=("Arial", 12, "bold"), fg="#55ff55" if rider['injury_weeks'] == 0 else "#ff5555", bg="#222222")
        self.lbl_status.pack(anchor="w", pady=(0, 20))

        # Real-World Imported Database Information Tab fields
        tk.Label(left, text=f"OVERALL RATING: {rider.get('ovr', 75)} OVR", font=("Arial", 14, "bold"), fg="#ffff55", bg="#222222").pack(anchor="w", pady=4)
        tk.Label(left, text=f"AGE: {rider.get('age', 22)}", font=("Arial", 14), fg="#ffffff", bg="#222222").pack(anchor="w", pady=4)
        tk.Label(left, text=f"TOTAL RESUMED WINS: {rider.get('wins', 0)}", font=("Arial", 14), fg="#ffffff", bg="#222222").pack(anchor="w", pady=4)
        tk.Label(left, text=f"CHAMPIONSHIPS WON: {rider.get('championships', 0)}", font=("Arial", 14), fg="#ff9900", bg="#222222").pack(anchor="w", pady=4)
        tk.Label(left, text=f"SERIES STANDINGS POINTS: {rider.get('points', 0)} PTS", font=("Arial", 14), fg="#55ff55", bg="#222222").pack(anchor="w", pady=4)
        tk.Label(left, text=f"TEAM MORALE RATING: {rider.get('morale', 85)}%", font=("Arial", 14), fg="#ffffff", bg="#222222").pack(anchor="w", pady=4)

        if is_player_owned:
            right = tk.Frame(f, bg="#222222", bd=2, relief="groove", padx=20, pady=20)
            right.pack(side="right", fill="both", expand=True, padx=10)
            tk.Label(right, text="ROSTER ACTIONS", font=("Arial", 16, "bold"), fg="#ffffff", bg="#222222").pack(pady=(0, 15))
            
            if rider["class"] == "250":
                tk.Button(right, text="PROMOTE TO 450", font=("Arial", 12, "bold"), bg="#55ff55", fg="#000000", width=15, command=self.action_promote_to_450).pack(pady=5)

            tk.Button(right, text="RELEASE RIDER", font=("Arial", 12, "bold"), bg="#aa2222", fg="#ffffff", width=15, command=self.action_release_rider).pack(pady=5)
            tk.Button(right, text="CHANGE BIKE NUMBER", font=("Arial", 12, "bold"), bg="#333333", fg="#ffffff", width=15, command=self.action_change_number).pack(pady=5)
            tk.Button(right, text="BENCH / REST RIDER", font=("Arial", 12, "bold"), bg="#333333", fg="#ffffff", width=15, command=self.action_toggle_rest).pack(pady=5)

        b_frame = tk.Frame(self.root, bg="#1a1a1a")
        b_frame.pack(fill="x", pady=20)
        tk.Button(b_frame, text="RETURN TO ROSTER", font=("Arial", 10, "bold"), width=18, bg="#555555", fg="#ffffff", command=lambda: self.display_roster_screen(is_player_owned)).pack()

    def action_promote_to_450(self):
        rider = self.teams_database[self.player_team][self.current_rider_key]
        if int(rider.get("age", 0)) <= 20 or int(rider.get("championships", 0)) < 1:
            messagebox.showwarning("Locked", "Requires Age > 20 and 1+ Championship completion benchmark.")
            return
        rider["class"] = "450"
        self.display_roster_screen(is_player_owned=True)

    def action_release_rider(self):
        if messagebox.askyesno("Warning", "Fire rider permanently?"):
            del self.teams_database[self.player_team][self.current_rider_key]
            self.display_roster_screen(is_player_owned=True)

    def action_change_number(self):
        rider = self.teams_database[self.player_team][self.current_rider_key]
        new_num = simpledialog.askstring("Number", "New bike number designation:")
        if new_num:
            new_num = new_num.strip().zfill(2)
            if any(d["num"] == new_num for k, d in self.teams_database[self.player_team].items() if k != self.current_rider_key):
                messagebox.showwarning("Error", "Number already claimed on team.")
            else:
                self.teams_database[self.player_team][self.current_rider_key]["num"] = new_num
                self.lbl_profile_title.config(text=f"{rider['name']} #{new_num}")

    def action_toggle_rest(self):
        rider = self.teams_database[self.player_team][self.current_rider_key]
        if rider["injury_weeks"] > 0:
            messagebox.showwarning("Action Blocked", "Rider is actively recovering from severe track injuries!")
            return
        if rider["status"] == "ACTIVE":
            rider["status"] = "RESTING"
            self.lbl_status.config(text="STATUS: RESTING", fg="#ff5555")
        else:
            rider["status"] = "ACTIVE"
            self.lbl_status.config(text="STATUS: ACTIVE", fg="#55ff55")

if __name__ == "__main__":
    root = tk.Tk()
    app = MotocrossGameUI(root)
    root.mainloop()