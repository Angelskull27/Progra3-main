# csp.py

class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints

    def consistent(self, var, value, assignment):
        """Verifica si asignar 'value' a 'var' es válido."""
        for n in self.neighbors[var]:
            if n in assignment and not self.constraints(var, value, n, assignment[n]):
                return False
        return True
