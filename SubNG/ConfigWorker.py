from json import loads, dumps
from base64 import b64decode, b64encode
from re import findall 

def CheckBase64(encoded_str):
    try:
        decoded_bytes = b64decode(encoded_str, validate=True)
        return decoded_bytes.decode('utf-8')
    except:
        return False

def NameEditor(Config: str, NewName: str):
    EditableConfig = Config
    SplitConfig = Config.split("://", -1)
    ConfigType = SplitConfig[0]
    ConfigData = SplitConfig[1]
    if X := CheckBase64(ConfigData):
        try:
            Data = loads(X)
            Data['ps'] = NewName
            Data = b64encode(dumps(Data).encode('utf-8')).decode('utf-8')
            EditableConfig = (ConfigType + "://" + Data).replace("\n", "")
        except : pass
    else:
        try:
            O = ConfigData.split("#", -1)
            O[1] = NewName
            EditableConfig = (ConfigType + "://" + "#".join(O)).replace("\n", "")
        except : pass
    #----------------------------------------------------------------
    return EditableConfig

def DetectConfig(Txt: str):
    return findall("(?:vless)://[^\s]+", Txt) #for all types -> (?:vmess|vless|trojan|ss)://[^\s]+
