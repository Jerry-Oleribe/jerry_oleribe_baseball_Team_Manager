# Baseball Team Manager (Sections 1–3) — CPRO 2201 Midterm

This project implements the **Baseball Team Manager** case study using **Sections 1–3** requirements:
- **Section 1:** core features + validation + CSV persistence
- **Section 2:** improved console formatting + dates (optional)
- **Section 3:** object-oriented design (Player + Lineup)

## Folder structure
- `ui.py` — Presentation layer (input/output only)
- `objects.py` — Business layer (Player, Lineup, rules)
- `db.py` — Data layer (read/write `players.csv`)
- `main.py` — Coordinates UI, objects, db

## How to run (PyCharm or Terminal)
1. Ensure `players.csv` is in the same folder as the `.py` files.
2. Run:
   ```bash
   python main.py
   ```

## CSV format
`players.csv` rows are stored as 4 columns:
```
full_name,position,at_bats,hits
```

Example row:
```
Tommy La Stella,3B,1316,360
```

## Notes for rubric alignment
- Input validation:
  - menu option must be valid
  - lineup numbers must be in range
  - at_bats/hits must be non-negative and hits <= at_bats
  - batting average is 0.0 when at_bats == 0
- Separation of layers: ui / objects / db (no circular imports)

## Video explanation checklist (5 minutes)
- Show menu working (all options)
- Explain Player + Lineup classes (encapsulation + iterator)
- Demonstrate CSV persistence (add a player, exit, restart, show player still there)
- Demonstrate error handling (enter a string where an integer is expected)
