"""
MCP Server for Ocular Dynamic Contour Tonometry (DCT) & Ocular Pulse Amplitude (OPA) Analysis.
Exposes tools for clinical-grade ocular pulse amplitude and true IOP assessment.
"""

import json
from typing import Dict, Any, Optional
from client import DynamicContourTonometryClient


def handle_evaluate_dct(params: Dict[str, Any]) -> Dict[str, Any]:
    iop_diastolic_mmhg = float(params.get("iop_diastolic_mmhg", 14.5))
    iop_systolic_mmhg = float(params.get("iop_systolic_mmhg", 17.5))
    quality_score = int(params.get("quality_score", 1))
    heart_rate_bpm = float(params.get("heart_rate_bpm", 72.0))
    eye_examined = str(params.get("eye_examined", "OD"))

    client = DynamicContourTonometryClient()
    return client.evaluate_dct(
        iop_diastolic_mmhg=iop_diastolic_mmhg,
        iop_systolic_mmhg=iop_systolic_mmhg,
        quality_score=quality_score,
        heart_rate_bpm=heart_rate_bpm,
        eye_examined=eye_examined
    )


TOOLS = {
    "evaluate_dct": {
        "description": "Calculates Pascal Dynamic Contour Tonometry (DCT) corneal biomechanics-independent IOP, Ocular Pulse Amplitude (OPA), and choroidal perfusion index.",
        "parameters": {
            "type": "object",
            "properties": {
                "iop_diastolic_mmhg": {
                    "type": "number",
                    "description": "Baseline diastolic intraocular pressure in mmHg (e.g. 14.2)."
                },
                "iop_systolic_mmhg": {
                    "type": "number",
                    "description": "Peak systolic intraocular pressure in mmHg (e.g. 17.4)."
                },
                "quality_score": {
                    "type": "integer",
                    "description": "Signal quality rating score Q from 1 (optimal) to 5 (unreliable), default 1."
                },
                "heart_rate_bpm": {
                    "type": "number",
                    "description": "Synchronous ocular pulse heart rate in beats per minute, default 72.0."
                },
                "eye_examined": {
                    "type": "string",
                    "description": "Eye tested ('OD' or 'OS'), default 'OD'."
                }
            },
            "required": ["iop_diastolic_mmhg", "iop_systolic_mmhg"]
        },
        "handler": handle_evaluate_dct
    }
}


def process_request(request_str: str) -> str:
    try:
        req = json.loads(request_str)
        method = req.get("method")
        req_id = req.get("id")

        if method == "tools/list":
            tools_list = [
                {
                    "name": name,
                    "description": spec["description"],
                    "inputSchema": spec["parameters"]
                }
                for name, spec in TOOLS.items()
            ]
            return json.dumps({"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools_list}})

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            args = params.get("arguments", {})

            if tool_name not in TOOLS:
                return json.dumps({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Tool '{tool_name}' not found"}
                })

            result = TOOLS[tool_name]["handler"](args)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, indent=2)
                        }
                    ]
                }
            })

        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32600, "message": f"Unsupported method '{method}'"}
            })

    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })


if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        if line.strip():
            print(process_request(line))
            sys.stdout.flush()
