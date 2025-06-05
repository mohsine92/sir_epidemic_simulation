# 🧬 SIR Epidemic Simulation (Python)

<p>This project is a simulation of a classic epidemiological model called SIR (Susceptible – Infected – Recovered) using Python. It demonstrates how an epidemic spreads through a closed population via a discrete mathematical model. The goal is to understand infection dynamics by translating scientific logic into code.</p>

![SIR_graphe](https://github.com/user-attachments/assets/6acfd613-b8db-4160-85b3-978e8b31f106)


## 🚀 Learning Objectives
- Implement a simple mathematical model (SIR) for simulation purposes  
- Use Python to structure and iterate dynamic systems  
- Visualize scientific data using Matplotlib  
- Apply programming tools to solve concrete scientific problems  

## 🧬 Brief Description of the Model
The SIR model divides a population into 3 states:

| Symbol | Meaning                         |
|--------|--------------------------------|
| S      | Susceptible (healthy individuals)  |
| I      | Infected individuals            |
| R      | Recovered or immune individuals |

Each day, individuals:

- Move from S → I at a transmission rate β (beta)  
- Move from I → R at a recovery rate γ (gamma)  

The model evolves in discrete time steps (using a Python loop), making it easy to understand and modify.

## 🛠️ Technical Stack
- Python 3.x  
- Matplotlib (for visualization)  
- (Optional) NumPy for vectorization and performance improvements  

## 🔭 Future Developments and Improvements

This project serves as a foundation to understand epidemiological modeling and numerical simulation. Several enhancements could make it more complete, interactive, and realistic:

- **Interactive Graphical Interface**  
  Add a simple interface (using Streamlit, Tkinter, or PyQt) to allow real-time modification of parameters like transmission rate, recovery rate, and initial population.

- **SEIR Model or Extensions**  
  Incorporate additional states such as “Exposed” (E) to simulate incubation periods, or more complex variants like vaccination or death rates.

- **Stochastic Simulation**  
  Replace the current deterministic model with a probabilistic simulation to better capture randomness in disease spread.

- **Real Data Integration**  
  Compare the simulation with real epidemiological data (e.g., publicly available COVID-19 datasets) to validate and calibrate the model.

- **Optimization and Vectorization**  
  Use NumPy to speed up calculations and simulate larger populations or longer durations.

- **Advanced Visualization**  
  Add interactive charts with Plotly, animations of the curves, or monitoring dashboards.

- **Documentation and Testing**  
  Implement unit tests and comprehensive code documentation to ease maintenance and future development.

These improvements help deepen scientific understanding while developing advanced technical skills.

## 📈 How to Run the Project

Clone the repository:

```bash
git clone https://github.com/mohsine92/sir_epidemic_simulation.git
cd sir_epidemic_simulation
pip install matplotlib
python3 main.py


