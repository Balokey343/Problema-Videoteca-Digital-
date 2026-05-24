# =====================================================================
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema 4: Videoteca Digital
# =====================================================================

def contar_peliculas_recientes_y_populares(matriz_videoteca, umbral_calificacion, anio_limite):
    """
    Función que recorre la matriz de la videoteca y cuenta cuántos títulos
    cumplen simultáneamente con los criterios de calificación y año.
    """
    conteo = 0
    
    
    for pelicula in matriz_videoteca:
       
        anio = pelicula[1]
        calificacion = pelicula[2]
        
        
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            conteo += 1
            
    return conteo

def main():
   
    videoteca = [
        ["Inception", 2010, 8.8, "Ciencia Ficción"],
        ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
        ["Parasite", 2019, 8.5, "Drama"],
        ["Everything Everywhere All at Once", 2022, 8.0, "Acción"],
        ["Dune: Part Two", 2024, 8.9, "Ciencia Ficción"],
        ["The Matrix", 1999, 8.7, "Ciencia Ficción"],
        ["Gladiator", 2000, 8.5, "Acción"]
    ]
    
    print("--- BIENVENIDO A LA AUDITORÍA DE LA VIDEOTECA DIGITAL ---")
    
   
    umbral_calif = 8.5
    anio_minimo = 2015
    
    print(f"\nCriterios de búsqueda seleccionados:")
    print(f"- Calificación mayor o igual a: {umbral_calif}")
    print(f"- Año de lanzamiento posterior o igual a: {anio_minimo}")
    print("-" * 50)
    
 
    resultado_conteo = contar_peliculas_recientes_y_populares(videoteca, umbral_calif, anio_minimo)
    
   
    print(f"\n[RESULTADO] El conteo total de títulos que cumplen con ambos criterios es: {resultado_conteo}")
    print("\nPrograma finalizado con éxito.")


if __name__ == "__main__":
    main()