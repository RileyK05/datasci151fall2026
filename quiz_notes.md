# DSCI 151 Quiz Notes — Lectures 1–4 + Lecture 5 (Sections I–V)

Scope: Lectures 1–4, plus Lecture 5 Sections I–V (through the `in` keyword).
Sections VI (logical operators) and VII (if/elif/else) are NOT on this quiz.

---

## 1. Objects, Types & Variables (Lecture 3)

- Common types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `numpy.ndarray`
- Check a type: `type(x)`
- Print multiple things in one cell: `print(a, b, c)`
- Assignment: `x = 3` means "assign 3 to x" (NOT "x equals 3")
- Variables are **case-sensitive**; must be defined before use (defining after = NameError)
- Naming: descriptive names allowed (letters, numbers, `_`; can't start with a number)

## 2. Printing & Strings

- `print(obj)` — prints to screen
- f-strings: `print(f"x is {x}")` — inserts variable values into text
- String quotes: single `'...'` and double `"..."` both work
  - Can't mix quote types in one string (error)
  - To put a quote inside, use the other type: `"Peter's favorite song"`
- String concatenation with `+`: `"Roxy" + " Music"` → `"Roxy Music"`
- `len(s)` — length of a string/list

## 3. Lists (Lecture 3)

```python
my_list = ["a", "b", "c", 12, 3.5]     # mixed types OK
len(my_list)                            # number of elements
my_list[0]                              # FIRST element (zero-indexed!)
my_list[-1]                             # last element
my_list[2] = "new"                      # overwrite an element (lists are mutable)
```

- Zero-indexing: element 0 is the first. For n elements, last index is n-1.
- Sub-lists / nesting: a list can contain lists; access with **double indexing**:
  ```python
  nested = [ [1, 2], [3, 4] ]
  nested[1][0]   # → 3
  ```
- Common quiz pattern: build `oscars_2022_2025 = [list2025, list2024, ...]`, then
  `oscars_2022_2025[1][0]` = element 0 of the 2024 list.

## 4. Tuples (Lecture 4)

```python
my_tuple = (32, 77, 19, 0, 14, 27)
my_tuple[4]          # indexing works the same as lists
```

- Tuples are **immutable** — can't change elements after creation
- Lists are **mutable** — `midterm_grades[i] = 73.2` works on lists, NOT on tuples

## 5. `.index` method (Lecture 4)

- `my_tuple.index(14)` → position of 14 in the tuple (first occurrence)
- Works on lists too: `student_ids.index("T-126")` → 5
- Use it to connect parallel lists/tuples:
  ```python
  student_index = student_ids.index("T-126")
  midterm_grades[student_index] = 73.2
  ```

## 6. Concatenation (Lecture 4)

- `+` combines lists, strings, tuples:
  ```python
  [winner] + runner_up      # list + list → list (wrap single item in [ ] first!)
  "Roxy" + " Music"         # string + string
  (1, 2) + (3,)             # tuple + tuple
  ```
- `[item] + list` puts `item` at element zero (used for "winner first" patterns)
- **Warning:** concatenation is NOT the same as nesting. `[a, b] + [c]` = flat list;
  don't confuse with putting a list inside another list.
- **Warning (aliasing):** `list_b = list_a` copies the *reference*, not the list —
  changing one changes "both". Use concatenation/slicing for an independent copy.

## 7. NumPy Arrays (Lecture 4)

```python
import numpy as np
arr = np.array([0, 10, 20, 30, 40])
```

- Element-by-element (vectorized) operations — NO loop needed:
  ```python
  temps_f = temps_c * (9/5) + 32        # every element transformed
  arr_a + arr_b                          # element-wise addition (same size required!)
  arr * 3                                # array + single number is fine (broadcasting)
  ```
- Compare two arrays → Boolean array (one True/False per element):
  ```python
  np.array([1, 2, 3]) > 2    # → array([False, False, True])
  ```
- Array vs single number comparison also works element-wise.

## 8. Math Constants & Functions

```python
import math
math.pi                 # 3.141592653589793 (NOT 3.14!)
math.sqrt(2)            # square root
import numpy as np
np.pi                   # same π, via numpy
np.sqrt(2 * np.pi)
np.exp(-x**2)           # e^(-x²) — element-wise on arrays
np.sin(t + 3)           # element-wise
np.mean(arr)            # average of the array
```

- Scientific notation: `1e-9` = 0.000000001 (single literal; `1e**-9` is a SyntaxError)
- `10**-9` also works (power operator)
- Integer division nuances: `1/3` → float; `**` is exponentiation

## 9. Plotting (Lectures 2 & 4)

Scatter plot (dots):
```python
import matplotlib.pyplot as plt
plt.scatter(x_vals, y_vals)
plt.xlabel("X label"); plt.ylabel("Y label"); plt.title("Title")
plt.show()                              # always finish with plt.show()
```

Line plot (curves/functions):
```python
x = np.linspace(-3, 3, 75)      # 75 evenly spaced points, endpoints included
y = np.exp(-x**2) / np.sqrt(2 * np.pi)   # vectorized formula
plt.plot(x, y)
plt.xlabel(...); plt.ylabel(...); plt.title(...)
plt.show()
```

- `np.linspace(start, stop, num)` — even spacing, endpoints included, args are plain numbers

### Linspace, slowly (your personal deep-dive)

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
2. **stop** — where it ends (included by default!)
3. **num** — HOW MANY points you want (count, not step size!)

```python
np.linspace(2, 4, 75)              # plain numbers work
np.linspace(2*np.pi, 4*np.pi, 75)  # math expressions work too (evaluated first!)
np.linspace(2, 4, 75) * np.pi      # alternative: generate 2→4, THEN scale (Solution 3 trick)
```

- `endpoint=True` is the default (stop value IS in the output); you rarely need to touch it
- Spacing between points = (stop − start) / (num − 1) — so with num=75, there are 74 gaps
- num is just "how many points" — more points = smoother curve, but the interval doesn't change
- If the interval involves π, you can write it inline (`2*np.pi`) or scale after (`np.linspace(2, 4, 75) * np.pi`) — both give the same result
- No parentheses-wrapping needed around args: `np.linspace((2*np.pi), (4*np.pi), 75)` works but the extra parens are pointless

The graphing recipe, every time (muscle memory):
```python
x = np.linspace(START, STOP, N)   # 1. domain → x values
y = <formula in x>                # 2. function → y values (vectorized, no loop)
plt.plot(x, y)                    # 3. draw the LINE through the points
plt.xlabel("...")                 # 4. label x-axis
plt.ylabel("...")                 # 5. label y-axis
plt.title("...")                  # 6. title
plt.show()                        # 7. display, suppress stray output
```

For composed functions f(g(t)): compute the INNER function first, store it,
then apply the OUTER formula to that result:
```python
t = np.linspace(A, B, 75)
inner = g(t)          # e.g. np.sin(t + 3)
y = f(inner)          # e.g. inner**2 - 5*inner + 2
plt.plot(t, y)        # x-axis is t (the input), NOT inner!
```
Key insight: after `y = f(inner)`, `y` is just an array of outputs — one per t.
Plot `t` vs `y` (input vs final output), skipping over the intermediate.
- Composed functions: evaluate inner first, then outer —
  ```python
  t = np.linspace(2*np.pi, 4*np.pi, 75)
  g = np.sin(t + 3)              # inner
  y = g**2 - 5*g + 2             # outer, applied to the result
  plt.plot(t, y)
  ```
- `plt.plot()` with no args draws nothing — pass x and y!

## 10. Data Frames (Lecture 2)

```python
import pandas as pd
df = pd.read_csv("data/features.csv")       # relative path, quotes matter
df.head()                                    # first 5 rows
df.shape                                     # (rows, columns)
df.columns                                   # column names (list-like)
df["mpg"].describe()                         # stats for ONE column (a Series)
df.describe()                                # stats for ALL numeric columns (different!)
df[features_of_interest[3]]                  # access column via list index (don't retype strings)
```

- If told to use a provided list of column names, index into it — count the position.
- "vs." convention: `"A" vs. "B"` means A on the **x-axis**, B on the **y-axis**.

## 11. Booleans & Comparisons (Lecture 5, I–II)

- `True` / `False` are Boolean objects (NOT the strings "True"/"False")
- Six comparison operators (all return a bool):
  `>` `<` `>=` `<=` `==` (equal) `!=` (not equal)
- `=` assigns; `==` compares. "x = 3" is assignment, "x == 3" is a question.
- Strings: `==` requires EXACT match (every character). `"Federal" == "federal"` → False
- Lists: `==` requires every element equal AND the same order

## 12. Floating-Point Equality (Lecture 5, II)

- `0.1 * 7 == 0.7` → **False** (rounding error, ~1e-16 discrepancy)
- Never use `==` for floats. Use a tolerance (epsilon):
  ```python
  epsilon = 1e-12            # solutions suggest 1e-12 to 1e-14 for this scale
  abs(x - y) < epsilon       # → True
  ```
- Choose epsilon: several orders bigger than the rounding noise (~1e-16),
  several orders smaller than differences you care about.
- Also: `math.isclose(x, y)` exists, but the quiz expects the `abs(x-y) < delta` form.

## 13. The `in` Keyword (Lecture 5, V)

Tests membership — works on strings, lists, tuples, NumPy arrays:

```python
"economic" in sentence        # substring search in a string (case-sensitive!)
"J" in ["June", "July"]       # EXACT match against each list element (False — no bare "J")
1 in np.array([1.0, 3.0])     # True — membership by element
"Biology" in majors           # exact element match in a list
```

Gotchas:
- `in` on a list means exact-match against elements (not substring of elements)
- `in` on a string means substring
- With floats in arrays, membership uses `==` internally → same float-equality trap
  (`0.1+0.1+0.1` vs `0.3`). Compare with tolerance instead.
- `2 in 22` → TypeError (left side must be a sequence); workaround: `str(2) in str(22)`

## 14. Quiz-Day Rituals (hard-won from practice quiz)

1. **Run ALL cells before submitting** (including ones you edit late) — graders check outputs
2. **Re-run after every edit** — an edited-but-unrun cell shows `exec=None`
3. `plt.show()` at the end of every plot — kills the `[<Line2D ...>]` text output
4. `print(...)` when instructions say "print to the screen" (a bare expression only displays)
5. When told not to type a string like "mpg": use the provided list — for data access
   AND for axis labels/titles (build labels with `+` concatenation or f-strings)
6. Describe on one column: `df[col].describe()`; on the whole frame: `df.describe()` — read carefully which is asked
7. Swap variables needs a temp: `temp = a; a = b; b = temp`
8. Epsilon range for near-1.0 comparisons: 1e-12 to 1e-14
9. Check `df.head()` output to confirm you read the right file/columns
10. `.index()` finds a position; use that position across parallel lists