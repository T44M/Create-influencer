from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

session = InstaPy(username='{{your inta ID}}', password='{{your insta PW}}', headless_browser=True)
with smart_run(session):
    session.set_do_follow(enabled=True, percentage=75)
    session.set_relationship_bounds(enabled=True,
                                potency_ratio=-1.21,
                                delimit_by_numbers=True,
                                max_followers=4590,
                                max_following=6000,
                                min_followers=25,
                                min_following=30)
    session.set_quota_supervisor(enabled=True,
                                stochastic_flow=True,
                                peak_follows_hourly=7,
                                peak_follows_daily=100,
                                peak_unfollows_hourly=5,
                                peak_unfollows_daily=100,
                                peak_server_calls_hourly=None,
                                peak_server_calls_daily=4700)
    session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM",
                        unfollow_after=42 * 60 * 60, sleep_delay=300)
    ammount_number = 50
    session.follow_user_followers(['{{target tag}}'],
                                amount=ammount_number, randomize=False,
                                sleep_delay=240)
    session.end()

