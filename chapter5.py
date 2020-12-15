#辞書やリストから特定の値を抜き出す

# coding: UTF-8

agesDictionary = {"歌手A":24, "歌手B":60, "歌手C":19}

songsDictionary = {
    "歌手A":["曲1","曲2","曲3"],
    "歌手B":["曲1","曲2","曲3","曲4","曲5"],
    "歌手C":["曲1","曲2"],
}

def pickUpAges(singerName):
    return agesDictionary[singerName]

def pickUpSongs(singerName, number):
    return songsDictionary[singerName][number]

if __name__ == "__main__":
    name = input("歌手の名前を入力してください：")
    print("彼/彼女は" + str(pickUpAges(name)) + "です。")
    number = input("曲の番号を選択してください：")
    print(str(pickUpSongs(name,int(number))) + "を流します。")