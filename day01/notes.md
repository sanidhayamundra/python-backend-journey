Notes · MD
# Day 01 – Setup, Git, venv & Python Basics
 
> Goal: Understand how Python differs from C++, set up a clean project, and make the first commit.
 
---
 
## 1. Git & GitHub
 
### What connects my folder to GitHub?
- `git clone <url>` creates the folder, downloads files, and creates a **hidden `.git` folder**.
- `.git` = the brain of the repo: full commit history, branches, settings, and the **remote address** (`origin`).
- VS Code sees `.git` → turns on Source Control features.
- Check the connection: `git remote -v`
### It is NOT a live sync
- Local repo (my PC) = **home**, GitHub = **warehouse**. Nothing moves unless I ship it.
- `git push` → send commits to GitHub
- `git pull` → bring changes from GitHub
### The 3 areas of Git
| Area | Analogy | Command to move forward |
|---|---|---|
| Working directory | Desk (editing files) | `git add` |
| Staging area | Packed box | `git commit` |
| Local repo (commit) | Sealed & labelled box | `git push` |
| Remote (GitHub) | Warehouse | – |
 
### One-time Git setup
```bash
git config --global user.name "Sanidhaya"
git config --global user.email "my-github-email"
git config --global init.defaultBranch main
```
 
### Daily flow
```bash
git status                      # what changed?
git add .                       # stage everything
git commit -m "Day N: message"  # save a snapshot
git push                        # upload to GitHub
```
 
### .gitignore
- A file in the **repo root** listing things Git must never track.
- Applies to all subfolders.
```
.venv/
__pycache__/
*.pyc
```
- Ignored files appear **greyed out** in VS Code.
---
 
## 2. Virtual Environment (venv)
 
### Why?
- Without venv, all libraries go into **one global Python** → version clashes between projects ("dependency hell").
- venv = each project gets its **own private Python + libraries**.
- Analogy: global Python = shared office kitchen; venv = personal lunchbox.
### What's inside `.venv`
```
.venv/
├── Scripts/python.exe, pip.exe, Activate.ps1
├── Lib/site-packages/   ← installed libraries go here
└── pyvenv.cfg
```
 
### What "activate" does
- Puts `.venv\Scripts` at the **front of PATH** (for that terminal only).
- So `python` / `pip` now mean the venv's copies.
- `(.venv)` in the prompt = I'm inside the lunchbox.
### Commands (Windows PowerShell)
```powershell
python -m venv .venv               # create
.venv\Scripts\Activate.ps1         # activate (every new terminal)
deactivate                         # leave
Get-Command python                 # which python am I using?
pip list                           # what's installed here?
```
- If scripts are blocked (one time): `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
- Mac/Linux activate: `source .venv/bin/activate` (use `python3` outside venv)
### Why `.venv` is in .gitignore
- Big, machine-specific, and rebuildable.
- Share the **recipe**, not the cooked food:
```powershell
pip freeze > requirements.txt      # save the recipe
pip install -r requirements.txt    # rebuild anywhere
```
 
---
 
## 3. How Python Works (vs C++)
 
### Interpreted, not compiled to machine code
- C++: compile whole program → machine code → run. Errors caught before running.
- Python: code → **bytecode** (`.pyc` in `__pycache__`) → run line by line by the Python VM.
- So errors appear **at runtime**, only when that line executes.
- Analogy: C++ = translate the whole book first; Python = live interpreter, sentence by sentence.
### Variables are name tags, not boxes ⭐
- C++: `int x = 5;` → a box holding 5.
- Python: `x = 5` → object `5` exists, `x` is a **tag** on it.
- Assignment **never copies**:
```python
a = [1, 2, 3]
b = a          # same object, two tags
b.append(4)    # a also changes
c = a.copy()   # real copy
```
- `is` → same object? (like comparing pointers)
- `==` → same value?
- `id(x)` → identity of the object
### Dynamic but strong typing
- Type belongs to the **object**, not the name → `x = 10` then `x = "hi"` is fine.
- Strong: `"5" + 5` → `TypeError` (no silent conversion).
- Type hints (not enforced, but used heavily by FastAPI):
```python
def add(a: int, b: int) -> int:
    return a + b
```
 
### Mutable vs Immutable
| Immutable (new object on change) | Mutable (changed in place) |
|---|---|
| int, float, str, bool, tuple | list, dict, set |
- Analogy: immutable = printed photo (print a new one); mutable = whiteboard.
- `s += "!"` on a string creates a **new** string (different `id`).
### Passing to functions
- Python passes the **reference (tag)**.
- Modify the object → caller sees it. Reassign the name → caller doesn't.
```python
def modify(lst):   lst.append(99)   # caller sees change
def reassign(lst): lst = [0]        # caller unaffected
```
- Similar to passing a pointer in C++: changing `*p` is visible, changing `p` is not.
---
 
## 4. Core Syntax Cheat-sheet
 
```python
# Indentation (4 spaces) instead of { }
if x > 5:
    print("big")
elif x == 5:
    print("five")
else:
    print("small")
 
for i in range(5): ...              # 0..4
for item in my_list: ...            # range-based for
for i, item in enumerate(my_list): ...
 
and / or / not                      # logical operators
7 / 2   # 3.5 (always float)
7 // 2  # 3   (integer division)
2 ** 10 # 1024 (power)
# ints never overflow (no long long needed)
 
name = "Sanidhaya"
print(f"Hello {name}")             # f-string
 
a, b = b, a                         # swap
 
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
 
n = int(input("Enter: "))           # input() always returns str
s[::-1]                             # reverse a string/list
nums[-1]                            # last element
nums[1:3]                           # slicing
```
 
### Collections
| Python | C++ equivalent | Notes |
|---|---|---|
| `list` `[1, 2]` | `vector` | mutable, ordered |
| `tuple` `(1, 2)` | `pair` / `tuple` | immutable |
| `dict` `{"a": 1}` | `unordered_map` | keeps insertion order; `d.get(k, default)` |
| `set` `{1, 2}` | `unordered_set` | unique items |
 
---
 
## 5. LLD Intro
 
- **HLD** = city map → which services exist and how they talk (booking, payment, inventory).
- **LLD** = floor plan of one building → classes, objects, relationships inside one service.
- LLD tests: **OOP** → **SOLID** → **Design Patterns** → full problems (Parking Lot, BookMyShow).
- First step of any LLD: **nouns → classes, verbs → methods**.
  - "Guest books Room for Dates" → `Guest`, `Room`, `Booking`; method `book()`.
---
 
## 6. Self-check (explain out loud)
- [ ] Why doesn't `b = a` copy a list in Python, when it does copy a `vector` in C++?
- [ ] Difference between `is` and `==`?
- [ ] Why can a typo inside an `if` go unnoticed until runtime?
- [ ] What does activating a venv actually change?
- [ ] Why is `.venv` in `.gitignore`, and how do we rebuild it?
- [ ] Is my local repo live-synced with GitHub? What moves changes?
- [ ] LLD vs HLD in one line each.