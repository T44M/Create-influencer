Create Influencer

This Instagram bot uses InstaPy to automate the functions of Instagram.

My test
https://www.instagram.com/beautiful.jpn/

Automation
-Follow by hashtag
-Unfollowing with specified conditions
-Like

Since the Instagram API does not support automatic posting of photos, Combin is recommended.
https://www.combin.com/product/free-instagram-scheduler/

Also, automated features may be trapped by Instagram's limits. Initially, it is recommended to start with a low number.

I downloaded the image from the hashtag, added the original user name to it, and post it as a retweet.
To download, you can use this library to do it in batches.

sudo pip3 install instaloader

ex,
Download 20 pictures and videos from the hashtag
instaloader --no-captions --no-metadata-json --no-compress-json --count 20 "#your hashtag"

Download only 20 pictures from the hashtag
instaloader --no-videos --no-captions --no-metadata-json --no-compress-json --count 20 "#your hashtag"


Lastly, we are not responsible for any account suspensions.

Enjoy!!