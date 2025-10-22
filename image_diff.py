import sys
from PIL import Image, ImageChops


def highlight_image_differences(image1, image2, output_path="differences.png"):
    try:
        img1 = Image.open(image1)
        img2 = Image.open(image2)
    except FileNotFoundError:
        print("Error: One or both of the files were not found.")
        return

    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)

    diff = ImageChops.difference(img1, img2)

    rgba = diff.convert("RGBA")
    datas = rgba.getdata()
    new_data = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append((255, 105, 180))
    rgba.putdata(new_data)

    diff = ImageChops.add_modulo(img1, rgba)

    diff.save(output_path)
    # diff.show()
    print(f"\nDifferences highlighted and saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python3 image_diff.py path_to_image_1 path_to_image_2 path_to_output"
        )
        quit()

    image1 = sys.argv[1]
    image2 = sys.argv[2]
    output_path = sys.argv[3]

    highlight_image_differences(image1, image2, output_path)
