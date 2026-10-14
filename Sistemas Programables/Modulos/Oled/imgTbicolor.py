# img2c.py - Opción B: imagen de 128x48 para la zona azul
from PIL import Image

# ---- CONFIGURACIÓN (cambia solo estas líneas) ----
ARCHIVO = "st2.png"     # imagen de entrada (en la misma carpeta del script)
NOMBRE  = "st2_48"      # nombre del arreglo en C y del archivo .h
W, H    = 128, 48         # tamaño de la zona azul
INVERTIR = False          # True para generar la imagen en negativo
# --------------------------------------------------

img = Image.open(ARCHIVO).convert("L")
img.thumbnail((W, H))                                  # conserva proporción
canvas = Image.new("L", (W, H), 0)
canvas.paste(img, ((W - img.width) // 2, (H - img.height) // 2))
bw = canvas.convert("1")                               # dithering Floyd-Steinberg

bpr = (W + 7) // 8                                     # bytes por fila
data = []
for y in range(H):
    for xb in range(bpr):
        b = 0
        for bit in range(8):
            x = xb * 8 + bit
            if x < W:
                pixel = bool(bw.getpixel((x, y)))
                if pixel != INVERTIR:
                    b |= 0x80 >> bit
        data.append(b)

with open(f"{NOMBRE}.h", "w") as f:
    f.write(f"#include <stdint.h>\nconst uint8_t {NOMBRE}[{len(data)}] = {{\n")
    for i in range(0, len(data), 16):
        f.write("  " + ", ".join(f"0x{v:02X}" for v in data[i:i+16]) + ",\n")
    f.write("};\n")

print(f"Generado {NOMBRE}.h ({len(data)} bytes, {W}x{H})")