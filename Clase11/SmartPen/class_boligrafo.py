class Boligrafo:
    def __init__(self, color: str, grosor_punta: str)->None:
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantidad_tinta = 80

    def escribir(self, texto: str)->str:
        """Esta funcion recibe como parametros una texto en string que seria el texto que uno escribe

        Argumentos:
            texto (str): Es un texto ya predefinido

        Retorno:
            str: Retorna una string que seria el mensaje
        """
        longitud_caracteres = len(texto)
        cadena = "No alcanza la tinta"

        if longitud_caracteres <= self.cantidad_tinta:
            self.cantidad_tinta -= longitud_caracteres
            cadena = texto

        return cadena
    
    def recargar(self, cantidad_tinta: int)->str:
        """Esta funcion recibe como parametros un numero entero que es representado como la cantidad de tinta

        Argumentos:
            cantidad_tinta (int): Un numero entero ya predefinido

        Retorna:
            str: retorna una string
        """
        self.cantidad_tinta + cantidad_tinta
        sobrante = self.cantidad_tinta - self.capacidad_tinta_maxima
        cadena = f"Se recargó la lapicera y sobró {sobrante} cantidad de tinta"

        if self.cantidad_tinta <= self.capacidad_tinta_maxima:
            cadena = "Lapicera Recargada"
        else:
            self.cantidad_tinta = self.capacidad_tinta_maxima

        return cadena
    