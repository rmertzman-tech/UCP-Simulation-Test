# UCP Ethical Simulation App (Flask Web Version)

This project provides a web-based interactive platform for exploring assumption-aware ethical simulations based on the **UCP v2.0 framework**. It enables users to model agents with distinct identity kernels and phenomenological reference frames (PRFs), and simulate ethical scenarios across diverse roles like instructor, researcher, or practitioner.

## 🌐 Features

- 🧠 **Agent-Centered Simulation** — Based on PRF and ITA roles
- 📊 Coherence Evaluation — Internal consistency tracking
- 📚 Classroom-Ready Modules — Trolley dilemma, whistleblower cases, paradigm shift walkthroughs
- 👥 Role-Based UI Adaptation — Instructor/researcher/practitioner mode
- 🌍 Narrative Logging — Ethical justifications over time
- ♿ Accessible Design — Screen-reader support and keyboard focus

---

## 🚀 Getting Started

### 1. Clone or Unzip
```bash
unzip UCP_Flask_WebApp.zip
cd UCP_Flask_WebApp
```

### 2. Create Python Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask
```

### 4. Run the App
```bash
python app.py
```

### 5. Open in Browser
Navigate to: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Classroom Use Cases

- Assign roles to students and simulate ethical case studies
- Let students modify agent PRFs and see coherence drift
- Run interactive debates or simulations with narrative feedback

## 📦 Folder Structure
```
UCP_Flask_WebApp/
├── app.py                  # Flask server
├── simulation_engine.py   # Simulation logic & agent model
├── templates/
│   └── index.html         # Main UI
├── static/
│   ├── style.css          # Stylesheet
│   └── app.js             # Client logic
└── README.md              # This guide
```

---

## 🤖 Authoring & Extending
- Add more modules or agent types in `simulation_engine.py`
- Update `index.html` or `app.js` to enhance UI/UX

---

## 📸 Screenshots
(You can paste screenshots here after running the app)

---

## 🧭 License
MIT or CC-BY-4.0 — Feel free to adapt for teaching, research, or development.

---

## 🙋 Need Help?
If you encounter bugs or want to extend the system, open an issue or start a discussion in the GitHub repository.
