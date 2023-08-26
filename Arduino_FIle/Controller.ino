int buttons[]={2,6,7,A0,3,4,5,8,A1};

void setup() {
  // put your setup code here, to run once:
  for (int i=0;i<=5;i++)
  {
    pinMode(buttons[i],INPUT);
  }
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i=digitalRead(buttons[0]);
  int j=digitalRead(buttons[1]);
  int z=digitalRead(buttons[2]);
  int g=analogRead(buttons[3]);
  int t=analogRead(buttons[8]);
  if(i==0)
  {
    Serial.println("A");
    delay(150);
  }
  if(j==0)
  {
    Serial.println("E");
    delay(250); 
  }
  if(z==0)
  {
    Serial.println("F");
    delay(250);
  }
  if(g>570)
  {
    Serial.println("+X");
    delay(250);
  }
  if(g<70)
  {
    Serial.println("-X");
    delay(250);
  }
  if(digitalRead(buttons[4])==0)
  {
    Serial.println("B");
    delay(150);  
  }
  if(digitalRead(buttons[5])==0)
  {
    Serial.println("C");
    delay(150);
  }
  if(digitalRead(buttons[6])==0)
  {
    Serial.println("D");
    delay(150);
  }
  if(digitalRead(buttons[7])==0)
  {
    Serial.println("K");
    delay(150);
  }
  if(t==0)
  {
    Serial.println("-Y");
    delay(250);
  }
  if(t>650)
  {
    Serial.println("+Y");
    delay(250);
  }
}
