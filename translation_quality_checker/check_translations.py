import pandas as pd
from google.cloud import translate_v2 as translate

def translate_text(text, target_language="en"):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result["translatedText"]

def check_translations(file_path):
    df = pd.read_csv(file_path)
    df["Google_Translation"] = df["Original_Text"].apply(translate_text)
    df["Match"] = df["Google_Translation"] == df["Translated_Text"]

    mismatches = df[~df["Match"]]
    print(f"Found {len(mismatches)} mismatches.")
    mismatches.to_csv("mismatches.csv", index=False)

if __name__ == "__main__":
    check_translations("sample_translations.csv")
