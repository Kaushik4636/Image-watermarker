# Simple Image Watermarker

This is a **basic Python script** designed to help you quickly add a text watermark to your digital images. Built using the popular **Pillow (PIL)** library, this tool provides a straightforward way to protect your visual content before sharing it online.

-----

## Features

  * **Core Functionality:** Adds custom text as a watermark to an image.
  * **Pillow Library:** Utilizes the robust Python Imaging Library for reliable image processing.
  * **Simple Execution:** Runs directly from the command line with minimal setup.

-----

## Requirements

You must have **Python 3** installed on your system. This project requires the **Pillow** library to handle all image manipulation tasks.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Kaushik4636/Image-watermarker.git
    cd Image-watermarker
    ```

2.  **Install the dependency** using `pip`:

    ```bash
    pip install Pillow
    ```

-----

## How to Use It

The script is designed to be run from your terminal.

1.  **Prepare the Image:** Place the image file you want to watermark (e.g., `photo.jpg`) into the main project directory.

2.  **Run the Script:** Execute the Python file. (Assuming the main script is named `watermark.py`):

    ```bash
    python watermark.py
    ```

3.  **Follow the Prompts:** The script will likely prompt you to:

      * Enter the **name of the image file** to process.
      * Enter the **text** you want to use as the watermark (e.g., `© MyName`).

4.  **Output:** A new, watermarked image will be saved in the same directory, typically with a name like `watermarked_[original_filename]`.

-----

## Contributing

Contributions are welcome\! If you have suggestions for improving this basic watermarker—such as adding features for image logos, batch processing, or transparency controls—please feel free to fork the repository and submit a pull request.

-----

## License

This project is licensed under the **MIT License**. See the `LICENSE.md` file for more details.
