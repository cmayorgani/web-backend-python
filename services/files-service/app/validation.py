from typing import List, Dict
from .schemas import ValidationResult

def validate_rows(rows: List[Dict[str, str]]) -> List[ValidationResult]:
    results = []
    # Ejemplo de validaciones: vacíos, tipo incorrecto (Col2 numérico), duplicados en Col1
    empty_count = sum(1 for r in rows if not r.get("Col1") or not r.get("Col2") or not r.get("Col3"))
    results.append(ValidationResult(rule="Campos vacíos", status="OK" if empty_count==0 else "WARN", detail=f"{empty_count} filas con vacíos" if empty_count else None))

    type_errors = 0
    for r in rows:
        try:
            float(r.get("Col2"))
        except Exception:
            type_errors += 1
    results.append(ValidationResult(rule="Col2 numérico", status="OK" if type_errors==0 else "ERROR", detail=f"{type_errors} filas con tipo incorrecto" if type_errors else None))

    seen = set()
    dup = 0
    for r in rows:
        v = r.get("Col1")
        if v in seen:
            dup += 1
        else:
            seen.add(v)
    results.append(ValidationResult(rule="Duplicados en Col1", status="OK" if dup==0 else "WARN", detail=f"{dup} duplicados" if dup else None))

    return results
