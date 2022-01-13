from aip import AipOcr

APP_ID = "25503782"
API_KEY = "ysvcECXTGZqWXYopG0Irumdy"
SECRET_KEY = "EbzjPK86QUgEaU871gQs1DBDGrA1qbcT"

client = AipOcr(appId=APP_ID, apiKey=API_KEY, secretKey=SECRET_KEY)


def return_cordinate(text, imagePath):
    with open(imagePath, 'rb') as fp:
        dic = client.general(fp.read())
        print(dic["words_result"])
        for word in dic["words_result"]:
            if word["words"] == text:
                x = int(word["location"]["left"]) + \
                    int(word["location"]["width"]) / 2
                y = int(word["location"]["top"]) + \
                    int(word["location"]["height"]) / 2
                return {"x": x / 3, "y": y / 3}
        return {}


def cordinate(text, imageBytes: bytes):
    dic = client.general(imageBytes)
    print(dic["words_result"])
    for word in dic["words_result"]:
        if word["words"] == text:
            x = int(word["location"]["left"]) + \
                int(word["location"]["width"]) / 2
            y = int(word["location"]["top"]) + \
                int(word["location"]["height"]) / 2
            return {"x": x / 3, "y": y / 3}
    return {}


def main():
    print(return_cordinate(
        "邀请患者", "/Users/andy/Github/appium/simples/screenshot_index.png"))


if __name__ == "__main__":
    main()
