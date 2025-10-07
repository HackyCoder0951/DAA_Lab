# 🧠 DAA_Lab
**Design and Analysis of Algorithms (DAA) – Python Implementations**

This repository contains a complete set of algorithm implementations written in **Python** for DAA laboratory and exam preparation.  
Each algorithm includes a **step-by-step explanation**, **pseudo code**, and **tested Python implementation** — matching standard DAA syllabi (Divide & Conquer, Greedy, Dynamic Programming, Backtracking, and Branch & Bound).

---

## 📘 Overview

| Unit | Category | Algorithms Included |
|------|-----------|---------------------|
| **UNIT I** | Algorithm Analysis | Algorithm basics, Time & Space complexity, Asymptotic notations |
| **UNIT II** | Divide & Conquer, Greedy, Traversal | Merge Sort, Quick Sort, Strassen’s Matrix Multiplication, Prim’s & Kruskal’s MST, Fractional Knapsack, BFS, DFS |
| **UNIT III** | Dynamic Programming, Backtracking, Branch & Bound | 0/1 Knapsack (DP), TSP (DP & Branch & Bound), N-Queens, Sum of Subsets |

---

## 🧩 Folder / File Structure

```
DAA_Lab/
│
├── 01_BinaryAndLinearSearchRec.py      # Linear and Binary Search
├── 02_QuickSortRec.py                  # Quick Sort (Recursive)
├── 03_MergeSort.py                     # Merge Sort (Divide & Conquer)
├── 04_StrassenMatrixMultiplication.py  # Strassen’s Algorithm
│
├── 05_PrimsMST.py                      # Prim’s Minimum Spanning Tree (Greedy)
├── 06_KruskalMST.py                    # Kruskal’s Minimum Spanning Tree (Greedy)
├── 07_FractionalKnapsack.py            # Fractional Knapsack Problem
│
├── 08_BFS.py                           # Breadth-First Search
├── 09_DFS.py                           # Depth-First Search
│
├── 10_Knapsack01_DP.py                 # 0/1 Knapsack using DP
├── 11_TSP_DP.py                        # Traveling Salesman Problem (DP)
│
├── 12_NQueenProblem.py                 # N-Queens using Backtracking
├── 13_SumOfSubsets.py                  # Sum of Subsets Problem (Backtracking)
├── 14_Knapsack_BranchAndBound.py       # 0/1 Knapsack using Branch & Bound
├── 15_TSP_BranchAndBound.py            # TSP using Branch & Bound
│
├── examples/                           # Example test cases (optional)
├── tests/                              # Unit tests (future scope)
└── README.md
```

---

## ⚙️ Requirements

- **Python 3.10+**  
- No external dependencies for core algorithms.  
- Optional (for testing and formatting):
  ```bash
  pip install pytest black ruff
  ```

---

## 🚀 How to Run

Each algorithm can be run individually:

```bash
# Example: Run Merge Sort
python 03_MergeSort.py
```

Many scripts include sample input/output blocks inside for quick testing.

---

## 💡 Example Output

**Quick Sort Example**

```
Input array: [10, 7, 8, 9, 1, 5]
Sorted array: [1, 5, 7, 8, 9, 10]
```

**Prim’s MST Example**

```
MST Edges:
0 - 1   Weight: 2
2 - 3   Weight: 4
Total cost of MST: 19
```

---

## 📈 Topics Covered

### 🧮 Divide and Conquer
- Binary Search  
- Merge Sort  
- Quick Sort  
- Strassen’s Matrix Multiplication

### 💰 Greedy Algorithms
- Prim’s Algorithm (MST)  
- Kruskal’s Algorithm (MST)  
- Fractional Knapsack Problem

### 🔍 Traversal Techniques
- BFS (Breadth-First Search)  
- DFS (Depth-First Search)

### 🧠 Dynamic Programming
- 0/1 Knapsack  
- Traveling Salesman Problem (TSP)

### 🧩 Backtracking
- N-Queens Problem  
- Sum of Subsets

### 🧭 Branch and Bound
- 0/1 Knapsack (B&B)
- Traveling Salesman Problem (B&B)

---

## 🧪 Future Improvements

- ✅ Add test cases using **pytest**
- ✅ Add Jupyter notebooks for visualization
- ✅ Add time complexity benchmark scripts
- ✅ Add interactive CLI input for all algorithms

---

## 🤝 Contributing

Contributions are welcome!

1. **Fork** this repository  
2. Create a new branch: `git checkout -b feature-new-algorithm`  
3. Commit changes: `git commit -m "Added Dijkstra’s algorithm"`  
4. Push to your branch: `git push origin feature-new-algorithm`  
5. Open a **Pull Request**

Please follow **PEP8 style** and include comments or docstrings for clarity.

---

## 📄 License

This project is licensed under the **MIT License** – free to use and modify with attribution.

---

## 👨‍💻 Author

**Hacky Coder**  
💼 GitHub: [HackyCoder0951](https://github.com/HackyCoder0951)  
📚 Project: *Design and Analysis of Algorithms in Python*  
📧 For academic use and open collaboration.

---

> “The best algorithm isn’t always the fastest — it’s the one that fits the problem elegantly.”