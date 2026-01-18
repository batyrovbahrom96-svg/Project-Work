Dynamic-Bridge-Analysis-OpenSeesPy

––––––––––––––––––––

Dynamic Bridge Analysis Using OpenSeesPy

Overview
This project presents a complete numerical framework for the static and dynamic analysis of a simply supported bridge subjected to moving vehicular loads using OpenSeesPy. The study focuses on midspan deflection response, modal characteristics, dynamic amplification, and the influence of vehicle speed.

The model is developed progressively from static reference analysis to full transient dynamic simulation with moving axle loads. The final output includes speed-dependent peak responses and the Dynamic Amplification Factor (DAF).

This repository is intended for academic and research use.

––––––––––––––––––––
Project Objectives

Develop a finite element beam model of a bridge using OpenSeesPy

Compute section properties and equivalent stiffness

Perform static load analysis for reference deflection

Perform modal analysis and extract natural frequencies

Implement moving truck loads in transient dynamic analysis

Investigate speed-dependent dynamic response

Compute Dynamic Amplification Factor (DAF)

Generate plots and tabulated results

––––––––––––––––––––
Folder Structure

src/
Contains all source codes used in the project.

beam_static.py
Basic static beam model

bridge_model.py
Core bridge finite element model

bridge_dynamic_base.py
Base dynamic analysis setup

section_properties.py
Section transformation and equivalent EI calculation

static_reference.py
Static reference deflection calculation

day6_check_modes.py
Modal analysis and Rayleigh damping calibration

moving_truck_dynamic_STABLE2.py
Final stable dynamic simulation with moving loads

speed_sweep_STABLE.py
Speed sweep driver for multiple vehicle velocities

daf_calculation.py
DAF computation from static and dynamic responses

results/
Contains numerical outputs and processed data.

daf_vs_speed_corrected.csv

daf_vs_speed_corrected.png

midspan_response.txt

midspan_deflection.png

plots/
Plotting utilities.

plot_daf.py

plot_daf_vs_speed.py

plot_results.py

––––––––––––––––––––
Requirements

This project uses Python and OpenSeesPy.

Install dependencies with:

pip install -r requirements.txt

Your requirements.txt should contain:

openseespy
numpy
matplotlib

––––––––––––––––––––
How to Run

Static reference deflection

python src/static_reference.py

Modal analysis

python src/day6_check_modes.py

Single-speed dynamic simulation

python src/moving_truck_dynamic_STABLE2.py 20

Speed sweep

python src/speed_sweep_STABLE.py

Plot DAF curve

python plots/plot_daf.py

––––––––––––––––––––
Methodology Summary

Bridge modeled as an Euler-Bernoulli beam

ElasticBeamColumn elements

Simply supported boundary conditions

Moving truck modeled using discrete axle forces

Newmark time integration

Rayleigh damping based on modal frequencies

Dynamic Amplification Factor defined as:

DAF = (Maximum Dynamic Deflection) / (Static Deflection)

––––––––––––––––––––
Key Outputs

Midspan deflection time histories

Peak dynamic deflection vs speed

DAF vs speed curve

Modal frequencies

Critical speed estimation

––––––––––––––––––––
Notes

All units are SI

Downward deflections are negative

Dynamic simulations are sensitive to time step size

Convergence criteria were tuned for stability

––––––––––––––––––––
Citation

If you use this work, please cite:

B. Batyrov, “Dynamic Bridge Analysis Using OpenSeesPy,” 2026.
