"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel


def clean_campaign_data():
    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """

    return


if __name__ == "__main__":
    clean_campaign_data()

import glob
import os
import pandas as pd


def clean_campaign_data():
    os.makedirs("files/output", exist_ok=True)

    archivos_zip = glob.glob("files/input/*.csv.zip")
    dfs = [pd.read_csv(archivo, compression="zip") for archivo in archivos_zip]
    df = pd.concat(dfs, ignore_index=True)

    meses = {
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "may": "05",
        "jun": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12",
    }

    client = pd.DataFrame()
    client["client_id"] = df["client_id"]
    client["age"] = df["age"]
    client["job"] = df["job"].str.replace(".", "", regex=False).str.replace("-", "_", regex=False)
    client["marital"] = df["marital"]
    client["education"] = df["education"].str.replace(".", "_", regex=False).replace("unknown", pd.NA)
    client["credit_default"] = df["credit_default"].apply(lambda x: 1 if x == "yes" else 0)
    client["mortgage"] = df["mortgage"].apply(lambda x: 1 if x == "yes" else 0)

    campaign = pd.DataFrame()
    campaign["client_id"] = df["client_id"]
    campaign["number_contacts"] = df["number_contacts"]
    campaign["contact_duration"] = df["contact_duration"]
    campaign["previous_campaign_contacts"] = df["previous_campaign_contacts"]
    campaign["previous_outcome"] = df["previous_outcome"].apply(lambda x: 1 if x == "success" else 0)
    campaign["campaign_outcome"] = df["campaign_outcome"].apply(lambda x: 1 if x == "yes" else 0)

    dias_str = df["day"].astype(str).str.zfill(2)
    meses_str = df["month"].str.lower().map(meses)
    campaign["last_contact_date"] = "2022-" + meses_str + "-" + dias_str

    economics = pd.DataFrame()
    economics["client_id"] = df["client_id"]
    economics["cons_price_idx"] = df["cons_price_idx"]
    economics["euribor_three_months"] = df["euribor_three_months"]

    client.to_csv("files/output/client.csv", index=False)
    campaign.to_csv("files/output/campaign.csv", index=False)
    economics.to_csv("files/output/economics.csv", index=False)


if __name__ == "__main__":
    clean_campaign_data()