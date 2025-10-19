import tkinter as tk
from tkinter import ttk
from collections import Counter

# Define all possible Mahjong hands with their tiles and point values
MAHJONG_HANDS = {
    # Special Hands (High Value)
    "Big Three Dragons": (["Red Dragon", "Red Dragon", "Red Dragon", 
                          "Green Dragon", "Green Dragon", "Green Dragon",
                          "White Dragon", "White Dragon", "White Dragon"], 50),
    "Little Three Dragons": (["Red Dragon", "Red Dragon", "Green Dragon", "Green Dragon",
                              "White Dragon", "White Dragon"], 40),
    "Big Four Winds": (["East Wind", "East Wind", "East Wind",
                        "South Wind", "South Wind", "South Wind",
                        "West Wind", "West Wind", "West Wind",
                        "North Wind", "North Wind", "North Wind"], 75),
    "Little Four Winds": (["East Wind", "East Wind", "South Wind", "South Wind",
                           "West Wind", "West Wind", "North Wind", "North Wind"], 60),
    "All Honors": (["East Wind", "South Wind", "West Wind", "North Wind",
                    "Red Dragon", "Green Dragon", "White Dragon"], 50),
    "All Terminals": (["1 Bamboo", "1 Bamboo", "1 Bamboo", "9 Bamboo", "9 Bamboo", "9 Bamboo",
                       "1 Character", "1 Character", "1 Character", "9 Character", "9 Character"], 50),
    
    # Dragons
    "Red Dragon Pong": (["Red Dragon", "Red Dragon", "Red Dragon"], 10),
    "Green Dragon Pong": (["Green Dragon", "Green Dragon", "Green Dragon"], 10),
    "White Dragon Pong": (["White Dragon", "White Dragon", "White Dragon"], 10),
    
    # Winds
    "East Wind Pong": (["East Wind", "East Wind", "East Wind"], 10),
    "South Wind Pong": (["South Wind", "South Wind", "South Wind"], 10),
    "West Wind Pong": (["West Wind", "West Wind", "West Wind"], 10),
    "North Wind Pong": (["North Wind", "North Wind", "North Wind"], 10),
    
    # Pure Hands
    "All Bamboo": (["1 Bamboo", "2 Bamboo", "3 Bamboo", "4 Bamboo", "5 Bamboo",
                    "6 Bamboo", "7 Bamboo", "8 Bamboo", "9 Bamboo"], 30),
    "All Characters": (["1 Character", "2 Character", "3 Character", "4 Character", "5 Character",
                        "6 Character", "7 Character", "8 Character", "9 Character"], 30),
    "All Dots": (["1 Dot", "2 Dot", "3 Dot", "4 Dot", "5 Dot",
                  "6 Dot", "7 Dot", "8 Dot", "9 Dot"], 30),
    
    # Straights
    "Pure Straight 1-9 Bamboo": (["1 Bamboo", "2 Bamboo", "3 Bamboo", "4 Bamboo", "5 Bamboo",
                                  "6 Bamboo", "7 Bamboo", "8 Bamboo", "9 Bamboo"], 25),
    "Pure Straight 1-9 Character": (["1 Character", "2 Character", "3 Character", "4 Character", "5 Character",
                                     "6 Character", "7 Character", "8 Character", "9 Character"], 25),
    "Pure Straight 1-9 Dot": (["1 Dot", "2 Dot", "3 Dot", "4 Dot", "5 Dot",
                               "6 Dot", "7 Dot", "8 Dot", "9 Dot"], 25),
    
    # Common Patterns
    "All Simples": (["2 Bamboo", "3 Bamboo", "4 Bamboo", "5 Bamboo", "6 Bamboo",
                     "7 Bamboo", "8 Bamboo", "2 Character", "3 Character"], 10),
    "Mixed Terminals": (["1 Bamboo", "9 Bamboo", "1 Character", "9 Character",
                         "1 Dot", "9 Dot", "East Wind"], 30),
    "Seven Pairs": (["1 Bamboo", "1 Bamboo", "3 Character", "3 Character",
                     "5 Dot", "5 Dot", "7 Bamboo", "7 Bamboo",
                     "East Wind", "East Wind", "Red Dragon", "Red Dragon",
                     "2 Character", "2 Character"], 25),
    
    # Triplets
    "All Triplets": (["2 Bamboo", "2 Bamboo", "2 Bamboo",
                      "5 Character", "5 Character", "5 Character",
                      "7 Dot", "7 Dot", "7 Dot"], 30),
    
    # Lower Value Patterns
    "No Honors": (["1 Bamboo", "2 Bamboo", "3 Bamboo", "4 Character", "5 Character",
                   "6 Dot", "7 Dot", "8 Bamboo", "9 Character"], 5),
    "Pong of 1s": (["1 Bamboo", "1 Bamboo", "1 Bamboo"], 5),
    "Pong of 9s": (["9 Bamboo", "9 Bamboo", "9 Bamboo"], 5),
}

class MahjongHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("Mahjong Hand Helper")
        self.root.geometry("900x700")
        
        # Available tiles
        self.tile_types = [
            "1 Bamboo", "2 Bamboo", "3 Bamboo", "4 Bamboo", "5 Bamboo", 
            "6 Bamboo", "7 Bamboo", "8 Bamboo", "9 Bamboo",
            "1 Character", "2 Character", "3 Character", "4 Character", "5 Character",
            "6 Character", "7 Character", "8 Character", "9 Character",
            "1 Dot", "2 Dot", "3 Dot", "4 Dot", "5 Dot",
            "6 Dot", "7 Dot", "8 Dot", "9 Dot",
            "East Wind", "South Wind", "West Wind", "North Wind",
            "Red Dragon", "Green Dragon", "White Dragon"
        ]
        
        self.selected_tiles = []
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Mahjong Hand Helper", 
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
        number_frame = tk.LabelFrame(selector_frame, text="Numbers", font=("Arial", 9, "bold"))
        number_frame.pack(fill=tk.X, pady=5)
        
        numbers_btn_frame = tk.Frame(number_frame)
        numbers_btn_frame.pack(pady=5)
        
        for num in range(1, 10):
            btn = tk.Button(numbers_btn_frame, text=str(num), width=3,
                           command=lambda n=num: self.add_to_text_field(str(n)),
                           font=("Arial", 10))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Suit buttons
        suit_frame = tk.LabelFrame(selector_frame, text="Suits", font=("Arial", 9, "bold"))
        suit_frame.pack(fill=tk.X, pady=5)
        
        suits_btn_frame = tk.Frame(suit_frame)
        suits_btn_frame.pack(pady=5)
        
        suits = [("Bamboo", "Bamboo"), ("Character", "Character"), ("Dot", "Dot")]
        for display, value in suits:
            btn = tk.Button(suits_btn_frame, text=display, width=10,
                           command=lambda v=value: self.add_to_text_field(v),
                           font=("Arial", 10))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Honor tiles buttons
        honor_frame = tk.LabelFrame(selector_frame, text="Honors", font=("Arial", 9, "bold"))
        honor_frame.pack(fill=tk.X, pady=5)
        
        # Winds
        winds_label = tk.Label(honor_frame, text="Winds:", font=("Arial", 9))
        winds_label.pack(anchor=tk.W, padx=5, pady=(5,0))
        
        winds_btn_frame = tk.Frame(honor_frame)
        winds_btn_frame.pack(pady=2)
        
        winds = [("East", "East Wind"), ("South", "South Wind"), 
                ("West", "West Wind"), ("North", "North Wind")]
        for display, value in winds:
            btn = tk.Button(winds_btn_frame, text=display, width=8,
                           command=lambda v=value: self.set_text_field(v),
                           font=("Arial", 9))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Dragons
        dragons_label = tk.Label(honor_frame, text="Dragons:", font=("Arial", 9))
        dragons_label.pack(anchor=tk.W, padx=5, pady=(5,0))
        
        dragons_btn_frame = tk.Frame(honor_frame)
        dragons_btn_frame.pack(pady=(2,5))
        
        dragons = [("Red", "Red Dragon"), ("Green", "Green Dragon"), 
                  ("White", "White Dragon")]
        for display, value in dragons:
            btn = tk.Button(dragons_btn_frame, text=display, width=8,
                           command=lambda v=value: self.set_text_field(v),
                           font=("Arial", 9))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Text field and add button
        entry_frame = tk.Frame(selector_frame)
        entry_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(entry_frame, text="Tile:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        self.tile_entry = tk.Entry(entry_frame, font=("Arial", 10), width=20)
        self.tile_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        add_btn = tk.Button(entry_frame, text="Add Tile", 
                           command=self.add_tile_from_entry, bg="#4CAF50", fg="black",
                           font=("Arial", 10, "bold"), padx=10, pady=5)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        clear_entry_btn = tk.Button(entry_frame, text="Clear", 
                                    command=self.clear_text_field, bg="#9E9E9E", fg="black",
                                    font=("Arial", 9), padx=5, pady=5)
        clear_entry_btn.pack(side=tk.LEFT, padx=2)
        
        # Selected tiles display
        selected_frame = tk.LabelFrame(left_frame, text="Your Hand", 
                                       font=("Arial", 10, "bold"))
        selected_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Listbox with scrollbar
        scroll = tk.Scrollbar(selected_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tiles_listbox = tk.Listbox(selected_frame, yscrollcommand=scroll.set,
                                        font=("Arial", 10), height=15)
        self.tiles_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.config(command=self.tiles_listbox.yview)
        
        # Buttons
        btn_frame = tk.Frame(left_frame)
        btn_frame.pack(pady=10)
        
        remove_btn = tk.Button(btn_frame, text="Remove Selected", 
                              command=self.remove_tile, bg="#f44336", fg="black",
                              padx=10, pady=5)
        remove_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(btn_frame, text="Clear All", 
                             command=self.clear_tiles, bg="#ff9800", fg="black",
                             padx=10, pady=5)
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
        self.results_text = tk.Text(right_frame, font=("Arial", 10), 
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
    
    def add_tile(self):
        tile = self.tile_var.get()
        self.selected_tiles.append(tile)
        self.tiles_listbox.insert(tk.END, tile)
    
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
        for hand_name, (required_tiles, points) in MAHJONG_HANDS.items():
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