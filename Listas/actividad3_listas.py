# 🎯 Actividad 3: Gestión de Lista de Reproducción Musical

# Crear lista de canciones
canciones = ["Song A", "Song B", "Song C", "Song D", "Song E"]

# Agregar una canción al final de la lista
canciones.append("Song F")
print("Después de append:", canciones, "\n")

# Insertar una canción en la segunda posición
canciones.insert(1, "Song G")
print("Después de insert:", canciones, "\n")

# Agregar varias canciones usando extend()
canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("Después de extend:", canciones, "\n")

# Eliminar una canción por su nombre
canciones.remove("Song C")
print("Después de remove:", canciones, "\n")

# Eliminar la última canción de la lista
ultima_cancion = canciones.pop()
print("Después de pop:", canciones, "\n")

# Mostrar la canción eliminada
print("Canción eliminada:", ultima_cancion)

# Ordenar la lista alfabéticamente
canciones.sort()
print("Después de sort:", canciones, "\n")

# Mostrar cantidad de canciones
print("Cantidad de canciones en la playlist:", len(canciones))

# Mostrar posición de una canción
print("Posición de la primera canción agregada (Song F):", canciones.index("Song F"))

# Contar cuántas veces aparece un elemento
print("Cantidad de veces que aparece 'Bonus Track 1':", canciones.count("Bonus Track 1"))
