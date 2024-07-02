from PIL import Image

def split_image(image_path, rows, cols):
    original_image = Image.open(image_path)
    width, height = original_image.size
    tile_width = width // cols
    tile_height = height // rows

    tiles = []
    for y in range(0, height, tile_height):
        for x in range(0, width, tile_width):
            box = (x, y, x + tile_width, y + tile_height)
            tile = original_image.crop(box)
            tiles.append(tile)

    return tiles

# Example usage
image_path = "signature.jpeg"
rows = 2
cols = 2

tiles = split_image(image_path, rows, cols)
for i, tile in enumerate(tiles):
    tile.show()
