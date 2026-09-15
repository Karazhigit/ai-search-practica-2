graph = {
    "Gate": [("Library", 2), ("Cafe", 1), ("Hall", 4)],
    "Library": [("Classroom", 4), ("Study Zone", 2)],
    "Cafe": [("Study Zone", 5), ("Robotics Lab", 2)],
    "Hall": [("Classroom", 1), ("Robotics Lab", 6)],
    "Classroom": [("AI Lab", 8)],
    "Study Zone": [("Robotics Lab", 1), ("AI Lab", 5)],
    "Robotics Lab": [("AI Lab", 4)],
    "AI Lab": []
}
