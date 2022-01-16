import os
import random

line = ".""\n"".""\n"".""\n"

##You can add your comments in the list text##
with open('list_of_post.txt', 'r', encoding="utf-8_sig") as f:
    comments = f.read().split("\n")
    post = random.choice(comments)

##You can add hashtags in the list text##
with open('hashtags.txt', 'r', encoding="utf-8_sig") as t:
    hashtags = t.read().split("\n")
    tags = random.sample(hashtags, 20)

##Then create your post comments on this text##
with open("post.txt", "w", encoding="utf-8_sig") as p:
    p.write(str(post) + "\n")
    p.write("Share your experience with #lovinjp" + "\n")
    p.write(str(line))
    p.write('Credit: @' + "\n")
    p.write("Love to travel??Follow: @beautiful.jpn" + "\n")
    p.write(str(line))
    p.write(" ".join(tags))