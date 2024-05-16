class KeyBoard:
    """
    KeyBoard Classe
    """

    def __init__(self, key, duration):
        self.key = key
        self.duration = duration
        """
        Class Constructor
        """
        
    def pressed(self):
        """
        Key pressed
        """
        print(f"A tecla pressionada foi {self.key} com duração de {self.duration} segundos")