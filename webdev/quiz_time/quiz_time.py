from flask import Flask, render_template, request

app = Flask(__name__)

quiz_vragen = {}
HUIDIGE_POGING = 1 # variabele om aantal pogingen bij te houden
pogingen = {} # Lege Dictionary


def laad_bestand():
  """Leest de quiz vragen en slaat het op in quiz_vragen"""
  # OPDRACHT 1.2

@app.route("/")
def index():
  """Start pagina"""
  # Opdracht 2.1 & 2.2
  return render_template("index.html")

@app.route("/start", methods=['GET'])
def start():
  """Start de quiz met de beschikbaren vragen, geladen door laad_bestand"""
  # Opdracht 1.3
  return render_template("vragen.html", vragen_en_antwoorden=[['a','b','c'],['e','f','g'],['h','i','j']])

@app.route("/vragen", methods=['GET'])
def vragen():
  """Handige pagina om alle ingelezen vragen te zien"""
  return "DUMMY VOOR OPDRACHT 1.2"


@app.route("/antwoorden", methods=['POST'])
def antwoorden():
  """Pagina na inzenden antwoorden"""
  
  aantal_goed_en_fout = controleer_antwoorden()

  return f"Resultaten:\n goed: {aantal_goed_en_fout[0]}\t fout: {aantal_goed_en_fout[1]}"

def controleer_antwoorden():
  """Controleerd antwoorden (n_goed, n_fout)"""
  # huidige implementatie is een dummy, te implementeren in opdracht 3
  return 0, 0

if __name__ == "__main__":
  app.run(debug=True)