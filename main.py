import multiprocessing as mp

import requests


def get_img(i, j):
    url = 'https://sephir.ch/ict/upload/foto_le/foto-' + str(i) + '_' + str(j) + '.jpg'
    response = requests.get(url)

    if response.status_code == 200 and response.headers['content-type'] == 'image/jpeg':
        with open('images/' + str(i) + '_' + str(j) + '.jpg', 'wb') as f:
            print('found: ' + str(i) + '_' + str(j) + '.jpg')
            f.write(response.content)
            f.close()
    else:
        print('nothing found: ' + str(i) + '_' + str(j) + '.jpg')


if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())

    for i in range(6043, 9999):
        for j in range(4981, 9999):
            # pool.apply(get_img, args=(i, j))
            get_img(i, j)
