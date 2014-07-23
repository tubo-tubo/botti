
const int cdsPin = 0;


void setup() {
	// pinMode(pin, mode);
	Serial.begin(38400);
}

void loop() {
	int cds = analogRead(cdsPin);
	Serial.println(cds);
	if(cds > 450){
		int spd = 0;
		while(true){
			cds = analogRead(cdsPin);
			if(cds > 450){
				spd += 1;
			}else{
				break;
			}
			if(spd>=10){
				Serial.println("落ちろー");
				break;
			}
			Serial.print(cds);
			Serial.print(":");
			delay(80);
		}
	}
	delay(300);
}

