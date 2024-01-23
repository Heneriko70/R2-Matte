lån = 5000000  # Setter lånet til 5 millioner kroner
rente = 0.052  # Setter renten til 5.2%
antall_terminer = 20  # Setter antall år/terminer til 20
avdrag = lån / antall_terminer  # Regner ut avdraget du må betale per termin
print("Du må betale ", avdrag, " i terminbeløp hvert år")  # Printer ut terminbeløpet


print("Saldo Start   Avdrag   Rente  Restlån")  # Printer ut en overskrift
for i in range(antall_terminer):
    print(
        f"{i+1:2} {lån:9.0f} {avdrag:7.0f} {rente*lån:7.0f} {lån-avdrag:9.2f}"
    )  # Printer ut en tabell med saldo, avdrag, rente og restlån
    lån = lån - avdrag
