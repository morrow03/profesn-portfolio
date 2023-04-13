Pro spuštění je potřeba mí nainstalovaný Python

			WINDOWS

Před spuštěním je potřeba konfigurace připojení
pro zjisteni ip adresy slouzi prikaz "ipconfig"
	soubor "config.json"
	ip -> 127.0.0.1 (ip adresa)
	port -> 65525 (povoleny ve skole)
	ip_start -> nejmensi adresa, kterou bude program vyhledavat 
	ip_konec -> nejvetsi adresa, kterou bude program vyhledavat
	port_start -> nejmensi port, ve kterem bude program vyhledavat
	port_konec -> nejvetsi port, ve kterem bude program vyhledavat

v prikazovem radku si najdeme slozku, ve ktere se nachazi dany soubor
po konfiguraci zadame do konzole "python main.py"

		---------------------
			LINUX

nunto spusit soubor "instalace.sh"
nutno nakonfigurovat (stejne jako ve Windows)
ve slozce /usr/local/bin/slovnik/config.json (cesta ke konfiguracnimu souboru)
pro zjisteni ip adresy slouzi prikaz "ip addr"
prikaz pro spusteni"sudo service slovnik start"