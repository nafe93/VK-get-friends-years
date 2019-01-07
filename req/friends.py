import requests
import datetime
from collections import Counter

access_token = "17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711"
#"3f6b4c043f6b4c043f6b4c04833f376b3e33f6b3f6b4c0463594eaa953af2dfd8083d6b"


def get_own_vk_id(uid):
    url = f"https://api.vk.com/method/users.get?v=5.71&access_token={access_token}" \
        f"&user_ids={uid}"

    r = requests.get(url).json()
    get_id = r['response'][0]['id']

    return get_id


def get_own_friends(uid):
    id = get_own_vk_id(uid)

    url = f"https://api.vk.com/method/friends.get?v=5.71&access_token={access_token}" \
        f"&user_id={id}&fields=bdate"

    friends = requests.get(url).json()['response']['items']
    return friends


def get_own_friends_by_data(uid):
    my_friends = get_own_friends(uid)
    my_friends_by_year = list()

    current_year = datetime.datetime.now().year

    for friend in my_friends:
        if 'bdate' in friend:
            if len(friend['bdate']) > 5:
                friend_year_birthday = int(friend['bdate'][-4:])
                friend_old = current_year - friend_year_birthday
                my_friends_by_year.append(friend_old)

    return my_friends_by_year


def calc_age(uid):
    calc_list = get_own_friends_by_data(uid)
    c = Counter(calc_list)
    c = c.most_common()
    c = sorted(c, key=lambda x: (-x[1], x[0]))

    return c


if __name__ == '__main__':
    res = calc_age('nafe93')
    print(res)
