# Py\_Boil 🔥

A lightweight Python package that helps developers quickly bootstrap projects by generating ready-to-use boilerplate code. With **py\_boil**, you can scaffold Python applications in seconds — from simple scripts to full-featured project structures.

---

## 📋 Table of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Installing Dev Dependencies](#installing-dev-dependencies)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## 📖 About The Project

Stop wasting time setting up the same boilerplate code for every project. **py\_boil** takes care of scaffolding your Python application, letting you focus on writing actual business logic.

### Features

* 📦 Generate project scaffolds instantly
* ⚡ Ready-to-use templates (from Hello World to package structures)
* 🛠️ Customizable templates planned in future versions
* 🚀 Helps maintain consistency across projects

---

## 🏗️ Built With

* [Python 3.8+](https://www.python.org/)
* [uv](https://github.com/astral-sh/uv) for dependency management and reproducible environments

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8+ and [uv](https://github.com/astral-sh/uv) installed:

```bash
python3 --version
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

Install dependencies and create a virtual environment with `uv`:

```bash
uv sync
```

This will:

* Create a `.venv/` automatically
* Install dependencies listed in `pyproject.toml`
* Pin them exactly via a local `uv.lock` file

### Installing Dev Dependencies

To install optional or development packages (like testing or formatting tools):

```bash
uv sync --dev
```

This will install your main dependencies **plus** all packages listed under `[project.optional-dependencies.dev]` in your `pyproject.toml`.

---

## 📝 Usage

Generate a simple Hello World project:

```bash
uv run py_boil new hello-world
```

Example output (placeholder):

```text
project/
├── main.py
└── README.md
```

---

## 🗺️ Roadmap

* [x] Basic Hello World template
* [ ] Package scaffold with setup files
* [ ] CLI options for customization
* [ ] User-defined templates

See the [open issues](https://github.com/your-username/py_boil/issues) for a full list of proposed features (and known issues).

---

## 🤝 Contributing

We use [uv](https://github.com/astral-sh/uv) for dependency management. To set up the development environment:

```bash
uv sync --dev
```

To contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **Apache 2.0 License**. See `LICENSE` for more information.

---

## 📬 Contact

Delali Funani – [dfunani@gmail.com](mailto:dfunani@gmail.com)

Project Link: [https://github.com/dfunani/py_boiler](https://github.com/dfunani/py_boiler)
