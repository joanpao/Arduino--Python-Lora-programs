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

# Abrimos la conexión con el puerto serial
# Windows
# arduino = serial.Serial('COM4', 9600)
# macOS
# arduino = serial.Serial('/dev/tty.wchusbserialxxxxxxxx', 9600)
arduino = serial.Serial('/dev/tty.wchusbserial58741248741', 9600)
# Esperamos a que se estabilice la conexión
time.sleep(2)

print("Conexión establecida. Enviando datos...\n")

#Envia mensajes numerados indefinidamente

try:
    contador = 0
    while True:
        mensaje = f"Mensaje numero {contador}\n"
        # Enviamos el mensaje
        arduino.write(mensaje.encode('utf-8'))  
        print(f"Enviado: {mensaje.strip()}")
        # Incrementa el contador de mensajes
        contador += 1
        # Esperamos un segundo entre mensajes
        time.sleep(1)  
except KeyboardInterrupt:
    print("\nFinalizando programa...")

finally:
    arduino.close()
    print("Puerto cerrado.")


