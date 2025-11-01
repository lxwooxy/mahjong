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
            for dragon in dragons:
                MAHJONG_HANDS.append((
                    f"FF {num}{num}{num} {num}{num}{num} {num}{num}{num} DDD - {s1}/{s2}/{s3}",
                    ["Flower"]*2 + [f"{num} {s1}"]*3 + [f"{num} {s2}"]*3 + [f"{num} {s3}"]*3 + [dragon]*3,
                    30
                ))

    # WINDS-DRAGONS SECTION
    MAHJONG_HANDS.extend([
        ("NNNN EEEE WWW SSSS", ["North Wind"]*4 + ["East Wind"]*3 + ["West Wind"]*3 + ["South Wind"]*4, 25),
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

    MAHJONG_HANDS.append((
        "FFF NN EE WWW SSSS",
        ["Flower"]*3 + ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*3 + ["South Wind"]*4,
        25
    ))

    # FFFF DDD NEWS DDD (any 2 different dragons)
    for d1, d2 in combinations(dragons, 2):
        MAHJONG_HANDS.append((
            "FFFF DDD NEWS DDD",
            ["Flower"]*4 + [d1]*3 + ["North Wind"] + ["East Wind"] + ["West Wind"] + ["South Wind"] + [d2]*3,
            25
        ))

    # Like Odd Numbers in 3 Suits (NNNN 1 11 111 SSSS)
    for odd in [1, 3, 5, 7, 9]:
        for s1, s2, s3 in permutations(suits, 3):
            MAHJONG_HANDS.append((
                f"NNNN {odd} {odd}{odd} {odd}{odd}{odd} SSSS",
                ["North Wind"]*4 + [f"{odd} {s1}"] + [f"{odd} {s2}"]*2 + [f"{odd} {s3}"]*3 + ["South Wind"]*4,
                25
            ))

    # Like Even Numbers in 3 Suits (EEEE 2 22 222 WWWW)
    for even in [2, 4, 6, 8]:
        for s1, s2, s3 in permutations(suits, 3):
            MAHJONG_HANDS.append((
                f"EEEE {even} {even}{even} {even}{even}{even} WWWW",
                ["East Wind"]*4 + [f"{even} {s1}"] + [f"{even} {s2}"]*2 + [f"{even} {s3}"]*3 + ["West Wind"]*4,
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
            [f"2 {s1}"]*3 + [f"4 {s1}"]*4 + [f"6 {s2}"]*3 + [f"8 {s2}"]*4,
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
        for even in [2, 4, 6, 8]:
            MAHJONG_HANDS.append((
                f"FFFF 2468 {even}{even}{even} {even}{even}{even} - {s1}/{s2}/{s3}",
                ["Flower"]*4 + [f"2 {s1}", f"4 {s1}", f"6 {s1}", f"8 {s1}"] + [f"{even} {s2}"]*3 + [f"{even} {s3}"]*3,
                25
            ))

    # FFF 22 44 666 8888 (Any 1 Suit)
    for suit in suits:
        MAHJONG_HANDS.append((
            f"FFF 22 44 666 8888 - {suit}",
            ["Flower"]*3 + [f"2 {suit}"]*2 + [f"4 {suit}"]*2 + [f"6 {suit}"]*3 + [f"8 {suit}"]*4,
            25
        ))

    # 222 4444 666 88 88 (Any 3 Suits, 2/4/6 in suit1, first pair 8s in suit2, second pair 8s in suit3)
    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"222 4444 666 88 88 - {s1}/{s2}/{s3}",
            [f"2 {s1}"]*3 + [f"4 {s1}"]*4 + [f"6 {s1}"]*3 + [f"8 {s2}"]*2 + [f"8 {s3}"]*2,
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
        for even in [2, 4, 6, 8]:
            MAHJONG_HANDS.append((
                f"22 44 66 88 {even}{even}{even} {even}{even}{even} - {s1}/{s2}/{s3}",
                [f"2 {s1}"]*2 + [f"4 {s1}"]*2 + [f"6 {s1}"]*2 + [f"8 {s1}"]*2 + [f"{even} {s2}"]*3 + [f"{even} {s3}"]*3,
                30
            ))

    # Kong Any Dragon
    MAHJONG_HANDS.extend([
        ("NN EE WWW SSS DDDD (Red)", ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*3 + ["South Wind"]*3 + ["Red Dragon"]*4, 30),
        ("NN EE WWW SSS DDDD (Green)", ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*3 + ["South Wind"]*3 + ["Green Dragon"]*4, 30),
        ("NN EE WWW SSS DDDD (White)", ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*3 + ["South Wind"]*3 + ["White Dragon"]*4, 30),
    ])

    # 369 SECTION
    # 333 6666 666 9999 (option 1: 2 suits, option 2: 3 suits)
    # Option 1: 333 6666 in s1, 666 9999 in s2
    for s1, s2 in permutations(suits, 2):
        MAHJONG_HANDS.append((
            f"333 6666 666 9999 - {s1}/{s2}",
            [f"3 {s1}"]*3 + [f"6 {s1}"]*4 + [f"6 {s2}"]*3 + [f"9 {s2}"]*4,
            25
        ))

    # Option 2: 333 6666 in s1, 666 in s2, 9999 in s3
    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"333 6666 666 9999 - {s1}/{s2}/${s3}",
            [f"3 {s1}"]*3 + [f"6 {s1}"]*4 + [f"6 {s2}"]*3 + [f"9 {s3}"]*4,
            25
        ))

    # FF 3333+6666=9999 (all in 1 suit OR 3s in s1, 6s in s2, 9s in s3)
    # Option 1: All in 1 suit
    for suit in suits:
        MAHJONG_HANDS.append((
            f"FF 3333+6666=9999 - {suit}",
            ["Flower"]*2 + [f"3 {suit}"]*4 + [f"6 {suit}"]*4 + [f"9 {suit}"]*4,
            25
        ))

    # Option 2: 3s in s1, 6s in s2, 9s in s3
    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"FF 3333+6666=9999 - {s1}/{s2}/{s3}",
            ["Flower"]*2 + [f"3 {s1}"]*4 + [f"6 {s2}"]*4 + [f"9 {s3}"]*4,
            25
        ))

    # 3333 DDD 3333 DDD (matching dragons with kongs)
    for s1, s2 in permutations(suits, 2):
        # Determine dragons for each suit
        if s1 == "Character":
            dragon1 = "Red Dragon"
        elif s1 == "Dot":
            dragon1 = "White Dragon"
        else:  # Bamboo
            dragon1 = "Green Dragon"
        
        if s2 == "Character":
            dragon2 = "Red Dragon"
        elif s2 == "Dot":
            dragon2 = "White Dragon"
        else:  # Bamboo
            dragon2 = "Green Dragon"
        
        MAHJONG_HANDS.append((
            f"3333 DDD 3333 DDD - {s1}/{s2}",
            [f"3 {s1}"]*4 + [dragon1]*3 + [f"3 {s2}"]*4 + [dragon2]*3,
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


    # 2025 222 555 DDDD (2025 in suit1 with soap as 0, 222 and 555 in suit2, 4 of any dragon)
        for s1, s2 in permutations(suits, 2):
            for dragon_pung in dragons:
                MAHJONG_HANDS.append((
                    f"2025 222 555 DDDD - {s1}/{s2}",
                    [f"2 {s1}", "White Dragon", f"2 {s1}", f"5 {s1}"] + 
                    [f"2 {s2}"]*3 + [f"5 {s2}"]*3 + [dragon_pung]*4,
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

    # 11111 WWWW 22222 (any wind)
    for suit in suits:
        for start in range(1, 9):
            for wind in ["North Wind", "East Wind", "West Wind", "South Wind"]:
                MAHJONG_HANDS.append((
                    f"{start}{start}{start}{start}{start} WWWW {start+1}{start+1}{start+1}{start+1}{start+1} - {suit}",
                    [f"{start} {suit}"]*5 + [wind]*4 + [f"{start+1} {suit}"]*5,
                    45
                ))

    # FF 11111 11 11111 (three different suits required)
    for num in range(1, 10):
        for s1, s2, s3 in combinations(suits, 3):
            MAHJONG_HANDS.append((
                f"FF {num}{num}{num}{num}{num} {num}{num} {num}{num}{num}{num}{num} - {s1}/{s2}/{s3}",
                ["Flower"]*2 + [f"{num} {s1}"]*5 + [f"{num} {s2}"]*2 + [f"{num} {s3}"]*5,
                45
            ))

    # CONSECUTIVE RUN SECTION
    for suit in suits:
        MAHJONG_HANDS.append((
            f"11 222 3333 444 55 - {suit}",
            [f"1 {suit}"]*2 + [f"2 {suit}"]*3 + [f"3 {suit}"]*4 + [f"4 {suit}"]*3 + [f"5 {suit}"]*2,
            25
        ))
        MAHJONG_HANDS.append((
            f"55 666 7777 888 99 - {suit}",
            [f"5 {suit}"]*2 + [f"6 {suit}"]*3 + [f"7 {suit}"]*4 + [f"8 {suit}"]*3 + [f"9 {suit}"]*2,
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

    # FFFF 1111 22 3333 -or- FFFF 111 22 3333 (any 1 or 3 suits, any 3 consec)
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
                f"FFFF {start}{start}{start}{start} {start+1}{start+1} {start+2}{start+2}{start+2}{start+2} - {s1}/{s2}/{s3}",
                ["Flower"]*4 + [f"{start} {s1}"]*4 + [f"{start+1} {s2}"]*2 + [f"{start+2} {s3}"]*4,
                25
            ))

    # FFF 123 4444 5555 (any 3 suits, any 5 consecutive numbers)
    for s1, s2, s3 in combinations(suits, 3):
        for start in range(1, 6):  # 1-5 for 5 consecutive (1-2-3-4-5 through 5-6-7-8-9)
            MAHJONG_HANDS.append((
                f"FFF {start}{start+1}{start+2} {start+3}{start+3}{start+3}{start+3} {start+4}{start+4}{start+4}{start+4} - {s1}/{s2}/{s3}",
                ["Flower"]*3 + [f"{start} {s1}", f"{start+1} {s1}", f"{start+2} {s1}"] + 
                [f"{start+3} {s2}"]*4 + [f"{start+4} {s3}"]*4,
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

    # FF 11 222 3333 DDD (any 1 suit, any 3 consec, matching dragon)
    for suit in suits:
        for start in range(1, 8):
            # Determine which dragon matches the suit
            if suit == "Character":
                dragon = "Red Dragon"
            elif suit == "Dot":
                dragon = "White Dragon"
            else:  # Bamboo
                dragon = "Green Dragon"
            
            MAHJONG_HANDS.append((
                f"FF {start}{start} {start+1}{start+1}{start+1} {start+2}{start+2}{start+2}{start+2} DDD - {suit}",
                ["Flower"]*2 + [f"{start} {suit}"]*2 + [f"{start+1} {suit}"]*3 + [f"{start+2} {suit}"]*4 + [dragon]*3,
                25
            ))

    # 111 222 3333 DD DD (any 1 suit for consec numbers, with 2 opp dragons)
    for suit in suits:
        for start in range(1, 8):
            # Get dragons that don't match the suit used
            available_dragons = []
            
            if suit != "Character":
                available_dragons.append("Red Dragon")
            if suit != "Bamboo":
                available_dragons.append("Green Dragon")
            if suit != "Dot":
                available_dragons.append("White Dragon")
            
            # Generate all combinations of 2 pairs from available dragons
            for d1, d2 in combinations(available_dragons, 2):
                MAHJONG_HANDS.append((
                    f"{start}{start}{start} {start+1}{start+1}{start+1} {start+2}{start+2}{start+2}{start+2} DD DD - {suit}",
                    [f"{start} {suit}"]*3 + [f"{start+1} {suit}"]*3 + [f"{start+2} {suit}"]*4 + [d1]*2 + [d2]*2,
                    30
                ))
    # 112345 1111 1111 (any 5 consec in one suit, two kongs of any number from that run in two other suits)
    for s1, s2, s3 in combinations(suits, 3):
        for start in range(1, 6):
            # Try all numbers in the consecutive run for the kongs
            for kong_num in range(start, start + 5):
                MAHJONG_HANDS.append((
                    f"{start}{start}{start+1}{start+2}{start+3}{start+4} {kong_num}{kong_num}{kong_num}{kong_num} {kong_num}{kong_num}{kong_num}{kong_num} - {s1}/{s2}/{s3}",
                    [f"{start} {s1}"]*2 + [f"{start+1} {s1}"] + [f"{start+2} {s1}"] + 
                    [f"{start+3} {s1}"] + [f"{start+4} {s1}"] + [f"{kong_num} {s2}"]*4 + [f"{kong_num} {s3}"]*4,
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
    # 11 333 5555 777 99 (any 1 suit OR 3 suits: 1&3 in s1, 5 in s2, 7&9 in s3)
    for suit in suits:
        MAHJONG_HANDS.append((
            f"11 333 5555 777 99 - {suit}",
            [f"1 {suit}"]*2 + [f"3 {suit}"]*3 + [f"5 {suit}"]*4 + [f"7 {suit}"]*3 + [f"9 {suit}"]*2,
            25
        ))

    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"11 333 5555 777 99 - {s1}/{s2}/{s3}",
            [f"1 {s1}"]*2 + [f"3 {s1}"]*3 + [f"5 {s2}"]*4 + [f"7 {s3}"]*3 + [f"9 {s3}"]*2,
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

    # 1111 333 5555 DDD -or- 5555 777 9999 DDD (any 1 suit with matching dragon)
    for suit in suits:
        # Determine which dragon matches the suit
        if suit == "Character":
            dragon = "Red Dragon"
        elif suit == "Dot":
            dragon = "White Dragon"
        else:  # Bamboo
            dragon = "Green Dragon"
        
        MAHJONG_HANDS.append((
            f"1111 333 5555 DDD - {suit}",
            [f"1 {suit}"]*4 + [f"3 {suit}"]*3 + [f"5 {suit}"]*4 + [dragon]*3,
            25
        ))
        MAHJONG_HANDS.append((
            f"5555 777 9999 DDD - {suit}",
            [f"5 {suit}"]*4 + [f"7 {suit}"]*3 + [f"9 {suit}"]*4 + [dragon]*3,
            25
        ))

    # FFFF 1111 + 9999 = 10 (1111 and 9999 in s1, the final 1+0 can be any other suit)
    for s1 in suits:
        for s2 in suits:
            if s1 != s2:
                MAHJONG_HANDS.append((
                    f"FFFF 1111 + 9999 = 10 - {s1}/{s2}",
                    ["Flower"]*4 + [f"1 {s1}"]*4 + [f"9 {s1}"]*4 + [f"1 {s2}"] + ["White Dragon"],
                    25
                ))

    # FFF 135 7777 9999 (any 1 suit OR 3 suits: 135 in s1, 7777 in s2, 9999 in s3)
    for suit in suits:
        MAHJONG_HANDS.append((
            f"FFF 135 7777 9999 - {suit}",
            ["Flower"]*3 + [f"1 {suit}"] + [f"3 {suit}"] + [f"5 {suit}"] + [f"7 {suit}"]*4 + [f"9 {suit}"]*4,
            25
        ))

    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"FFF 135 7777 9999 - {s1}/{s2}/{s3}",
            ["Flower"]*3 + [f"1 {s1}"] + [f"3 {s1}"] + [f"5 {s1}"] + [f"7 {s2}"]*4 + [f"9 {s3}"]*4,
            25
        ))

   # 111 333 5555 DD DD -or- 555 777 9999 DD DD (numbers in one suit, dragons opposite)
    for s1 in suits:
        # Get opposite dragons
        available_dragons = []
        if s1 != "Character":
            available_dragons.append("Red Dragon")
        if s1 != "Bamboo":
            available_dragons.append("Green Dragon")
        if s1 != "Dot":
            available_dragons.append("White Dragon")
        
        dragon1, dragon2 = available_dragons
        
        MAHJONG_HANDS.append((
            f"111 333 5555 DD DD - {s1}",
            [f"1 {s1}"]*3 + [f"3 {s1}"]*3 + [f"5 {s1}"]*4 + [dragon1]*2 + [dragon2]*2,
            30
        ))
        MAHJONG_HANDS.append((
            f"555 777 9999 DD DD - {s1}",
            [f"5 {s1}"]*3 + [f"7 {s1}"]*3 + [f"9 {s1}"]*4 + [dragon1]*2 + [dragon2]*2,
            30
        )) 
    
    # 11 333 NEWS 333 55 -or- 55 777 NEWS 777 99 (any 2 suits)
    for s1, s2 in permutations(suits, 2):
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
            [f"1 {s1}"]*4 + [f"3 {s1}"]*2 + [f"5 {s2}"]*2 + [f"7 {s2}"]*2 + [f"9 {s1}"]*4,
            30
        ))

    # FF 11 33 111 333 55 -or- FF 55 77 555 777 99 (any 3 suits)
    for s1, s2, s3 in combinations(suits, 3):
        MAHJONG_HANDS.append((
            f"FF 11 33 111 333 55 - {s1}/{s2}/{s3}",
            ["Flower"]*2 + [f"1 {s1}"]*2 + [f"3 {s1}"]*2 + [f"1 {s2}"]*3 + [f"3 {s2}"]*3 + [f"5 {s3}"]*2,
            30
        ))
        MAHJONG_HANDS.append((
            f"FF 55 77 555 777 99 - {s1}/{s2}/{s3}",
            ["Flower"]*2 + [f"5 {s1}"]*2 + [f"7 {s1}"]*2 + [f"5 {s2}"]*3 + [f"7 {s2}"]*3 + [f"9 {s3}"]*2,
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
