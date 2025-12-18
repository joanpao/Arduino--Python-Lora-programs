// LoRa32 TTGO OLED / Lilygo LoRa32 T3 V1.6.1 => ESP32 PICO-D4 
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

//OLED pins
#define OLED_SDA 21
#define OLED_SCL 22
#define OLED_RST 16
#define SCREEN_WIDTH 128  // OLED display width, in pixels
#define SCREEN_HEIGHT 64  // OLED display height, in pixels

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RST);


void setup() {
  Wire.begin(OLED_SDA, OLED_SCL);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3c, false, false);
  Serial.begin(9600);
  
  display.clearDisplay();
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.print("ESPERANDO DATOS ...  ");
  display.display();
}

void loop() {
  // Si hay datos disponibles desde el puerto serie (enviados por Python)
  if (Serial.available() > 0) {
    // Lee hasta nueva línea
    String recibido = Serial.readStringUntil('\n'); 
    // Elimina espacios en blanco al inicio y final 
    recibido.trim(); 
    // Display mensajes
    display.clearDisplay();
    display.setCursor(0, 15);
    display.print("Mensaje RX: ");
    display.display();
    display.setCursor(0,30);
    display.println(recibido);
    display.display();

  }


}
