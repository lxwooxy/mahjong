import tkinter as tk
from tkinter import ttk
from collections import Counter
from itertools import product

# Define all possible Mahjong hands based on the official card
MAHJONG_HANDS = []

def generate_suit_variants(pattern, suits, points, name_template, same_suit=True):
    """Generate hand variants for different suit combinations"""
    hands = []
    if same_suit:
        # All tiles must be same suit
        for suit in suits:
            tiles = []
            for item in pattern:
                if isinstance(item, int):
                    tiles.append(f"{item} {suit}")
                else:  # It's a special tile (Wind/Dragon/Flower)
                    tiles.append(item)
            hands.append((name_template.format(suit=suit), tiles, points))
    else:
        # Tiles must be different suits (for multi-color patterns)
        # pattern is list of (numbers, suit_type) tuples
        for suit_combo in product(suits, repeat=len([p for p in pattern if isinstance(p[0], list)])):
            tiles = []
            suit_idx = 0
            for item in pattern:
                if isinstance(item[0], list):
                    # This is a number group that needs a suit
                    for num in item[0]:
                        tiles.append(f"{num} {suit_combo[suit_idx]}")
                    suit_idx += 1
                else:
                    # Special tile
                    tiles.append(item)
            # Only add if suits are actually different where required
            if len(set(suit_combo)) == len(suit_combo):
                hands.append((name_template.format(suits=suit_combo), tiles, points))
    return hands

# WINDS-DRAGONS SECTION
MAHJONG_HANDS.extend([
    ("All Winds & Dragons", ["North Wind"]*4 + ["East Wind"]*4 + ["West Wind"]*4 + ["South Wind"]*4, 25),
    ("All Winds & Dragons (3 Consec in 1 Suit + 3 Dragons)", 
     ["1 Bamboo", "2 Bamboo", "3 Bamboo"] + ["Red Dragon"]*3 + ["Green Dragon"]*3 + ["White Dragon"]*3, 25),
    ("All Winds, Dragons & News", ["East Wind"]*2 + ["West Wind"]*2 + ["South Wind"]*2, 25),
    ("All Winds, Dragons, News & 123", ["Red Dragon"]*3 + ["Green Dragon"]*3 + ["White Dragon"]*3, 25),
    ("All Winds, Dragons & News (Any 2 Suits)", ["Red Dragon"]*3, 25),
    ("Like Odd Numbers in 3 Suits", ["North Wind"]*4 + ["1 Bamboo", "1 Character", "1 Dot"]*4, 25),
    ("Like Even Numbers in 3 Suits", ["East Wind"]*4 + ["2 Bamboo", "2 Character", "2 Dot"]*4, 25),
    ("2025 Any 1 Suit", ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*2 + ["South Wind"]*2 + 
     ["2 Bamboo", "0 Bamboo", "2 Bamboo", "5 Bamboo"], 30),
    ("Kong Any Dragon", ["North Wind"]*2 + ["East Wind"]*2 + ["West Wind"]*2 + ["South Wind"]*2 + 
     ["Red Dragon"]*4, 30),
])

# 369 SECTION
suits = ["Bamboo", "Character", "Dot"]
MAHJONG_HANDS.extend([
    ("369 - Any 2 or 3 Suits", ["3 Bamboo"]*3 + ["6 Character"]*4 + ["6 Character"]*2 + 
     ["9 Dot"]*4 + ["9 Dot"]*3, 25),
    ("FF + Kongs", ["3 Bamboo"]*4 + ["6 Bamboo"]*4 + ["9 Bamboo"]*3, 25),
    ("369 Any 2 Suits w/ Dragons", ["3 Bamboo"]*4 + ["Red Dragon"]*3 + ["3 Character"]*4 + 
     ["White Dragon"]*3, 25),
    ("369 Any 2 Suits", ["3 Bamboo"]*3 + ["3 Character"]*3 + ["3 Dot"]*3, 25),
    ("369 + 9999 Any 2 Suits", ["3 Bamboo"]*3 + ["6 Bamboo"]*3 + ["9 Bamboo"]*4, 25),
    ("Kong 3, 6 or 9", ["3 Bamboo"]*3 + ["6 Character"]*2 + ["9 Dot"]*3 + 
     ["3 Character"]*4 + ["3 Dot"]*3, 30),
    ("369 w/ Dragons Any 3 Suits", ["3 Bamboo"]*3 + ["Red Dragon"] + ["6 Character"]*3 + 
     ["Green Dragon"] + ["9 Dot"]*3 + ["White Dragon"], 30),
])

# SINGLES AND PAIRS SECTION
MAHJONG_HANDS.extend([
    ("Singles Any 1 Suit, Any 4 Consec Nos", 
     ["North Wind"]*2 + ["East Wind"] + ["West Wind"] + ["South Wind"]*2 + 
     ["1 Bamboo", "1 Bamboo", "2 Bamboo", "2 Bamboo", "3 Bamboo", "3 Bamboo", "4 Bamboo", "4 Bamboo"], 50),
    ("Any 2 Suits w/ Matching Dragons", ["2 Bamboo"]*2 + ["4 Bamboo"]*2 + ["6 Bamboo"]*2 + 
     ["8 Bamboo"]*2 + ["Red Dragon"]*2 + ["2 Character"]*2 + ["4 Character"]*2 + 
     ["6 Character"]*2 + ["8 Character"]*2 + ["White Dragon"]*2, 50),
    ("Pairs 3, 6, 9 in Third Suit", ["3 Bamboo"]*2 + ["3 Character"]*2 + ["6 Bamboo"]*2 + 
     ["6 Character"]*2 + ["9 Bamboo"]*2 + ["9 Character"]*2 + ["3 Dot"]*2, 50),
    ("Any 3 Suits, Any 2 Consec Nos", ["1 Bamboo"]*2 + ["1 Character"]*2 + ["2 Bamboo"]*2 + 
     ["2 Character"]*2 + ["1 Dot"]*2 + ["2 Dot"]*2, 50),
    ("Pairs Any Like Odd Nos in Opp Suits", ["1 Bamboo"]*2 + ["3 Character"]*2 + 
     ["5 Bamboo"]*2 + ["5 Dot"]*2 + ["7 Character"]*2 + ["9 Bamboo"]*2 + ["1 Dot"]*2, 50),
    ("2025 Any 3 Suits", ["2 Bamboo"]*2 + ["0 Bamboo"]*2 + ["2 Character"]*2 + 
     ["5 Character"]*2 + ["2 Dot"]*2 + ["0 Dot"]*2 + ["2 Dot"]*2 + ["5 Dot"]*2, 75),
])

# QUINTS SECTION
MAHJONG_HANDS.extend([
    ("Quint - Any 3 Suits, Any 3 Consec Nos", ["1 Bamboo"]*2 + ["2 Character"]*4 + 
     ["3 Dot"]*5 + ["3 Character"]*3, 40),
    ("Quint - Any 1 Suit, Any 2 Consec Nos, Any Wind", 
     ["1 Bamboo"]*5 + ["North Wind"]*4 + ["2 Bamboo"]*5 + ["2 Character"]*2, 45),
    ("Quint - Any 3 Suits, Any Like Nos", ["1 Bamboo"]*5 + ["1 Character"]*2 + 
     ["1 Dot"]*5 + ["1 Character"]*2, 45),
])

# CONSECUTIVE RUN SECTION
for suit in suits:
    MAHJONG_HANDS.extend([
        (f"Run 1-9 {suit}", [f"{i} {suit}" for i in [1,1,2,2,2,3,3,3,3,4,4,4,5,5]], 25),
        (f"Run Any 4 Consec {suit}", [f"{i} {suit}" for i in [1,1,1,2,2,2,2,3,3,3,4,4,4,4]], 25),
        (f"Run Any 3 Consec {suit}", [f"{i} {suit}" for i in [1,1,1,1,2,2,3,3,3,3]], 25),
    ])

MAHJONG_HANDS.extend([
    ("Run w/ Pair in Run", [f"{i} Bamboo" for i in [1,1,1,1,2,2,3,3,3,3]], 25),
    ("Run Any 5 Consec (Any 3 Suits)", ["1 Bamboo"]*3 + ["2 Character"]*3 + 
     ["3 Dot"]*3 + ["4 Bamboo"]*3 + ["5 Character"]*5, 25),
    ("Run Any 3 Consec (Any 1 Suit)", ["1 Bamboo"]*3 + ["1 Bamboo", "2 Bamboo", "2 Bamboo"] + 
     ["3 Bamboo"]*3 + ["Red Dragon"]*3, 25),
    ("Run w/ Opp Dragons", ["1 Bamboo"]*3 + ["2 Bamboo"]*3 + ["3 Bamboo"]*3 + 
     ["Red Dragon"]*2 + ["White Dragon"]*2, 30),
    ("Run w/ Matching Kongs", ["1 Bamboo"]*5 + ["2 Bamboo"]*3 + ["3 Bamboo"]*5 + 
     ["1 Character"]*4 + ["1 Dot"]*4, 30),
    ("Run + Same 3 Consec", ["1 Bamboo"]*2 + ["2 Bamboo"]*2 + ["3 Bamboo"]*3 + 
     ["1 Character"]*2 + ["2 Character"]*2 + ["3 Character"]*3, 30),
])

# 13579 SECTION  
MAHJONG_HANDS.extend([
    ("13579 - Any 1 or 3 Suits", ["1 Bamboo"]*3 + ["3 Character"]*5 + ["5 Dot"]*5 + 
     ["7 Bamboo"]*2 + ["9 Character"]*2, 25),
    ("13579 - Any 2 Suits", ["1 Bamboo"]*3 + ["3 Bamboo"]*4 + ["3 Character"]*3 + 
     ["5 Character"]*5 + ["5 Bamboo"]*5, 25),
    ("13579 - Any 1 Suit", ["1 Bamboo"]*3 + ["3 Bamboo"]*3 + ["5 Bamboo"]*5 + 
     ["Red Dragon"]*3 + ["5 Dot"]*5 + ["7 Dot"]*3 + ["9 Dot"]*4 + ["White Dragon"]*3, 25),
    ("13579 FF + 9999", ["1 Bamboo"]*2 + ["1 Bamboo"]*3 + ["9 Bamboo"]*4, 25),
    ("13579 FF", ["1 Bamboo"]*3 + ["3 Bamboo"]*5 + ["7 Bamboo"]*4 + ["9 Bamboo"]*4, 25),
    ("13579 w/ Opp Dragons", ["1 Bamboo"]*3 + ["3 Bamboo"]*3 + ["5 Bamboo"]*5 + 
     ["Red Dragon"]*2 + ["White Dragon"]*2 + ["5 Character"]*5 + ["7 Character"]*3 + 
     ["9 Character"]*4 + ["Red Dragon"]*2 + ["White Dragon"]*2, 30),
    ("13579 NEWS", ["1 Bamboo"]*3 + ["3 Bamboo"]*3 + ["5 Bamboo"]*5 + 
     ["5 Character"]*2 + ["7 Character"]*2 + ["7 Dot"]*2 + ["North Wind"] + 
     ["East Wind"] + ["West Wind"] + ["South Wind"] + ["7 Bamboo"]*3 + ["7 Character"]*2 + 
     ["9 Character"]*2, 30),
    ("13579 - Any 2 Suits", ["1 Bamboo"]*3 + ["3 Bamboo"]*3 + ["5 Bamboo"]*5 + 
     ["7 Bamboo"]*2 + ["9 Bamboo"]*4, 30),
    ("13579 FF", ["1 Bamboo"]*2 + ["3 Bamboo"]*3 + ["1 Character"]*3 + ["3 Character"]*3 + 
     ["5 Bamboo"]*5 + ["5 Character"]*2 + ["5 Dot"]*5 + ["7 Dot"]*5 + ["7 Character"]*3 + 
     ["9 Character"]*2, 30),
])

class MahjongHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("Mahjong Hand Helper - Official Rules")
        self.root.geometry("1000x750")
        
        # Available tiles
        self.tile_types = []
        for i in range(1, 10):
            self.tile_types.extend([f"{i} Bamboo", f"{i} Character", f"{i} Dot"])
        self.tile_types.extend(["East Wind", "South Wind", "West Wind", "North Wind",
                               "Red Dragon", "Green Dragon", "White Dragon"])
        
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
        
        # Number buttons (1-9)
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
        
        suits = [("Bamboo", "Bamboo"), ("Character", "Character"), ("Dot", "Dot")]
        for display, value in suits:
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
        dragons_btn_frame.pack(pady=(2,5))
        
        dragons = [("Red", "Red Dragon"), ("Green", "Green Dragon"), 
                  ("White", "White Dragon")]
        for display, value in dragons:
            btn = tk.Button(dragons_btn_frame, text=display, width=8,
                           command=lambda v=value: self.set_text_field(v),
                           font=("Arial", 11, "bold"))
            btn.pack(side=tk.LEFT, padx=2)
        
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
        
        # Listbox with scrollbar
        scroll = tk.Scrollbar(selected_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tiles_listbox = tk.Listbox(selected_frame, yscrollcommand=scroll.set,
                                        font=("Arial", 12), height=15)
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
        """Add text to the entry field (for building tile names)"""
        current = self.tile_entry.get()
        if current and not current.endswith(" "):
            self.tile_entry.insert(tk.END, " " + text)
        else:
            self.tile_entry.insert(tk.END, text)
    
    def set_text_field(self, text):
        """Set the entire text field (for complete tile names like winds/dragons)"""
        self.tile_entry.delete(0, tk.END)
        self.tile_entry.insert(0, text)
    
    def clear_text_field(self):
        """Clear the text entry field"""
        self.tile_entry.delete(0, tk.END)
    
    def add_tile_from_entry(self):
        """Add tile from the text entry field"""
        tile = self.tile_entry.get().strip()
        if tile:
            # Validate the tile
            if tile in self.tile_types:
                self.selected_tiles.append(tile)
                self.tiles_listbox.insert(tk.END, tile)
                self.tile_entry.delete(0, tk.END)
            else:
                # Try to find a close match
                tile_lower = tile.lower()
                for valid_tile in self.tile_types:
                    if valid_tile.lower() == tile_lower:
                        self.selected_tiles.append(valid_tile)
                        self.tiles_listbox.insert(tk.END, valid_tile)
                        self.tile_entry.delete(0, tk.END)
                        return
                # If no match, show error in entry
                self.tile_entry.delete(0, tk.END)
                self.tile_entry.insert(0, "Invalid tile! Try again...")
                self.root.after(1500, self.clear_text_field)
    
    def remove_tile(self):
        selection = self.tiles_listbox.curselection()
        if selection:
            idx = selection[0]
            self.tiles_listbox.delete(idx)
            self.selected_tiles.pop(idx)
    
    def clear_tiles(self):
        self.selected_tiles.clear()
        self.tiles_listbox.delete(0, tk.END)
    
    def analyze_hand(self):
        if not self.selected_tiles:
            self.display_results("Please select some tiles first!")
            return
        
        # Count tiles in hand
        hand_counter = Counter(self.selected_tiles)
        
        # Calculate match score for each hand
        hand_scores = []
        for hand_name, required_tiles, points in MAHJONG_HANDS:
            required_counter = Counter(required_tiles)
            
            # Count how many required tiles we have
            matches = 0
            for tile, count in required_counter.items():
                matches += min(hand_counter.get(tile, 0), count)
            
            # Calculate percentage and score
            total_required = len(required_tiles)
            match_percentage = (matches / total_required) * 100
            
            # Only include if we have at least some tiles
            if matches > 0:
                hand_scores.append({
                    'name': hand_name,
                    'matches': matches,
                    'total_required': total_required,
                    'percentage': match_percentage,
                    'points': points,
                    'missing': total_required - matches,
                    'required_tiles': required_counter
                })
        
        # Sort by match count, then by points
        hand_scores.sort(key=lambda x: (x['matches'], x['points']), reverse=True)
        
        # Display top 3
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
            result += f"Missing: {hand['missing']} tiles\n\n"
            
            result += "Required tiles:\n"
            for tile, count in sorted(hand['required_tiles'].items()):
                result += f"  • {tile}: {count}x\n"
            
            result += "\n" + "-" * 60 + "\n\n"
        
        return result
    
    def display_results(self, text):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, text)
        self.results_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MahjongHelper(root)
    root.mainloop()