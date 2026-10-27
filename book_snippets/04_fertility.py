import io, tarfile, urllib.request
from transformers import AutoTokenizer

# FLORES-200: the same 997 sentences in Uzbek and English (CC BY-SA 4.0).
# Simplified for print: raw text and s.split() words (the notebook normalizes ʻ/ʼ).
URL = "https://dl.fbaipublicfiles.com/nllb/flores200_dataset.tar.gz"
tar = tarfile.open(fileobj=io.BytesIO(urllib.request.urlopen(URL).read()))
def read(lang):
    data = tar.extractfile(f"./flores200_dataset/dev/{lang}.dev").read()
    return data.decode("utf-8").splitlines()
uz, en = read("uzn_Latn"), read("eng_Latn")

def n_tokens(tok, sentences):  # tokens without special tokens (BOS/EOS)
    return sum(len(tok(s, add_special_tokens=False).input_ids) for s in sentences)
def n_words(sentences):
    return sum(len(s.split()) for s in sentences)

for name in ["gpt2", "Qwen/Qwen2.5-0.5B", "xlm-roberta-base"]:
    tok = AutoTokenizer.from_pretrained(name)
    t_uz, t_en = n_tokens(tok, uz), n_tokens(tok, en)
    print(f"{name:18} fertility uz={t_uz / n_words(uz):.2f} en={t_en / n_words(en):.2f}"
          f"  parity={t_uz / t_en:.2f}")
