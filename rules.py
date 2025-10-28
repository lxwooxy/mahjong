from itertools import permutations, combinations

def generate_mahjong_hands():
    # Define all possible Mahjong hands based on the official card
    MAHJONG_HANDS = []

    suits = ["Bamboo", "Character", "Dot"]
    dragons = ["Red Dragon", "Green Dragon", "White Dragon"]
    # ANY LIKE NUMBERS SECTION

    # FFFF 11 111 111 11 (Any 3 Suits, Pairs Must Be Same Suit)
    for num in range(1, 10):
        for s1, s2, s3 in combinations(suits, 3):
            MAHJONG_HANDS.append((
                f"FFFF {num}{num} {num}{num}{num} {num}{num}{num} {num}{num} - {s1}/{s2}/{s3}",
                ["Flower"]*4 + [f"{num} {s1}"]*2 + [f"{num} {s2}"]*3 + [f"{num} {s3}"]*3 + [f"{num} {s1}"]*2,
                30
            ))
            # Add more permutations where pairs are in different suits
            MAHJONG_HANDS.append((
                f"FFFF {num}{num} {num}{num}{num} {num}{num}{num} {num}{num} - {s1}/{s2}/{s3}",
                ["Flower"]*4 + [f"{num} {s2}"]*2 + [f"{num} {s1}"]*3 + [f"{num} {s3}"]*3 + [f"{num} {s2}"]*2,
                30
            ))
            MAHJONG_HANDS.append((
                f"FFFF {num}{num} {num}{num}{num} {num}{num}{num} {num}{num} - {s1}/{s2}/{s3}",
                ["Flower"]*4 + [f"{num} {s3}"]*2 + [f"{num} {s1}"]*3 + [f"{num} {s2}"]*3 + [f"{num} {s3}"]*2,
                30
            ))
            
    # FF 1111 D 1111 D 11 

    for num in range(1, 10):
        for s1, s2, s3 in combinations(suits, 3):
            for d1, d2 in combinations(dragons, 2):
                # All 6 ways to arrange 4,4,2 across three suits
                MAHJONG_HANDS.append((
                    f"FF {num}{num}{num}{num} D {num}{num}{num}{num} D {num}{num} - {s1}/{s2}/{s3}",
                    ["Flower"]*2 + [f"{num} {s1}"]*4 + [d1] + [f"{num} {s2}"]*4 + [d2] + [f"{num} {s3}"]*2,
                    25
                ))
                MAHJONG_HANDS.append((
                    f"FF {num}{num}{num}{num} D {num}{num}{num}{num} D {num}{num} - {s1}/{s2}/{s3}",
                    ["Flower"]*2 + [f"{num} {s1}"]*4 + [d1] + [f"{num} {s3}"]*4 + [d2] + [f"{num} {s2}"]*2,
                    25
                ))
                MAHJONG_HANDS.append((
                    f"FF {num}{num}{num}{num} D {num}{num}{num}{num} D {num}{num} - {s1}/{s2}/{s3}",
                    ["Flower"]*2 + [f"{num} {s2}"]*4 + [d1] + [f"{num} {s1}"]*4 + [d2] + [f"{num} {s3}"]*2,
                    25
                ))
                MAHJONG_HANDS.append((
                    f"FF {num}{num}{num}{num} D {num}{num}{num}{num} D {num}{num} - {s1}/{s2}/{s3}",
                    ["Flower"]*2 + [f"{num} {s2}"]*4 + [d1] + [f"{num} {s3}"]*4 + [d2] + [f"{num} {s1}"]*2,
                    25
                ))
                MAHJONG_HANDS.append((
                    f"FF {num}{num}{num}{num} D {num}{num}{num}{num} D {num}{num} - {s1}/{s2}/{s3}",
                    ["Flower"]*2 + [f"{num} {s3}"]*4 + [d1] + [f"{num} {s1}"]*4 + [d2] + [f"{num} {s2}"]*2,
                    25
                ))
                MAHJONG_HANDS.append((
                    f"FF {num}{num}{num}{num} D {num}{num}{num}{num} D {num}{num} - {s1}/{s2}/{s3}",
                    ["Flower"]*2 + [f"{num} {s3}"]*4 + [d1] + [f"{num} {s2}"]*4 + [d2] + [f"{num} {s1}"]*2,
                    25
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

    # Add variations for FF 123 DD DDD DDDD (any 3 consecutive in any suit, any 2, 3, and 4 dragons)
    for suit in suits:
        for start in range(1, 8):  # 1-7 start positions for consecutive
            # Generate all ways to distribute 2, 3, 4 among the three dragon types
            dragon_distributions = [
                (2, 3, 4),  # RD=2, GD=3, WD=4
                (2, 4, 3),  # RD=2, GD=4, WD=3
                (3, 2, 4),  # RD=3, GD=2, WD=4
                (3, 4, 2),  # RD=3, GD=4, WD=2
                (4, 2, 3),  # RD=4, GD=2, WD=3
                (4, 3, 2),  # RD=4, GD=3, WD=2
            ]
            
            for rd_count, gd_count, wd_count in dragon_distributions:
                MAHJONG_HANDS.append((
                    f"FF {start}{start+1}{start+2} DD DDD DDDD - {suit}",
                    ["Flower"]*2 + [f"{start} {suit}", f"{start+1} {suit}", f"{start+2} {suit}"] + 
                    ["Red Dragon"]*rd_count + ["Green Dragon"]*gd_count + ["White Dragon"]*wd_count,
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
            [f"2 {suit}"]*3 + [f"4 {suit}"]*4 + [f"6 {suit}"]*3 + [f"8 {suit}"]*4,
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
        # 2s
        MAHJONG_HANDS.append((
            f"FFFF 2025 222 222 - {s1}/{s2}/{s3}",
            ["Flower"]*4 + [f"2 {s1}", "White Dragon", f"2 {s1}", f"5 {s1}"] + 
            [f"2 {s2}"]*3 + [f"2 {s3}"]*3,
            25
        ))
        # 5s
        MAHJONG_HANDS.append((
            f"FFFF 2025 555 555 - {s1}/{s2}/{s3}",
            ["Flower"]*4 + [f"2 {s1}", "White Dragon", f"2 {s1}", f"5 {s1}"] + 
            [f"5 {s2}"]*3 + [f"5 {s3}"]*3,
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

    # Remove duplicate hands (same tiles, same points)
    seen = set()
    unique_hands = []
    for hand_name, tiles, points in MAHJONG_HANDS:
        # Create a sortable representation of the tiles
        tiles_tuple = tuple(sorted(tiles))
        key = (tiles_tuple, points)
        if key not in seen:
            seen.add(key)
            unique_hands.append((hand_name, tiles, points))

    return unique_hands
