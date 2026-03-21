# ❗ Error Analysis

We analyzed cases where the model predictions were incorrect.

---

## 🔍 Failure Cases (Examples)

1. Text: "ok"
   - Problem: Too short → no clear meaning

2. Text: "fine"
   - Problem: Could mean calm OR upset

3. "felt lighter, but still stressed"
   - Problem: Mixed emotions

4. "kept thinking about work"
   - Problem: Could be focused or stressed

5. "not much change"
   - Problem: Neutral but unclear intensity

6. "better after some time"
   - Problem: Time-based emotion not captured

7. "mind was all over the place"
   - Problem: Could be restless or overwhelmed

8. "calm now"
   - Problem: No context of previous state

9. "session was okay"
   - Problem: Very vague

10. "a bit off"
    - Problem: Weak emotional signal

---

## 🧠 Insights

- Short text leads to poor predictions  
- Ambiguous words confuse the model  
- Mixed emotions are hard to classify  
- Model relies heavily on keywords  
- Some labels in data may be noisy  

---

## 🔧 Improvements

- Use larger dataset  
- Use deep learning models (like BERT)  
- Add context from previous entries  
- Improve labeling quality  