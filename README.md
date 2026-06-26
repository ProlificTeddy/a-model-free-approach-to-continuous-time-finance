# A Model-Free Approach to Continuous-Time Finance

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/downloads/)
[![arXiv](https://img.shields.io/badge/arXiv-2211.15531v1-b31b1b.svg)](https://arxiv.org/pdf/2211.15531v1)

This repository contains a Python implementation of the concepts and methods presented in the research paper **[A Model-Free Approach to Continuous-Time Finance](https://arxiv.org/pdf/2211.15531v1)** by Henry Chiu and Rama Cont. The paper introduces a novel, pathwise, and model-free framework for continuous-time finance using causal functional calculus. This approach eliminates the reliance on probabilistic assumptions, offering a robust foundation for financial modeling, hedging, and pricing in a deterministic setting.

---

## 📜 Overview of the Paper

The paper proposes a **non-probabilistic, pathwise framework** for continuous-time finance, which departs from traditional stochastic calculus-based methods. The key contributions of the paper include:

1. **Self-Financing Portfolios**: 
   - A new definition of self-financing portfolios that does not rely on stochastic integration.
   - Demonstration that the value of a self-financing portfolio can be expressed as a pathwise integral.

2. **Arbitrage-Free Framework**:
   - The domain of the proposed functional calculus is inherently arbitrage-free, ensuring consistency in financial modeling.

3. **Path-Dependent Hedging**:
   - Formulation of the hedging problem for path-dependent payoffs across a generic set of scenarios.
   - Application of Isaacs' transition principle from differential games to derive a verification theorem for the optimal hedging solution.

4. **Asian Option Pricing**:
   - Explicit solutions for the pricing and hedging of Asian options using the proposed framework.

This implementation focuses on the **pathwise integral for self-financing portfolios** and the **hedging of path-dependent payoffs**, with a specific example for **Asian options**.

---

## ⚙️ How It Works

### 1. **Pathwise Integral for Self-Financing Portfolios**
The paper defines a self-financing portfolio as one where the change in portfolio value is entirely determined by the trading strategy and the price path of the underlying asset. The pathwise integral is computed as:
\[
V_t = V_0 + \int_0^t \phi_u \, dS_u
\]
where \( V_t \) is the portfolio value, \( \phi_u \) is the trading strategy, and \( S_u \) is the price path of the underlying asset.

This implementation uses **finite differences** to approximate the pathwise integral, avoiding the need for stochastic integration.

---

### 2. **Path-Dependent Hedging for Asian Options**
The Asian option payoff depends on the average price of the underlying asset over a specified period:
\[
\text{Payoff} = \max\left(0, \frac{1}{T} \int_0^T S_t \, dt - K\right)
\]
where \( K \) is the strike price and \( T \) is the maturity.

The hedging strategy is derived by solving a **fully non-linear path-dependent equation** using numerical methods. The implementation includes:
- Simulation of price paths for the underlying asset.
- Calculation of the Asian option payoff.
- Optimization of the hedging strategy using the principles outlined in the paper.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Required Python libraries:
  - `numpy`
  - `scipy`
  - `matplotlib`

You can install the dependencies using pip:
```bash
pip install numpy scipy matplotlib
```

---

### Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/model-free-finance.git
cd model-free-finance
```

---

### Usage

The core implementation is provided in the `implementation.py` script. Below are the steps to run the script:

#### 1. **Simulating Price Paths**
To simulate price paths for the underlying asset:
```bash
python implementation.py --simulate-paths --num-paths 1000 --time-horizon 1 --time-steps 100
```
- `--num-paths`: Number of simulated price paths.
- `--time-horizon`: Total time horizon (e.g., 1 year).
- `--time-steps`: Number of time steps in the simulation.

#### 2. **Asian Option Pricing**
To calculate the price of an Asian option:
```bash
python implementation.py --price-asian-option --strike-price 100 --time-horizon 1 --num-paths 1000 --time-steps 100
```
- `--strike-price`: Strike price of the Asian option.
- `--time-horizon`: Maturity of the option.
- `--num-paths`: Number of simulated price paths.
- `--time-steps`: Number of time steps in the simulation.

#### 3. **Hedging Strategy Optimization**
To compute the optimal hedging strategy for a path-dependent payoff:
```bash
python implementation.py --hedge --strike-price 100 --time-horizon 1 --num-paths 1000 --time-steps 100
```
- `--strike-price`: Strike price of the Asian option.
- `--time-horizon`: Maturity of the option.
- `--num-paths`: Number of simulated price paths.
- `--time-steps`: Number of time steps in the simulation.

#### 4. **Visualizing Results**
The script generates visualizations of:
- Simulated price paths.
- Asian option payoff distribution.
- Hedging performance.

The plots are saved in the `output/` directory.

---

## 📊 Example Output

### Simulated Price Paths
![Simulated Price Paths](output/simulated_paths.png)

### Asian Option Payoff Distribution
![Asian Option Payoff](output/asian_option_payoff.png)

### Hedging Strategy Performance
![Hedging Performance](output/hedging_performance.png)

---

## 📚 References
- Henry Chiu, Rama Cont. *A Model-Free Approach to Continuous-Time Finance*. [arXiv:2211.15531v1](https://arxiv.org/pdf/2211.15531v1).

---

## 🛠️ Contributing
Contributions are welcome! If you'd like to improve this implementation or add new features, feel free to fork the repository and submit a pull request.

---

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.