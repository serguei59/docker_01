FROM python:3.12-slim
#creation d un dossier app dans mon container et le definit comme repertoire de travail: là où s executent les commandes
WORKDIR /app
# je copie le code depuis le dossier où est mon dockerfile vers le dossier /app de mon container
COPY . /app
# execution du fichier
CMD ["python","main.py"]