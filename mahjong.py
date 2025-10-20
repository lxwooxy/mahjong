import tkinter as tk
from tkinter import ttk
from collections import Counter
from itertools import combinations

# Define all possible Mahjong hands based on the official card
MAHJONG_HANDS = []

suits = ["Bamboo", "Character", "Dot"]

# WINDS-DRAGONS SECTION
MAHJONG_HANDS.extend([
    ("NNNN EEEE WWW SSSS", ["North Wind"]*4 + ["East Wind"]*4 + ["West Wind"]*3 + ["South Wind"]*3, 25),
    ("NNN EEEE WWWW SSS", ["North Wind"]*3 + ["East Wind"]*4 + ["West Wind"]*4 + ["South Wind"]*3, 25),
])

# Add variations for FF 123 DD DDD DDDD (any 3 consecutive in any suit, any 3 dragons)
for suit in suits:
    for start in range(1, 8):  # 1-7 start positions for consecutive
        MAHJONG_HANDS.append((
            f"FF {start}{start+1}{start+2} DDD DDD DDD - {suit}",
            ["Flower"]*2 + [f"{start} {suit}", f"{start+1} {suit}", f"{start+2} {suit}"] + 
            ["Red Dragon"]*3 + ["Green Dragon"]*3 + ["White Dragon"]*3,
            25
        ))

MAHJONG_HANDS.extend([
    ("FFF NN EE WWW SSSS", ["Flower"]*3 + ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*3 + ["South Wind"]*4, 25),
    ("FFFF DDD NEWS DDD", ["Flower"]*4 + ["Red Dragon"]*3 + ["North Wind"] + ["East Wind"] + ["West Wind"] + ["South Wind"] + ["Green Dragon"]*3, 25),
])

# Like Odd Numbers in 3 Suits (NNNN 1 11 111 SSSS)
for odd in [1, 3, 5, 7, 9]:
    MAHJONG_HANDS.append((
        f"NNNN {odd} {odd}{odd} {odd}{odd}{odd} SSSS",
        ["North Wind"]*4 + [f"{odd} Bamboo"] + [f"{odd} Character"]*2 + [f"{odd} Dot"]*3 + ["South Wind"]*4,
        25
    ))

# Like Even Numbers in 3 Suits (EEEE 2 22 222 WWWW)
for even in [2, 4, 6, 8]:
    MAHJONG_HANDS.append((
        f"EEEE {even} {even}{even} {even}{even}{even} WWWW",
        ["East Wind"]*4 + [f"{even} Bamboo"] + [f"{even} Character"]*2 + [f"{even} Dot"]*3 + ["West Wind"]*4,
        25
    ))

# 2025 variations
for suit in suits:
    MAHJONG_HANDS.append((
        f"NN EEE WWW SS 2025 - {suit}",
        ["North Wind"]*2 + ["East Wind"]*3 + ["West Wind"]*3 + ["South Wind"]*2 + 
        [f"2 {suit}", "White Dragon", f"2 {suit}", f"5 {suit}"],
        30
    ))
    MAHJONG_HANDS.append((
        f"NNN EE WW SSS 2025 - {suit}",
        ["North Wind"]*3 + ["East Wind"]*2 + ["West Wind"]*2 + ["South Wind"]*3 + 
        [f"2 {suit}", "White Dragon", f"2 {suit}", f"5 {suit}"],
        30
    ))

# Kong Any Dragon
MAHJONG_HANDS.extend([
    ("NN EE WWW SSS DDDD (Red)", ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*3 + ["South Wind"]*3 + ["Red Dragon"]*4, 30),
    ("NN EE WWW SSS DDDD (Green)", ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*3 + ["South Wind"]*3 + ["Green Dragon"]*4, 30),
    ("NN EE WWW SSS DDDD (White)", ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*3 + ["South Wind"]*3 + ["White Dragon"]*4, 30),
])

# 369 SECTION
# 333 6666 666 9999 (different suits for different colors)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"333 6666 666 9999 - {s1}/{s2}/{s3}",
        [f"3 {s1}"]*3 + [f"6 {s2}"]*4 + [f"6 {s2}"]*2 + [f"9 {s3}"]*4 + [f"9 {s3}"],
        25
    ))

# FF 3333+6666=9999 (need all three groups)
for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"FF 3333+6666=9999 - {s1}/{s2}",
        ["Flower"]*2 + [f"3 {s1}"]*4 + [f"6 {s1}"]*4 + [f"9 {s2}"]*4,
        25
    ))
    MAHJONG_HANDS.append((
        f"FF 3333+6666=9999 - {s2}/{s1}",
        ["Flower"]*2 + [f"3 {s2}"]*4 + [f"6 {s2}"]*4 + [f"9 {s1}"]*4,
        25
    ))

# 3333 DDD 3333 DDD (matching dragons with kongs)
for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"3333 DDD 3333 DDD - {s1}/{s2}",
        [f"3 {s1}"]*4 + ["Red Dragon"]*3 + [f"3 {s2}"]*4 + ["Green Dragon"]*3,
        25
    ))

# FFF 3333 369 9999
for suit in suits:
    MAHJONG_HANDS.append((
        f"FFF 3333 369 9999 - {suit}",
        ["Flower"]*3 + [f"3 {suit}"]*4 + [f"3 {suit}", f"6 {suit}", f"9 {suit}"] + [f"9 {suit}"]*4,
        25
    ))

# 33 66 99 3333 3333 (like kongs 3, 6 or 9)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"33 66 99 3333 3333 - {s1}/{s2}/{s3}",
        [f"3 {s1}"]*2 + [f"6 {s2}"]*2 + [f"9 {s3}"]*2 + [f"3 {s1}"]*4 + [f"3 {s2}"]*4,
        25
    ))

# FF 333 D 666 D 999 D
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"FF 333 D 666 D 999 D - {s1}/{s2}/{s3}",
        ["Flower"]*2 + [f"3 {s1}"]*3 + ["Red Dragon"] + [f"6 {s2}"]*3 + 
        ["Green Dragon"] + [f"9 {s3}"]*3 + ["White Dragon"],
        30
    ))

# SINGLES AND PAIRS
# NN EW SS 11 22 33 44
for suit in suits:
    for start in range(1, 7):  # any 4 consecutive
        MAHJONG_HANDS.append((
            f"NN EW SS {start}{start} {start+1}{start+1} {start+2}{start+2} {start+3}{start+3} - {suit}",
            ["North Wind"]*2 + ["East Wind"] + ["West Wind"] + ["South Wind"]*2 + 
            [f"{start} {suit}"]*2 + [f"{start+1} {suit}"]*2 + [f"{start+2} {suit}"]*2 + [f"{start+3} {suit}"]*2,
            50
        ))

# FF 2468 DD 2468 DD (any 2 suits with matching dragons)
for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"FF 2468 DD 2468 DD - {s1}/{s2}",
        ["Flower"]*2 + [f"2 {s1}"]*2 + [f"4 {s1}"]*2 + [f"6 {s1}"]*2 + [f"8 {s1}"]*2 + 
        ["Red Dragon"]*2 + [f"2 {s2}"]*2 + [f"4 {s2}"]*2 + [f"6 {s2}"]*2 + [f"8 {s2}"]*2 + ["White Dragon"]*2,
        50
    ))

# 336699 336699 33 (pairs 3,6,9 in third suit)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"336699 336699 33 - {s1}/{s2}/{s3}",
        [f"3 {s1}"]*2 + [f"3 {s2}"]*2 + [f"6 {s1}"]*2 + [f"6 {s2}"]*2 + 
        [f"9 {s1}"]*2 + [f"9 {s2}"]*2 + [f"3 {s3}"]*2,
        50
    ))

# FF 11 22 11 22 11 22 (any 3 suits, any 2 consec)
for start in range(1, 9):
    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"FF {start}{start} {start+1}{start+1} {start}{start} {start+1}{start+1} {start}{start} {start+1}{start+1} - {s1}/{s2}/{s3}",
            ["Flower"]*2 + [f"{start} {s1}"]*2 + [f"{start+1} {s1}"]*2 + 
            [f"{start} {s2}"]*2 + [f"{start+1} {s2}"]*2 + [f"{start} {s3}"]*2 + [f"{start+1} {s3}"]*2,
            50
        ))

# Pairs odd numbers in opposite suits
MAHJONG_HANDS.append((
    "11 33 55 77 99 11 11",
    ["1 Bamboo"]*2 + ["3 Character"]*2 + ["5 Bamboo"]*2 + ["5 Dot"]*2 + 
    ["7 Character"]*2 + ["9 Bamboo"]*2 + ["1 Dot"]*2,
    50
))

# FF 2025 2025 2025 (any 3 suits)
MAHJONG_HANDS.append((
    "FF 2025 2025 2025",
    ["Flower"]*2 + ["2 Bamboo"]*2 + ["0 Bamboo"]*2 + ["2 Bamboo"]*2 + ["5 Bamboo"]*2 + 
    ["2 Character"]*2 + ["5 Character"]*2 + ["2 Dot"]*2 + ["5 Dot"]*2,
    75
))

# QUINTS
# FF 111 2222 33333
for s1, s2, s3 in combinations(suits, 3):
    for start in range(1, 8):
        MAHJONG_HANDS.append((
            f"FF {start}{start}{start} {start+1}{start+1}{start+1}{start+1} {start+2}{start+2}{start+2}{start+2}{start+2} - {s1}/{s2}/{s3}",
            ["Flower"]*2 + [f"{start} {s1}"]*3 + [f"{start+1} {s2}"]*4 + [f"{start+2} {s3}"]*5,
            40
        ))

# 11111 NNNN 22222
for suit in suits:
    for start in range(1, 9):
        MAHJONG_HANDS.append((
            f"{start}{start}{start}{start}{start} NNNN {start+1}{start+1}{start+1}{start+1}{start+1} - {suit}",
            [f"{start} {suit}"]*5 + ["North Wind"]*4 + [f"{start+1} {suit}"]*5,
            45
        ))

# FF 11111 11 11111
for num in range(1, 10):
    for s1, s2 in combinations(suits, 2):
        MAHJONG_HANDS.append((
            f"FF {num}{num}{num}{num}{num} {num}{num} {num}{num}{num}{num}{num} - {s1}/{s2}",
            ["Flower"]*2 + [f"{num} {s1}"]*5 + [f"{num} {s2}"]*2 + [f"{num} {s1}"]*5,
            45
        ))

# CONSECUTIVE RUN SECTION
for suit in suits:
    MAHJONG_HANDS.append((
        f"11 222 3333 444 55 - {suit}",
        [f"1 {suit}"]*2 + [f"2 {suit}"]*3 + [f"3 {suit}"]*4 + [f"4 {suit}"]*4 + [f"5 {suit}"]*2,
        25
    ))
    MAHJONG_HANDS.append((
        f"55 666 7777 888 99 - {suit}",
        [f"5 {suit}"]*2 + [f"6 {suit}"]*3 + [f"7 {suit}"]*4 + [f"8 {suit}"]*4 + [f"9 {suit}"],
        25
    ))

# 111 2222 333 4444 -or- 111 2222 333 4444 (any 1 or 2 suits, any 4 consec)
for s1 in suits:
    for start in range(1, 7):
        MAHJONG_HANDS.append((
            f"{start}{start}{start} {start+1}{start+1}{start+1}{start+1} {start+2}{start+2}{start+2} {start+3}{start+3}{start+3}{start+3} - {s1}",
            [f"{start} {s1}"]*3 + [f"{start+1} {s1}"]*4 + [f"{start+2} {s1}"]*3 + [f"{start+3} {s1}"]*4,
            25
        ))

for s1, s2 in combinations(suits, 2):
    for start in range(1, 7):
        MAHJONG_HANDS.append((
            f"{start}{start}{start} {start+1}{start+1}{start+1}{start+1} {start+2}{start+2}{start+2} {start+3}{start+3}{start+3}{start+3} - {s1}/{s2}",
            [f"{start} {s1}"]*3 + [f"{start+1} {s1}"]*4 + [f"{start+2} {s2}"]*3 + [f"{start+3} {s2}"]*4,
            25
        ))

# FFFF 1111 22 3333 -or- FF 111 22 3333 (any 1 or 3 suits, any 3 consec)
for suit in suits:
    for start in range(1, 8):
        MAHJONG_HANDS.append((
            f"FFFF {start}{start}{start}{start} {start+1}{start+1} {start+2}{start+2}{start+2}{start+2} - {suit}",
            ["Flower"]*4 + [f"{start} {suit}"]*4 + [f"{start+1} {suit}"]*2 + [f"{start+2} {suit}"]*4,
            25
        ))

for s1, s2, s3 in combinations(suits, 3):
    for start in range(1, 8):
        MAHJONG_HANDS.append((
            f"FF {start}{start}{start} {start+1}{start+1} {start+2}{start+2}{start+2}{start+2} - {s1}/{s2}/{s3}",
            ["Flower"]*2 + [f"{start} {s1}"]*3 + [f"{start+1} {s2}"]*2 + [f"{start+2} {s3}"]*4,
            25
        ))

# FFF 111 22 33333 (any 3 suits, any 5 consec)
for s1, s2, s3 in combinations(suits, 3):
    for start in range(1, 6):
        MAHJONG_HANDS.append((
            f"FFF {start}{start}{start} {start+1}{start+1} {start+2}{start+2}{start+2}{start+2}{start+2} - {s1}/{s2}/{s3}",
            ["Flower"]*3 + [f"{start} {s1}"]*3 + [f"{start+1} {s2}"]*2 + [f"{start+2} {s3}"]*5,
            25
        ))

# FFF 1 222 3333 DDD (any 1 suit, any 3 consec)
for suit in suits:
    for start in range(1, 8):
        MAHJONG_HANDS.append((
            f"FFF {start} {start+1}{start+1}{start+1} {start+2}{start+2}{start+2}{start+2} DDD - {suit}",
            ["Flower"]*3 + [f"{start} {suit}"] + [f"{start+1} {suit}"]*3 + [f"{start+2} {suit}"]*4 + ["Red Dragon"]*3,
            25
        ))

# 111 222 3333 DD DD (any 3 suits, any 3 consec with opp dragons)
for s1, s2, s3 in combinations(suits, 3):
    for start in range(1, 8):
        MAHJONG_HANDS.append((
            f"{start}{start}{start} {start+1}{start+1}{start+1} {start+2}{start+2}{start+2}{start+2} DD DD - {s1}/{s2}/{s3}",
            [f"{start} {s1}"]*3 + [f"{start+1} {s2}"]*3 + [f"{start+2} {s3}"]*4 + ["Red Dragon"]*2 + ["White Dragon"]*2,
            30
        ))

# 112345 1111 1111 (any 5 consec, pair any no in run, kongs match pair)
for suit in suits:
    for start in range(1, 6):
        MAHJONG_HANDS.append((
            f"{start}{start}{start+1}{start+2}{start+3}{start+4} {start}{start}{start}{start} {start}{start}{start}{start} - {suit}",
            [f"{start} {suit}"]*2 + [f"{start+1} {suit}"] + [f"{start+2} {suit}"] + 
            [f"{start+3} {suit}"] + [f"{start+4} {suit}"] + [f"{start} {suit}"]*4 + [f"{start} {suit}"]*4,
            30
        ))

# FF 1 22 333 1 22 333 (any 2 suits, any same 3 consec)
for s1, s2 in combinations(suits, 2):
    for start in range(1, 8):
        MAHJONG_HANDS.append((
            f"FF {start} {start+1}{start+1} {start+2}{start+2}{start+2} {start} {start+1}{start+1} {start+2}{start+2}{start+2} - {s1}/{s2}",
            ["Flower"]*2 + [f"{start} {s1}"] + [f"{start+1} {s1}"]*2 + [f"{start+2} {s1}"]*3 + 
            [f"{start} {s2}"] + [f"{start+1} {s2}"]*2 + [f"{start+2} {s2}"]*3,
            30
        ))

# 13579 SECTION
# 11 333 5555 777 99 -or- 11 333 5555 777 99 (any 1 or 3 suits)
for suit in suits:
    MAHJONG_HANDS.append((
        f"11 333 5555 777 99 - {suit}",
        [f"1 {suit}"]*2 + [f"3 {suit}"]*3 + [f"5 {suit}"]*4 + [f"7 {suit}"]*3 + [f"9 {suit}"]*2,
        25
    ))

for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"11 333 5555 777 99 - {s1}/{s2}/{s3}",
        [f"1 {s1}"]*2 + [f"3 {s2}"]*3 + [f"5 {s3}"]*4 + [f"7 {s1}"]*3 + [f"9 {s2}"]*2,
        25
    ))

# 111 3333 333 5555 -or- 555 7777 777 9999 (any 2 suits)
for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"111 3333 333 5555 - {s1}/{s2}",
        [f"1 {s1}"]*3 + [f"3 {s1}"]*4 + [f"3 {s2}"]*3 + [f"5 {s2}"]*4,
        25
    ))
    MAHJONG_HANDS.append((
        f"555 7777 777 9999 - {s1}/{s2}",
        [f"5 {s1}"]*3 + [f"7 {s1}"]*4 + [f"7 {s2}"]*3 + [f"9 {s2}"]*4,
        25
    ))

# 1111 333 5555 DDD -or- 5555 777 9999 DDD (any 1 suit)
for suit in suits:
    MAHJONG_HANDS.append((
        f"1111 333 5555 DDD - {suit}",
        [f"1 {suit}"]*4 + [f"3 {suit}"]*3 + [f"5 {suit}"]*4 + ["Red Dragon"]*3,
        25
    ))
    MAHJONG_HANDS.append((
        f"5555 777 9999 DDD - {suit}",
        [f"5 {suit}"]*4 + [f"7 {suit}"]*3 + [f"9 {suit}"]*4 + ["Green Dragon"]*3,
        25
    ))

# FFFF 1111 + 9999 = 10 (any 2 suits, these nos only)
for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"FFFF 1111 + 9999 = 10 - {s1}/{s2}",
        ["Flower"]*4 + [f"1 {s1}"]*4 + [f"9 {s2}"]*4 + [f"1 {s1}"] + ["White Dragon"],
        25
    ))

# FFF 135 7777 9999 -or- FFF 135 7777 9999 (any 1 or 3 suits)
for suit in suits:
    MAHJONG_HANDS.append((
        f"FFF 135 7777 9999 - {suit}",
        ["Flower"]*3 + [f"1 {suit}"] + [f"3 {suit}"] + [f"5 {suit}"] + [f"7 {suit}"]*4 + [f"9 {suit}"]*4,
        25
    ))

for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"FFF 135 7777 9999 - {s1}/{s2}/{s3}",
        ["Flower"]*3 + [f"1 {s1}"] + [f"3 {s2}"] + [f"5 {s3}"] + [f"7 {s1}"]*4 + [f"9 {s2}"]*4,
        25
    ))

# 111 333 5555 DD DD -or- 555 777 9999 DD DD (any 3 suits w opp dragons)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"111 333 5555 DD DD - {s1}/{s2}/{s3}",
        [f"1 {s1}"]*3 + [f"3 {s2}"]*3 + [f"5 {s3}"]*4 + ["Red Dragon"]*2 + ["White Dragon"]*2,
        30
    ))
    MAHJONG_HANDS.append((
        f"555 777 9999 DD DD - {s1}/{s2}/{s3}",
        [f"5 {s1}"]*3 + [f"7 {s2}"]*3 + [f"9 {s3}"]*4 + ["Red Dragon"]*2 + ["White Dragon"]*2,
        30
    ))

# 11 333 NEWS 333 55 -or- 55 777 NEWS 777 99 (any 2 suits)
for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"11 333 NEWS 333 55 - {s1}/{s2}",
        [f"1 {s1}"]*2 + [f"3 {s1}"]*3 + ["North Wind"] + ["East Wind"] + ["West Wind"] + ["South Wind"] + 
        [f"3 {s2}"]*3 + [f"5 {s2}"]*2,
        30
    ))
    MAHJONG_HANDS.append((
        f"55 777 NEWS 777 99 - {s1}/{s2}",
        [f"5 {s1}"]*2 + [f"7 {s1}"]*3 + ["North Wind"] + ["East Wind"] + ["West Wind"] + ["South Wind"] + 
        [f"7 {s2}"]*3 + [f"9 {s2}"]*2,
        30
    ))

# 1111 33 55 77 9999 (any 2 suits)
for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"1111 33 55 77 9999 - {s1}/{s2}",
        [f"1 {s1}"]*4 + [f"3 {s1}"]*2 + [f"5 {s2}"]*2 + [f"7 {s2}"]*2 + [f"9 {s2}"]*4,
        30
    ))

# FF 11 33 111 333 55 -or- FF 55 77 555 777 99 (any 3 suits)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"FF 11 33 111 333 55 - {s1}/{s2}/{s3}",
        ["Flower"]*2 + [f"1 {s1}"]*2 + [f"3 {s2}"]*2 + [f"1 {s1}"]*3 + [f"3 {s2}"]*3 + [f"5 {s3}"]*2,
        30
    ))
    MAHJONG_HANDS.append((
        f"FF 55 77 555 777 99 - {s1}/{s2}/{s3}",
        ["Flower"]*2 + [f"5 {s1}"]*2 + [f"7 {s2}"]*2 + [f"5 {s1}"]*3 + [f"7 {s2}"]*3 + [f"9 {s3}"]*2,
        30
    ))

# More runs - will add remaining lines next

class MahjongHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("Mahjong Hand Helper - Official Rules")
        self.root.geometry("1000x750")
        
        # Available tiles
        self.tile_types = []
        for i in range(1, 10):  # 1-9 only, no 0
            self.tile_types.extend([f"{i} Bamboo", f"{i} Character", f"{i} Dot"])
        self.tile_types.extend(["East Wind", "South Wind", "West Wind", "North Wind",
                               "Red Dragon", "Green Dragon", "White Dragon",
                               "Flower", "Joker"])
        
        self.selected_tiles = []
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Mahjong Hand Helper - Official Rules", 
                        font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        # Instructions
        instructions = tk.Label(self.root, 
                               text="Select tiles from your hand, then click 'Find Best Hands' to see top 3 potential scoring hands",
                               font=("Arial", 10))
        instructions.pack(pady=5)
        
        # Main container
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left side - Tile selection
        left_frame = tk.LabelFrame(main_frame, text="Select Your Tiles", 
                                   font=("Arial", 12, "bold"))
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Tile selector
        selector_frame = tk.Frame(left_frame)
        selector_frame.pack(pady=10, padx=10, fill=tk.X)
        
        # Number buttons (1-9, removed 0)
        number_frame = tk.LabelFrame(selector_frame, text="Numbers", font=("Arial", 11, "bold"))
        number_frame.pack(fill=tk.X, pady=5)
        
        numbers_btn_frame = tk.Frame(number_frame)
        numbers_btn_frame.pack(pady=5)
        
        for num in range(1, 10):
            btn = tk.Button(numbers_btn_frame, text=str(num), width=3,
                           command=lambda n=num: self.add_to_text_field(str(n)),
                           font=("Arial", 12, "bold"))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Suit buttons
        suit_frame = tk.LabelFrame(selector_frame, text="Suits", font=("Arial", 11, "bold"))
        suit_frame.pack(fill=tk.X, pady=5)
        
        suits_btn_frame = tk.Frame(suit_frame)
        suits_btn_frame.pack(pady=5)
        
        suits_list = [("Bamboo", "Bamboo"), ("Character", "Character"), ("Dot", "Dot")]
        for display, value in suits_list:
            btn = tk.Button(suits_btn_frame, text=display, width=10,
                           command=lambda v=value: self.add_to_text_field(v),
                           font=("Arial", 12, "bold"))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Honor tiles buttons
        honor_frame = tk.LabelFrame(selector_frame, text="Honors", font=("Arial", 11, "bold"))
        honor_frame.pack(fill=tk.X, pady=5)
        
        # Winds
        winds_label = tk.Label(honor_frame, text="Winds:", font=("Arial", 11))
        winds_label.pack(anchor=tk.W, padx=5, pady=(5,0))
        
        winds_btn_frame = tk.Frame(honor_frame)
        winds_btn_frame.pack(pady=2)
        
        winds = [("East", "East Wind"), ("South", "South Wind"), 
                ("West", "West Wind"), ("North", "North Wind")]
        for display, value in winds:
            btn = tk.Button(winds_btn_frame, text=display, width=8,
                           command=lambda v=value: self.set_text_field(v),
                           font=("Arial", 11, "bold"))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Dragons
        dragons_label = tk.Label(honor_frame, text="Dragons:", font=("Arial", 11))
        dragons_label.pack(anchor=tk.W, padx=5, pady=(5,0))
        
        dragons_btn_frame = tk.Frame(honor_frame)
        dragons_btn_frame.pack(pady=2)
        
        dragons = [("Red", "Red Dragon"), ("Green", "Green Dragon"), 
                  ("White", "White Dragon")]
        for display, value in dragons:
            btn = tk.Button(dragons_btn_frame, text=display, width=8,
                           command=lambda v=value: self.set_text_field(v),
                           font=("Arial", 11, "bold"))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Flowers
        flowers_label = tk.Label(honor_frame, text="Flowers:", font=("Arial", 11))
        flowers_label.pack(anchor=tk.W, padx=5, pady=(5,0))
        
        flowers_btn_frame = tk.Frame(honor_frame)
        flowers_btn_frame.pack(pady=2)
        
        flower_btn = tk.Button(flowers_btn_frame, text="Flower", width=8,
                              command=lambda: self.set_text_field("Flower"),
                              font=("Arial", 11, "bold"), bg="#FFB6C1")
        flower_btn.pack(side=tk.LEFT, padx=2)
        
        # Jokers
        joker_label = tk.Label(honor_frame, text="Jokers:", font=("Arial", 11))
        joker_label.pack(anchor=tk.W, padx=5, pady=(5,0))
        
        joker_btn_frame = tk.Frame(honor_frame)
        joker_btn_frame.pack(pady=(2,5))
        
        joker_btn = tk.Button(joker_btn_frame, text="Joker", width=8,
                             command=lambda: self.set_text_field("Joker"),
                             font=("Arial", 11, "bold"), bg="#FFA500")
        joker_btn.pack(side=tk.LEFT, padx=2)
        
        # Text field and add button
        entry_frame = tk.Frame(selector_frame)
        entry_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(entry_frame, text="Tile:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.tile_entry = tk.Entry(entry_frame, font=("Arial", 12), width=20)
        self.tile_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        add_btn = tk.Button(entry_frame, text="Add Tile", 
                           command=self.add_tile_from_entry, bg="#4CAF50", fg="black",
                           font=("Arial", 12, "bold"), padx=10, pady=5)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        clear_entry_btn = tk.Button(entry_frame, text="Clear", 
                                    command=self.clear_text_field, bg="#9E9E9E", fg="black",
                                    font=("Arial", 11), padx=5, pady=5)
        clear_entry_btn.pack(side=tk.LEFT, padx=2)
        
        # Selected tiles display
        selected_frame = tk.LabelFrame(left_frame, text="Your Hand", 
                                       font=("Arial", 10, "bold"))
        selected_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Listbox with scrollbar (enable multiple selection)
        scroll = tk.Scrollbar(selected_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tiles_listbox = tk.Listbox(selected_frame, yscrollcommand=scroll.set,
                                        font=("Arial", 12), height=15, 
                                        selectmode=tk.EXTENDED)  # Allow multiple selection
        self.tiles_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.config(command=self.tiles_listbox.yview)
        
        # Buttons
        btn_frame = tk.Frame(left_frame)
        btn_frame.pack(pady=10)
        
        remove_btn = tk.Button(btn_frame, text="Remove Selected", 
                              command=self.remove_tile, bg="#f44336", fg="black",
                              font=("Arial", 11, "bold"), padx=10, pady=5)
        remove_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(btn_frame, text="Clear All", 
                             command=self.clear_tiles, bg="#ff9800", fg="black",
                             font=("Arial", 11, "bold"), padx=10, pady=5)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Right side - Results
        right_frame = tk.LabelFrame(main_frame, text="Best Potential Hands", 
                                    font=("Arial", 12, "bold"))
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        analyze_btn = tk.Button(right_frame, text="Find Best Hands", 
                               command=self.analyze_hand, bg="#2196F3", fg="black",
                               font=("Arial", 12, "bold"), padx=15, pady=8)
        analyze_btn.pack(pady=10)
        
        # Results display
        self.results_text = tk.Text(right_frame, font=("Arial", 11), 
                                    wrap=tk.WORD, state=tk.DISABLED)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def add_to_text_field(self, text):
        current = self.tile_entry.get()
        if current and not current.endswith(" "):
            self.tile_entry.insert(tk.END, " " + text)
        else:
            self.tile_entry.insert(tk.END, text)
    
    def set_text_field(self, text):
        self.tile_entry.delete(0, tk.END)
        self.tile_entry.insert(0, text)
    
    def clear_text_field(self):
        self.tile_entry.delete(0, tk.END)
    
    def add_tile_from_entry(self):
        tile = self.tile_entry.get().strip()
        if tile:
            if tile in self.tile_types:
                self.selected_tiles.append(tile)
                self.tiles_listbox.insert(tk.END, tile)
                self.tile_entry.delete(0, tk.END)
            else:
                tile_lower = tile.lower()
                for valid_tile in self.tile_types:
                    if valid_tile.lower() == tile_lower:
                        self.selected_tiles.append(valid_tile)
                        self.tiles_listbox.insert(tk.END, valid_tile)
                        self.tile_entry.delete(0, tk.END)
                        return
                self.tile_entry.delete(0, tk.END)
                self.tile_entry.insert(0, "Invalid tile! Try again...")
                self.root.after(1500, self.clear_text_field)
    
    def remove_tile(self):
        selection = self.tiles_listbox.curselection()
        if selection:
            # Remove tiles in reverse order to maintain correct indices
            for idx in reversed(selection):
                self.tiles_listbox.delete(idx)
                self.selected_tiles.pop(idx)
    
    def clear_tiles(self):
        self.selected_tiles.clear()
        self.tiles_listbox.delete(0, tk.END)
    
    def analyze_hand(self):
        if not self.selected_tiles:
            self.display_results("Please select some tiles first!")
            return
        
        hand_counter = Counter(self.selected_tiles)
        joker_count = hand_counter.get("Joker", 0)
        
        hand_scores = []
        for hand_name, required_tiles, points in MAHJONG_HANDS:
            required_counter = Counter(required_tiles)
            
            matches = 0
            for tile, count in required_counter.items():
                matches += min(hand_counter.get(tile, 0), count)
            
            remaining_jokers = joker_count
            tiles_needed = []
            
            for tile, required_count in required_counter.items():
                have_count = hand_counter.get(tile, 0)
                needed = required_count - have_count
                
                if needed > 0 and required_count >= 3:
                    tiles_needed.append((tile, needed, required_count))
            
            tiles_needed.sort(key=lambda x: x[2], reverse=True)
            
            jokers_used = 0
            for tile, needed, required_count in tiles_needed:
                if remaining_jokers > 0:
                    can_use = min(needed, remaining_jokers)
                    jokers_used += can_use
                    remaining_jokers -= can_use
                    matches += can_use
            
            total_required = len(required_tiles)
            match_percentage = (matches / total_required) * 100
            
            if matches > 0:
                hand_scores.append({
                    'name': hand_name,
                    'matches': matches,
                    'total_required': total_required,
                    'percentage': match_percentage,
                    'points': points,
                    'missing': total_required - matches,
                    'required_tiles': required_counter,
                    'jokers_used': jokers_used
                })
        
        hand_scores.sort(key=lambda x: (x['matches'], x['points']), reverse=True)
        self.display_results(self.format_top_hands(hand_scores[:3]))
    
    def format_top_hands(self, top_hands):
        if not top_hands:
            return "No matching hands found with your current tiles."
        
        result = "TOP 3 POTENTIAL HANDS:\n\n"
        result += "=" * 60 + "\n\n"
        
        for i, hand in enumerate(top_hands, 1):
            result += f"#{i}: {hand['name']}\n"
            result += f"Points Value: {hand['points']} points\n"
            result += f"Progress: {hand['matches']}/{hand['total_required']} tiles "
            result += f"({hand['percentage']:.1f}%)\n"
            if hand.get('jokers_used', 0) > 0:
                result += f"Jokers Used: {hand['jokers_used']}\n"
            result += "\n"
            
            result += "The Line:\n"
            result += self.format_line_pattern(hand['required_tiles'])
            result += "\n\n"
            
            result += "What You Have:\n"
            hand_counter = Counter(self.selected_tiles)
            result += self.format_what_you_have(hand['required_tiles'], hand_counter, hand.get('jokers_used', 0))
            result += "\n\n"
            
            result += "Missing:\n"
            result += self.format_missing_tiles(hand['required_tiles'], hand_counter, hand.get('jokers_used', 0))
            result += "\n"
            
            result += "\n" + "-" * 60 + "\n\n"
        
        return result
    
    def format_line_pattern(self, required_tiles):
        line = ""
        for tile, count in sorted(required_tiles.items()):
            abbrev = self.get_tile_abbreviation(tile)
            line += abbrev * count + " "
        return line.strip()
    
    def format_what_you_have(self, required_tiles, hand_counter, jokers_used=0):
        line = ""
        remaining_jokers = jokers_used
        
        tiles_with_jokers = []
        for tile, required_count in sorted(required_tiles.items()):
            have_count = hand_counter.get(tile, 0)
            
            jokers_for_tile = 0
            if required_count >= 3 and remaining_jokers > 0:
                needed = required_count - have_count
                if needed > 0:
                    jokers_for_tile = min(needed, remaining_jokers)
                    remaining_jokers -= jokers_for_tile
            
            tiles_with_jokers.append((tile, required_count, have_count, jokers_for_tile))
        
        for tile, required_count, have_count, jokers_for_tile in tiles_with_jokers:
            abbrev = self.get_tile_abbreviation(tile)
            line += abbrev * have_count
            line += "J" * jokers_for_tile
            missing = required_count - have_count - jokers_for_tile
            line += "_" * missing
            line += " "
        
        return line.strip()
    
    def format_missing_tiles(self, required_tiles, hand_counter, jokers_used=0):
        missing = []
        remaining_jokers = jokers_used
        
        for tile, required_count in sorted(required_tiles.items()):
            have_count = hand_counter.get(tile, 0)
            needed = required_count - have_count
            
            if needed > 0:
                jokers_for_tile = 0
                if required_count >= 3 and remaining_jokers > 0:
                    jokers_for_tile = min(needed, remaining_jokers)
                    remaining_jokers -= jokers_for_tile
                
                still_needed = needed - jokers_for_tile
                if still_needed > 0:
                    abbrev = self.get_tile_abbreviation(tile)
                    missing.append(abbrev * still_needed)
        
        if not missing:
            return "None - You have all tiles!"
        return " ".join(missing)
    
    def get_tile_abbreviation(self, tile):
        if tile == "North Wind":
            return "N"
        elif tile == "East Wind":
            return "E"
        elif tile == "West Wind":
            return "W"
        elif tile == "South Wind":
            return "S"
        elif tile == "Red Dragon":
            return "D"
        elif tile == "Green Dragon":
            return "D"
        elif tile == "White Dragon":
            return "D"
        elif tile == "Flower":
            return "F"
        elif tile == "Joker":
            return "J"
        else:
            parts = tile.split()
            if len(parts) == 2:
                number = parts[0]
                suit = parts[1][0]
                return f"{number}{suit}"
            return tile
    
    def display_results(self, text):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, text)
        self.results_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MahjongHelper(root)
    root.mainloop()