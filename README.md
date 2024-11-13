# Tic Tac Toe AI 🎲

Welcome to **Tic Tac Toe AI**, a web-based version of the classic game where players can challenge a computer opponent using the powerful Minimax algorithm! This project combines the simplicity of Django with engaging frontend animations and dynamic AI gameplay.

## 🌟 Features

- **Single-Player Mode**: Play against an AI opponent that uses the Minimax algorithm for strategic moves.
- **Engaging Animations**: Visual feedback for every move, win, and draw to enhance user experience.
- **Dynamic UI**: Responsive design with a centered board and interactive elements.
- **Game Result Display**: Modal window to show the result (Win, Lose, or Tie) after each game.
- **Rematch & Restart Options**: Easily start a new game or reset to the initial state.

## 🔥 Live Demo

Check out the live version of this project [here](https://your-app-name.onrender.com) (Replace with your Render URL).

![Game Screenshot](https://your-github-image-url) <!-- Screenshot of the gameplay (replace with actual URL) -->

## 🚀 Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python 3.8+
- Django 4.0+
- Git
- PostgreSQL (for deployment) or SQLite (for local development)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
2. **Create a Virtual Environment**
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3.**Install Dependencies**

    ```bash
    
    pip install -r requirements.txt
4. **Set Up Database**

   For SQLite (default for local development), skip this step.

   For PostgreSQL:
   - Update `DATABASES` settings in `settings.py` with your PostgreSQL credentials.
   - Run migrations to set up the database:

      ```bash
     python manage.py migrate
     ```

5. **Run the Server**

    ```bash
   python manage.py runserver

  Open your browser and navigate to http://127.0.0.1:8000/ to start playing!
   
