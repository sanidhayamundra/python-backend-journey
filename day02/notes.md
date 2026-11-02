# Day 02 – Terminal, REPL, SSH, Data Types, PEP 8 + Internet & Networking

> Dev: terminal basics, REPL, SSH key (Day 1 leftovers) + data types, input/print, PEP 8
> System design: how the internet works (Day 1 leftover) + TCP/UDP, ports, HTTP/HTTPS

---

# DEV TRACK

## 1. Terminal Basics (PowerShell)

- Terminal = talking to the computer by typing instead of clicking.
- Analogy: File Explorer = pointing at menu pictures; terminal = telling the waiter exactly what you want.

```powershell
pwd                 # where am I?
ls                  # list files (dir also works)
cd day01            # go into folder
cd ..               # go up one level
cd ~                # go to home folder
mkdir day02         # create folder
ni day02\test.py    # create empty file (New-Item)
rm day02\test.py    # delete file (no Recycle Bin!)
cls                 # clear screen
```

### Paths
- **Absolute**: full address from drive → `C:\Users\sanid\python-backend-journey\day01` (works from anywhere)
- **Relative**: from current location → `day01`
- `.` = this folder, `..` = parent folder
- Analogy: absolute = full postal address; relative = "two houses to the left"

### Shortcuts
- **Tab** → autocomplete names
- **Up arrow** → previous commands

---

## 2. REPL (Read → Eval → Print → Loop)

- Python's interactive mode: type one line → instant result.
- Start: `python` → prompt `>>>` → leave: `exit()`
- No `print()` needed in REPL (it shows values automatically); needed in `.py` files.
- Analogy: `.py` file = posting a full letter; REPL = phone call with instant replies.
- C++ never had this — always had to compile a whole program to test one line.

```python
>>> type(3.5)          # check a type
>>> help(str.upper)    # built-in docs (q to quit)
>>> dir("hello")       # everything a string can do
```

---

## 3. SSH Key for GitHub

### Concept
- A **key pair**:
  - **Private key** (`id_ed25519`) → stays on my PC, NEVER share
  - **Public key** (`id_ed25519.pub`) → given to GitHub
- Analogy: public key = padlock given to GitHub; private key = the only key that opens it. No password travels over the internet.

### Steps (PowerShell)
```powershell
# 1. Generate key pair
ssh-keygen -t ed25519 -C "my-github-email"

# 2. Copy PUBLIC key (.pub!) to clipboard
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard

# 3. GitHub → Settings → SSH and GPG keys → New SSH key → paste

# 4. Test
ssh -T git@github.com
# → "Hi <username>! You've successfully authenticated..."

# 5. Switch repo from HTTPS to SSH
git remote set-url origin git@github.com:<username>/python-backend-journey.git
git remote -v
```
- Remote "connection" is just an address stored in `.git` → `set-url` changes that address.

---

## 4. Variables Recap

- Variables = **name tags** on objects, not boxes.
- Type belongs to the **object**, not the name (dynamic typing).
- `is` → same object; `==` → same value.
- **Rule: use `is` ONLY for `None`** (`if x is None:`). Use `==` for everything else.
- Why: Python caches small ints (-5 to 256), so `is` gives confusing results:
```python
a = 256; b = 256;   a is b   # True  (cached)
a = 1000; b = 1000; a is b   # may be False
```

---

## 5. Data Types

### int – unlimited size
```python
2 ** 200    # works fine — no overflow, no long long needed
```
- Convenient, but slower than C++ ints.

### float – decimals (IEEE 754, same as C++ double)
```python
0.1 + 0.2              # 0.30000000000000004
round(0.1 + 0.2, 2) == 0.3   # True
```
- 0.1 can't be stored exactly in binary (like 1/3 = 0.333... in decimal).
- Never compare floats with `==` → use `round()` or `math.isclose()`.
- **Money**: use `Decimal` or store in paise as `int`.

### bool
- `True` / `False` (capital letters!)
- bool is a subtype of int: `True + True == 2`

### None
- "No value" → like `nullptr` in C++.
- A function with no `return` returns `None`.

### str
- `'hi'` and `"hi"` are the same.
- No separate `char` type → one character = string of length 1.

### Checking types
```python
type(42)                 # <class 'int'>
isinstance(42, int)      # True  (preferred in real code)
isinstance(True, int)    # True  (bool is a kind of int)
```

### Conversions
```python
int("42")     # 42
int(3.99)     # 3 (cuts off decimal)
float("3.5")  # 3.5
str(10)       # "10"
```

---

## 6. input() and print()

### print()
```python
print("a", "b", "c")           # a b c
print("a", "b", "c", sep="-")  # a-b-c
print("Loading", end="...")    # no newline at end
print("done")                  # Loading...done
```

### input() ALWAYS returns str
```python
age = int(input("Age: "))      # convert immediately
```

### Multiple values on one line (like cin >> a >> b)
```python
a, b = map(int, input().split())
# "10 20" → split() → ["10","20"] → map(int) → 10, 20 → unpack
```

---

## 7. PEP 8 – Python Style Guide

- Official style rules. Not enforced, but every professional codebase follows them.
- Analogy: traffic rules — the car still moves if you break them, but everyone gets confused.

| Thing | Style | Example |
|---|---|---|
| Variables, functions | snake_case | `room_price`, `get_booking()` |
| Classes | PascalCase | `HotelBooking` |
| Constants | UPPER_CASE | `MAX_GUESTS = 4` |
| Indentation | 4 spaces (no tabs) | |
| Operators | spaces around | `x = a + b` |
| Line length | ≤ 79 (Black uses 88) | |
| Blank lines | 2 between top-level functions/classes | |
| Imports | at top of file | |

- C++ often uses camelCase → **Python uses snake_case**.
- Tools Ruff + Black will auto-check/fix this (Day 18).

---

## 8. Operators Gotcha
```python
7 / 2     # 3.5  (always float)
7 // 2    # 3
-7 // 2   # -4   (Python floors DOWN; C++ truncates toward zero → -3)
"5" * 3   # "555"
```

---

# SYSTEM DESIGN TRACK

## 1. Client-Server Model

- **Client** = asks (browser, mobile app, Postman)
- **Server** = answers (computer running a program like FastAPI/Django)
- Analogy: restaurant → customer (client) orders, kitchen (server) prepares, you never enter the kitchen.
- Running my own API locally → my laptop becomes the server.

---

## 2. IP Address – computer's postal address

- **IPv4**: `142.250.183.14` (4 numbers, 0–255) → ~4.3 billion, ran out
- **IPv6**: `2404:6800:4009:82b::200e` → practically unlimited
- **Public IP**: address on the internet
- **Private IP**: address inside home/office network (`192.168.x.x`)
- **127.0.0.1 / localhost**: "this same computer"
- Analogy: public IP = building address; private IP = flat number; router = security guard delivering parcels to flats.

---

## 3. DNS – the internet's phonebook

- Translates names (`google.com`) → IP addresses.
- Analogy: contacts app — tap "Mom", phone finds the number.
- Try: `nslookup google.com`

### Lookup order (each step only if previous doesn't know)
1. Browser cache
2. OS cache
3. DNS resolver (ISP like Jio/Airtel, or 8.8.8.8)
4. Root server → "ask .com servers"
5. TLD server (.com) → "ask Google's name servers"
6. Authoritative server → returns the IP ✅

- Answer is cached at each level → next lookup is instant.

---

## 4. URL Anatomy

```
https://www.treebo.com:443/hotels/delhi?checkin=2026-12-01#reviews
scheme  domain         port path        query string        fragment
```
- **scheme**: protocol (http/https)
- **domain**: name DNS converts to IP
- **port**: door on server (443 default for HTTPS, usually hidden)
- **path**: which resource
- **query string**: extra params `key=value&key2=value2`
- **fragment**: position in page, browser-only, never sent to server

---

## 5. What happens when you type a URL ⭐ (interview question)

1. **Parse URL** → scheme, domain, path...
2. **DNS lookup** → domain → IP
3. **TCP connection** → 3-way handshake on port 443
4. **TLS handshake** → agree on encryption, server shows certificate
5. **HTTP request** → `GET /hotels/delhi`
6. **Server processing** → runs code, queries DB, builds response
7. **HTTP response** → status (200), headers, body (HTML/JSON)
8. **Render** → browser draws page; extra requests for CSS/JS/images

- DevTools → Network → click request → **Timing**: DNS Lookup, Initial connection, SSL, Waiting (TTFB), Content Download = these exact steps.

---

## 6. TCP vs UDP

### TCP – reliable
- **3-way handshake**: SYN → SYN-ACK → ACK
- Data arrives complete and in order; lost pieces re-sent
- Slower
- Analogy: **phone call** — confirm the other person is there, ask them to repeat if missed

### UDP – fast
- No handshake, no delivery/order guarantee, lost data is gone
- Very fast, lightweight
- Analogy: **live radio broadcast** — keeps transmitting, static = lost word

| TCP | UDP |
|---|---|
| Every byte matters | Speed > perfection |
| Websites, APIs, downloads, email, DB, payments, bookings | Video calls, live streaming, games, DNS |

- Video call → skip a lost frame rather than freeze (old frame is useless).
- Booking/payment → losing data is a disaster → TCP.

---

## 7. Ports – doors on a server

- One server runs many programs; the **port** decides which program gets the data.
- Analogy: IP = office building address; port = department number.
- Range: 0–65535

| Port | Used by |
|---|---|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 5432 | PostgreSQL |
| 6379 | Redis |
| 8000 | Django / FastAPI dev servers |

- Try: `Test-NetConnection google.com -Port 443` → `TcpTestSucceeded : True`

---

## 8. HTTP – language of the web

- Runs **on top of TCP**: TCP delivers bytes, HTTP defines what they mean.

### Request
- **Method**: GET (read), POST (create), PUT/PATCH (update), DELETE (remove)
- **Path**: `/hotels/delhi`
- **Headers**: `Content-Type: application/json`, `Authorization: Bearer <token>`
- **Body** (optional): data like JSON

### Response
- **Status code**:
  - `2xx` success → 200 OK, 201 Created
  - `3xx` redirect → 301 Moved Permanently
  - `4xx` **client's** mistake → 400, 401 Unauthorized, 404 Not Found
  - `5xx` **server's** mistake → 500 Internal Server Error, 503 Service Unavailable
- **Headers**
- **Body**: HTML, JSON, image...

### Stateless
- Every request is independent; server doesn't remember previous ones.
- That's why login needs cookies/tokens (JWT, Day 49) sent with every request.

- Try: `curl.exe -v https://example.com` (`>` = request, `<` = response)
- In PowerShell use `curl.exe`, not `curl` (plain `curl` is a different command).

---

## 9. HTTPS = HTTP + TLS

- Plain HTTP = readable text → anyone on the network can read it.
- TLS adds:
  1. **Encryption** → only browser and server can read data
  2. **Identity** → server shows a **certificate** signed by a trusted authority
- Analogy: HTTP = postcard; HTTPS = sealed tamper-proof envelope + courier showing govt ID (certificate).
- HTTPS → port 443; HTTP → port 80
- 🔒 padlock in browser = HTTPS working (click to see certificate)

---

## Self-check (explain out loud)
- [ ] What does `cd ..` do? Absolute vs relative path?
- [ ] Why never share the file without `.pub`?
- [ ] Why `0.1 + 0.2 != 0.3`? How should money be stored?
- [ ] What does `input()` always return?
- [ ] Why use `is` only for `None`?
- [ ] Every step from typing a URL to seeing the page
- [ ] When to choose UDP over TCP? One example each
- [ ] 4xx vs 5xx — whose mistake?
- [ ] What two things does TLS add to HTTP?