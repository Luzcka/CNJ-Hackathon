"""
Create final base

@date Oct 16, 2020
@author Inova Ixtepô
"""

import glob
import io
import json
import random
import time

import numpy as np
import pandas as pd
import tqdm

# Make sure the TRTs data are inside this folder
from tinydb import TinyDB

from utils.path_constants import CNPJ_DATABASE_PATH, CNJ_DATABASE_PATH, PROCESSED_DATABASE_PATH, SERVENTIAS_PATH, TINY_DB_PATH
from utils.values_constants import Status, REAL_CNPJS, CLASSES_CONHECIMENTO, CLASSES_EXECUCAO


def generate_hq_cnpj(punctuation=False):
    """
    Generate Head Quartes CNPJ:

    Base on code from: https://wiki.python.org.br/GeradorDeCnpj

    :param punctuation: Whether or not to have punctuations
    :return: CNPJ in str format
    """

    n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
    n = get_check_digits(n)

    if punctuation:
        return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)
    else:
        return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)


def get_check_digits(n):
    v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
    # calcula dígito 1 e acrescenta ao total
    s = sum(x * y for x, y in zip(reversed(n), v))
    d1 = 11 - s % 11
    if d1 >= 10:
        d1 = 0
    n.append(d1)
    # idem para o dígito 2
    s = sum(x * y for x, y in zip(reversed(n), v))
    d2 = 11 - s % 11
    if d2 >= 10:
        d2 = 0
    n.append(d2)

    return n


def generate_branchs_cnpjs(hq_cnpj, num_branchs, punctuation=False):
    """
    Returns a list of branch CNPJ base on HQ

    :param   hq_cnpj:     CNPJ for Head Quarters
    :param   num_branchs: # of CNPJ for branchs to generate

    :return: List of branchs CNPJs
    """

    list_branchs_cnpj = list()

    for branch_i in range(2, num_branchs + 2):

        n = [int(d) for d in hq_cnpj[0:8]] + [int(d) for d in str(branch_i).zfill(4)]

        n = get_check_digits(n)

        if punctuation:
            list_branchs_cnpj.append("%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n))
        else:
            list_branchs_cnpj.append("%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n))

    return list_branchs_cnpj


def create_list_of_cnpj(number_cnpjs, max_filiais=5):
    print("Generating %d CNPJs" % number_cnpjs)

    output_path = CNPJ_DATABASE_PATH

    # List of generated CNPJs, where:
    # Pos 0: CNPJ
    # Pos 1: CNPJ for HQ, which is None when Pos 0 is an HQ.
    df_cnpj_database = pd.DataFrame(columns=["cnpj", "cnpj_hq"])

    hq_i = 0
    avg_branchs = 0
    hqs = 0

    pbar = tqdm.tqdm(total=number_cnpjs)
    while hq_i < number_cnpjs - len(REAL_CNPJS):
        list_cnpj = list()

        # Randomly generates branch count for this CNPJ
        rand_branchs = random.random() ** 50
        num_branchs = round(rand_branchs * max_filiais)

        hq_i += num_branchs + 1
        pbar.update(num_branchs + 1)

        avg_branchs += num_branchs
        hqs += 1
        # Generate random Head Quarters CNPJ
        hq_cnpj = generate_hq_cnpj(punctuation=False)

        list_cnpj.append([hq_cnpj, None])

        # Generate random Branch CNPJ based on HQ
        branchs_cnpjs = generate_branchs_cnpjs(hq_cnpj, num_branchs)
        list_cnpj.extend([[branch_cnpj, hq_cnpj] for branch_cnpj in branchs_cnpjs])

        df = pd.DataFrame(data=list_cnpj, columns=["cnpj", "cnpj_hq"])

        df_cnpj_database = df_cnpj_database.append(df, ignore_index=True)

        del df, list_cnpj, branchs_cnpjs

    # Include some real CNPJs
    for real_cnpj in REAL_CNPJS:
        list_cnpj = list()

        list_cnpj.append([real_cnpj, None])

        rand_branchs = random.random() ** 15
        num_branchs = round(rand_branchs * max_filiais)

        branchs_cnpjs = generate_branchs_cnpjs(real_cnpj, num_branchs)
        list_cnpj.extend([[branch_cnpj, real_cnpj] for branch_cnpj in branchs_cnpjs])

        df = pd.DataFrame(data=list_cnpj, columns=["cnpj", "cnpj_hq"])
        df_cnpj_database = df_cnpj_database.append(df, ignore_index=True)

    df_cnpj_database.to_csv(output_path, index=False)


def generate_value_case(valor, mean, std_dev):
    if valor > 10:
        return valor

    return round(mean * (1 + np.random.normal(scale=0.2)), 2)


def fill_status(classe_processual):
    cod = int(classe_processual)


def read_serventias():
    serventias_df = pd.read_csv(SERVENTIAS_PATH, sep=";")

    area_dict = dict(zip(serventias_df["SEQ_ORGAO"], serventias_df["NOMEDAVARA"]))

    return area_dict


def create_final_base():
    # List all courts paths
    list_trts_paths = glob.glob(CNJ_DATABASE_PATH + "*")

    # List paths to all cases in each courts and add to a list
    list_cases_paths = list()

    # Content of the files
    json_data = list()

    random.shuffle(list_trts_paths)
    max_valor = 0

    df_final = pd.DataFrame(columns=["num_processo", "trt", "vara", "millis", "codigo_vara", "data_ajuizamento", "valor_causa", "status", "cnpj"])

    print("Loading files")
    list_files_trt = list()
    for trt_path in list_trts_paths:
        list_files_trt.extend(glob.glob(trt_path + "/*"))

    random.shuffle(list_files_trt)

    cnpj_df = pd.read_csv(CNPJ_DATABASE_PATH)

    conh_count = exec_count = liq_count = skip_count = 0

    varas_dict = read_serventias()

    for case_path in tqdm.tqdm(list(list_files_trt)):
        # Read the file, which contains a list of cases
        content = open(case_path, encoding="utf-8").read()

        # Transform into json object
        json_content = json.loads(content)
        random.shuffle(json_content)

        data_file = list()

        for case in json_content:

            # Skip case from other instances

            if case["grau"] != "G1":
                continue

            tribunal = case["siglaTribunal"]
            numero_unico = case["dadosBasicos"]["numero"]
            dataAjuizamento = case["dadosBasicos"]["dataAjuizamento"]

            try:
                millisInsercao = int(case["millisInsercao"])
            except:
                millisInsercao = int(round(time.time() * 1000))

            try:
                classe_processual = int(case["dadosBasicos"]["classeProcessual"])
            except:
                classe_processual = None

            try:
                codigo_vara = int(case["dadosBasicos"]["orgaoJulgador"]["codigoOrgao"])
            except:
                codigo_vara = None

            try:
                valor_causa = case["dadosBasicos"]["valorCausa"]
            except:
                valor_causa = None

            # Skip cases with empty classes
            if classe_processual is None or codigo_vara is None:
                continue

            try:
                vara = str(varas_dict[codigo_vara]).upper().replace("  ", " ")
            except:
                vara = None

            if vara is None:
                continue

            # Get status from class
            if classe_processual in CLASSES_CONHECIMENTO:
                status = Status.CONHECIMENTO.value
                conh_count += 1
            elif classe_processual in CLASSES_EXECUCAO:
                status = Status.EXECUCAO.value
                exec_count += 1
            else:  # The remaining cases will be "forced" to be in "LIQUIDACAO" stage
                status = Status.LIQUIDACAO.value
                liq_count += 1

            # Get a random CNPJ
            while True:
                try:
                    random_idx = random.randint(0, cnpj_df.shape[0])
                    cnpj_row = cnpj_df.iloc[random_idx]
                    cnpj_processo = int(cnpj_row["cnpj"])
                    break
                except:
                    pass

            data_file.append([numero_unico, tribunal, vara, millisInsercao,
                              codigo_vara, dataAjuizamento, valor_causa, status, cnpj_processo])

            # print(numero_unico, tribunal, millisInsercao, classe_processual, codigo_vara, dataAjuizamento, valor_causa, status)
            # time.sleep(1)

        local_df = pd.DataFrame(data=data_file, columns=["num_processo", "trt", "vara", "millis",
                                                         "codigo_vara", "data_ajuizamento", "valor_causa", "status", "cnpj"])

        df_final = df_final.append(local_df, ignore_index=False)

        # Free your memory, you must...
        del json_content, content, data_file, local_df

    print("=" * 100)
    print("Exporting processed database...")
    df_final.drop_duplicates(subset="num_processo", keep="last", inplace=True)
    df_final.dropna(subset=["valor_causa"], inplace=True)

    media = df_final["valor_causa"].mean()
    std_dev = np.std(np.array(df_final["valor_causa"]))

    df_final["valor_causa"] = df_final["valor_causa"].apply(lambda valor: generate_value_case(valor, media, std_dev))

    df_final = df_final.sample(frac=1)
    df_final.to_json(PROCESSED_DATABASE_PATH, orient="records", force_ascii=False)

    db = TinyDB(TINY_DB_PATH)
    db.truncate()

    with io.open(PROCESSED_DATABASE_PATH, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    db.insert_multiple(data)

    # df_final.head(n=50).to_json("data/final_database_menor.json", orient="records", force_ascii=False)
    # df_final.head(n=50).to_csv("data/final_database_menor.csv", index=False)
