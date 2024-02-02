GigaDevice GD25Q16C 2MB Python memory driver for FT4222 USB to SPI bridge. Quad and Dual width demonstrated. Python module ft4222 is used.

![picture](https://github.com/charkster/GD25Q32C/blob/main/gd25q32c_pin_diagram.png)

Memory SO pin connects to FT4222 MISO pin. Memory SI pin connects to FT4222 MOSI pin. Memory CS pin connects to FT4222 SS0O. FT4222 SS pin needs to be tied high (VOUT3V3).
Memory QE bit in Status Register needs to be set high (this is a non-volitle write so it just needs to be done once) in order for WP and HOLD pins to become IO2 and IO3.

![picture](https://github.com/charkster/gd25q16c_ft4222/blob/main/umft4222ev-d_pinout.png)

