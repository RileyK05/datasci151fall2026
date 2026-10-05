# DSCI 151 Quiz Notes — Lectures 1–4 + Lecture 5 (Sections I–V)

**Scope (from the professor):** Lectures 1–4, plus Lecture 5 Sections I–V
(ends at the `in` keyword). Sections VI (logical operators) and VII
(if/elif/else) are **NOT** on the quiz — don't study them for this.

**How to use these notes:** Sections 1–10 are reference ("how do I write X").
Sections 11–14 are trap-avoidance ("where do I lose points"). If you only
have 5 minutes, read §14 (rituals), §12 (float equality), and the linspace
deep-dive in §9.

---

## 1. Objects, Types & Variables (Lecture 3)

- Almost everything in Python is an **object**. Common types:
  - `int` (whole numbers: `3`, `-17`)
  - `float` (decimals: `3.25`, `0.1`)
  - `str` (text: `"hello"`)
  - `bool` (`True` / `False`)
  - `list` (`[1, 2, 3]`), `tuple` (`(1, 2, 3)`)
  - `numpy.ndarray` (arrays, later)
- Check any object's type: `type(x)` → e.g. `<class 'int'>`
- Assignment: `x = 3` means **"assign the value 3 to the name x"**
  - NOT "x equals 3" — it stores, it doesn't compare
  - Re-assigning overwrites: `x = 3`, then `x = 5` → x is now 5
  - `x = x + 1` is legal and common (right side computed first, then stored)
- Variables are **case-sensitive**: `age` and `Age` are different names
- A variable must be **defined before use** — using an undefined name → `NameError`
- Naming rules: letters, digits, underscore; can't start with a digit;
  can't use reserved words (`if`, `in`, `print` is allowed but shadows the function)
- Print several things in one cell: `print(a, b, c)` — a bare variable only
  displays if it's the LAST line of the cell

## 2. Printing & Strings (Lectures 3–4)

- `print(obj)` — writes to the screen. Without it, only the last expression
  in a cell auto-displays (and some methods return nothing visible).
- f-strings — insert variables into text:
  ```python
  print(f"x is {x} and y is {y}")
  ```
- Quotes: single `'...'` and double `"..."` are both strings and both work
  - **Cannot mix** opening and closing types: `type('Hello World!")` → error
  - To include an apostrophe, use double quotes outside: `"Peter's favorite song"`
- String concatenation (`+` glues strings, in order):
  ```python
  "Roxy" + " Music"        # → "Roxy Music"
  ```
  - Watch for **spaces**! " Music" vs "Music" — the quiz (Q.B) hides spaces
    inside the pieces; read each list element character-by-character
- `len(s)` — how many characters in a string / elements in a list
- Strings are also sequences: `s[0]` is the first character (zero-indexed, like lists)

## 3. Lists (Lecture 3)

```python
my_list = ["a", "b", "c", 12, 3.5]     # mixed types are fine
len(my_list)                            # → 5 (number of elements)
my_list[0]                              # → "a"  FIRST element (zero-indexed!)
my_list[-1]                             # → 3.5  last element (negative counts back)
my_list[2] = "new"                      # overwrite one element — lists are MUTABLE
```

- **Zero-indexing:** element 0 is the first; for n elements, valid indices are
  `0` through `n-1`. Index n → IndexError.
- Negative indexing: `-1` = last, `-2` = second-to-last, etc.
- Lists can hold **any** objects — including other lists:
  ```python
  nested = [ [1, 2], [3, 4] ]
  nested[1]        # → [3, 4]      (the sub-list)
  nested[1][0]     # → 3           (double indexing: list, then element)
  ```
- **The quiz pattern** (a's oscars / 1a's grammys):
  ```python
  nominees_2024 = [winner_2024] + runner_up_2024     # winner first
  oscars_2022_2025 = [nominees_2025, nominees_2024, nominees_2023, nominees_2022]
  oscars_2022_2025[1][0]     # → element 0 of the 2024 list (the winner)
  ```
  Read `[1][0]` as: "first pick the sub-list at position 1, THEN pick position 0 inside it."

## 4. Tuples (Lecture 4)

```python
my_tuple = (32, 77, 19, 0, 14, 27)
my_tuple[4]          # → 14 (indexing identical to lists)
my_tuple[-1]         # → 27
```

- **Tuples are IMMUTABLE** — once created, elements cannot be changed.
  `my_tuple[0] = 99` → TypeError.
- **Lists are MUTABLE** — `midterm_grades[5] = 73.2` works fine.
- Why tuples exist: store values that should *never* change (IDs, constants).
- Quiz trap: "fix a grade in `midterm_grades`" works because it's a list.
  If the data were a tuple, the same code would crash.
- Conversion (in case asked): `list(my_tuple)` → list; `tuple(my_list)` → tuple.

## 5. The `.index` Method (Lecture 4)

Find **where** something lives in a sequence:

```python
my_tuple.index(14)          # → 4
student_ids.index("T-126")  # → 5   (works on lists AND tuples)
```

- Returns the position of the **first occurrence**.
- Searching for something absent → ValueError.
- **The parallel-sequences pattern** (quiz Q.b / grade fixing):
  ```python
  student_index = student_ids.index("T-126")   # find WHERE the student is
  midterm_grades[student_index] = 73.2         # use the SAME position in the other list
  ```
  This works because the two sequences line up element-for-element.

## 6. Concatenation (Lecture 4)

`+` combines two sequences of the same type **end-to-end**:

```python
[winner] + runner_up      # list + list → NEW list of 10 elements
"Roxy" + " Music"         # string + string → longer string
(1, 2) + (3,)             # tuple + tuple → longer tuple
```

- To put a single item at the front of a list, **wrap it in brackets first**:
  `[item] + list`. (Writing `item + list` with a bare string fails — str + list is an error.)
- Concatenation makes a **new** sequence; the originals are unchanged.
- **Warning — flat vs nested:** `[a, b] + [c]` → `[a, b, c]` (flat). Putting a list
  INSIDE another list (`[a, [b, c]]`) is nesting. They look similar, behave totally differently.
- **Warning — copying:** `list_b = list_a` does NOT copy the list; both names point
  to the *same* list (aliasing). Change one, "both" change:
  ```python
  a = [1, 2]
  b = a          # same list!
  b.append(3)
  print(a)       # → [1, 2, 3]   — surprised? that's aliasing
  ```
  Independent copy: `b = a + []` or `b = a[:]` (slicing).

## 7. NumPy Arrays (Lecture 4)

```python
import numpy as np
temps_c = np.array([0, 10, 20, 30, 40])
```

**Why arrays:** lists + `+` concatenate; arrays + `+` add element-by-element.
NumPy = "NUMerical PYthon" — built for math on whole grids of numbers at once.

- **Vectorized operations** — every element transformed, NO loop needed:
  ```python
  temps_f = temps_c * (9/5) + 32      # → [32, 50, 68, 86, 104] in one line
  ```
- Array-to-array (must be the SAME SIZE):
  ```python
  np.array([1, 2, 3]) + np.array([10, 20, 30])   # → [11, 22, 33]
  ```
- Array + single number (broadcasting — number is applied to every element):
  ```python
  np.array([1, 2, 3]) * 3        # → [3, 6, 9]
  ```
- Wrong sizes → ValueError (can't pair up elements).

## 8. Math Constants, Functions & Scientific Notation (Lectures 3–4)

```python
import math
math.pi                 # 3.141592653589793 — the real π (never type 3.14!)
math.sqrt(2)            # 1.414...
import numpy as np
np.pi                   # same π, available through numpy too
np.sqrt(2 * np.pi)      # sqrt of an expression — element-wise on arrays
np.exp(-x**2)           # e^(-x²)  — euler's number raised element-wise
np.sin(t + 3)           # trig — element-wise
np.mean(arr)            # average; np.mean(temps_f) → average Fahrenheit
```

Arithmetic operators reference:
```python
3.2 + 1.7    # addition
5 - 11       # subtraction
4 * 3        # multiplication
1 / 7        # division → float (always), even 4/2 → 2.0
2 ** 5       # exponentiation → 32
7 // 2       # floor division → 3 (drops the remainder)
7 % 2        # modulo → 1 (the remainder)
```

- **Scientific notation:** `1e-9` = 0.000000001 — a single number literal.
  - `epsilon = 1e-9` ✔
  - `epsilon = 1e**-9` ✘ SyntaxError — `e` in a literal is not an operator
  - `epsilon = 10**-9` ✔ (same value, via the power operator)
- Parentheses control order of operations — `2 + 3 * 4` = 14; `(2 + 3) * 4` = 20.

## 9. Plotting (Lectures 2 & 4)

### Scatter plot — dots, for data points

```python
import matplotlib.pyplot as plt          # usually imported once at the top

plt.scatter(df["mpg"], df["acceleration"])   # x first, y second
plt.xlabel("MPG")
plt.ylabel("Acceleration")
plt.title("MPG vs Acceleration")
plt.show()                               # ALWAYS last — hides stray text output
```

- **"A vs. B" convention: A goes on the x-axis, B on the y-axis.** (mpg vs acceleration → mpg is x)
- Both axis labels + title are **graded requirements**, not decoration.
- `plt.show()` is a graded requirement — without it the cell prints
  `[<matplotlib.lines.Line2D at 0x...>]` above the figure.

### Line plot — connected curves, for functions

```python
x = np.linspace(-3, 3, 75)                # domain: 75 evenly spaced points
y = np.exp(-x**2) / np.sqrt(2 * np.pi)    # formula, vectorized over all 75 points
plt.plot(x, y)                            # line through the points
plt.xlabel("x"); plt.ylabel("pdf"); plt.title("Standard normal pdf")
plt.show()
```

- scatter = loose dots (data), plot = connected line (functions).

### Linspace, slowly (the deep-dive)

`np.linspace(A, B, N)` answers ONE question:
**"Give me N numbers, evenly spaced, starting at A and ending at B."**

Think of it as a ruler: A is the left end, B is the right end, N is how many tick marks.

```python
np.linspace(0, 10, 5)      # → [0, 2.5, 5, 7.5, 10]   (5 points, 0 to 10)
np.linspace(-3, 3, 75)     # → 75 points from -3 to 3
np.linspace(2*np.pi, 4*np.pi, 75)   # → 75 points from ~6.28 to ~12.57
```

The three slots, in order, ALWAYS:
1. **start** — where the interval begins (leftmost number)
2. **stop** — where it ends (**included** by default!)
3. **num** — HOW MANY points you want (**count, not step size!**)

```python
np.linspace(2, 4, 75)              # plain numbers work
np.linspace(2*np.pi, 4*np.pi, 75)  # math expressions work (evaluated first!)
np.linspace(2, 4, 75) * np.pi      # alt: generate 2→4, THEN scale (Solution 3 trick)
```

- `endpoint=True` is the default (the stop value IS in the output); rarely changed.
- Spacing between points = (stop − start) / (num − 1) — 75 points = 74 gaps.
- num = "how many points": more points → smoother curve, same interval.
- π intervals: write inline (`2*np.pi`) or scale after — both identical results.
- Extra parentheses around arguments work but are pointless —
  `np.linspace((2*np.pi), (4*np.pi), 75)` == `np.linspace(2*np.pi, 4*np.pi, 75)`.

### Graphing recipe (muscle memory, in order)

```python
x = np.linspace(START, STOP, N)   # 1. domain → x values
y = <formula in x>                # 2. function → y values (vectorized, no loop)
plt.plot(x, y)                    # 3. draw the LINE through the points
plt.xlabel("...")                 # 4. label x-axis
plt.ylabel("...")                 # 5. label y-axis
plt.title("...")                  # 6. title
plt.show()                        # 7. display + suppress stray output
```

`plt.plot()` with no arguments draws NOTHING — always pass x and y.

### Composed functions f(g(t)) — inner first, then outer

```python
t = np.linspace(2*np.pi, 4*np.pi, 75)   # domain is the INNER function's input
g_vals = np.sin(t + 3)                  # INNER function first, store the result
y = g_vals**2 - 5*g_vals + 2            # OUTER formula applied to that result
plt.plot(t, y)                          # x-axis = t (the input), NOT g_vals!
plt.show()
```

- Each intermediate (`g_vals`) is just another array — normal vectorized math applies.
- **Plot the original input (`t`) against the final output (`y`).** The
  intermediate is scaffolding.
- Using helper functions is fine and matches homework style:
  ```python
  def f(x):  return x**2 - 5*x + 2     # one function taking the array
  y = f(np.sin(t + 3))                 # feed g's output into f
  ```
  or two helpers: `y = f(g(t))` — Python evaluates `g(t)` first (inner-out).

## 10. Data Frames / pandas (Lecture 2)

```python
import pandas as pd
df = pd.read_csv("data/features.csv")   # relative path, in quotes, file extension included
df.head()        # first 5 rows — use to VERIFY you loaded the right file
df.shape         # (rows, columns)
df.columns       # column names
df["mpg"]        # one column (a Series)
df["mpg"].describe()   # stats for ONE column: count/mean/std/min/25%/50%/75%/max
df.describe()          # stats for ALL numeric columns — DIFFERENT thing!
```

- Read questions carefully: "describe the variable mpg" = `df[...].describe()`
  (one column). "Display descriptive statistics" unqualified could be the frame.
- **The "don't type the string" constraint:** when a list of names is provided
  (`features_of_interest = ["acceleration", "cylinders", "horsepower", "mpg"]`),
  count the position and index:
  - `"mpg"` is at index **3** → `df[features_of_interest[3]]`
  - `"acceleration"` is at index **0** → `df[features_of_interest[0]]`
- This constraint applies to **labels and titles too** — build them from the list:
  ```python
  plt.xlabel(features_of_interest[3])
  plt.title("Relationship between " + features_of_interest[3] + " and " + features_of_interest[0])
  # or with an f-string:
  plt.title(f"Relationship between {features_of_interest[3]} and {features_of_interest[0]}")
  ```
- Relative paths: the notebook and the data folder sit side by side, so
  `"quiz_data/features.csv"` (from notebook location) — check `df.head()` to confirm.
- **"A vs. B"** in pandas questions: A on x-axis, B on y-axis.

## 11. Booleans & Comparison Operators (Lecture 5, I–II)

- Booleans are the objects `True` and `False` — **not** the strings "True"/"False".
- Six comparison operators — each produces one boolean:
  | Operator | Meaning |
  |---|---|
  | `>` | greater than |
  | `<` | less than |
  | `>=` | greater or equal |
  | `<=` | less or equal |
  | `==` | **equal** (comparison, not assignment!) |
  | `!=` | not equal |
- **`=` assigns, `==` asks.** `x = 3` stores; `x == 3` produces True/False.
- Strings: `==` requires **every character to match exactly**:
  ```python
  "Hello World!" == "Hello World !"   # False — one extra space!
  "Federal" == "federal"              # False — case-sensitive
  'ab' == 'ba'                        # False — order matters
  ```
- Lists: `==` requires **every element equal, in the same order, same length**:
  ```python
  [1,2,3] == [1,2,3]        # True
  [1,2,3] == [2,3,1]        # False — different order
  [2,3,1] == [2,3,1,4]      # False — different length
  ```

## 12. Floating-Point Equality (Lecture 5, II) — THE epsilon section

**The trap:** floats carry tiny rounding errors:
```python
x = 0.1 * 7
y = 0.7
print(x == y)             # → False  (!!)
print(abs(x - y))         # → 1.1102230246251565e-16  (the error is ~10⁻¹⁶)
```

**The fix — compare with a tolerance (epsilon/delta):**
```python
epsilon = 1e-12                        # solutions used 1e-13; "1e-12 or 1e-14 fine too"
print(abs(x - y) < epsilon)            # → True
```

- Form to memorize: **`abs(x - y) < delta`** (the quiz wants this shape)
- Choosing delta: bigger than the rounding noise (~1e-16), smaller than any
  difference you care about → **1e-12 to 1e-14** for numbers of magnitude ~1
- `1e-12` is scientific notation: 10⁻¹². `1e**-12` is a SyntaxError;
  `10**-12` also works.
- One decimal place → about one "step" of float precision; differences of
  ~1e-16 are noise, differences of 0.1 are real.
- Note `math.isclose(x, y)` exists in real Python, but write the `abs() < delta`
  form — that's what the course tests.

## 13. The `in` Keyword (Lecture 5, V)

Membership test — does X appear in Y? Returns a boolean.

```python
# Strings — SUBSTRING search (is it inside, anywhere):
sentence = "The Federal Reserve makes forecasts"
"economic" in sentence     # True
"bank" in sentence         # False
"F" in sentence            # True
"federal" in sentence      # False — CASE-SENSITIVE

# Lists — EXACT match against each element (not substring!):
"J" in ["June", "July", "August"]        # False — no element equals "J"
"J" in ["June", "July", "August", "J"]   # True — exact element "J" exists
"Biology" in majors                      # True — exact element match
"June" in ["June", "July"]               # True

# NumPy arrays / tuples — element membership:
1 in np.array([1.0, 3.0, -17])   # True
2 in [0, 22, "x"]                # False
```

**Gotchas:**
- string → substring; list/array → whole-element exact match. Different semantics!
- Case-sensitive everywhere: `"federal" in` ≠ `"Federal" in`.
- Float membership inside arrays uses `==` internally → same float trap:
  ```python
  x = 0.1 + 0.1 + 0.1; y = 0.3
  1 in np.array([x/y, 3.0])   # → False! (x/y is 0.9999999999999999)
  ```
- `2 in 22` → TypeError (right side must be a sequence). Workaround:
  `str(2) in str(22)` → True (string of digits, substring search).
- Typical quiz usage (Q.F): `print("Biology" in majors)` — one line, no loop.

## 14. Quiz-Day Rituals (hard-won from the practice quiz)

1. **Run ALL cells before submitting** — graders grade the visible outputs.
2. **Re-run after EVERY edit** — an edited-but-unrun cell shows `exec=None`.
3. **`plt.show()`** at the end of every plot cell — required, kills stray `[<Line2D>]`.
4. **`print(...)`** when instructions say "print to the screen" — a bare
   expression only displays if it's the cell's last line.
5. **"Don't type the string"** = index the provided list — for data access
   AND labels/titles (via `+` or f-strings).
6. **Describe on a column** = `df[col].describe()`; on the whole frame =
   `df.describe()`. Read which one is asked.
7. **Swap needs a temp:** `temp = a; a = b; b = temp`
   (`b = a; a = b` just duplicates — both end up as the original a).
8. **Epsilon window:** 1e-12 to 1e-14 for magnitude-1 comparisons; write `abs(x-y) < delta`.
9. **`df.head()`** immediately after loading — confirms right file/columns.
10. **`.index()`** finds a position; apply that position to the paired list.
11. **"A vs. B"** = A on x-axis, B on y-axis. In scatter AND line plots.
12. **Check cell hygiene before submitting:** no `exec=None`, no error outputs,
    every plot has an image output, no debug `print`s you don't want seen.
13. **Eager check:** if the instructions show the expected output or target
    string, run your cell and compare character-for-character.

## 15. One-Minute Panic Sheet (while the quiz is open)

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# data
df = pd.read_csv("quiz_data/features.csv"); df.head()
df["mpg"].describe()                  # or df[features_of_interest[3]].describe()

# scatter: A vs B → A on x
plt.scatter(df[L[3]], df[L[0]]); plt.xlabel(...); plt.ylabel(...); plt.title(...); plt.show()

# line plot of a function
t = np.linspace(start, stop, 75)
y = <formula in t>                    # vectorized — no loop, ever
plt.plot(t, y); plt.xlabel(...); plt.ylabel(...); plt.title(...); plt.show()

# composed f(g(t)):
g = np.sin(t + 3)                     # inner first
y = g**2 - 5*g + 2                    # outer second
plt.plot(t, y)                        # input vs final output

# floats
abs(x - y) < 1e-12                    # NEVER x == y for floats

# membership
"Biology" in majors                   # bool, exact match

# position lookup
i = my_tuple.index(item)              # then use i elsewhere

# swap
temp = a; a = b; b = temp
```