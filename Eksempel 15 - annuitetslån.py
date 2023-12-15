lån = 100000
rente = 0.03
annuitet = 15000
antall_terminer = 0

print("Saldo start   Avdrag   Rente  Restlån")
while lån > 0:  # Så lenge du har over 0 i lån kjører løkken
    start = lån  # Setter start til å være lik lån
    rentebeløp = lån * rente  # Regner ut rentebeløp ved å ta lånet ganget med renten
    avdrag = (
        annuitet - rentebeløp
    )  # Regner ut avdrag ved å ta annuitet minus rentebeløp
    lån = lån - avdrag  # Finner ut av hvor mye lån du nå har igjen
    print(
        f"{antall_terminer + 1:2}  {start:9.0f} {avdrag:7.0f} {rentebeløp: 7.0f} {lån:9.2f}"
    )
    antall_terminer = antall_terminer + 1
