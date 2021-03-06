def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)



def serch_index(sorted_array, target_number):

    # ここから記述

    array_len = len(sorted_array)
    target_pos = 0

    #比較対象がなくなるまで探索
    while array_len != 1:
        array_len = len(sorted_array)
        center_pos = array_len // 2     #探索配列の中間の位置を取得

        #探索数値が見つかった場合
        if target_number == sorted_array[center_pos]:
            return target_pos + center_pos

        #中間の値>探索数値の場合、探索配列を前半分に
        elif target_number < sorted_array[center_pos]:
            del sorted_array[center_pos:]

        #探索数値>中間の値の場合、探索配列を後ろ半分に
        else:
            del sorted_array[:center_pos+1]
            target_pos += center_pos + 1    #探索配列から除いた個数を 'target_pos' で保持


    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1


if __name__ == '__main__':
    main()
