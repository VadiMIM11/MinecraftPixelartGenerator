# Image to Pixel Art Converter

This is a simple Python program that converts an image (`.png`) into pixel art using a given set of textures. The intended use case is to create pixel art with **Minecraft textures**, but you can use any other texture set as well.

## Install PIL
- `pip install pillow`

## Features

- Converts any `.png` image into a pixel art version.
- Uses a set of textures to replace pixels, creating a blocky, game-like appearance.
- Designed with **Minecraft textures** in mind but works with any texture pack.
- Outputs the final pixel art as a `.png` file.

## How It Works

1. The program reads the input image and downsizes it to a chosen resolution.
2. It analyzes the colors in the image and matches them to the closest available texture from the texture set.
3. The textures are placed to create a new **pixelated** version of the original image.
4. The final output is saved as a new `.png` file.

## Custom Texture Packs

- While **Minecraft textures** are the default choice, you can replace them with any other texture set.
- Simply provide a folder containing the textures you want to use.
- The program will automatically map the textures to the closest colors in the input image.

## Example

| Original Image | Pixel Art Output |
|---------------|-----------------|
| <img src="https://github.com/user-attachments/assets/7a29a762-761c-455e-bcbc-8e319e4202bb" alt="Original Image" width="500"/> | <img src="https://github.com/user-attachments/assets/d4532108-dbf9-48bd-8b3c-8413358efcbd" alt="Pixel Art" width="500"/> |

---

