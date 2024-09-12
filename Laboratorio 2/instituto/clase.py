from typing import List
from .estudiante import devolver_materias

def estudiante_registrado_en_materia(nombre_estudiante: str, materia: str) -> bool:
    try:
        materias: List[str] = devolver_materias(nombre_estudiante)
        return materia in materias
    except ValueError as e:
        print(e)
        return False