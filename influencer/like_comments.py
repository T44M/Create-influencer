from instapy import InstaPy

session = InstaPy(username='{{your inta ID}}', password='{{your insta PW}}', headless_browser=True)
session.login()

session.set_relationship_bounds(enabled=True,
                                potency_ratio=-1.21,
                                delimit_by_numbers=True,
                                max_followers=5988,
                                max_following=2965,
                                min_followers=19,
                                min_following=11)
session.set_quota_supervisor(enabled=True, stochastic_flow=True,
                            peak_likes_hourly=20,
                            peak_likes_daily=350,
                            peak_comments_hourly=5,
                            peak_comments_daily=30,
                            peak_server_calls_hourly=None,
                            peak_server_calls_daily=4700)

#comments section
session.set_do_comment(True, comment_liked_photo=True, percentage=50)
session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
session.set_comments([{{add your preference comments, you can use Emoji as well}}'], media='Photo')

#like section (Chnage tags here)
session.set_do_like(enabled=True, percentage=100) 
session.set_delimit_liking(enabled=True, max_likes=150, min_likes=0)
session.set_dont_like(['depression', 'girl', 'naked', 'nude', 'sex'])    
session.like_by_tags([{{add tag}}], use_random_tags=True, amount=1)

session.end()
