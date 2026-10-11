
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// I2C LCD address: try 0x3F if 0x27 doesn't work
LiquidCrystal_I2C lcd(0x27, 16, 2);

const int GREEN_LED = 2;
const int RED_LED   = 3;
const int BUZZER    = 4;

const unsigned long STARTUP_DELAY = 7000;

void setup() {
  Serial.begin(9600);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, LOW);
  noTone(BUZZER);

  // Initialize LCD
  lcd.init();
  lcd.backlight();
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("SmartAttend");

  lcd.setCursor(0, 1);
  lcd.print("Starting...");

  Serial.println("SYSTEM_STARTING");

  // Demo trigger after 7 seconds
  delay(STARTUP_DELAY);

  // Simulated attendance confirmation
  digitalWrite(GREEN_LED, HIGH);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("YOGI");

  lcd.setCursor(0, 1);
  lcd.print("PRESENT");

  tone(BUZZER, 1000);
  delay(1000);
  noTone(BUZZER);

  // Python will receive this message
  Serial.println("YOGI_PRESENT");
  Serial.println("Attendance event generated");
}

void loop() {
  // One-time demonstration.
  // RFID-triggered attendance will be implemented later.
}
