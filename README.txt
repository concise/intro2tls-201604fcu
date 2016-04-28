參考資料

    第一週用的投影片 https://goo.gl/7AZpoz
    第二週螢幕錄影一 https://www.youtube.com/watch?v=4UOk38ni0Lc
    第二週螢幕錄影二 https://www.youtube.com/watch?v=o6YKZa3UdIw
    TLS 1.2 標準文件 https://tools.ietf.org/html/rfc5246
    SSL/TLS 維基百科 https://en.wikipedia.org/wiki/Transport_Layer_Security
    Python3 語言文件 https://docs.python.org/3/


作業：拆解 TLS 封包

    撰寫一個程式（建議使用 Python 3 語言）去拆解、解密 TLS 封包

    你必須要讓助教知道如何運行你的程式，特別是當你使用的程式語言不是
    Python 3 時，或者當你的程式需要用到外部、第三方函式庫時。


程式要求

    1.  主程式要接受 5 個 command-line 參數，這 5 個參數都是檔案路徑，
        他們的意義如下列所示：

            a. input file 1: recorded client-to-server traffic
            b. input file 2: recorded server-to-client traffic
            c. input file 3: server long-term RSA private key
            d. output file 1: decrypted client-to-server traffic
            e. output file 2: decrypted server-to-client traffic

        正常運作的程式，會從前三個檔案讀取資料，並把結果寫入後兩個檔案

    2.  假設雙方協議的 SSL/TLS 版本是 TLS 1.2 而 cipher suite 則是
        TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)


範例輸入輸出

    在 test1/ 目錄之下有 in1 、 in2 、 in3 三個檔案，分別為客戶端發出的封包、
    伺服器端回覆的封包、伺服器端的 RSA 私鑰。假如 decoder.py 程式已經完成了，
    想要解密 TLS 流量，可以下這個指令：

        python3 decoder.py test1/in1 test1/in2 test1/in3 test1/out1 test1/out2

    如此一來 decoder.py 程式就會將解密後的結果寫入 test1/out1 與 test1/out2
    兩個檔案。如果要檢驗答案是否正確，可以用 diff 指令來做到：

        diff -q test1/out1 test1/out1_answer

        diff -q test1/out2 test1/out2_answer

    如果給 diff 的兩個檔案內容不一致，它就會發出訊息告知。

    現在有 test1 、 test2 、 test3 、 test4 共四組測試資料，已附上解密後的答案。
    本作業的評分將會採用和它們類似的測資進行。


參考程式 decoder.py 有三個函式可能對你有幫助：

    TLS_PRF

        實作了 TLS 的 pseudorandom function (RFC 5246 Section 5)

    RSA_DECRYPT

        實作了 RSA 解密

    AES128CBC_DECRYPT

        實作了 AES-128 的 CBC mode 解密


注意事項

    在 decoder.py 中負責密碼學運算的 RSA_DECRYPT 與 AES128CBC_DECRYPT 這
    兩個函式都呼叫了一個名為「 openssl 」的外部程式。在 Linux 作業系統中，
    通常 openssl 會安裝到 /usr/bin/openssl 這個位置。

    如果你使用的不是 Linux 作業系統，參考程式中的那兩個函式就不能用了，
    你需要找 RSA / AES-128-CBC / HMAC-SHA-256 等密碼學運算的函式庫來使用。

    撰寫程式的過程中，記得常常做備份，以免不小心把辛苦的成果都銷毀了。
