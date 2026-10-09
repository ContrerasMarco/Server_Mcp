from fastmcp import FastMCP #importamos la libreria de fastmcp

mcp = FastMCP("Calcula impuesto") #se crea la instancia del servidor mcp en offline

#creacion de las tool

@mcp.tool()

def calcular_impuesto(sueldo_bruto : int) -> str: #funcion para calcular el impuesto a pagar

    if sueldo_bruto <=943501:
        return(f"Tu sueldo de {sueldo_bruto} esta exento de impuesto")

    elif sueldo_bruto <= 2096670 :
        sueldo_total = sueldo_bruto - (sueldo_bruto * 0.020)
        return(f"tu sueldo total es de {sueldo_total} ya que tuviste que pagar 2.20 % de impuesto")
    elif sueldo_bruto <= 3494450 :
        sueldo_total =sueldo_bruto - (sueldo_bruto * 0.0452)
        return(f"tu sueldo total es de {sueldo_total} ya que tuviste que pagar 4.5 % de impuesto")
    elif sueldo_bruto <= 4892230 :
        sueldo_total =sueldo_bruto - (sueldo_bruto * 0.0709)
        return(f"tu sueldo total es de {sueldo_total} ya que tuviste que pagar 7.09 % de impuesto")
    elif sueldo_bruto <=6290010 :
        sueldo_total =sueldo_bruto - (sueldo_bruto * 0.1062)
        return(f"tu sueldo total es de {sueldo_total} ya que tuviste que pagar 10.62 % de impuesto")
    elif sueldo_bruto <=8386680 :
        sueldo_total =sueldo_bruto - (sueldo_bruto * 0.1557)
        return(f"tu sueldo total es de {sueldo_total} ya que tuviste que pagar 15.57 % de impuesto")   
    elif sueldo_bruto <=21665590 :
        sueldo_total =sueldo_bruto - (sueldo_bruto * 0.2748)
        return(f"tu sueldo total es de {sueldo_total} ya que tuviste que pagar 27.48 % de impuesto")        
    else :
        sueldo_total =sueldo_bruto - (sueldo_bruto * 0.35)
        return(f"tu sueldo total es de {sueldo_total} ya que tuviste que pagar 35 % de impuesto")        
        
@mcp.resource("config://politica-beneficios") 
              
def obtener_politica_beneficios() -> str: 
        
    """Devuelve el texto oficial sobre las políticas de beneficios de la empresa."""
    return ( 
         "POLÍTICA DE BENEFICIOS 2026:\n" 
         "1. Aguinaldo de fin de año equivalente a 1 mes de sueldo bruto.\n" 
         "2. Seguro médico privado cubierto al 100% para empleados con más de 1 año.\n" 
         "3. Límite máximo de bono de antigüedad: 25%."
    )

if __name__ == "__main__": 
    mcp.run()