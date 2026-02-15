import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [
    "notebook", "ruler", "bagpack", "eraser", "marker", "lamp", "plug", "wire", "charger", "speaker", 
    "remote", "pillowcase", "bedsheet", "curtain", "mat", "bucket", "soap", "shampoo", "towel", "brush", 
    "comb", "razor", "candle", "match", "stove", "oven", "fridge", "freezer", "toaster", "blender", "mixer", 
    "plate", "bowl", "jug", "kettle", "straw", "napkin", "tissue", "soapbox", "phonecase", "earbuds", 
    "headphones", "charger", "battery", "suitcase", "backpack", "belt", "jeans", "shirt", "jacket", "sweater", 
    "socks", "gloves", "scarf", "umbrella", "boots", "sandals", "sneakers", "cap", "helmet", "lock", "key", 
    "chain", "rope", "tape", "glue", "scissors", "notebook", "diary", "folder", "file", "stapler", "clip", 
    "pin", "calendar", "map", "passport", "ticket", "coin", "cash", "purse", "basket", "tray", "mug", 
    "thermos", "bottlecap", "brush", "sponge", "pan", "pot", "mug", "apple", "ball", "cat", "dog", "egg", 
    "fish", "goat", "hat", "ink", "jam", "kite", "lion", "milk", "nest", "oven", "pen", "queen", "rat", "sun", 
    "tree", "umbrella", "van", "water", "box", "yarn", "zoo", "baby", "book", "cake", "chair", "cup", "door", 
    "ear", "eye", "face", "farm", "fire", "flag", "flower", "food", "game", "girl", "hand", "head", "home", 
    "leaf", "leg", "map", "moon", "name", "nose", "paper", "pig", "rain", "rock", "rope", "room", "shoe", 
    "shop", "star", "stick", "table", "time", "town", "wall", "wind", "wood", "bag", "brush", "car", "cloud", 
    "corn", "cow", "day", "dish", "dust", "field", "hill", "horse", "juice", "light", "ring", "road", "spoon", 
    "stone", "store", "towel", "toy", "truck", "bird", "bread", "cheese", "chalk", "cloth", "dirt", "fan", 
    "grass", "lamp", "list", "lock", "mug", "note", "pie", "plant", "soap", "sock", "stamp", "tin", "wave", 
    "wheat", "wire", "ball", "bench", "berry", "boot", "cap", "card", "coat", "crab", "desk", "doll", "fence", 
    "frog", "gift", "hole", "jar", "log", "nail", "path", "pond", "seed", "shell", "shop", "tag", "tent", "tool", 
    "train", "wheel", "worm", "run", "walk", "jump", "sit", "stand", "sleep", "eat", "drink", "read", "write", 
    "play", "work", "talk", "listen", "watch", "cook", "clean", "open", "close", "start", "stop", "come", "go", 
    "give", "take", "make", "build", "break", "cut", "wash", "drive", "learn", "teach", "help", "smile", "cry", 
    "laugh", "call", "send", "buy", "sell", "find", "lose", "show", "hide", "move", "stay", "wait", "draw", 
    "paint", "swim", "climb", "sing", "dance", "shout", "whisper", "push", "pull", "fix", "catch", "throw", 
    "hold", "bring", "carry", "choose", "win", "lose", "share", "follow", "lead", "love", "hate", "like", 
    "dislike", "think", "know", "see", "hear", "feel", "touch", "smell", "count", "change", "jump", "look", 
    "turn", "answer", "ask", "hope", "plan", "dream", "try", "begin", "finish", "apple", "ball", "cat", "dog", 
    "house", "car", "book", "table", "chair", "phone", "water", "food", "tree", "sky", "sun", "moon", "star", 
    "bed", "bag", "shoe", "door", "window", "road", "street", "cup", "pen", "paper", "school", "home", "flower", 
    "river", "lake", "mountain", "beach", "garden", "grass", "bird", "fish", "baby", "child", "friend", "family", 
    "mother", "father", "brother", "sister", "room", "city", "village", "shop", "market", "bus", "train", "bike", 
    "plane", "computer", "laptop", "keyboard", "mouse", "light", "fan", "clock", "watch", "TV", "radio", 
    "bottle", "box", "clothes", "hat", "ring", "toy", "fruit", "vegetable", "cake", "bread", "milk", "egg", 
    "chocolate", "candy", "cookie", "pizza", "sandwich", "orange", "banana", "mango", "lemon", "plate", 
    "spoon", "fork", "knife", "pillow", "blanket", "mirror", "wallet"
]
end=False
quit=False
lives=6
x=lives+1
a=random.choice(word_list)
b=len(a)
dash=[]
for _ in range(b):
    dash+="_"
print(dash)
while end==False:
    print(stages[lives])
    guess=input("Guess a letter:")
    for pos in range(b):
        letter=a[pos]
        if letter==guess:
            dash[pos]=letter
            print(dash)  
    if "_" not in dash:
        end=True       
        print("You WIN!!!!")
    if guess not in a:
        lives=lives-1
        if lives==0:
            print(stages[0],"\n")
            end=True
            print("You LOSE!!!!")
                
    
    
            
            
                        

               
                
         
    

