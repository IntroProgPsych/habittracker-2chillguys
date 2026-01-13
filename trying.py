# Data definitions
MENU_OPTIONS = {
    "1": "Add daily entry",
    "2": "Analyze stress patterns",
    "3": "View all entries",
    "4": "Add coping strategies",
    "5": "View coping strategies",
    "6": "Exit",
}

ENTRY_FIELDS = [
    ("date", str, "What is today's date? ", None, None),
    ("stress_level", int, "Rate your stress level (1-10): ", 1, 10),
    ("mood", str, "How is your mood? (great/good/okay/poor): ", None, None),
    ("sleep_hours", int, "How many hours did you sleep? (0-24): ", 0, 24),
    ("exercise_minutes", int, "Minutes of exercise today (0+): ", 0, None),
]

WELCOME_MESSAGE = "Welcome to the Student Stress & Wellbeing Tracker!\nTrack your stress levels and wellbeing to understand your patterns.\n"
SUCCESS_MESSAGE = "✓ Entry saved successfully!"
GOODBYE_MESSAGE = "Thank you for using the Stress & Wellbeing Tracker!\nRemember to take care of your mental health! 🎓"


def get_valid_input(prompt, input_type=str, min_val=None, max_val=None):
    """Get and validate user input with type conversion and range checking."""
    while True:
        try:
            user_input = input(prompt)
            if input_type == int:
                return validate_int(user_input, min_val, max_val)
            else:
                return validate_string(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}")


def validate_int(user_input, min_val, max_val):
    """Validate and convert string to integer with range checking."""
    value = int(user_input)
    if min_val is not None and value < min_val:
        print(f"Please enter a number >= {min_val}")
        raise ValueError()
    if max_val is not None and value > max_val:
        print(f"Please enter a number <= {max_val}")
        raise ValueError()
    return value


def validate_string(user_input):
    """Validate and clean string input."""
    if len(user_input.strip()) == 0:
        print("Input cannot be empty. Please try again.")
        raise ValueError()
    return user_input.strip()


def get_daily_log():
    """Collect daily wellbeing data by gathering each field."""
    print("\n--- Daily Wellbeing Check-in ---")
    entry = {}
    for field_name, field_type, prompt, min_v, max_v in ENTRY_FIELDS:
        value = get_valid_input(prompt, field_type, min_v, max_v)
        if field_name == "mood":
            value = value.lower()
        entry[field_name] = value
    return entry


def get_stress_levels(entries):
    """Extract stress levels from entries."""
    return [entry["stress_level"] for entry in entries]


def print_average_stress(entries):
    """Calculate and print average stress level."""
    stress_levels = get_stress_levels(entries)
    avg_stress = sum(stress_levels) / len(stress_levels)
    print(f"Average stress level: {avg_stress:.1f}/10")


def print_stress_extremes(entries):
    """Find and print highest and lowest stress days."""
    highest = max(entries, key=lambda e: e["stress_level"])
    lowest = min(entries, key=lambda e: e["stress_level"])
    print(f"Highest stress: {highest['stress_level']}/10 on {highest['date']}")
    print(f"Lowest stress: {lowest['stress_level']}/10 on {lowest['date']}")


def get_mood_counts(entries):
    """Count frequency of each mood."""
    mood_counts = {}
    for entry in entries:
        mood = entry["mood"]
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
    return mood_counts


def print_mood_frequency(entries):
    """Print mood frequency distribution."""
    mood_counts = get_mood_counts(entries)
    print("\nMood frequency:")
    for mood, count in mood_counts.items():
        print(f"  {mood.capitalize()}: {count} time(s)")


def get_average_sleep(entries):
    """Calculate average sleep hours."""
    return sum(e["sleep_hours"] for e in entries) / len(entries)


def get_average_exercise(entries):
    """Calculate average exercise minutes."""
    return sum(e["exercise_minutes"] for e in entries) / len(entries)


def print_sleep_and_exercise(entries):
    """Print average sleep and exercise statistics."""
    avg_sleep = get_average_sleep(entries)
    avg_exercise = get_average_exercise(entries)
    print(f"\nAverage sleep: {avg_sleep:.1f} hours")
    print(f"Average exercise: {avg_exercise:.1f} minutes")


def analyze_stress_pattern(entries):
    """Orchestrate stress pattern analysis."""
    if not entries:
        print("No entries to analyze.")
        return
    print("\n--- Stress Pattern Analysis ---")
    print_average_stress(entries)
    print_stress_extremes(entries)
    print_mood_frequency(entries)
    print_sleep_and_exercise(entries)


def add_strategy_to_list(strategies):
    """Prompt user to enter a single coping strategy."""
    strategy = get_valid_input("Strategy: ")
    if strategy.lower() == "done":
        return False
    strategies.append(strategy)
    return True


def get_coping_strategies():
    """Collect coping strategies from user until they enter 'done'."""
    print("\n--- Coping Strategies ---")
    strategies = []
    print("Enter your coping strategies (type 'done' when finished):")
    while add_strategy_to_list(strategies):
        pass
    if not strategies:
        print("Please add at least one strategy.")
        return get_coping_strategies()
    return strategies


def display_menu():
    title = "== Student Stress & Wellbeing Tracker Menu =="
    print(title)
    for position, option in MENU_OPTIONS.items():
        print(f"{position}. {option}")
    print("=" * len(title))


def print_entry(entry, index):
    """Print a single entry with all its fields."""
    print(f"\nEntry {index}:")
    print(f"  Date: {entry['date']}")
    print(f"  Stress: {entry['stress_level']}/10")
    print(f"  Mood: {entry['mood']}")
    print(f"  Sleep: {entry['sleep_hours']} hours")
    print(f"  Exercise: {entry['exercise_minutes']} minutes")


def view_all_entries(entries):
    """Display all recorded entries."""
    if not entries:
        print("No entries recorded yet.")
        return
    print("\n--- All Entries ---")
    for i, entry in enumerate(entries, 1):
        print_entry(entry, i)


def print_coping_strategies_list(strategies):
    """Print all coping strategies in numbered format."""
    print("\n--- Your Coping Strategies ---")
    for i, strategy in enumerate(strategies, 1):
        print(f"{i}. {strategy}")


def display_strategies(strategies):
    """Display strategies or message if none exist."""
    if strategies:
        print_coping_strategies_list(strategies)
    else:
        print("No coping strategies recorded yet.")


def handle_add_entry(entries):
    """Add a daily entry to the list."""
    entry = get_daily_log()
    entries.append(entry)
    print(SUCCESS_MESSAGE)


def handle_add_strategies(strategies):
    """Add coping strategies to the list."""
    new_strategies = get_coping_strategies()
    strategies.extend(new_strategies)
    print(f"✓ Added {len(new_strategies)} strategy/strategies!")


def process_menu_choice(choice, entries, strategies):
    """Execute action based on menu choice."""
    if choice == 1:
        handle_add_entry(entries)
    elif choice == 2:
        analyze_stress_pattern(entries)
    elif choice == 3:
        view_all_entries(entries)
    elif choice == 4:
        handle_add_strategies(strategies)
    elif choice == 5:
        display_strategies(strategies)
    elif choice == 6:
        return False
    else:
        print("Invalid choice. Please select 1-6.")
    return True


def my_code():
    #Main program loop
    print(WELCOME_MESSAGE)
    entries, strategies = [], []
    
    while True:
        display_menu()
        choice = get_valid_input("Select an option (1-6): ", int, 1, 6)
        if not process_menu_choice(choice, entries, strategies):
            print(GOODBYE_MESSAGE)
            break


if __name__ == "__main__":
    my_code()