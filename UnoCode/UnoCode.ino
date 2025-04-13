#include <Arduino.h>
const int BUTTON_PIN = 12;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(BUTTON_PIN) == LOW) { // Button pressed
    Serial.println("OPEN_YOUTUBE");     // Send a signal to the computer
    delay(1000); // Prevent multiple triggers
  }
}