# 📊 PERBANDINGAN 3 VERSI MAIN.PY

## Versi 1: BASIC GAME 
**File:** `main_v1.py`
**Tagline:** "Player vs Maze"

### Fitur Yang Ada:
```
✅ Window setup (800x800)
✅ Maze rendering dengan walls
✅ Player object
✅ Arrow key movement (Up/Down/Left/Right)
✅ Collision detection (wall check)
✅ Score counter (increment saat move)
✅ Simple info display (Level + Score)
```

### Fitur Yang TIDAK Ada:
```
❌ Food system
❌ Stamina/HP system
❌ Zombies
❌ Exit door
❌ Pause feature
❌ Menu
❌ Multiple levels
❌ Game over screen
```

### Ukuran File: ~120 lines
### Complexity: ⭐ (Beginner)

---

## Versi 2: FOOD & STAMINA SYSTEM
**File:** `main_v2.py`
**Tagline:** "Player vs Maze + Resource Management"

### Fitur Baru Ditambahkan:
```
✨ Food collection system
✨ Stamina/HP management
✨ HP bar visual display
✨ Stamina berkurang saat move
✨ Food restore stamina (10-20 points)
✨ Game over saat stamina 0
✨ Restart button (Press 1)
✨ Food counter display
```

### Fitur Dari V1 yang Masih Ada:
```
✅ Basic movement & maze
✅ Score system
✅ Info display
```

### Ukuran File: ~200 lines
### Complexity: ⭐⭐ (Intermediate)
### Progress: ~40% dari final game

---

## Versi 3: COMPLETE GAME (FINAL)
**File:** `main_v3.py` (sama dengan main.py sekarang)
**Tagline:** "Full Zombie Maze Runner Game"

### Fitur Baru Ditambahkan:
```
🎮 Zombie AI dengan pathfinding
🎮 Main menu system (4 options)
🎮 Level selection (Easy/Medium/Hard)
🎮 Endless mode dengan wave scaling
🎮 Exit door (win condition)
🎮 Pause/Resume (Press P)
🎮 Back to menu (Press M)
🎮 Difficulty scaling (zombie speed)
🎮 Win condition screen
🎮 Visual effects (overlay, animations)
```

### Fitur Dari V1-V2 yang Masih Ada:
```
✅ Maze movement system
✅ Stamina management
✅ Food collection
✅ Score system
```

### Ukuran File: ~600 lines
### Complexity: ⭐⭐⭐ (Advanced)
### Progress: 100% - FINAL VERSION

---

## 🔄 EVOLUTION CHART

```
┌─────────────────────────────────────────────┐
│         VERSION 1 (Basic)                   │
│  - Player Movement                          │
│  - Maze Navigation                          │
│  - Score Tracking                           │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│      VERSION 2 (Intermediate)               │
│  + Food System                              │
│  + Stamina/HP Management                    │
│  + Resource Strategy                        │
│  + Restart Functionality                    │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│      VERSION 3 (Complete)                   │
│  + Enemy AI (Zombies)                       │
│  + Menu System                              │
│  + Multiple Levels                          │
│  + Endless Mode                             │
│  + Win/Loss Conditions                      │
│  + Pause Feature                            │
│  + Visual Polish                            │
└─────────────────────────────────────────────┘
```

---

## 📈 FEATURE PROGRESSION TABLE

| Feature | V1 | V2 | V3 |
|---------|----|----|-----|
| Player Movement | ✅ | ✅ | ✅ |
| Maze/Walls | ✅ | ✅ | ✅ |
| Score Display | ✅ | ✅ | ✅ |
| Food Collection | ❌ | ✅ | ✅ |
| Stamina System | ❌ | ✅ | ✅ |
| Zombies | ❌ | ❌ | ✅ |
| Menu System | ❌ | ❌ | ✅ |
| Level Selection | ❌ | ❌ | ✅ |
| Exit Door/Win | ❌ | ❌ | ✅ |
| Endless Mode | ❌ | ❌ | ✅ |
| Pause Feature | ❌ | ❌ | ✅ |
| Game Over Screen | ❌ | ✅ | ✅ |

---

## 🎯 GAME DESIGN PROGRESSION

### V1: Exploration Phase
- Player belajar navigasi maze
- Fokus: "Bisakah saya tembus maze ini?"
- Difficulty: Low (no enemies, no time limit)

### V2: Resource Management Phase  
- Player belajar balance movement dengan stamina
- Fokus: "Bagaimana saya keluar sambil cukup stamina?"
- Difficulty: Medium (stamina pressure, resource hunting)

### V3: Action Strategy Phase
- Player belajar avoid enemies sambil collect resources
- Fokus: "Bagaimana saya survive vs zombies dan capai exit?"
- Difficulty: High (enemies, time pressure, multiple strategies)

---

## 💾 SWAP INSTRUCTIONS

Untuk swap antara versi (saat melakukan 3 push):

### Swap ke V1
```powershell
Copy-Item main_v1.py main.py -Force
python main.py
```

### Swap ke V2
```powershell
Copy-Item main_v2.py main.py -Force
python main.py
```

### Swap ke V3 (Final)
```powershell
Copy-Item main_v3.py main.py -Force
python main.py
```

---

## 📚 KEY CONCEPTS PER VERSI

### V1 Teaches:
- Coordinate system (screen_x, screen_y)
- Collision detection
- Game loop basics

### V2 Teaches:
- State management (stamina, HP)
- Resource management
- UI rendering (bar graphs)
- Event handling (restart)

### V3 Teaches:
- AI pathfinding (Dijkstra)
- Complex state management
- Menu systems
- Game flow (menu → play → game over)

---

Last Updated: May 8, 2026
For detailed push instructions, lihat: `TUTORIAL_PUSH_3_KALI.md`
