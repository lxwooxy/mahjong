import tkinter as tk
from tkinter import ttk
from collections import Counter
from itertools import combinations
from PIL import Image, ImageTk
import os

# Define all possible Mahjong hands based on the official card
MAHJONG_HANDS = []

suits = ["Bamboo", "Character", "Dot"]

# ANY LIKE NUMBERS SECTION
# FF 1111 D 1111 D 11 (Any 3 Suits)
for num in range(1, 10):
    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"FF {num}{num}{num}{num} D {num}{num}{num}{num} D {num}{num} - {s1}/{s2}/{s3}",
            ["Flower"]*2 + [f"{num} {s1}"]*4 + ["Red Dragon"] + [f"{num} {s2}"]*4 + 
            ["Green Dragon"] + [f"{num} {s3}"]*2,
            25
        ))

# FFFF 11 111 111 11 (Any 3 Suits, Pairs Must Be Same Suit)
for num in range(1, 10):
    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"FFFF {num}{num} {num}{num}{num} {num}{num}{num} {num}{num} - {s1}/{s2}/{s3}",
            ["Flower"]*4 + [f"{num} {s1}"]*2 + [f"{num} {s2}"]*3 + [f"{num} {s3}"]*3 + [f"{num} {s1}"]*2,
            30
        ))

# FF 111 111 111 DDD (Any 3 Suits, Any Dragon)
for num in range(1, 10):
    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"FF {num}{num}{num} {num}{num}{num} {num}{num}{num} DDD - {s1}/{s2}/{s3}",
            ["Flower"]*2 + [f"{num} {s1}"]*3 + [f"{num} {s2}"]*3 + [f"{num} {s3}"]*3 + ["Red Dragon"]*3,
            30
        ))

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
    
# 2468 SECTION
# 222 4444 666 8888 (any 1 or 2 suits)
for suit in suits:
    MAHJONG_HANDS.append((
        f"222 4444 666 8888 - {suit}",
        [f"2 {suit}"]*3 + [f"4 {suit}"]*4 + [f"6 {suit}"]*4 + [f"8 {suit}"]*4,
        25
    ))

for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"222 4444 666 8888 - {s1}/{s2}",
        [f"2 {s1}"]*3 + [f"4 {s1}"]*4 + [f"6 {s2}"]*4 + [f"8 {s2}"]*4,
        25
    ))

# FF 2222 + 4444 = 6666 -or- FF 2222 + 6666 = 8888 (Any 3 Suits)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"FF 2222 + 4444 = 6666 - {s1}/{s2}/{s3}",
        ["Flower"]*2 + [f"2 {s1}"]*4 + [f"4 {s2}"]*4 + [f"6 {s3}"]*4,
        25
    ))
    MAHJONG_HANDS.append((
        f"FF 2222 + 6666 = 8888 - {s1}/{s2}/{s3}",
        ["Flower"]*2 + [f"2 {s1}"]*4 + [f"6 {s2}"]*4 + [f"8 {s3}"]*4,
        25
    ))

# 22 444 66 888 DDDD (Any 1 Suit)
for suit in suits:
    MAHJONG_HANDS.append((
        f"22 444 66 888 DDDD - {suit}",
        [f"2 {suit}"]*2 + [f"4 {suit}"]*3 + [f"6 {suit}"]*2 + [f"8 {suit}"]*3 + ["Red Dragon"]*4,
        25
    ))

# FFFF 2468 222 222 (Any 3 Suits, Like Pungs Any Even No.)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"FFFF 2468 222 222 - {s1}/{s2}/{s3}",
        ["Flower"]*4 + [f"2 {s1}", f"4 {s1}", f"6 {s1}", f"8 {s1}"] + [f"2 {s2}"]*3 + [f"2 {s3}"]*3,
        25
    ))

# FFF 22 44 666 8888 (Any 1 Suit)
for suit in suits:
    MAHJONG_HANDS.append((
        f"FFF 22 44 666 8888 - {suit}",
        ["Flower"]*3 + [f"2 {suit}"]*2 + [f"4 {suit}"]*2 + [f"6 {suit}"]*3 + [f"8 {suit}"]*4,
        25
    ))

# 222 4444 666 88 88 (Any 3 Suits, Pairs 8s Only)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"222 4444 666 88 88 - {s1}/{s2}/{s3}",
        [f"2 {s1}"]*3 + [f"4 {s2}"]*4 + [f"6 {s3}"]*3 + [f"8 {s1}"]*2 + [f"8 {s2}"]*2,
        25
    ))

# FF 2222 DDDD 2222 (Any 3 Suits, Like Kongs Any Even No.)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"FF 2222 DDDD 2222 - {s1}/{s2}/{s3}",
        ["Flower"]*2 + [f"2 {s1}"]*4 + ["Red Dragon"]*4 + [f"2 {s2}"]*4,
        25
    ))

# 22 44 66 88 222 222 (Any 3 Suits, Like Pungs Any Even No.)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"22 44 66 88 222 222 - {s1}/{s2}/{s3}",
        [f"2 {s1}"]*2 + [f"4 {s2}"]*2 + [f"6 {s3}"]*2 + [f"8 {s1}"]*2 + [f"2 {s2}"]*3 + [f"2 {s3}"]*3,
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

# 2025 SECTION
# FF 2025 2025 2025 (any 3 suits)
MAHJONG_HANDS.append((
    "FF 2025 2025 2025",
    ["Flower"]*2 + 
    ["2 Bamboo", "White Dragon", "2 Bamboo", "5 Bamboo"] + 
    ["2 Character", "White Dragon", "2 Character", "5 Character"] + 
    ["2 Dot", "White Dragon", "2 Dot", "5 Dot"],
    75
))

# FFFF 2025 222 222 (Any 3 Suits, Like Pungs 2s or 5s in Opp. Suits)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"FFFF 2025 222 222 - {s1}/{s2}/{s3}",
        ["Flower"]*4 + [f"2 {s1}", "White Dragon", f"2 {s1}", f"5 {s1}"] + 
        [f"2 {s2}"]*3 + [f"2 {s3}"]*3,
        25
    ))

# 222 0000 222 5555 (Any 2 Suits)
for s1, s2 in combinations(suits, 2):
    MAHJONG_HANDS.append((
        f"222 0000 222 5555 - {s1}/{s2}",
        [f"2 {s1}"]*3 + ["White Dragon"]*4 + [f"2 {s2}"]*3 + [f"5 {s2}"]*4,
        25
    ))

# 2025 222 555 DDDD (Any 3 Suits)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"2025 222 555 DDDD - {s1}/{s2}/{s3}",
        [f"2 {s1}", "White Dragon", f"2 {s1}", f"5 {s1}"] + 
        [f"2 {s2}"]*3 + [f"5 {s3}"]*3 + ["Red Dragon"]*4,
        30
    ))

# FF 222 000 222 555 (Any 3 Suits)
for s1, s2, s3 in combinations(suits, 3):
    MAHJONG_HANDS.append((
        f"FF 222 000 222 555 - {s1}/{s2}/{s3}",
        ["Flower"]*2 + [f"2 {s1}"]*3 + ["White Dragon"]*3 + 
        [f"2 {s2}"]*3 + [f"5 {s3}"]*3,
        30
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


class MahjongHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("Mahjong Hand Helper - Official Rules")
        self.root.geometry("1920x1080")
        
        # Available tiles
        self.tile_types = []
        for i in range(1, 10):  # 1-9 only, no 0
            self.tile_types.extend([f"{i} Bamboo", f"{i} Character", f"{i} Dot"])
        self.tile_types.extend(["East Wind", "South Wind", "West Wind", "North Wind",
                               "Red Dragon", "Green Dragon", "White Dragon",
                               "Flower", "Joker"])
        
        # Map tile names to image filenames
        self.tile_to_image = {
            "1 Bamboo": "1bam.png", "2 Bamboo": "2bam.png", "3 Bamboo": "3bam.png",
            "4 Bamboo": "4bam.png", "5 Bamboo": "5bam.png", "6 Bamboo": "6bam.png",
            "7 Bamboo": "7bam.png", "8 Bamboo": "8bam.png", "9 Bamboo": "9bam.png",
            "1 Character": "1crack.png", "2 Character": "2crack.png", "3 Character": "3crack.png",
            "4 Character": "4crack.png", "5 Character": "5crack.png", "6 Character": "6crack.png",
            "7 Character": "7crack.png", "8 Character": "8crack.png", "9 Character": "9crack.png",
            "1 Dot": "1dot.png", "2 Dot": "2dot.png", "3 Dot": "3dot.png",
            "4 Dot": "4dot.png", "5 Dot": "5dot.png", "6 Dot": "6dot.png",
            "7 Dot": "7dot.png", "8 Dot": "8dot.png", "9 Dot": "9dot.png",
            "East Wind": "east.png", "South Wind": "south.png", 
            "West Wind": "west.png", "North Wind": "north.png",
            "Red Dragon": "reddragon.png", "Green Dragon": "greendragon.png", 
            "White Dragon": "soap.png",
            "Flower": "flower.png", "Joker": "joker.png"
        }
        
        self.selected_tiles = []
        self.tile_images = {}  # Store PhotoImage objects
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Mahjong Hand Helper - Official Rules", 
                        font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        # Instructions
        instructions = tk.Label(self.root, 
                            text="Click on tiles to add them to your hand, then click 'Find Best Hands'",
                            font=("Arial", 11))
        instructions.pack(pady=5)
        
        # Main container - split left and right
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configure grid weights for resizing
        main_frame.grid_columnconfigure(0, weight=5)  # Left gets 3/4
        main_frame.grid_columnconfigure(1, weight=1)  # Right gets 1/4
        main_frame.grid_rowconfigure(0, weight=1)
        
        # Left half - will contain tile selection (top) and hand (bottom)
        left_half = tk.Frame(main_frame)
        left_half.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        # Right half - results
        right_half = tk.LabelFrame(main_frame, text="Best Potential Hands", 
                                    font=("Arial", 12, "bold"))
        right_half.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        
        # === LEFT HALF TOP: Tile Selection ===
        tile_selection_frame = tk.LabelFrame(left_half, text="Select Your Tiles", 
                                            font=("Arial", 12, "bold"))
        tile_selection_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False, pady=(0, 5))
        
        # Create scrollable frame for tile buttons
        tile_canvas = tk.Canvas(tile_selection_frame, height=450)
        tile_scrollbar = tk.Scrollbar(tile_selection_frame, orient="vertical", command=tile_canvas.yview)
        scrollable_frame = tk.Frame(tile_canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: tile_canvas.configure(scrollregion=tile_canvas.bbox("all"))
        )
        
        tile_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        tile_canvas.configure(yscrollcommand=tile_scrollbar.set)
        
        # Load and display tile images
        self.load_tile_images(scrollable_frame)
        
        tile_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tile_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # === LEFT HALF BOTTOM: Your Hand ===
        hand_section = tk.LabelFrame(left_half, text="Your Hand", 
                                    font=("Arial", 12, "bold"))
        hand_section.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, pady=(5, 0))
        
        # Create canvas for scrollable hand display
        self.hand_canvas = tk.Canvas(hand_section, height=160, bg="white")
        hand_scrollbar = tk.Scrollbar(hand_section, orient="horizontal", 
                                    command=self.hand_canvas.xview)
        self.hand_frame = tk.Frame(self.hand_canvas, bg="white")
        
        self.hand_frame.bind(
            "<Configure>",
            lambda e: self.hand_canvas.configure(scrollregion=self.hand_canvas.bbox("all"))
        )
        
        self.hand_canvas.create_window((0, 0), window=self.hand_frame, anchor="nw")
        self.hand_canvas.configure(xscrollcommand=hand_scrollbar.set)
        
        self.hand_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        hand_scrollbar.pack(side=tk.BOTTOM, fill=tk.X, padx=5)
        
        # Store hand tile widgets for easy removal
        self.hand_tile_widgets = []
        
        # Clear button for hand
        btn_frame = tk.Frame(hand_section)
        btn_frame.pack(pady=5)
        
        clear_btn = tk.Button(btn_frame, text="Clear All", 
                            command=self.clear_tiles, bg="#ff9800", fg="black",
                            font=("Arial", 11, "bold"), padx=10, pady=5)
        clear_btn.pack()
        
        # === RIGHT HALF: Results ===
        analyze_btn = tk.Button(right_half, text="Find Best Hands", 
                            command=self.analyze_hand, bg="#2196F3", fg="black",
                            font=("Arial", 12, "bold"), padx=15, pady=8)
        analyze_btn.pack(pady=10)
        
        # Results display
        self.results_text = tk.Text(right_half, font=("Arial", 10), 
                                    wrap=tk.WORD, state=tk.DISABLED)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def load_tile_images(self, parent):
        """Load tile images and create buttons"""
        # Create a container with two columns
        container = tk.Frame(parent)
        container.pack(fill=tk.BOTH, expand=True)
        
        # Left column for Bamboo, Character, Dot, Dragons
        left_column = tk.Frame(container)
        left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Right column for Winds and Special
        right_column = tk.Frame(container)
        right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=5)
        
        # === LEFT COLUMN ===
        # Bamboo tiles
        bam_frame = tk.LabelFrame(left_column, text="Bamboo", font=("Arial", 10, "bold"))
        bam_frame.pack(fill=tk.X, padx=5, pady=2)
        
        bam_btn_frame = tk.Frame(bam_frame)
        bam_btn_frame.pack(pady=5)
        
        for i in range(1, 10):
            tile_name = f"{i} Bamboo"
            self.create_tile_button(bam_btn_frame, tile_name)
        
        # Character tiles
        char_frame = tk.LabelFrame(left_column, text="Character (Crack)", font=("Arial", 10, "bold"))
        char_frame.pack(fill=tk.X, padx=5, pady=2)
        
        char_btn_frame = tk.Frame(char_frame)
        char_btn_frame.pack(pady=5)
        
        for i in range(1, 10):
            tile_name = f"{i} Character"
            self.create_tile_button(char_btn_frame, tile_name)
        
        # Dot tiles
        dot_frame = tk.LabelFrame(left_column, text="Dot", font=("Arial", 10, "bold"))
        dot_frame.pack(fill=tk.X, padx=5, pady=2)
        
        dot_btn_frame = tk.Frame(dot_frame)
        dot_btn_frame.pack(pady=5)
        
        for i in range(1, 10):
            tile_name = f"{i} Dot"
            self.create_tile_button(dot_btn_frame, tile_name)
        
        # Dragons 
        dragon_frame = tk.LabelFrame(left_column, text="Dragons", font=("Arial", 10, "bold"))
        dragon_frame.pack(fill=tk.X, padx=5, pady=2)
        
        dragon_btn_frame = tk.Frame(dragon_frame)
        dragon_btn_frame.pack(pady=5)
        
        for dragon in ["Red Dragon", "Green Dragon", "White Dragon"]:
            self.create_tile_button(dragon_btn_frame, dragon)
        
        # === RIGHT COLUMN ===
        # Winds in NEWS configuration
        wind_frame = tk.LabelFrame(right_column, text="Winds", font=("Arial", 10, "bold"))
        wind_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Create a grid for NEWS layout
        wind_grid = tk.Frame(wind_frame)
        wind_grid.pack(pady=5)
        
        # North (top center)
        north_frame = tk.Frame(wind_grid)
        north_frame.grid(row=0, column=1, padx=2, pady=2)
        self.create_tile_button(north_frame, "North Wind")
        
        # West (middle left) - East (middle right)
        west_frame = tk.Frame(wind_grid)
        west_frame.grid(row=1, column=0, padx=2, pady=2)
        self.create_tile_button(west_frame, "West Wind")
        
        east_frame = tk.Frame(wind_grid)
        east_frame.grid(row=1, column=2, padx=2, pady=2)
        self.create_tile_button(east_frame, "East Wind")
        
        # South (bottom center)
        south_frame = tk.Frame(wind_grid)
        south_frame.grid(row=2, column=1, padx=2, pady=2)
        self.create_tile_button(south_frame, "South Wind")
        
        # Special tiles
        special_frame = tk.LabelFrame(right_column, text="Special", font=("Arial", 10, "bold"))
        special_frame.pack(fill=tk.X, padx=5, pady=5)
        
        special_btn_frame = tk.Frame(special_frame)
        special_btn_frame.pack(pady=5)
        
        for special in ["Flower", "Joker"]:
            self.create_tile_button(special_btn_frame, special)

    def create_tile_button(self, parent, tile_name):
        """Create a button with tile image"""
        img_path = os.path.join("images", self.tile_to_image[tile_name])
        
        #print(f"Attempting to load: {tile_name} from {img_path}")
        
        try:
            # Check if file exists
            if not os.path.exists(img_path):
                #print(f"  FILE NOT FOUND: {img_path}")
                raise FileNotFoundError(f"Image not found: {img_path}")
            
            #print(f"  File exists, loading...")
            # Load and resize image
            img = Image.open(img_path)
            #print(f"  Image opened: {img.size}")
            img = img.resize((50, 70), Image.Resampling.LANCZOS)
            #print(f"  Image resized to 50x70")
            photo = ImageTk.PhotoImage(img)
            #print(f"  PhotoImage created")
            
            # Store reference to prevent garbage collection
            self.tile_images[tile_name] = photo
            
            # Create button with image
            btn = tk.Button(parent, image=photo, 
                        command=lambda t=tile_name: self.add_tile(t),
                        relief=tk.RAISED, borderwidth=2)
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            #print(f"  SUCCESS: Button created for {tile_name}")
            
        except Exception as e:
            # #print error for debugging
            #print(f"  ERROR loading image for {tile_name}: {e}")
            #print(f"  Exception type: {type(e).__name__}")
            import traceback
            traceback.print_exc()
            
            # Fallback to text button if image not found
            btn = tk.Button(parent, text=tile_name.split()[0], 
                        command=lambda t=tile_name: self.add_tile(t),
                        width=6, height=3, font=("Arial", 9))
            btn.pack(side=tk.LEFT, padx=2, pady=2)

    def add_tile(self, tile_name):
        """Add a tile to the hand with image display"""
        self.selected_tiles.append(tile_name)
        
        # Create a frame for this tile
        tile_container = tk.Frame(self.hand_frame, bg="white", relief=tk.RAISED, borderwidth=2)
        tile_container.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Load and display the tile image
        img_path = os.path.join("images", self.tile_to_image[tile_name])
        try:
            img = Image.open(img_path)
            img = img.resize((50, 70), Image.Resampling.LANCZOS)  # Slightly smaller for hand display
            photo = ImageTk.PhotoImage(img)
            
            # Create label with image
            idx = len(self.hand_tile_widgets)
            img_label = tk.Label(tile_container, image=photo, bg="white", cursor="hand2")
            img_label.image = photo  # Keep a reference
            img_label.pack()
            
            # Make the tile clickable to remove it
            img_label.bind("<Button-1>", lambda e, i=idx: self.remove_tile_by_index(i))
            tile_container.bind("<Button-1>", lambda e, i=idx: self.remove_tile_by_index(i))
            
            # Store the container and index
            self.hand_tile_widgets.append((tile_container, tile_name))
            
        except Exception as e:
            # Fallback to text if image fails
            idx = len(self.hand_tile_widgets)
            text_label = tk.Label(tile_container, text=tile_name.split()[0], 
                                bg="lightgray", width=6, height=4, relief=tk.RAISED, cursor="hand2")
            text_label.pack()
            
            # Make the tile clickable to remove it
            text_label.bind("<Button-1>", lambda e, i=idx: self.remove_tile_by_index(i))
            tile_container.bind("<Button-1>", lambda e, i=idx: self.remove_tile_by_index(i))
            
            self.hand_tile_widgets.append((tile_container, tile_name))
            
            
    def remove_tile_by_index(self, index):
        """Remove a specific tile from the hand by its index"""
        if 0 <= index < len(self.hand_tile_widgets):
            # Remove the widget
            container, tile_name = self.hand_tile_widgets[index]
            container.destroy()
            
            # Remove from data structures
            self.hand_tile_widgets.pop(index)
            self.selected_tiles.pop(index)
            
            # Update all remaining buttons to have correct indices
            for i, (container, _) in enumerate(self.hand_tile_widgets):
                # Find and update the remove button
                for widget in container.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(command=lambda idx=i: self.remove_tile_by_index(idx))
    
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
        """Clear all tiles from the hand"""
        self.selected_tiles.clear()
        
        # Destroy all tile widgets
        for container, _ in self.hand_tile_widgets:
            container.destroy()
        
        self.hand_tile_widgets.clear()
    
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