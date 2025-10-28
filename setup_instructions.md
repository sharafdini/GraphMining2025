# 🧰 Environment Setup Guide — Graph Mining (M.Sc. Data Science 2025)
Department of Mathematics, Persian Gulf University (PGU)

This document provides a **step-by-step guide** for installing all required software and libraries to run the course notebooks and code smoothly on Windows, Linux, or macOS.

---

## 1. Install Python or Conda

**Option A — Recommended:** [Anaconda](https://www.anaconda.com/download)  
**Option B:** [Python](https://www.python.org/downloads/) (≥ 3.9)

Check installation:
```bash
python --version
# or
conda --version
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/USERNAME/graph-mining-msc-2025.git
cd graph-mining-msc-2025
```

---

## 3. Create and Activate Environment

**Conda:**
```bash
conda env create -f environment.yml
conda activate graph-mining-msc-2025
```

**Pip:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open a notebook from `lectures/` or `assignments/`.

---

## 5. Verify Installation

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
nx.draw(G, with_labels=True)
plt.show()
```

✅ If the graph appears, the installation is correct.

---

## 6. Troubleshooting

- `ModuleNotFoundError`: Reinstall dependencies  
- Wrong Python version: Use Python ≥ 3.9  
- Torch-Geometric errors on Windows: install PyTorch first, then `torch-geometric`

---

## 🧑‍🏫 Instructor

**Reza Sharafdini**  
Department of Mathematics  
Persian Gulf University (PGU)  
📧 sharafdini@pgu.ac.ir
