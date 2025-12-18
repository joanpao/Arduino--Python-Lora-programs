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
//Libraries for OLED Display
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

void setup() {
  Serial.begin(9600);  // Inicializa la comunicación serial
  while (!Serial) {
    ; // Espera a que se abra el puerto serie (necesario para algunos Arduinos)
  }
  Serial.println("Arduino listo para recibir datos.");
}

void loop() {
  // Si hay datos disponibles desde el puerto serie (enviados por Python)
  if (Serial.available() > 0) {
    String recibido = Serial.readStringUntil('\n');  // Lee hasta nueva línea
    recibido.trim(); // Elimina espacios en blanco al inicio y final
    Serial.print("Mensaje recibido: ");
    Serial.println(recibido);  // Imprime el mensaje de vuelta
  }

  // Opcional: envía un mensaje cada cierto tiempo
  // delay(2000);
  // Serial.println("Hola desde Arduino");
}
