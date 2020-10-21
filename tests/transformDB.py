import io
import os
import pathlib
import json
import yaml
from tinydb import TinyDB, Query, where


def main():
    CONFIG_FILE_NAME = "GroupAPI.yaml"
    JSON_DB_NAME_ORIGEM = "final_database.json"
    JSON_DB_NAME_DESTINO = "processos.json"
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Load configuration
    ConfigFile = os.path.join(CURRENT_DIR, CONFIG_FILE_NAME)
    with open(ConfigFile, "r", encoding="utf-8") as ConfigFile:
        Configuration = yaml.load(ConfigFile, Loader=yaml.SafeLoader)
    RootDataDir = pathlib.Path(Configuration["Input"]["RootDataDir"])
    JsonDB = os.path.join(RootDataDir, JSON_DB_NAME_DESTINO)
    JsonDBFonte = os.path.join(RootDataDir, JSON_DB_NAME_ORIGEM)

    db = TinyDB(JsonDB)
    db.truncate()

    with io.open(JsonDBFonte, "r", encoding="utf-8") as json_file:  
        data = json.load(json_file)    
    db.insert_multiple(data)        
    #for record in data:
    #    db.insert(record)


if __name__ == "__main__":
    main()


