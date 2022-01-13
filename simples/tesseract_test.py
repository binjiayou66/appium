from PIL import Image
import pytesseract


def main():
    text = pytesseract.image_to_string(
        Image.open('/Users/andy/Github/appium/simples/english01.png'), lang='chi_sim')
    print(text)

    text = pytesseract.image_to_string(
        Image.open('/Users/andy/Github/appium/simples/chinese01.png'), lang='chi_sim')
    print(text)

    print(pytesseract.image_to_boxes(Image.open(
        '/Users/andy/Github/appium/simples/english01.png')))

    print(pytesseract.image_to_data(Image.open(
        '/Users/andy/Github/appium/simples/english01.png')))


if __name__ == "__main__":
    main()
