# main.py
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import gui_helpers
import file_operations
import sentiment_analysis
import pandas as pd
from youtube_comments import get_video_id, get_comments
from PIL import Image, ImageTk

def clearAll():
    for field in [negativeField, neutralField, positiveField, overallField, emotionField]:
        field.delete(0, tk.END)
    textArea.delete(1.0, tk.END)
    pieChartLabel.config(image='')

def detect_sentiment():
    text = textArea.get(1.0, tk.END).strip()
    if text:
        update_sentiment_results(text)
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

def detect_sentiment_from_file(filename):
    text = file_operations.read_text_from_file(filename)
    if text:
        update_sentiment_results(text)
    else:
        messagebox.showerror("Error", f"File '{filename}' not found.")

def update_sentiment_results(text):
    sentiment_dict = sentiment_analysis.analyze_sentiment(text)

    for field in [negativeField, neutralField, positiveField, overallField, emotionField]:
        field.delete(0, tk.END)

    negativeField.insert(0, f"{sentiment_dict['neg']*100:.2f}% Negative")
    neutralField.insert(0, f"{sentiment_dict['neu']*100:.2f}% Neutral")
    positiveField.insert(0, f"{sentiment_dict['pos']*100:.2f}% Positive")

    

    if sentiment_dict['compound'] >= 0.01:
        overallField.insert(0, "Positive")
    elif sentiment_dict['compound'] <= -0.01:
        overallField.insert(0, "Negative")
    else:
        overallField.insert(0, "Neutral")

    emotionField.insert(0, sentiment_dict['emotion'])

    sentiment_pie_buffer = sentiment_analysis.generate_sentiment_pie(sentiment_dict)
    sentiment_pie_image = Image.open(sentiment_pie_buffer)
    sentiment_pie_photo = ImageTk.PhotoImage(sentiment_pie_image)
    pieChartLabel.config(image=sentiment_pie_photo)
    pieChartLabel.image = sentiment_pie_photo

def browse_file():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a Text File",
        filetypes=(("Text files", "*.txt"),)
    )
    if filename:

        detect_sentiment_from_file(filename)


  

def analyze_youtube_comments():
    url = simpledialog.askstring("YouTube URL", "Enter YouTube video URL:")
    if url:
        video_id = get_video_id(url)
        if video_id:
            comments = get_comments(video_id)
            if comments:
                all_comments = " ".join(comments)
                update_sentiment_results(all_comments)
                textArea.delete(1.0, tk.END)
                textArea.insert(tk.END, f"Analyzed {len(comments)} comments")
            else:
                messagebox.showerror("Error", "No comments found or unable to fetch comments.")
        else:
            messagebox.showerror("Error", "Invalid YouTube URL.")


def calculate_accuracy(csv_filename, max_rows=500):
    try:
       
        data = pd.read_csv(csv_filename, header=None, names=['text', 'sentiment'], nrows=max_rows)
        total = len(data)
        correct = 0

        for index, row in data.iterrows():
            try:
                text = str(row['text']).strip() 
                
                predicted_sentiment = sentiment_analysis.analyze_sentiment(text)
                predicted_label = 'Positive' if predicted_sentiment['compound'] >= 0.05 else 'Negative' if predicted_sentiment['compound'] <= -0.05 else 'Neutral'

                if predicted_label == 'Positive':
                    predicted_label_numeric = 1
                elif predicted_label == 'Negative':
                    predicted_label_numeric = -1
                else:
                    predicted_label_numeric = 0

                if predicted_label_numeric == int(row['sentiment']):
                    correct += 1
            except Exception as e:
                print(f"Error processing row {index}: {str(e)}")

        accuracy = (correct / total) * 100
        messagebox.showinfo("Accuracy", f"Accuracy: {accuracy:.2f}%")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{csv_filename}' not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))



if __name__ == "__main__":
    gui = gui_helpers.create_gui()

    textArea, negativeField, neutralField, positiveField, overallField, emotionField, pieChartLabel = gui_helpers.create_widgets(gui, detect_sentiment, clearAll)

    gui_helpers.add_file_button(gui, browse_file)
    gui_helpers.add_youtube_button(gui, analyze_youtube_comments)

    # Adding a button for accuracy calculation
    accuracy_button = tk.Button(gui, text="Calculate Accuracy", command= lambda:calculate_accuracy("C:/Users/GAURAV/Desktop/sentiment analysis/accuracy file/reddit.csv"))
    accuracy_button.grid(row=8, column=0, columnspan=2, pady=10)  # Adjust row, column, and other options as needed

    gui.mainloop()

