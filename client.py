"""
Ocular Dynamic Contour Tonometry (DCT) & Ocular Pulse Amplitude (OPA) Client.
Zero-mock pure Python standard library implementation.
Calculates Ocular Pulse Amplitude (OPA = IOP_systolic - IOP_diastolic),
cornea-independent true IOP, and choroidal pulsatile perfusion status.
"""

import math
from typing import Dict, Any, Optional


class DynamicContourTonometryClient:
    """
    Evaluates corneal biomechanics-independent true IOP and choroidal pulsatile perfusion via Pascal DCT:
    - Concave tip matches corneal curvature, cancelling corneal bending forces (independent of CCT)
    - IOP_diastolic (mmHg): minimum baseline intraocular pressure
    - IOP_systolic (mmHg): peak systolic intraocular pressure
    - OPA (mmHg): IOP_systolic - IOP_diastolic (pulsatile ocular blood volume change)
    - Quality score Q (1 = best, 5 = uninterpretable)
    """

    def __init__(self):
        pass

    def evaluate_dct(
        self,
        iop_diastolic_mmhg: float,
        iop_systolic_mmhg: float,
        quality_score: Optional[int] = 1,
        heart_rate_bpm: Optional[float] = 72.0,
        eye_examined: Optional[str] = "OD"
    ) -> Dict[str, Any]:
        """
        Calculates DCT and OPA metrics.
        iop_diastolic_mmhg: trough diastolic IOP in mmHg (8.0 to 45.0 mmHg).
        iop_systolic_mmhg: peak systolic IOP in mmHg (10.0 to 50.0 mmHg).
        quality_score: 1 (optimal) to 5 (poor signal).
        """
        if iop_diastolic_mmhg <= 0 or iop_systolic_mmhg <= 0:
            raise ValueError("Intraocular pressure measurements must be strictly positive.")
        if iop_systolic_mmhg < iop_diastolic_mmhg:
            raise ValueError("Systolic IOP cannot be lower than diastolic IOP.")

        # Ocular Pulse Amplitude (OPA in mmHg)
        opa = iop_systolic_mmhg - iop_diastolic_mmhg

        # Mean Intraocular Pressure (mmHg)
        mean_iop = iop_diastolic_mmhg + (opa / 3.0)

        # Signal reliability based on Pascal DCT quality rating
        validity = "Reliable (Q1-Q2)" if quality_score in (1, 2) else "Questionable / Artifact (Q3-Q5)"

        # Clinical choroidal perfusion & glaucoma interpretation:
        # Normal OPA: 2.0 to 4.5 mmHg
        # Low OPA (< 1.8 mmHg): Ocular Ischemic Syndrome (OIS), carotid stenosis, low-tension glaucoma hypoperfusion
        # Elevated OPA (> 5.0 mmHg): Systemic hypertension, active high-tension glaucoma, ocular vascular engorgement
        if opa < 1.8:
            perfusion_state = "Attenuated Ocular Pulse Amplitude (Choroidal Hypoperfusion)"
            clinical_risk = "Reduced pulsatile ocular blood flow; investigate for internal carotid artery stenosis, ocular ischemic syndrome, or normal-tension glaucoma vascular dysregulation."
        elif opa > 4.8:
            perfusion_state = "Exaggerated Ocular Pulse Amplitude (Hyperdynamic Choroidal Pulsation)"
            clinical_risk = "Elevated stroke volume pulse or high-tension glaucoma vascular resistance; correlates with elevated cardiovascular pulse pressure."
        else:
            perfusion_state = "Normal Physiological Ocular Pulse Amplitude"
            clinical_risk = "Stable pulsatile choroidal hemodynamics with physiological ocular volume compliance."

        return {
            "status": "success",
            "dct_pressures_mmhg": {
                "iop_diastolic_mmhg": round(iop_diastolic_mmhg, 1),
                "iop_systolic_mmhg": round(iop_systolic_mmhg, 1),
                "mean_iop_mmhg": round(mean_iop, 1),
                "ocular_pulse_amplitude_opa_mmhg": round(opa, 2)
            },
            "signal_quality": {
                "quality_score_q": quality_score,
                "reliability_rating": validity,
                "heart_rate_bpm": heart_rate_bpm,
                "eye_examined": eye_examined
            },
            "hemodynamic_assessment": {
                "perfusion_state": perfusion_state,
                "clinical_risk": clinical_risk
            }
        }
