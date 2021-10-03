class SlapData:
    numbers_array = [1, 2, 3, 4]

    slap_types = {
        1: {
            'name': 'batman',
            'image_path': 'res/images/pls_slap/batman-slap-meme.jpeg',
            'profile_hw': 140,
            'slapper_loc': (180, 60),
            'beater_loc': (350, 200)
        },
        2: {
            'name': 'girl_slap',
            'image_path': 'res/images/pls_slap/FaceSlap-1024x683.jpg',
            'profile_hw': 300,
            'slapper_loc': (80, 140),
            'beater_loc': (700, 180)
        },
        3: {
            'name': 'spank',
            'image_path': 'res/images/pls_slap/spank_boy.jpg',
            'profile_hw': 140,
            'slapper_loc': (240, 0),
            'beater_loc': (360, 240)
        },
        4: {
            'name': 'uncle',
            'image_path': 'res/images/pls_slap/uncle_boy.png',
            'profile_hw': 80,
            'slapper_loc': (180, 60),
            'beater_loc': (30, 100)
        }
    }


class CongratsData:
    numbers_array = [1, 2]

    cong_types = {
        1: {
            'name': 'ribbon',
            'trans_over': True,
            'image_path': 'res/images/congrats/ribbon.png',
        },
        2: {
            'name': 'carpet',
            'trans_over': False,
            'image_path': 'res/images/congrats/carpet.png',
            'profile_hw': 380,
            'congrats_loc': (160, 160)
        }
    }


class WantedData:
    numbers_array = [1, 2]

    want_types = {
        1: {
            'name': 'dead_or_alive',
            'image_path': 'res/images/make_wanted/deadoralive.jpg',
            'profile_hw': 400,
            'congrats_loc': (150, 300)
        },
        2: {
            'name': 'mostwanted',
            'image_path': 'res/images/make_wanted/mostwanted.jpg',
            'profile_hw': 300,
            'congrats_loc': (90, 220)
        }
    }


class DangerData:
    numbers_array = [1]

    dang_types = {
        1: {
            'name': 'dead_or_alive',
            'image_path': 'res/images/in_danger/danger_image.png',
            'profile_hw': 150,
            'danger_loc': (270, 60)
        }
    }


class JailData:
    numbers_array = [1]

    jail_types = {
        1: {
            'name': 'jail',
            'trans_over': True,
            'image_path': 'res/images/in_jail/jail_image.png'
        }
    }
