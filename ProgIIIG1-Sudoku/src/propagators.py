# propagators.py
# Implementación de los propagadores MAC, FC y AC3 compatibles
# con un CSP basado en diccionarios.

from collections import deque


# ============================================================
#                 AC-3 (Arc Consistency 3)
# ============================================================

def ac3(csp):
    """
    AC-3 para un CSP basado en un diccionario:
    csp = {
        "variables": [...],
        "domains": {var: [lista de valores]},
        "neighbors": {var: set(...)}
        "constraint": (función binaria)
    }
    """
    queue = deque([(Xi, Xj) for Xi in csp["variables"] for Xj in csp["neighbors"][Xi]])

    while queue:
        Xi, Xj = queue.popleft()
        if revise(csp, Xi, Xj):
            if len(csp["domains"][Xi]) == 0:
                return False  # dominio vacío → sin solución
            for Xk in csp["neighbors"][Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))

    return True


def revise(csp, Xi, Xj):
    """
    Revisa el arco (Xi, Xj)
    Elimina valores del dominio de Xi que no tengan soporte en Xj.
    Devuelve True si se removió algo.
    """
    revised = False
    domXi = csp["domains"][Xi]
    domXj = csp["domains"][Xj]

    to_remove = []

    for x in domXi:
        # Debe existir un valor y en Xj que satisfaga la restricción
        if not any(csp["constraint"](Xi, x, Xj, y) for y in domXj):
            to_remove.append(x)

    if to_remove:
        for x in to_remove:
            domXi.remove(x)
        revised = True

    return revised



# ============================================================
#              Forward Checking (opcional)
# ============================================================

def forward_checking(csp, Xi, value, assignment):
    """
    Aplica forward checking después de asignar Xi = value.
    Devuelve True si no hay conflicto.
    """
    for Xj in csp["neighbors"][Xi]:
        if Xj not in assignment:
            for v in csp["domains"][Xj][:]:
                if not csp["constraint"](Xi, value, Xj, v):
                    csp["domains"][Xj].remove(v)
            if not csp["domains"][Xj]:
                return False
    return True



# ============================================================
#         MAC (Maintaining Arc Consistency) opcional
# ============================================================

def mac(csp, Xi, assignment):
    """
    Mantiene consistencia de arcos MAC después de una asignación.
    """
    queue = deque([(Xk, Xi) for Xk in csp["neighbors"][Xi]])

    while queue:
        Xk, Xvar = queue.popleft()
        if revise(csp, Xk, Xvar):
            if not csp["domains"][Xk]:
                return False
            for Xj in csp["neighbors"][Xk]:
                if Xj not in assignment:
                    queue.append((Xj, Xk))

    return True
