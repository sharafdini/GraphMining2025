# 📊 Graph Mining — M.Sc. Data Science (2025)

This repository contains the source codes used for teaching **Graph Mining** in **2025** in the **M.Sc. program of Data Science** at the **Department of Mathematics**, Persian Gulf University (PGU).

The course introduces both the **theoretical foundations** and **practical techniques** of graph mining, providing students with hands-on experience in analyzing, processing, and learning from complex network data.

---

## 🧠 Course Topics

- Graph Representation & Preprocessing
- Graph Metrics & Centrality Measures
- Spectral Graph Theory
- Graph Clustering & Community Detection
- Graph Embedding & Dimensionality Reduction
- Link Prediction & Anomaly Detection
- Applications of Graph Mining

---

## 📁 Repository Structure

```
├── lectures/           # Jupyter notebooks and slides used during lectures
├── assignments/        # Practical exercises and problem sets
├── datasets/           # Sample graph datasets (toy and real-world)
├── utils/              # Helper functions, visualization tools, and algorithms
├── projects/           # Student and research projects
├── requirements.txt    # Python dependencies
└── README.md           # Course documentation
```

---

## ⚙️ Installation Guide

```bash
git clone https://github.com/USERNAME/graph-mining-msc-2025.git
cd graph-mining-msc-2025
```

### Conda (Recommended)
```bash
conda env create -f environment.yml
conda activate graph-mining-msc-2025
```

### Pip (Alternative)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Launch Jupyter Notebook:
```bash
jupyter notebook
```

---

## 🧰 Example Usage

```python
import networkx as nx
G = nx.karate_club_graph()
nx.draw(G, with_labels=True)
```

---

## 🧑‍🏫 Instructor

**Reza Sharafdini**  
Department of Mathematics  
Persian Gulf University (PGU)  
📧 sharafdini@pgu.ac.ir

---

## 📄 License

This repository is provided for educational and research purposes. You may use, adapt, and redistribute the materials with proper attribution.
