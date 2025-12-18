/*
 * Copyright (C) 2025 Juan Pablo Sanchez EA5JTT
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2
 * as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 */
import serial
import time

# Abrimos la conexión con el puerto serial
# Windows
# arduino = serial.Serial('COM4', 9600)
# macOS
arduino = serial.Serial('/dev/tty.wchusbserial58741248741', 9600)
time.sleep(2)  # Esperamos a que se estabilice la conexión

print("Conexión establecida. Esperando datos...\n")

try:
    while True:
        if arduino.in_waiting > 0:
            linea = arduino.readline().decode('utf-8').strip()
            print(f"Recibido: {linea}")
except KeyboardInterrupt:
    print("\nFinalizando programa...")

finally:
    arduino.close()
    print("Puerto cerrado.")

