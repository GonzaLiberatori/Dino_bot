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
```
### Important Usage Instructions

For the bot to function correctly, follow these essential steps:

1.  **Windowed Mode**: The Chrome Dino game must be open in a Chrome window, not fullscreen.
2.  **Window Positioning**: The bot will automatically attempt to move the Chrome window to the top-left corner of your screen **((0, 0))**.
3.  **White Background**: The current obstacle detection logic is optimized for the **daytime (white background)** game mode, where obstacles are dark.
4.  **Start the Game**: You must manually start the dinosaur game (by pressing the spacebar) before executing the bot.

***

## 💡 Basic Functionality

The bot operates in an infinite loop performing the following actions:

* **Screen Capture**: It uses the `get_game_frame()` function to obtain a grayscale capture of the Chrome window's content.
* **Obstacle Detection**: The `detect_obstacle()` function defines a **Region of Interest (ROI)** (a box in front of the dinosaur, with configurable coordinates: `scan_x_start`, `scan_y_start`, `scan_width`, `scan_height`) where it searches for cacti or birds.
* **Thresholding**: It converts the ROI and applies an inverse binary threshold (`cv2.THRESH_BINARY_INV`) to count the number of dark pixels.
* **Jump**: If the non-zero pixel count (obstacle pixels) exceeds the predefined limit (`obstacle_limit = 100`), the `jump()` function is called, simulating the pressing of the **space** key.
* **Cooldown**: A brief delay (`jump_cooldown = 0.1` seconds) is applied between jumps to prevent unnecessary multiple key presses.

***

## 🛣️ Contributions and Future Improvements

The project is open to contributions. Here are some key ideas for future enhancements:

1.  **Night Mode (Color Change Detection)**:
    * The current detection method fails when the game switches to night mode (dark background/light obstacles). Logic needs to be implemented to **detect the mode change** (e.g., by monitoring the average background color).
    * Upon detecting night mode, the `detect_obstacle` function must **adjust the threshold and the type of thresholding** (`cv2.THRESH_BINARY_INV` vs. `cv2.THRESH_BINARY`) to detect light obstacles on a dark background.
2.  **Dynamic ROI Adjustment**:
    * At higher speeds, the bot should scan further ahead of the dinosaur. The position of the Region of Interest (ROI) could be adjusted dynamically based on the score (which reflects the game speed).
3.  **Pattern Recognition Improvement**:
    * Implement more sophisticated logic, such as shape recognition or using *templates*, to more accurately differentiate between large, small cacti, and birds, instead of just counting dark pixels.
