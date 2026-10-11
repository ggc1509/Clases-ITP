/**
 * Configuración SSD1306 para NUCLEO-F410RB
 * Bus: I2C1 (PB8 = SCL, PB9 = SDA), pantalla 128x64
 */
#ifndef __SSD1306_CONF_H__
#define __SSD1306_CONF_H__

#define STM32F4									// **

#define SSD1306_USE_I2C							// **
#define SSD1306_I2C_PORT        hi2c1			// **
#define SSD1306_I2C_ADDR        (0x3C << 1)   // prueba 0x3D si no responde

// Descomentar si la imagen sale girada o en negativo
// #define SSD1306_MIRROR_VERT
// #define SSD1306_MIRROR_HORIZ
// #define SSD1306_INVERSE_COLOR

#define SSD1306_INCLUDE_FONT_6x8
#define SSD1306_INCLUDE_FONT_7x10
#define SSD1306_INCLUDE_FONT_11x18
#define SSD1306_INCLUDE_FONT_16x26

#define SSD1306_WIDTH           128
#define SSD1306_HEIGHT          64

#endif /* __SSD1306_CONF_H__ */
