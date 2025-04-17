import random  # Für zufällige Auswahl von Zeichen
# Für vordefinierte Zeichengruppen (Buchstaben, Zahlen, Sonderzeichen)
import string

# Funktion zur Passwort-Generierung


def passwort_generieren(laenge, gross, klein, zahlen, sonder):
    zeichen = ""  # Leerer String, in den wir erlaubte Zeichen sammeln

    # Zeichenarten je nach Benutzereingabe hinzufügen
    if gross:
        zeichen += string.ascii_uppercase  # Großbuchstaben
    if klein:
        zeichen += string.ascii_lowercase  # Kleinbuchstaben
    if zahlen:
        zeichen += string.digits           # Ziffern 0–9
    if sonder:
        zeichen += string.punctuation      # Sonderzeichen wie !@#$%

    # Wenn keine Zeichenart gewählt wurde
    if not zeichen:
        return "❌ Keine Zeichenart ausgewählt!"

    # Passwort wird aus zufällig gewählten Zeichen der erlaubten Gruppe erstellt
    passwort = ''.join(random.choice(zeichen) for _ in range(laenge))
    return passwort


# 🧑‍💻 Benutzerinteraktion: Eingaben abfragen
länge = int(input("🔢 Wie lang soll das Passwort sein? "))

groß = input("🅰️ Großbuchstaben erlauben? (j/n): ").lower() == "j"
klein = input("🔡 Kleinbuchstaben erlauben? (j/n): ").lower() == "j"
zahlen = input("🔢 Zahlen erlauben? (j/n): ").lower() == "j"
sonder = input("🔣 Sonderzeichen erlauben? (j/n): ").lower() == "j"

# 🎯 Passwort erzeugen und anzeigen
ergebnis = passwort_generieren(länge, groß, klein, zahlen, sonder)
print(f"\n🔐 Dein generiertes Passwort: {ergebnis}")
