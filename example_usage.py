"""
Example usage of Ocular Dynamic Contour Tonometry (DCT) & Ocular Pulse Amplitude (OPA) Analysis.
Demonstrates normal pulsatile perfusion vs low OPA carotid insufficiency.
"""

from client import DynamicContourTonometryClient

def main():
    client = DynamicContourTonometryClient()

    print("=== Case 1: Healthy Physiological Pulsation ===")
    normal_case = client.evaluate_dct(
        iop_diastolic_mmhg=14.2,
        iop_systolic_mmhg=17.4,
        quality_score=1,
        heart_rate_bpm=70.0,
        eye_examined="OD"
    )
    print("Normal IOP & OPA:")
    print(f"  Diastolic IOP: {normal_case['dct_pressures_mmhg']['iop_diastolic_mmhg']} mmHg")
    print(f"  Systolic IOP:  {normal_case['dct_pressures_mmhg']['iop_systolic_mmhg']} mmHg")
    print(f"  OPA:           {normal_case['dct_pressures_mmhg']['ocular_pulse_amplitude_opa_mmhg']} mmHg")
    print(f"  Perfusion:     {normal_case['hemodynamic_assessment']['perfusion_state']}")

    print("\n=== Case 2: Ocular Ischemic Syndrome / Internal Carotid Stenosis ===")
    attenuated_case = client.evaluate_dct(
        iop_diastolic_mmhg=11.5,
        iop_systolic_mmhg=12.6,
        quality_score=2,
        heart_rate_bpm=74.0,
        eye_examined="OS"
    )
    print("Attenuated OPA:")
    print(f"  Diastolic IOP: {attenuated_case['dct_pressures_mmhg']['iop_diastolic_mmhg']} mmHg")
    print(f"  Systolic IOP:  {attenuated_case['dct_pressures_mmhg']['iop_systolic_mmhg']} mmHg")
    print(f"  OPA:           {attenuated_case['dct_pressures_mmhg']['ocular_pulse_amplitude_opa_mmhg']} mmHg")
    print(f"  Perfusion:     {attenuated_case['hemodynamic_assessment']['perfusion_state']}")
    print(f"  Clinical Risk: {attenuated_case['hemodynamic_assessment']['clinical_risk']}")

if __name__ == "__main__":
    main()
