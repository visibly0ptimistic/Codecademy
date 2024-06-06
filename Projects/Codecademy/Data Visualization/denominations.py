from wordcloud import WordCloud
import matplotlib.pyplot as plt
from fpdf import FPDF
from PIL import Image
import os

data = {
    "Baptists": "Emphasis on personal faith in Jesus, baptism as a sign of personal conversion, individual Bible reading and scripture memorization.",
    "Methodists": "Focus on service to others, helping the poor, and working for justice.",
    "Presbyterians": "Intellectual approach to the Christian faith, emphasis on studying and understanding God, founding important universities.",
    "Lutherans": "Focus on the gospel, distinction between law and gospel, emphasis on salvation by faith alone, sacred worship environment.",
    "Catholics": "Impact on the world, emphasis on the institution of the church, founding hospitals and universities, contributions to art, music, and science, charitable organization.",
    "Anglicans": "Incorporation of the best aspects of other Christian traditions, diversity of belief, ornate worship style combined with passionate sermons.",
    "Eastern Orthodox": "Reverence for tradition, belief in apostolic heritage, connection to the past through iconography and worship style.",
    "Oriental Orthodox": "Humility and forgiveness in the face of persecution, unique characteristics of each separate church (e.g., heritage, historical significance).",
    "Pentecostals": "Focus on the Holy Spirit, recognition of the Holy Spirit's role in faith, fastest-growing form of Christianity.",
    "Moravians": "Emphasis on missions, community, and being warriors for Christ.",
    "Assyrian Church of the East": "Christian group with a history of planting Christianity in non-Christian lands.",
    "Congregationalists": "Simple style, focus on God, descendants of the Puritans who emphasize God's control over everything."
}

# Create word clouds for each denomination and save as png
for denomination, text in data.items():
    wordcloud = WordCloud(width=800, height=800, 
                          background_color='white', 
                          stopwords=None, 
                          min_font_size=10).generate(text)
    
    plt.figure(figsize=(8, 8), facecolor=None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad=0)
    plt.savefig(f"{denomination}_wordcloud.png")
    plt.close()

# Create a PDF document to include all word clouds
pdf = FPDF()
for denomination in data.keys():
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=denomination, ln=True, align='C')
    img_path = f"{denomination}_wordcloud.png"
    pdf.image(img_path, x=10, y=20, w=190)
    os.remove(img_path)  # Remove the image file after adding it to the PDF

pdf_output = "Denominations_Wordcloud.pdf"
pdf.output(pdf_output)

pdf_output
