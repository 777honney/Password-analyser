# 🔐 Password Analyser

NOT FINISHHHHHHHHHHHHHHHHHHHHH

A small tool that analyses the strength of a password using four simple criteria. The project comes in **two versions**:

- a **console** version in Python (terminal);
- a **web** version in HTML + [PyScript](https://pyscript.net/), which runs Python directly in the browser, with no server required.

---

## ✨ Features

The analyser checks that the password meets the following criteria:

| Criterion | Condition |
|---|---|
| Length | At least **8 characters** |
| Numbers | At least **1 digit** (0-9) |
| Uppercase | At least **1 uppercase letter** (A-Z) |
| Lowercase | At least **1 lowercase letter** (a-z) |

For each criterion, a message tells you whether it is met. At the end, the program prints an overall verdict:

- **STRONG PASSWORD** if all 4 criteria are met;
- **WEAK PASSWORD** if at least one criterion is not met.

---

## 📁 Project structure

The project has two parts:

```
.
├── password_analyser.py   # Console version (Python)
├── index.html             # Web version (HTML + PyScript)
└── README.md
```

> Adjust the file names to match the ones you actually use.

---

## 🖥️ Console version (Python)

### Requirements

- Python 3.x installed on your machine.

### Run the program

```bash
python password_analyser.py
```

### Usage examples

```
Enter a password: Abc12345
Password length is sufficient.
Password contains at least one number.
Password contains at least one uppercase letter.
Password contains at least one lowercase letter.
STRONG PASSWORD: It meets all the criteria for a strong password.
```

```
Enter a password: abc
It is less than 8 characters long.
It does not contain any numbers.
It does not contain any uppercase letters.
Password contains at least one lowercase letter.
WEAK PASSWORD: It does not meet all the criteria for a strong password.
```

---

## 🌐 Web version (PyScript)

The web version uses the same analysis logic, but with a browser interface: a masked input field (`type="password"`), an **Analyze** button and a results area.

### Open the page

1. Open `index.html` in your browser.
2. Type a password in the input field.
3. Click **Analyze** to display the result.

> ⚠️ An internet connection is required on first load, since PyScript is loaded from the `pyscript.net` CDN.
> Depending on your browser, it may be better to serve the page through a small local server rather than opening the file directly:
>
> ```bash
> python -m http.server 8000
> ```
> then go to `http://localhost:8000`.

---

## ⚙️ How it works

Both versions rely on:

- three reference strings: `number`, `uppercase` and `lowercase`;
- the `any()` function combined with a generator expression to test whether **at least one character** of the password belongs to each category;
- `len(password)` to check the length;
- a final condition combining all the tests to decide whether the password is strong or weak.

Example of a test:

```python
if not any(char in number for char in password):
    print("It does not contain any numbers.")
```

In the web version, messages are first collected in a list (`messages`), then displayed all at once in the `<pre id="result">` element using `"\n".join(messages)`. The `@when("click", "#analyze")` decorator binds the Python function to the button click.

---

## 🔒 Privacy

- The password you enter is **neither stored nor sent** to any server: the analysis runs entirely locally (in the terminal or in the browser).


---

## ⚠️ Current limitations

- The tool only checks the password's **composition**, not its real-world strength (for example, `Password1` is considered "strong" even though it is very common).
- **Special characters** (`!@#$%`…) are not taken into account.
- There is no detection of common passwords, predictable patterns or character sequences.

---

## 🚀 Possible improvements

- Add a check for **special characters** (the `string` module is already imported in the code: `string.punctuation`).
- Display a **score** or strength meter (weak / medium / strong).
- Compare the password against a **list of common passwords**.
- Refactor the code into functions to avoid repeating the tests.
- Improve the web interface (colours, visual strength indicator).

---

## 🛠️ Technologies

- **Python 3**
- **HTML5**
- **[PyScript](https://pyscript.net/)** to run Python in the browser

---

## 📄 License

Project created for educational purposes. Free to use and modify.
