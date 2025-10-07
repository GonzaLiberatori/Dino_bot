# 🤖 Dino Bot: Automated Bot for the Chrome Dinosaur Game

This is a bot project developed in Python that uses computer vision and user interface automation to play the Chrome Dinosaur game autonomously.

***

## ⚙️ Technologies Used

The project relies on the following Python libraries for obstacle detection and game control, as defined in `requirements.txt`:

* **OpenCV (`opencv-python`)**: Used for image processing, including grayscale conversion and thresholding to isolate obstacles.
* **NumPy (`numpy`)**: Essential for handling images as efficient data matrices.
* **`mss`**: Used for high-speed screen capture of the game window.
* **`pygetwindow`**: To identify and manipulate the Chrome window, ensuring it is correctly positioned for detection.
* **`pyautogui`**: Used to simulate the jump key press (**space**) when an obstacle is detected.

***

## 📝 Requirements and Installation

To run the bot, you will need **Python 3.x** and the specified libraries.

1.  **Clone the repository** (or download the source code):

    ```bash
    git clone [REPOSITORY_URL]
    cd dino_bot
    ```

2.  **Install Python dependencies**:
    The necessary dependencies are listed in the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

***

## 🚀 Execution

To start the bot, run the main script `main.py`:

```bash
python dino_bot_code/main.py
