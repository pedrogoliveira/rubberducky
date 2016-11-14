/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "Arduino.h"

#define TESTPIN 13
#define INTERVAL 100

void setup()
{
  // initialize LED digital pin as an output.
  //pinMode(LED_BUILTIN, OUTPUT);
  pinMode(TESTPIN, OUTPUT);
}

void loop()
{
  // turn the LED on (HIGH is the voltage level)
  //digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(TESTPIN, HIGH);

  // wait for a second
  delay(INTERVAL);

  // turn the LED off by making the voltage LOW
  //digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(TESTPIN, LOW);

   // wait for a second
  delay(INTERVAL);
}
