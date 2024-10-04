from flask import Flask, render_template, request

app = Flask(__name__)

quiz_vragen = []
pogingen = []

def laad_bestand():
  """Leest de quiz vragen en slaat het op in quiz_vragen"""
  # OPDRACHT 1.2

@app.route("/")
def index():
  """Start pagina"""
  # Opdracht 2.1 & 2.2
  return render_template("index.html")

@app.route("/start")
def start():
  """Start de quiz met de beschikbaren vragen, geladen door laad_bestand"""
  # Opdracht 1.3
  return render_template("vragen.html", vragen_en_antwoorden=[['a','b','c'],['e','f','g'],['h','i','j']])

@app.route("/vragen")
def vragen():
  """Handige pagina om alle ingelezen vragen te zien"""
  return "DUMMY VOOR OPDRACHT 1.2"


@app.route("/verzend_antwoorden", methods=['POST'])
def verzend_antwoorden():
  """Pagina na inzenden antwoorden"""
  print(str(request.form))
  return "HI"

if __name__ == "__main__":
  app.run(debug=True)