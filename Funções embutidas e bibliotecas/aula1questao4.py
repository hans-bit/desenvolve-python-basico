from datetime import datetime

agora = datetime.now()

data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

print("Data e hora atuais:", data_formatada)
