#
# Copyright (C) 2025 Juan Pablo Sanchez EA5JTT
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
import serial
import time

# Conectamos al puerto serial
arduino = serial.Serial('/dev/tty.wchusbserial58741248741', 9600)
time.sleep(2)  # Esperamos que se estabilice la conexión

print("Conexión establecida. Escribe un mensaje para enviar al Arduino.")
print("Escribe 'salir' para terminar.\n")

try:
    while True:
        mensaje = input(">> ")
        if mensaje.lower() == 'salir':
            break
        arduino.write((mensaje + '\n').encode('utf-8'))  # Añade \n para que Arduino detecte el final
        print(f"Enviado: {mensaje}")
except KeyboardInterrupt:
    print("\nInterrupción del usuario.")

finally:
    arduino.close()
    print("Puerto cerrado.")

