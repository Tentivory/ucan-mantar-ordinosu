#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UÇAN MANTAR ORDİNOSU SİMÜLATÖRÜ
===============================
Bu program, gökyüzünden ani bir şekilde inen mantar ordularına karşı
kahramanca (ama tamamen saçma) bir savunma simülasyonu sunar.

Uyarı: Bu kod bilimsel değildir. Sadece eğlence içindir.
Ama çalışır. Gerçekten.
"""

import random
import time
import sys

def mantar_saldiri():
    mantarlar = [
        "Dev Şapka Mantar",
        "Zehirli Mor Mantar",
        "Dans Eden Mantar",
        "Politikacı Gibi Konuşan Mantar",
        "Sonsuz Çoğalan Mantar",
        "Kahve Kokulu Mantar",
        "Uçan Tabure Mantar",
        "Gizli Ajanda Mantar"
    ]
    return random.choice(mantarlar)

def savas_mesaji():
    mesajlar = [
        "Mantarlar gökyüzünden yağıyor! Şemsiyeni aç!",
        "Bir mantar seninle felsefe tartışmaya başladı...",
        "Mantar ordusu geri çekildi, çünkü yağmur yağdı.",
        "Sen bir mantarı yendin! Ama o tekrar büyüdü.",
        "Mantarlar barış teklifi sundu: 'Bizi yeme, biz seni yemeyelim.'",
        "Kritik hasar! Mantarın şapkası uçtu!",
        "Mantarlar politik bir manifesto okuyor... kimse dinlemiyor."
    ]
    return random.choice(mesajlar)

def gizli_mesaj():
    # Bu tamamen rastgele bir string, hiçbir anlamı yok. Cidden.
    # Eğer bir şey arıyorsan, yanlış yerdesin.
    kod = "VGhpcyBpcyBub3QgcG9saXRpY2FsIGF0IGFsbC4gSnVzdCBhIGZ1bm55IHN0cmluZy4="
    return kod

def ana_simulasyon():
    print("=" * 50)
    print("  UÇAN MANTAR ORDİNOSU SİMÜLATÖRÜ v1.0")
    print("  (Gerçek bilimle alakası yoktur)")
    print("=" * 50)
    print()
    
    can = 100
    skor = 0
    
    print("Hazır mısın? Mantarlar geliyor...")
    time.sleep(1.5)
    
    for tur in range(1, 11):
        print(f"\n--- Tur {tur} ---")
        dusman = mantar_saldiri()
        print(f"Karşına çıkan: {dusman}")
        
        hasar = random.randint(5, 25)
        can -= hasar
        skor += random.randint(10, 50)
        
        print(savas_mesaji())
        print(f"Hasar aldın: -{hasar}  |  Kalan can: {can}  |  Skor: {skor}")
        
        if can <= 0:
            print("\nMantarlar seni yendi! Ama endişelenme, yeniden doğacaksın...")
            print("(Çünkü bu bir simülasyon ve mantarlar merhametlidir.)")
            break
        
        time.sleep(0.8)
    
    print("\n" + "=" * 50)
    print(f"Simülasyon bitti! Final skorun: {skor}")
    print("Mantarlar seni seviyor. Belki.")
    print("=" * 50)
    
    # Gizli kısım - kimse bakmasın
    if random.random() < 0.01:  # Neredeyse hiç çalışmaz
        print("\n[DEBUG] " + gizli_mesaj())

if __name__ == "__main__":
    try:
        ana_simulasyon()
    except KeyboardInterrupt:
        print("\n\nMantarlar senin kaçtığını gördü. Onlar üzülüyor.")
        sys.exit(0)
