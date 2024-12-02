import os
import csv
from collections import defaultdict

# Function to calculate attendance
def calculate_attendance(directory):
    attendance_dict = defaultdict(int)

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, mode="r", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    # Skip the header if it exists
                    header = next(reader, None)
                    for row in reader:
                        if row:  # Ensure the row is not empty
                            name = row[1].strip()
                            attendance_dict[name] += 1
            except Exception as e:
                print(f"Error reading file {filename}: {e}")

    # Sort the dictionary by attendance count in descending order
    sorted_attendance = dict(sorted(attendance_dict.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_attendance

# Main script
if __name__ == "__main__":
    directory = input("Enter the directory path containing the CSV files: ").strip()
    
    if os.path.isdir(directory):
        attendance = calculate_attendance(directory)
        print("\nTotal Attendance (Sorted by Most Events Attended):")
        for name, count in attendance.items():
            print(f"{name}: {count} events")
    else:
        print("Invalid directory. Please check the path and try again.")
