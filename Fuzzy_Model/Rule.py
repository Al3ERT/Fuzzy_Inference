class Rule:
    def __init__(self, antecedent,*consequences):
        self.antecedent = antecedent
        self.consequences = consequences
    
    def __str__(self):
        string = "" 
        for consequence in consequences:
            string += str(consequence) + ", "
        string = string[:2]
        return f'{self.antecedent} => {string}'