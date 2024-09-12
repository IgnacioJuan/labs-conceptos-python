from typing import Dict, List

estudiantes_materias: Dict[str, List[str]] = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"]
}

def devolver_materias(nombre_estudiante: str) -> List[str]:
    try:
        return estudiantes_materias[nombre_estudiante]
    except KeyError:
        raise ValueError(f"El estudiante {nombre_estudiante} no está registrado.")