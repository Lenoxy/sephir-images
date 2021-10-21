import grequests

k_start = 1000
k_end = 2000

if __name__ == '__main__':
    for i in range(5990, 7000):
        secondary_urls = []
        for j in range(k_start, k_end):
            secondary_urls.append((i, j, 'https://sephir.ch/ict/upload/foto_le/foto-' + str(i) + '_' + str(j) + '.jpg'))

        rs = (grequests.get(u[2]) for u in secondary_urls)
        responses = grequests.map(rs)

        for k in range(k_start, k_end):
            if responses[k-k_start].status_code == 200 and responses[k-k_start].headers['content-type'] == 'image/jpeg':
                with open('images/' + str(i) + '_' + str(k) + '.jpg', 'wb') as f:
                    print('found: ' + str(i) + '_' + str(k) + '.jpg')
                    f.write(responses[k].content)
                    f.close()
            else:
                print('nothing found: ' + str(i) + '_' + str(k) + '.jpg')

