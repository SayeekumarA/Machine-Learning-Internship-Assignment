# 📱 Edge / Deployment Plan

This system can be deployed on mobile or run locally.

---

## 🚀 Deployment Approach

1. Convert model into a backend API (Flask/FastAPI)
2. Connect with frontend (HTML/CSS/JS UI)
3. User enters text → system returns result

---

## 📦 Running on Device

- Model is lightweight (SVM + Ridge)
- Can run on:
  - Mobile
  - Laptop
  - Offline system

---

## ⚡ Optimizations

### 1. Model Size
- Use simple models (already done)
- Avoid heavy deep learning models

### 2. Speed (Latency)
- Preload TF-IDF vectorizer
- Preload model in memory
- Avoid retraining

### 3. Memory
- Limit TF-IDF features (e.g., 2000 max)
- Use sparse matrices

---

## 🧠 Handling Edge Cases

### Short text ("ok", "fine")
- Mark as uncertain

### Missing values
- Fill with average values

### Conflicting signals
- Use metadata (stress, energy) to decide

---

## ⚖️ Tradeoffs

| Option | Pros | Cons |
|------|------|------|
| Simple model | Fast, lightweight | Less accurate |
| Complex model | More accurate | Slow, heavy |

---

## 🎯 Final Goal

Fast, reliable system that works even:
- offline  
- with limited resources  
- on real-world messy input  