# search.py

def mrv(assignment, csp):
    unassigned = [v for v in csp.variables if v not in assignment]
    return min(unassigned, key=lambda var: len(csp.domains[var]))


def forward_check(csp, var, value, assignment):
    """
    Non-destructive forward checking: verify that for each neighbor (or all other variables
    if no neighbors structure is provided) that is not yet assigned there is at least one
    value in its domain that is consistent with assignment U {var: value}.
    """
    temp_assignment = assignment.copy()
    temp_assignment[var] = value

    # Determine neighbors: prefer csp.neighbors if available, otherwise consider all other variables.
    if hasattr(csp, 'neighbors'):
        neighbors = csp.neighbors.get(var, [])
    else:
        neighbors = [v for v in csp.variables if v != var]

    for n in neighbors:
        if n in temp_assignment:
            continue
        has_support = False
        for val in csp.domains.get(n, []):
            if csp.consistent(n, val, temp_assignment):
                has_support = True
                break
        if not has_support:
            return False
    return True


def backtracking_search(csp):
    return backtrack({}, csp)


def backtrack(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment

    var = mrv(assignment, csp)

    for value in list(csp.domains[var]):
        if csp.consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment, csp)
            if result:
                return result
            assignment.pop(var)

    return None
def backtrack_fc(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment

    var = mrv(assignment, csp)

    for value in list(csp.domains[var]):
        if csp.consistent(var, value, assignment):
            assignment[var] = value
            # Hacer forward checking
            if forward_check(csp, var, value, assignment):
                result = backtrack_fc(assignment, csp)
                if result:
                    return result
            # Deshacer asignación y restaurar dominios
            assignment.pop(var)
            # Aquí deberías restaurar los dominios eliminados si implementas forward checking con eliminación permanente

    return None