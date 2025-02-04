import gradio as gr
import pandas as pd

# URL pubblico del Google Sheet esportato in CSV
url = 'https://docs.google.com/spreadsheets/d/1Oh3nrbdWjKuh9twJsc9yJLppiJeD_BZyKgCTOxRkALM/export?format=csv'

# Funzione per caricare il CSV online
def get_data():
    try:
        return pd.read_csv(url)
    except Exception as e:
        return pd.DataFrame({"Errore": [str(e)]})  # Restituisce un errore visibile nella UI

# Creazione della UI con Gradio
with gr.Blocks() as demo:
    with gr.Tab("Classifica"):
        gr.Markdown("# 📊 Classifica degli LLM italiani")
        form_link = "https://forms.gle/Gc9Dfu52xSBhQPpAA"
        gr.Markdown(
            f"I modelli sono testati su SQuAD-it e ordinati per F1 Score e EM (Exact Match)."
            f"Si ringrazia il @galatolo per il codice dell'eval."
            f"Se volete aggiungere il vostro modello, compilate il form [qui]({form_link})."
        )

        # Carica la leaderboard da Google Sheets
        gr.DataFrame(get_data(), every=3600)

    with gr.Tab("Test della community"):
        gr.Markdown("# 🏆 Evaluation aggiuntive fatte dalla community")
        discord_link = "https://discord.com/invite/nfgaTG3H"
        gr.Markdown(
            f"@giux78 sta lavorando sull'integrazione di nuovi dataset di benchmark italiani. "
            f"Se volete contribuire anche voi, unitevi al [Discord della community]({discord_link})."
        )

        # Carica i dati con aggiornamento ogni ora
        gr.DataFrame(get_data(), every=3600)

# Lancia l'app Gradio
demo.launch()

