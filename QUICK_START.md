# 🚀 QUICK START: 3 Push Dalam 5 Menit

## Apa yang sudah saya siapkan untuk Anda:

```
📁 d:\coding\paa\Maze-Game\
├── main.py (current - yang final)
├── main_v1.py ← Push #1 (Basic Game)
├── main_v2.py ← Push #2 (+ Food & Stamina)
├── main_v3.py ← Push #3 (Complete - sama dengan main.py)
├── TUTORIAL_PUSH_3_KALI.md (Panduan lengkap)
└── VERSION_COMPARISON.md (Perbandingan fitur)
```

---

## ⚡ PUSH #1 - Mulai Sekarang

**Tujuan:** Push versi basic game (player + maze + movement)

```powershell
# 1. Buka PowerShell di folder project
cd d:\coding\paa\Maze-Game

# 2. Swap main.py ke versi 1
Copy-Item main_v1.py main.py -Force

# 3. Test jalan tidak ada error
python main.py
# → Tekan arrow keys untuk gerak player
# → Tekan Q untuk close

# 4. Siapkan commit
git add main.py

# 5. Commit dengan pesan
git commit -m "v1: Basic maze game dengan player movement"

# 6. PUSH! 🎉
git push origin main

# Done! Cek GitHub 3-5 menit kemudian
```

**Cek di GitHub:**
- Buka: github.com/[your-username]/Maze-Game
- Scroll ke commits history
- Lihat commit baru dengan pesan "v1: Basic maze game..."

---

## ⏸️ Setelah Push #1 Selesai

Tunggu GitHub update (3-5 menit), verifikasi commit #1 ada, baru lanjut ke Push #2.

---

## 🎮 PUSH #2 - Tambah Food & Stamina

(Lakukan setelah Push #1 selesai)

```powershell
# 1. Swap ke versi 2
Copy-Item main_v2.py main.py -Force

# 2. Test
python main.py
# → Lihat HP bar di kanan atas
# → Kumpulkan food untuk restore HP
# → Tekan 1 untuk restart saat game over

# 3. Commit & Push
git add main.py
git commit -m "v2: Tambah food system dan stamina management"
git push origin main

# Done Push #2! ✅
```

---

## 🧟 PUSH #3 - Final Complete Game

(Lakukan setelah Push #2 selesai)

```powershell
# 1. Swap ke versi 3 (final)
Copy-Item main_v3.py main.py -Force

# 2. Test full features
python main.py
# → Menu terbuka
# → Tekan up/down untuk navigate
# → Tekan Enter untuk select level
# → Tekan P untuk pause
# → Tekan M untuk back to menu
# → Coba endless mode
# → Capai exit door untuk win!

# 3. Commit & Push FINAL
git add main.py
git commit -m "v3: Complete game dengan zombies, menu, endless mode"
git push origin main

# SELESAI! 🎉🎉🎉
```

---

## ✅ Verification Checklist

### After Each Push:
- [ ] Git status clean (tidak ada uncommitted changes)
- [ ] Commit message muncul di GitHub
- [ ] main.py file updated di GitHub
- [ ] Bisa pull kembali dari GitHub

### Final Checklist (After Push #3):
- [ ] GitHub shows 3 commits total (atau lebih)
- [ ] main.py di GitHub adalah versi 3 (complete)
- [ ] Bisa main game dengan semua fitur
- [ ] History commit terlihat jelas

---

## 🆘 Troubleshooting

### Error: "git: not found"
```powershell
# Install git atau gunakan Git Bash
# https://git-scm.com/download/win
```

### Error: "main.py jalan error"
```powershell
# Pastikan di folder yang benar
cd d:\coding\paa\Maze-Game

# Test import
python -c "import turtle; print('OK')"
```

### Error: "push rejected"
```powershell
# Pull dulu
git pull origin main

# Coba push lagi
git push origin main
```

### Mau lihat detail setiap push:
```powershell
# Lihat history commit
git log --oneline

# Lihat detail commit tertentu
git show <commit-hash>
```

---

## 📚 Untuk Info Lengkap

Lihat file-file ini:
- **`TUTORIAL_PUSH_3_KALI.md`** ← Panduan detail step-by-step
- **`VERSION_COMPARISON.md`** ← Perbandingan fitur ketiga versi

---

**Siap? Mari mulai Push #1! 🚀**

Tips: Copy-paste command di atas, jalankan satu per satu di PowerShell.
