# Ocular Dynamic Contour Tonometry (DCT) & Ocular Pulse Amplitude (OPA) Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard-green.svg)](https://modelcontextprotocol.io/)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)](requirements.txt)
[![Status: Production-Ready](https://img.shields.io/badge/status-production--ready-success.svg)](https://github.com/alphaparkinc)

A zero-dependency, mathematically rigorous personal agent skill that evaluates corneal biomechanics-independent true intraocular pressure (IOP) and pulsatile choroidal microvascular perfusion using Pascal Dynamic Contour Tonometry.

## Architecture

```mermaid
flowchart TD
    A[Pascal Contour Tip Sensor] --> B[Continuous IOP Waveform Tracking]
    B --> C[Trough Diastolic & Peak Systolic IOP Extraction]
    C --> D[Ocular Pulse Amplitude OPA = IOP_sys - IOP_dia]
    D --> E[Choroidal Perfusion & Carotid Stenosis Screening]
    E --> F[Personalized Glaucoma & Vascular Summary]
```

## Quick Start

```python
from client import DynamicContourTonometryClient

client = DynamicContourTonometryClient()
result = client.evaluate_dct(
    iop_diastolic_mmhg=14.2,
    iop_systolic_mmhg=17.4,
    quality_score=1
)
print("OPA (mmHg):", result["dct_pressures_mmhg"]["ocular_pulse_amplitude_opa_mmhg"])
print("Perfusion Status:", result["hemodynamic_assessment"]["perfusion_state"])
```

## License
Apache-2.0
