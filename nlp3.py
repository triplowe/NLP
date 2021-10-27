from pathlib import Path
import imageio
from wordcloud import WordCloud
import wordcloud

text = Path('RomeoAndJuliet.txt').read_text()

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap='prism', mask=mask_image,
                      background_color='white')

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

print("done")
