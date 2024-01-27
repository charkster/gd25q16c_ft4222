from gd25q16c_ft4222 import gd25q16c_ft4222

spi_flash = gd25q16c_ft4222(debug=False)
print("Status Register Lower is 0x{:02x}".format(spi_flash.read_status_register_lower()))
print("Status Register Upper is 0x{:02x}".format(spi_flash.read_status_register_upper()))
#print("Set QE (Quad Enable) bit which sets HOLD pin to be IO3 and WP pin to be IO2")
#spi_flash.write_enable()
#spi_flash.write_status_register([0x00, 0x02])
print("Unique ID bytes are as follows:")
print(spi_flash.read_unique_id())
print("Identification bytes are as follows:")
print(spi_flash.read_identification())
print("Manufacturer Device ID bytes are as follows:")
print(spi_flash.manufacturer_device_id())
print("Erase entire device")
spi_flash.chip_erase(debug=True)

print(spi_flash.read_data(address=(0 * spi_flash.PAGE_size_addr), num_bytes=256)) # first page
print(spi_flash.read_data(address=((spi_flash.NUM_PAGES - 1) * spi_flash.PAGE_size_addr), num_bytes=256)) # last page

print("Program all pages to have sequential values (this should take 8192 * 0.6ms = 5 seconds, but takes longer??")
list_page_of_bytes = list(range(0, 256))
for pages in range(0,spi_flash.NUM_PAGES):
	spi_flash.program_page(address=(pages * spi_flash.PAGE_size_addr), page_bytes=list_page_of_bytes, debug=False)
	
print("Read first and last pages, single width")
print(spi_flash.read_data(address=(0 * spi_flash.PAGE_size_addr), num_bytes=256)) # first page
print(spi_flash.read_data(address=((spi_flash.NUM_PAGES - 1) * spi_flash.PAGE_size_addr), num_bytes=256)) # last page

print("Read first and last pages, quad width")
spi_flash.set_width('quad')
print(spi_flash.read_data(address=(0 * spi_flash.PAGE_size_addr), num_bytes=256)) # first page
print(spi_flash.read_data(address=((spi_flash.NUM_PAGES - 1) * spi_flash.PAGE_size_addr), num_bytes=256)) # last page

print("Read first and last pages, dual width")
spi_flash.set_width('dual')
print(spi_flash.read_data(address=(0 * spi_flash.PAGE_size_addr), num_bytes=256)) # first page
print(spi_flash.read_data(address=((spi_flash.NUM_PAGES - 1) * spi_flash.PAGE_size_addr), num_bytes=256)) # last page
