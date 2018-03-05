# Sentence Similarity ID

Kemiripan kalimat bahasa Indonesia memanfaatkan korpus wordnet yang tersedia di Internet dan menggunakan metode chunk similarity yang diadopsi dari Paper `VRep` pada kompetisi SemEval 2016. Metode chunk similarity pada proses ini digunakan sebagai sentence similarity.

## Installation

1. Siapkan NTLK Python
2. Download WordNet Bahasa dari tautan dibawah (paling bawah)
3. Salin data WordNet tersebut ke struktur direktori ntlk sbb:
```
ntlk_data + tokenizer
          |
          + corpora -- + wordnet
          .            |
          .            + omw --- + msa
                       .         |
                       .         + ind <-- taruh disini
```
_note: jika folder corpora, wordnet, ind belum ada, silahkan buat sendiri manual_
4. Make a fun

## Usage

1. Pastikan nltk dengan wordnet bahasa dapat digunakan
2. Jalankan `python main.py`

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


## Credits

VRep at SemEval-2016 Task 1 and Task 2: A System for Interpretable Semantic Similarity

http://www.people.vcu.edu/~henryst/vrepAtSemeval2016.pdf

WordNet Bahasa

https://sourceforge.net/p/wn-msa/tab/HEAD/tree/trunk/

