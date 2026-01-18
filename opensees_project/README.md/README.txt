––––––––––––––––––––––
README.me
––––––––––––––––––––––

Dynamic Analysis of a Simply Supported Bridge Subjected to Moving Truck Loads Using OpenSeesPy
Abstract

This project presents a numerical investigation of the dynamic response of a simply supported bridge subjected to moving truck loads. The bridge is modeled using beam elements in OpenSeesPy. Both static and dynamic analyses are performed, and the Dynamic Amplification Factor (DAF) is evaluated over a range of vehicle speeds. The study includes modal analysis, Rayleigh damping calibration, moving load simulation, and speed sweep analysis to identify critical response characteristics.

Problem Description

Bridges subjected to moving vehicles experience dynamic effects that can significantly amplify structural responses compared to static loading. These effects depend on vehicle speed, axle spacing, structural stiffness, damping, and natural frequencies. This project aims to:

Compute static reference deflection

Simulate moving truck loads dynamically

Perform modal analysis

Calculate the Dynamic Amplification Factor (DAF)

Study the effect of vehicle speed on structural response

Methodology

Section Property Calculation

Composite section transformed using modular ratio

Equivalent EI computed

Static Analysis

Concentrated axle loads applied

Midspan deflection recorded

Modal Analysis

Natural frequencies extracted

Rayleigh damping coefficients calibrated

Dynamic Moving Load Analysis

Truck modeled as moving concentrated loads

Time-stepping integration

Peak midspan deflection extracted

Speed Sweep

Vehicle speeds from 2 m/s to 40 m/s

DAF calculated at each speed

Post-processing

CSV output

Automated plotting

Folder Structure
opensees_project/
│
├── LICENSE
├── README.md
├── requirements.txt
│
├── src/
│   ├── beam_static.py
│   ├── bridge_dynamic_base.py
│   ├── bridge_model.py
│   ├── daf_calculation.py
│   ├── day6_check_modes.py
│   ├── moving_truck_dynamic_STABLE2.py
│   ├── section_properties.py
│   ├── speed_sweep_STABLE.py
│   └── static_reference.py
│
├── results/
│   ├── daf_vs_speed_corrected.csv
│   ├── daf_vs_speed_corrected.png
│   ├── midspan_deflection.png
│   └── midspan_response.txt
│
└── plots/
    ├── plot_daf.py
    ├── plot_daf_vs_speed.py
    └── plot_results.py

Requirements

Install dependencies using:

pip install -r requirements.txt


Main dependencies:

openseespy

numpy

matplotlib

How to Run
1. Static Reference
python src/static_reference.py

2. Modal Analysis
python src/day6_check_modes.py

3. Single Speed Dynamic Run
python src/moving_truck_dynamic_STABLE2.py 20

4. Speed Sweep
python src/speed_sweep_STABLE.py

5. Plot Results
python plots/plot_daf.py

Outputs

Midspan time history

Peak deflections

DAF vs speed curves

CSV files for post-processing

Key Results

Static midspan deflection computed

Dynamic response varies strongly with speed

Maximum DAF occurs at low speeds

DAF decreases as speed increases for this system

No resonance observed within tested speed range

Figures

All figures are stored in the results/ folder.

Author

Bakhrom Botirov
Civil Engineering – Structural / Computational Mechanics