# 🐍 Python Pool - 42 Next Curriculum

![Language](https://img.shields.io/badge/Language-Python_3-yellow)
![Standard](https://img.shields.io/badge/Style-PEP_8_/_Flake8_/_Mypy-blue)
![Curriculum](https://img.shields.io/badge/School-42_Madrid-black)

A structured collection of **Python 3** modules (`py00` through `py10`) completed as part of the **42 Madrid** curriculum. The repository covers core language fundamentals, data structures, object-oriented programming (OOP), exception handling, package architecture, design patterns, strict schema validation, and functional programming.

---

## 📚 Curriculum Modules Overview

| Module | Directory | Core Concepts Covered | Exercises |
| :--- | :--- | :--- | :--- |
| **Module 00** | [`./py00`](./py00) | Python syntax, built-in data types, control flow, functions, and basic I/O. | `ex0` – `ex7` |
| **Module 01** | [`./py01`](./py01) | Data structures (`list`, `tuple`, `dict`, `set`), comprehensions, and string manipulation. | `ex0` – `ex6` |
| **Module 02** | [`./py02`](./py02) | Object-Oriented Programming (OOP), classes, inheritance, encapsulation, and magic methods. | `ex0` – `ex4` |
| **Module 03** | [`./py03`](./py03) | Error and exception handling, file I/O, modules, packages, and decorators. | `ex0` – `ex6` |
| **Module 04** | [`./py04`](./py04) | Advanced data processing, stream management, and secure file operations. | `ex0` – `ex3` |
| **Module 05b** | [`./py05b`](./py05b) | Virtual environments (`venv`), dependency management (`pip`/`pyproject.toml`), `.env` secrets, package architecture (`__init__.py`), relative/absolute imports, and circular dependency resolution. | `ex0` – `ex1` + packages |
| **Module 06b** | [`./py06b`](./py06b) | Object-oriented design patterns: Factory pattern, Strategy pattern, capabilities, abstract interfaces, and polymorphic data pipelines. | `ex3` – `ex4` + systems |
| **Module 09** | [`./py09`](./py09) | Strict data validation, schema modeling, nested models, and custom field/model validators (`space_station`, `alien_contact`, `space_crew`). | `ex0` – `ex2` |
| **Module 10** | [`./py10`](./py10) | Functional programming: `lambda` expressions, higher-order functions, lexical closures, `functools` (`reduce`, `partial`, `lru_cache`, `singledispatch`), and custom decorators. | `ex0` – `ex4` |

---

## 🛠️ Technical Standards & Tools

- **Python Version:** Python 3.10+
- **Code Quality:** Adheres to **PEP 8** styling guidelines and strict static type-checking (`flake8` and `mypy --strict` compliant).
- **Environment:** Linux / WSL2

---

## 🚀 Usage

```bash
# Clone the repository
git clone git@github.com:ryskeman/Python-Pool-42Next.git
cd Python-Pool-42Next

# Run any specific exercise
python3 py00/ex0/ft_hello_garden.py
python3 py10/ex4/decorator_mastery.py
```
