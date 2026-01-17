from flask import Flask, render_template, request
from Bio import Entrez

# NCBI'a kimin istek gönderdiğini bildirmek için e-posta adresinizi belirtin
Entrez.email = "jules@example.com"

app = Flask(__name__)

def search_ncbi(organism, term):
    """
    Belirtilen organizma ve terim için NCBI'da arama yapar.
    Bir kayıt bulunursa True, aksi takdirde False döner.
    """
    try:
        query = f'"{organism}"[Organism] AND "{term}"'
        handle = Entrez.esearch(db="protein", term=query, retmax="1")
        record = Entrez.read(handle)
        handle.close()
        # Eğer 'Count' anahtarı varsa ve değeri 0'dan büyükse, kayıt var demektir.
        if "Count" in record and int(record["Count"]) > 0:
            return True
    except Exception as e:
        print(f"Hata: {e}")
    return False

@app.route('/')
def index():
    """Ana sayfayı gösterir."""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """
    Formdan gelen verileri işler, NCBI sorgusunu yapar
    ve sonuçları bir matris olarak gösterir.
    """
    organisms_raw = request.form.get('organisms', '')
    terms_raw = request.form.get('terms', '')

    # Boş satırları filtreleyerek listeleri oluştur
    organisms = [org.strip() for org in organisms_raw.splitlines() if org.strip()]
    terms = [term.strip() for term in terms_raw.splitlines() if term.strip()]
    
    # Sonuç matrisini oluştur
    results_matrix = []
    for org in organisms:
        row = [org]  # Satırın ilk elemanı organizma adı
        for term in terms:
            # Her bir organizma-terim çifti için arama yap ve sonucu ekle
            found = search_ncbi(org, term)
            row.append(found)
        results_matrix.append(row)

    return render_template('results.html', terms=terms, results=results_matrix)

if __name__ == '__main__':
    app.run(debug=True)
