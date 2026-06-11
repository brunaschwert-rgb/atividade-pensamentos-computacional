#include <WiFi.h>
#include "time.h"

// --- Configurações do Wi-Fi ---
const char* ssid       = "NOME_DA_SUA_REDE_WIFI";
const char* password   = "SENHA_DO_SEU_WIFI";

// --- Configurações de Fuso Horário (NTP) ---
// GMT -3 (Brasília): -3 horas * 3600 segundos = -10800
const long  gmtOffset_sec = -10800; 
const int   daylightOffset_sec = 0; // 0 porque o Brasil não tem mais horário de verão
const char* ntpServer = "a.st1.ntp.br"; // Servidor oficial do Brasil

void setup() {
  Serial.begin(115200);

  // Conectando ao Wi-Fi
  Serial.printf("Conectando a rede: %s \n", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi Conectado!");

  // Inicializa e configura a busca do horário oficial via NTP
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
}

void loop() {
  delay(1000);
  imprimirHorarioLocal();
}

// Função para ler o horário interno atualizado e exibir no Monitor Serial
void imprimirHorarioLocal() {
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Erro ao obter o horário.");
    return;
  }
  
  // Exibe no formato: Hora:Minuto:Segundo
  Serial.printf("Horário Atual: %02d:%02d:%02d\n", 
                timeinfo.tm_hour, 
                timeinfo.tm_min, 
                timeinfo.tm_sec);
                
  // DICA: Substitua o Serial.printf acima pelo código de envio 
  // de dados para o modelo específico do seu display digital (Ex: TM1637 ou OLED)
}
