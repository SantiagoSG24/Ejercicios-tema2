# Texto original
texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Separar el texto en partes usando el delimitador '#'
partes = texto_original.split('#')

# Formatear el texto
texto_formateado = partes[0].capitalize() + "...\n\n"
for parte in partes[1:]:
    texto_formateado += parte.capitalize() + ".\n"

# Mostrar el resultado
print(texto_formateado)