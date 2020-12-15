#reモジュールを使用した正規表現の実装

# coding: UTF-8

import re

#"oo"が登場する単語に一致する正規表現
def oo_re(l):
    matches = re.findall(".oo",l)
    return matches

if __name__ == "__main__":
    l = "The ghost that says boo hounts the loo"
    print(oo_re(l))
