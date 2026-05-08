# 📋 TUTORIAL: PUSH 3 KALI DENGAN PROGRESS BERTAHAP

## 📊 Struktur 3 Versi Game

| Versi | Fitur | File |
|-------|-------|------|
| **V1** | Basic Game: Player + Walls + Movement | `main_v1.py` |
| **V2** | Food System + Stamina Management | `main_v2.py` |
| **V3** | Complete Game: Zombies, Menu, Endless Mode, Exit | `main_v3.py` |

---

## 🚀 LANGKAH-LANGKAH PUSH 3 KALI

### **PUSH #1: Versi 1 (Basic Game)**

Fitur yang ditambahkan:
- ✅ Setup game window
- ✅ Player bisa bergerak dengan arrow keys
- ✅ Maze dengan walls
- ✅ Score display sederhana

**Langkah-langkah:**

1. **Ganti main.py dengan main_v1.py**
   ```powershell
   Copy-Item -Path main_v1.py -Destination main.py -Force
   ```

2. **Test game berjalan**
   ```powershell
   python main.py
   ```
   - Coba gerak player dengan arrow keys
   - Pastikan tidak bisa tembus wall

3. **Check git status**
   ```powershell
   git status
   ```

4. **Stage perubahan**
   ```powershell
   git add main.py
   ```

5. **Commit dengan pesan deskriptif**
   ```powershell
   git commit -m "v1: Basic maze game dengan player movement"
   ```

6. **Push ke repository**
   ```powershell
   git push origin main
   ```

---

### **PUSH #2: Versi 2 (Add Food & Stamina)**

Fitur yang ditambahkan:
- ✅ Food collection system
- ✅ Stamina management (HP bar)
- ✅ Stamina berkurang saat bergerak
- ✅ Food restore stamina
- ✅ Game over ketika stamina habis

**Langkah-langkah:**

1. **Ganti main.py dengan main_v2.py**
   ```powershell
   Copy-Item -Path main_v2.py -Destination main.py -Force
   ```

2. **Test game berjalan**
   ```powershell
   python main.py
   ```
   - Lihat HP bar di kanan atas
   - Kumpulkan food untuk restore stamina
   - Pastikan game over saat HP habis
   - Tekan 1 untuk restart

3. **Check perubahan**
   ```powershell
   git diff main.py
   ```

4. **Stage perubahan**
   ```powershell
   git add main.py
   ```

5. **Commit**
   ```powershell
   git commit -m "v2: Tambah food system dan stamina management"
   ```

6. **Push ke repository**
   ```powershell
   git push origin main
   ```

---

### **PUSH #3: Versi 3 (Complete Game - Final)**

Fitur yang ditambahkan:
- ✅ Zombie AI dengan pathfinding
- ✅ Main menu dengan 4 level options
- ✅ Multiple levels (Easy, Medium, Hard)
- ✅ Endless mode
- ✅ Exit door (win condition)
- ✅ Pause functionality
- ✅ Difficulty scaling

**Langkah-langkah:**

1. **Ganti main.py dengan main_v3.py**
   ```powershell
   Copy-Item -Path main_v3.py -Destination main.py -Force
   ```

2. **Test game berjalan**
   ```powershell
   python main.py
   ```
   - Tekan up/down untuk navigate menu
   - Tekan Enter untuk select level
   - Coba 3 level berbeda
   - Coba endless mode
   - Tekan P untuk pause
   - Tekan M untuk kembali ke menu
   - Capai exit door untuk win

3. **Check perubahan final**
   ```powershell
   git diff main.py
   ```

4. **Stage perubahan**
   ```powershell
   git add main.py
   ```

5. **Commit final**
   ```powershell
   git commit -m "v3: Complete game dengan zombies, menu, endless mode"
   ```

6. **Push final ke repository**
   ```powershell
   git push origin main
   ```

---

## 🎮 TESTING CHECKLIST

### Push #1 Testing:
- [ ] Game window terbuka
- [ ] Player bisa bergerak 4 arah
- [ ] Tidak bisa tembus wall
- [ ] Score menambah saat gerak
- [ ] Exit code 0 saat close game

### Push #2 Testing:
- [ ] HP bar visible
- [ ] HP berkurang saat bergerak
- [ ] Food bisa dikumpulkan
- [ ] HP restore saat ambil food
- [ ] Game over saat HP 0
- [ ] Restart dengan tombol 1

### Push #3 Testing:
- [ ] Menu terbuka saat start
- [ ] Bisa select 3 level + endless
- [ ] Zombies bergerak mengejar
- [ ] Exit door terlihat
- [ ] Win saat capai exit
- [ ] Pause berfungsi (tombol P)
- [ ] Kembali menu (tombol M)
- [ ] Endless mode looping

---

## 📝 PERINTAH GIT REFERENCE

| Perintah | Fungsi |
|----------|--------|
| `git status` | Lihat file yang berubah |
| `git add main.py` | Stage perubahan |
| `git diff main.py` | Lihat detail perubahan |
| `git commit -m "pesan"` | Simpan perubahan dengan pesan |
| `git push origin main` | Upload ke repository |
| `git log` | Lihat history commit |
| `git log --oneline` | Lihat history singkat |

---

## 💡 TIPS PENTING

1. **Backup files tua:** Main_v1, v2, v3 tetap ada untuk referensi
2. **Test dulu sebelum push:** Jangan push code yang belum tested
3. **Pesan commit jelas:** Jelaskan fitur apa yang ditambah
4. **Push dalam urutan:** Jangan skip ke v3 langsung
5. **Internet stabil:** Pastikan koneksi saat push

---

## ❌ COMMON ISSUES & SOLUSI

### Issue: "fatal: not a git repository"
```powershell
# Pastikan berada di folder project
cd d:\coding\paa\Maze-Game
```

### Issue: "main.pynya tidak bisa jalan"
```powershell
# Cek module yang di-import berfungsi
python -c "import turtle; print('OK')"
```

### Issue: Push error
```powershell
# Pull dulu sebelum push
git pull origin main
git push origin main
```

### Issue: Ingin batalkan commit terakhir
```powershell
# Lihat commit terakhir
git log --oneline

# Undo commit (file tetap ada)
git reset --soft HEAD~1
```

---

## ✅ SETELAH SEMUA PUSH SELESAI

1. **Bersihkan file versi** (opsional):
   ```powershell
   Remove-Item main_v1.py, main_v2.py, main_v3.py
   ```

2. **Verify di GitHub:**
   - Buka repository di GitHub
   - Cek 3 commit terakhir ada
   - Pastikan main.py adalah versi 3 (final)

3. **Celebrate! 🎉**
   - Kamu sudah berhasil push game dengan 3 tahap progress

---

## 📞 COMMAND SUMMARY (QUICK COPY-PASTE)

**PUSH #1:**
```powershell
Copy-Item main_v1.py main.py -Force
python main.py
git add main.py
git commit -m "v1: Basic maze game dengan player movement"
git push origin main
```

**PUSH #2:**
```powershell
Copy-Item main_v2.py main.py -Force
python main.py
git add main.py
git commit -m "v2: Tambah food system dan stamina management"
git push origin main
```

**PUSH #3:**
```powershell
Copy-Item main_v3.py main.py -Force
python main.py
git add main.py
git commit -m "v3: Complete game dengan zombies, menu, endless mode"
git push origin main
```

---

Semoga sukses! 🚀
