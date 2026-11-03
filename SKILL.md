---
name: genpark-personal-agent-ocular-dynamic-contour-tonometry-opa-skill
version: 1.0.0
description: Calculates Pascal Dynamic Contour Tonometry (DCT) corneal biomechanics-independent IOP, Ocular Pulse Amplitude (OPA), and choroidal vascular compliance.
license: Apache-2.0
compatibility:
  python: ">=3.9"
  openclaw: ">=1.0.0"
  mcp: ">=1.0.0"
---

# Ocular Dynamic Contour Tonometry (DCT) & Ocular Pulse Amplitude (OPA) Skill

A zero-dependency personal agent skill for calculating corneal biomechanics-independent true intraocular pressure and choroidal pulsatile blood flow dynamics via Pascal Dynamic Contour Tonometry.

## Features
- **Corneal Thickness Independence**: Cancels corneal curvature bending resistance artifacts.
- **Ocular Pulse Amplitude (OPA)**: Computes peak systolic to trough diastolic ocular pulse pressure wave amplitude ($\Delta \text{IOP} = \text{IOP}_{\text{sys}} - \text{IOP}_{\text{dia}}$).
- **Choroidal Hemodynamic Evaluation**: Differentiates carotid insufficiency / ocular ischemic syndrome ($<1.8\text{ mmHg}$) from normal pulsation ($2.0-4.8\text{ mmHg}$) and hyperdynamic pulsation ($>4.8\text{ mmHg}$).
- **Signal Reliability Grading**: Validates Pascal DCT quality score ($Q1-Q5$).

## MCP Server Integration
Exposes `evaluate_dct` for autonomous glaucoma risk stratifications and ocular microvascular screening.
