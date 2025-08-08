
void setup() 
{
  Serial.begin(9600);
}

String line {""};

void loop() 
{
  while (Serial.available()) 
  {
    char inChar = Serial.read();
    if(inChar == '\n')
    {
      Serial.println("Received "+line);
      line = "";
    }
    else
    {
      line += inChar;
    }
  }
  delay(1);
}
