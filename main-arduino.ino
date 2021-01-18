#include "DHT.h"
#include <SPI.h>  // gerekli kütüphanelerin dahil edilmesi
#include <SD.h>

float sicaklik=0.0;
const int chipSelect = 10; // microSd kart haberleşme pini

#define dhtPin 2 // dht pini

DHT dht(dhtPin, DHT11);  // dht tanımlanması
File myFile; // dosya nesnemiz

void setup()
{
  Serial.begin(9600);
  dht.begin(); // dht yi başlatıyoruz
  SD.begin(chipSelect); // microSd modülü başlatıyoruz
}
void loop()
{

  sicaklik = dht.readTemperature();  // sıcaklığı okuyoruz (C)
      

  Serial.print(sicaklik); //Celcius
  Serial.println();

  myFile = SD.open("olcum.txt",FILE_WRITE); // "! Daha önceden micro sd kartımızda oluşturuduğumuz olcum.txt !" adlı dosyayı yazmak için açıyoruz

  myFile.print(sicaklik);
  myFile.println();

  myFile.close(); 
  

  delay(1500); // ölçümler 1.5 s de bir alınıyor
}
