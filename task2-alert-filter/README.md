# Task 2 — Alert Filter

## Run

```bash
python task2-alert-filter/filter_alerts.py
```

No dependencies. Python 3.8+ only.

---

## Result

```
disk 90%
payment failed
db timeout
критичных 3
```

---

## Limitations

- **Static file.** The script reads a fixed JSON file; no live monitoring or streaming.
- **Level field only.** Events without a `level` field are silently ignored (safe but invisible).
