# from docx import Document
# from docx.shared import Inches
from pydub import AudioSegment
import post
import csv
chapters = [{"summary": "Learn how to easily tailor your trousers at home. No sewing machine required required. Here are the tools you'll need to get started.", "gist": "How To Tailor Your Trousers", "headline": "Thomas teaches you how to easily tailor your trousers at home", "start": 250, "end": 38066}, {"summary": "Use an existing pair of trousers that fit you perfectly as a guide. Turn your pants inside out, then lay your perfect fitting pair on top. You can slim your pants from the inside seam, the outside seam, or both. Switch out the safety pins with sewing pins and you're good to go.", "gist": "How to Slim Your Trousers", "headline": "You can slim your pants from the inside seam, the outside seam", "start": 38178, "end": 107278}, {"summary": "Cut your thread so it's more than twice the length you'll be tapering. Double thread the needle for maximum strength. Now take your thread ripper and cut a two to three inch stretch of hem. Press the new seam flat so it will drape cleanly.",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "gist": "How to Make a T-Shirt With a Knot", "headline": "Step one: Cut your thread so it's more than twice the length needed", "start": 107444, "end": 211258}, {"summary": "Measure and Pin just like when slimming your trousers. If you have the perfect fitting pair of pants, you can use them to get the right measurements. Now let's talk about how to hem those trousers that are too long.", "gist": "How to hem Your Trousers That Are Too Long", "headline": "How to hem those trousers that are too long", "start": 211354, "end": 319938}, {"summary": "This technique also works on any kind of trousers, including jeans and chinos. What piece of clothing do you want to learn to tailor next? Let me know down in the comments.", "gist": "How To Tuck Your T-Shirt Fit!", "headline": "This technique also works on any kind of trousers, including jeans and chinos", "start": 320104, "end": 339570}]

# document = Document()

# filename = "tailor.mp3"
# document.add_heading(filename[:-4], 0)

# for i in chapters:
#     chapter = i['gist']
#     text = i['summary']
#     document.add_heading(chapter, level=1)
#     document.add_paragraph(text)

# document.add_page_break()

# document.save('demo.docx')


song = AudioSegment.from_mp3('tailor.mp3')

with open('something.csv', 'w', newline='') as file:
    fieldnames = ['props', 'val']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for i in chapters:
        start = i['start']
        stop = i['end']
        name = 'mod'+str(chapters.index(i))+'.mp3'
        first_10_secs = song[start:stop]
        first_10_secs.export(name, format="mp3")

        url = post.post1(name)
        id_ = post.post2(url, str(chapters.index(i)))
        num = str(chapters.index(i))

        writer.writerow({'props': num, 'val': id_})


# slice out the first 10 secs of the video

# chapters = []
# texts = []
# for i in dictionary["chapters"]:
#     chapter = i['gist']
#     text = i['summary']
#     chapters.append(chapter)
#     texts.append(text)
#     print('\n##'+chapter)
#     print(text)
