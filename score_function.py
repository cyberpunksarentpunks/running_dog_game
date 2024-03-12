# this will be a module for counting a score and saving it with a player name to the database

import sqlite3

def write_score_to_database():

    # Connect to the database (create it if it doesn't exist)
    connection = sqlite3.connect("highscores.db")
    cursor = connection.cursor()

    # Create a table for highscores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT,
            score INTEGER
        )
    """)

    # Commit and close the connection
    connection.commit()
    connection.close()


def display_highscores():
    from main import WIDTH, WHITE, screen, button_font
    connection = sqlite3.connect("highscores.db")
    cursor = connection.cursor()

    # Fetch highscores from the database
    cursor.execute("SELECT player_name, score FROM highscores ORDER BY score DESC LIMIT 10")
    highscores = cursor.fetchall()

    connection.close()

    # Display highscores on the screen
    y_position = 100
    for i, (player_name, score) in enumerate(highscores, start=1):
        highscore_text = button_font.render(f"{i}. {player_name}: {score}", True, WHITE)
        screen.blit(highscore_text, (WIDTH // 2 - 100, y_position))
        y_position += 50
        
