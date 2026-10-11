# Uso: python img2c.py foto.png logo   ->  genera logo.h
from PIL import Image
import sys

#src, name = sys.argv[1], sys.argv[2]

#src, name = "gato1.png", "gato1"
#src, name = "gato2.png", "gato2"
#src, name = "itp.png", "itp"
#src, name = "st1.png", "st1"
#src, name = "hidalgo1.png", "hidalgo1"
#src, name = "carro1.png", "carro1"
#src, name = "carro2.png", "carro2"
#src, name = "tractor1.png", "tractor1"
src, name = "camion1.png", "camion1"



img = Image.open(src).convert("L")
img.thumbnail((128, 64))
canvas = Image.new("L", (128, 64), 0)
canvas.paste(img, ((128 - img.width) // 2, (64 - img.height) // 2))
bw = canvas.convert("1")

data = []
for y in range(64):
    for xb in range(16):
        b = 0
        for bit in range(8):
            if bw.getpixel((xb * 8 + bit, y)):
                b |= 0x80 >> bit
        data.append(b)

with open(f"{name}.h", "w") as f:
    f.write(f"#include <stdint.h>\nconst uint8_t {name}[{len(data)}] = {{\n")
    for i in range(0, len(data), 16):
        f.write("  " + ", ".join(f"0x{v:02X}" for v in data[i:i+16]) + ",\n")
    f.write("};\n")
